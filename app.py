#!flask/bin/python
from flask import Flask
from flask import jsonify
from flask import abort
from flask import request

import json
import os

app = Flask(__name__)

app.route('/')
def index():
    return "RelicScale API, v0.1"

@app.route('/api/v0.1/webhook', methods = ['POST'])
def receive_NR_webhook():
    alerts = request.form.getlist('alert')
    print alerts

    if not alerts:
        print("Incorrect data, expecting 'alert | deployment'")
        return ""

    for alert in alerts:
        alert_json = json.loads(alert)
        print('App Name %s' % alert_json['application_name'])
        print('Severity %s' % alert_json['severity'])
        print('Descripton %s' % alert_json['short_description'])
        if alert_json['application_name'] == "APPLICATION NAME" and alert_json['severity'] == "critical" and "New alert" in alert_json['short_description']:      
            os.system ("curl --include --request POST 'https://lon.autoscale.api.rackspacecloud.com/v1.0/execute/1/AUTOSCALE_SCALE_UP_WEBHOOK/' -v")
            print "Scaling up"
            return ""
        elif alert_json['application_name'] == "APPLICATION NAME" and alert_json['severity'] == "critical" and "Ended alert" in alert_json['short_description']:
            os.system ("curl --include --request POST 'https://lon.autoscale.api.rackspacecloud.com/v1.0/execute/1/AUTOSCALE_SCALE_DOWN_WEB_HOOK/' -v")
            print "Scaling down"
            return ""
        else:
            print "No action"
            return ""

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
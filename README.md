###RelicScale

This is a simple Python and Flask RESTful api that sits between Newrelic and Autoscale. This can obviously be used for other tasks but the code her eis exepcting input frpm Newrelic.

This version is looking for alerts sent from a monitored application (not server). Newrelic will trigger an alert based on its APDEX score.


####Setting up server

git clone git@github.com:AutomationSupport/relicscale.git

```
- mkdir /api
- cd api
- virtualenv flask

New python executable in flask/bin/python
Installing setuptools............................done.
Installing pip...................done.

- flask/bin/pip install flask
- copy contents of relicscale into /api
- chmod a+x app.py
- ./app.py
```

You will need to allow port 5000 through the firewall.  

Or deploy via Chef cookbook: https://github.com/niven01/python-api  


####Usage

RelicScale looks for the following application alert criteria

- Application name
- Severity
- Short description

If the crtieria matches specified pattern RelicScale will POST to either the scale up or scale down Autoscale webhook.

In order to configure API you will need to change two parts per Autoscale webhook.  

- APPLICATION NAME
- AUTOSCALE_SCALE_UP_WEB_HOOK or AUTOSCALE_SCALE_DOWN_WEB_HOOK

TO DO:

Improve install  
Run as a service  
Deploy app via chef and install as a service  
Use variables for APPLICATION NAME and WEBHOOKS  


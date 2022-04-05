#import uuid
#import requests
from flask import Flask, render_template
from flask_session import Session  # https://pythonhosted.org/Flask-Session
#import msal
#import pyodbc
#from azure.keyvault.secrets import SecretClient
#from azure.identity import DefaultAzureCredential
import app_config


app = Flask(__name__)
app.config.from_object(app_config)
Session(app)

# This section is needed for url_for("foo", _external=True) to automatically
# generate http scheme when this sample is running on localhost,
# and to generate https scheme when it is deployed behind reversed proxy.
# See also https://flask.palletsprojects.com/en/1.0.x/deploying/wsgi-standalone/#proxy-setups
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

@app.route("/")
def index():
    
    loc_addr='Test Information'
    return render_template('index2.html', loc_id=loc_addr)





#app.jinja_env.globals.update(_build_auth_code_flow=_build_auth_code_flow)  # Used in template

if __name__ == "__main__":
    app.run()


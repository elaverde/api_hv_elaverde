from api.config import app, db
from api.routes import *
from dotenv import load_dotenv
import os
load_dotenv()
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    mode = str(os.environ.get("MODE"))
    if mode == "development":
        app.run(host="0.0.0.0",port=5000,debug=True)
    else:
        app.run(ssl_context=(str(os.environ.get("SSLCertificateFile")), str(os.environ.get("SSLCertificateKeyFile"))), host="0.0.0.0",port=5000,debug=True)
        





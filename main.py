from api.config import app, db
from api.routes import *
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0",port=5000,debug=True)





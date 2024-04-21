from api.config import app
from api.routes import *


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=5000)
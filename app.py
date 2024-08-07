from flask import Flask
from controllers.sentiment import sentiment_blueprint

app = Flask(__name__)
app.register_blueprint(sentiment_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)

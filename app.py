from flask import Flask, render_template
from controllers.product_controller import products_blueprint
from controllers.sport_controller import sports_blueprint

app = Flask(__name__)

app.register_blueprint(products_blueprint)
app.register_blueprint(sports_blueprint)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
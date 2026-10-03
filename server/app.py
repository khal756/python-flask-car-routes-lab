from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flatiron Cars"

@app.route("/<model>")
def car_model(model):
    existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog"
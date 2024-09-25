## Mobile Image Classifier App
from flask import Flask

app = Flask(__name__)

@app.get("/")
def route():
    return {"Hello World"}
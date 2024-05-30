from flask import Flask, render_template
from app.models.crawler import myscraping

from app import app

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/raspar-page")
def raspagem():
    result = myscraping()
    return render_template('pageRaspagem.html', result=result)
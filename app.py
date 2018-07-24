from flask import Flask, render_template, redirect
import pymongo
from scrape_mars import scrape


conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.mars_db

app = Flask(__name__)

@app.route("/scrape")
def scrape_():
    mars_data = scrape()
    db['data'].insert(mars_data)
    return "Data Loaded"

@app.route("/")
def index():
    dict = db.mars.find_one()
    return render_template("index.html", dict=dict)



if __name__ == "__main__":s
    app.run(debug=True)

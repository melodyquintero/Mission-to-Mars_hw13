from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


# create instance of Flask app
app = Flask(__name__)

'''
Add this for new version of flask_pymongo
'''
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app)


@app.route("/")
def index():
    mars_data = mongo.db.mars.find()
    return render_template("index.html", mars_data=mars_data)

@app.route("/scrape")
def scrape():
    # Run scraped functions
    mars_data = scrape_mars.scrape()
    mongo.db.mars.insert(mars_data)
   
    return render_template("index.html", mars_data=mars_data)




if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo 
import scrape_mars

app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/meh_app")

@app.route("/")
def home():
    mars_mash = mongo.db.collection.find_one()
    
    return render_template("index.html", monster=mars_mash)

@app.route("/scrape")
def scraper():
    mars_dict = scrape_mars.scrape()
    mongo.db.collection.update({}, mars_dict, upsert=True)

    return redirect("/", code =302)

if __name__ == "__main__":
    app.run(debug=True)
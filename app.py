from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo 
import scrape

app = Flask(__name__)


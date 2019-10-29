import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)


app.config['MONGO_DBNAME'] = 'mileston-project'
app.config['MONGO_URI'] = 'mongodb+srv://Cat:Kot@myfirstcluster-tlipu.mongodb.net/milestone-project?retryWrites=true&w=majority'
mongo = PyMongo(app)

@app.route('/')

@app.route('/main')
def main():
    return render_template('main.html', 
                            tasks=mongo.db.tasks.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
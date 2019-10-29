{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":40,"position":40,"stack":[[{"start":{"row":0,"column":0},"end":{"row":13,"column":0},"action":"insert","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId","","app = Flask(__name__)","","app.config['MONGO_DBNAME'] = 'task_manager'","app.config['MONGO_URI'] = 'mongodb+srv://Cat:Kot@myfirstcluster-tlipu.mongodb.net/task_manager?retryWrites=true&w=majority'","","mongo = PyMongo(app)","","@app.route('/')",""],"id":1}],[{"start":{"row":7,"column":0},"end":{"row":10,"column":20},"action":"remove","lines":["app.config['MONGO_DBNAME'] = 'task_manager'","app.config['MONGO_URI'] = 'mongodb+srv://Cat:Kot@myfirstcluster-tlipu.mongodb.net/task_manager?retryWrites=true&w=majority'","","mongo = PyMongo(app)"],"id":2}],[{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":12,"column":0},"end":{"row":15,"column":23},"action":"insert","lines":["if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":4}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":1},"action":"insert","lines":["d"],"id":5},{"start":{"row":10,"column":1},"end":{"row":10,"column":2},"action":"insert","lines":["e"]},{"start":{"row":10,"column":2},"end":{"row":10,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":10,"column":3},"end":{"row":10,"column":4},"action":"insert","lines":[" "],"id":6},{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":["h"]}],[{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"insert","lines":["e"],"id":7},{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"insert","lines":["l"]},{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"insert","lines":["l"]},{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["o"]}],[{"start":{"row":10,"column":9},"end":{"row":10,"column":11},"action":"insert","lines":["()"],"id":8}],[{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"insert","lines":[":"],"id":9}],[{"start":{"row":10,"column":12},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":10},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]},{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"insert","lines":["r"]},{"start":{"row":11,"column":5},"end":{"row":11,"column":6},"action":"insert","lines":["e"]},{"start":{"row":11,"column":6},"end":{"row":11,"column":7},"action":"insert","lines":["t"]},{"start":{"row":11,"column":7},"end":{"row":11,"column":8},"action":"insert","lines":["u"]}],[{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"insert","lines":["r"],"id":11},{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"insert","lines":[" "],"id":12}],[{"start":{"row":11,"column":11},"end":{"row":11,"column":13},"action":"insert","lines":["''"],"id":13}],[{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"insert","lines":["h"],"id":14},{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"insert","lines":["e"]},{"start":{"row":11,"column":14},"end":{"row":11,"column":15},"action":"insert","lines":["l"]},{"start":{"row":11,"column":15},"end":{"row":11,"column":16},"action":"insert","lines":["l"]},{"start":{"row":11,"column":16},"end":{"row":11,"column":17},"action":"insert","lines":["o"]}],[{"start":{"row":11,"column":17},"end":{"row":11,"column":18},"action":"insert","lines":[" "],"id":15},{"start":{"row":11,"column":18},"end":{"row":11,"column":19},"action":"insert","lines":["w"]},{"start":{"row":11,"column":19},"end":{"row":11,"column":20},"action":"insert","lines":["o"]},{"start":{"row":11,"column":20},"end":{"row":11,"column":21},"action":"insert","lines":["r"]},{"start":{"row":11,"column":21},"end":{"row":11,"column":22},"action":"insert","lines":["l"]},{"start":{"row":11,"column":22},"end":{"row":11,"column":23},"action":"insert","lines":["d"]}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":20},"action":"insert","lines":["mongo = PyMongo(app)"],"id":16}],[{"start":{"row":10,"column":0},"end":{"row":11,"column":24},"action":"remove","lines":["def hello():","    return 'hello world'"],"id":17}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":1},"action":"insert","lines":["@"],"id":18},{"start":{"row":10,"column":1},"end":{"row":10,"column":2},"action":"insert","lines":["a"]},{"start":{"row":10,"column":2},"end":{"row":10,"column":3},"action":"insert","lines":["p"]},{"start":{"row":10,"column":3},"end":{"row":10,"column":4},"action":"insert","lines":["p"]}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":["."],"id":19},{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"insert","lines":["r"]},{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"insert","lines":["o"]},{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"insert","lines":["u"]},{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["t"]},{"start":{"row":10,"column":9},"end":{"row":10,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"insert","lines":[" "],"id":20}],[{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"remove","lines":[" "],"id":21}],[{"start":{"row":10,"column":10},"end":{"row":10,"column":12},"action":"insert","lines":["()"],"id":22}],[{"start":{"row":10,"column":11},"end":{"row":10,"column":13},"action":"insert","lines":["''"],"id":23}],[{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"insert","lines":["/"],"id":24},{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"insert","lines":["m"]},{"start":{"row":10,"column":14},"end":{"row":10,"column":15},"action":"insert","lines":["a"]},{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"insert","lines":["i"]},{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"insert","lines":["n"]}],[{"start":{"row":10,"column":19},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":25},{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"insert","lines":["d"]},{"start":{"row":11,"column":1},"end":{"row":11,"column":2},"action":"insert","lines":["e"]},{"start":{"row":11,"column":2},"end":{"row":11,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":11,"column":3},"end":{"row":11,"column":4},"action":"insert","lines":[" "],"id":26},{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"insert","lines":["m"]},{"start":{"row":11,"column":5},"end":{"row":11,"column":6},"action":"insert","lines":["a"]},{"start":{"row":11,"column":6},"end":{"row":11,"column":7},"action":"insert","lines":["i"]},{"start":{"row":11,"column":7},"end":{"row":11,"column":8},"action":"insert","lines":["n"]}],[{"start":{"row":11,"column":8},"end":{"row":11,"column":10},"action":"insert","lines":["()"],"id":27}],[{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"insert","lines":[":"],"id":28}],[{"start":{"row":11,"column":11},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":29},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":12,"column":4},"end":{"row":13,"column":56},"action":"insert","lines":["return render_template('tasks.html', ","                            tasks=mongo.db.tasks.find())"],"id":30}],[{"start":{"row":12,"column":28},"end":{"row":12,"column":33},"action":"remove","lines":["tasks"],"id":31},{"start":{"row":12,"column":28},"end":{"row":12,"column":29},"action":"insert","lines":["m"]},{"start":{"row":12,"column":29},"end":{"row":12,"column":30},"action":"insert","lines":["a"]},{"start":{"row":12,"column":30},"end":{"row":12,"column":31},"action":"insert","lines":["i"]},{"start":{"row":12,"column":31},"end":{"row":12,"column":32},"action":"insert","lines":["n"]}],[{"start":{"row":9,"column":15},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":32}],[{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":33},{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":43},"action":"insert","lines":["app.config['MONGO_DBNAME'] = 'task_manager'"],"id":34}],[{"start":{"row":8,"column":30},"end":{"row":8,"column":42},"action":"remove","lines":["task_manager"],"id":35},{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":["m"]},{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"insert","lines":["i"]},{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"insert","lines":["l"]},{"start":{"row":8,"column":33},"end":{"row":8,"column":34},"action":"insert","lines":["e"]},{"start":{"row":8,"column":34},"end":{"row":8,"column":35},"action":"insert","lines":["s"]},{"start":{"row":8,"column":35},"end":{"row":8,"column":36},"action":"insert","lines":["t"]},{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"insert","lines":["o"]},{"start":{"row":8,"column":37},"end":{"row":8,"column":38},"action":"insert","lines":["n"]}],[{"start":{"row":8,"column":38},"end":{"row":8,"column":39},"action":"insert","lines":["-"],"id":36},{"start":{"row":8,"column":39},"end":{"row":8,"column":40},"action":"insert","lines":["p"]},{"start":{"row":8,"column":40},"end":{"row":8,"column":41},"action":"insert","lines":["r"]},{"start":{"row":8,"column":41},"end":{"row":8,"column":42},"action":"insert","lines":["o"]},{"start":{"row":8,"column":42},"end":{"row":8,"column":43},"action":"insert","lines":["j"]},{"start":{"row":8,"column":43},"end":{"row":8,"column":44},"action":"insert","lines":["e"]},{"start":{"row":8,"column":44},"end":{"row":8,"column":45},"action":"insert","lines":["c"]},{"start":{"row":8,"column":45},"end":{"row":8,"column":46},"action":"insert","lines":["t"]}],[{"start":{"row":8,"column":47},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":37}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":123},"action":"insert","lines":["app.config['MONGO_URI'] = 'mongodb+srv://Cat:Kot@myfirstcluster-tlipu.mongodb.net/task_manager?retryWrites=true&w=majority'"],"id":38}],[{"start":{"row":9,"column":82},"end":{"row":9,"column":94},"action":"remove","lines":["task_manager"],"id":39},{"start":{"row":9,"column":82},"end":{"row":9,"column":83},"action":"insert","lines":["m"]},{"start":{"row":9,"column":83},"end":{"row":9,"column":84},"action":"insert","lines":["i"]},{"start":{"row":9,"column":84},"end":{"row":9,"column":85},"action":"insert","lines":["l"]},{"start":{"row":9,"column":85},"end":{"row":9,"column":86},"action":"insert","lines":["e"]},{"start":{"row":9,"column":86},"end":{"row":9,"column":87},"action":"insert","lines":["s"]},{"start":{"row":9,"column":87},"end":{"row":9,"column":88},"action":"insert","lines":["t"]},{"start":{"row":9,"column":88},"end":{"row":9,"column":89},"action":"insert","lines":["o"]},{"start":{"row":9,"column":89},"end":{"row":9,"column":90},"action":"insert","lines":["n"]},{"start":{"row":9,"column":90},"end":{"row":9,"column":91},"action":"insert","lines":["e"]}],[{"start":{"row":9,"column":91},"end":{"row":9,"column":92},"action":"insert","lines":["-"],"id":40},{"start":{"row":9,"column":92},"end":{"row":9,"column":93},"action":"insert","lines":["p"]},{"start":{"row":9,"column":93},"end":{"row":9,"column":94},"action":"insert","lines":["r"]},{"start":{"row":9,"column":94},"end":{"row":9,"column":95},"action":"insert","lines":["o"]}],[{"start":{"row":9,"column":95},"end":{"row":9,"column":96},"action":"insert","lines":["j"],"id":41},{"start":{"row":9,"column":96},"end":{"row":9,"column":97},"action":"insert","lines":["e"]},{"start":{"row":9,"column":97},"end":{"row":9,"column":98},"action":"insert","lines":["c"]},{"start":{"row":9,"column":98},"end":{"row":9,"column":99},"action":"insert","lines":["t"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":99},"end":{"row":9,"column":99},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1572352122387,"hash":"fcb9158f9311628ac0aad18c4cd79fdb87d5276e"}
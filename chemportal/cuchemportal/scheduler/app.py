from cuchemportal.scheduler.workerB import trim_string
from cuchemportal.scheduler.workerA import concatenate_strings
from flask import (
   Flask,
   request,
   jsonify,
)
@app.route("/add")
def add():
   first_str = request.args.get('first_num')
   second_str = request.args.get('second_num')
   result = concatenate_strings.delay(first_str, second_str )
   return jsonify({'result': result}), 200


@app.route("/subtract")
def subtract():
   first_str = request.args.get('first_num')
   result = trim_string.delay(first_str)
   return jsonify({'result': result}), 200


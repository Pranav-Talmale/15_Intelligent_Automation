from flask import Flask, request, jsonify
from vanna.remote import VannaDefault
from vanna.ollama import Ollama
from vanna.vannadb.vannadb_vector import VannaDB_VectorStore

vanna_model_name="chinnok"
vanna_api_key = "b74e1cedb9064cc0ba33b7d4fb2e47c9"

class MyVanna(VannaDB_VectorStore, Ollama):
    def __init__(self, config=None):
        MY_VANNA_MODEL = "chinnok"
        VannaDB_VectorStore.__init__(self, vanna_model=MY_VANNA_MODEL, vanna_api_key="b74e1cedb9064cc0ba33b7d4fb2e47c9", config=config)
        Ollama.__init__(self, config=config)

vn = MyVanna(config={'model': 'stable-code'})

#Connect to DB
vn.connect_to_mysql(
    host="localhost",
    dbname="emp_database",
    user="root",
    password="12345",
    port=3306
)

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def route1():
    # Extracting the 'param' field from form-encoded POST data
    question = request.form.get('question', 'default_value')
    sql = vn.generate_sql(question)
    df = vn.run_sql(sql)
    summary = vn.generate_summary(question=question, df=df)
    
    # Constructing the response object
    response = {
        'answer': summary,
        'question': question
    }
    
    # Returning the response as JSON
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)

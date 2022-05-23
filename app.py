from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import json
import qrcode

app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''

# init MYSQL
mysql = MySQL(app)


# First route auto-create
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# First test get method
@app.get('/test')
def test():
    return 'Test'


# Method that return the json request
@app.route('/getRequest')
def get_request():
    data = request.json
    return jsonify(data)


# Method that add a Person Object in MySQL Database
@app.post('/add')
def add():
    try:
        conn = mysql.connection
        cur = conn.cursor()
        data = request.json
        nome = data['nome']
        cognome = data['cognome']
        cur.execute("INSERT INTO new_table (Nome, Cognome) VALUES (%s, %s)", (nome, cognome))
        conn.commit()
        description = 'E stato inserito correttamente la persona ' + nome + ' ' + cognome
        return json.dumps({'Result': 'OK', 'Description': description})
    except:
        description = 'Errore durante l inserimento della persona'
        return json.dumps({'Result': 'OK', 'Description': description})


# Method that return all Person in MySQL Database
@app.route('/getAll')
def get_all():
    conn = mysql.connection
    cur = conn.cursor()
    cur.execute("SELECT * FROM new_table")
    data = cur.fetchall()
    return jsonify(data)


if __name__ == '__main__':
    app.run()

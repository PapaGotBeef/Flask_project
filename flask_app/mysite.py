from flask import Flask
from flask import render_template
from flask import request
import sqlite3 as sql
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)
@app.route('/stock')
def list_data():
    
    conn = sql.connect('inv.db')
    conn.row_factory = sql.Row
    cur = conn.cursor()
    cur.execute('SELECT * FROM stock')
    rows =cur.fetchall()
    return render_template("stock.html", rows = rows)
@app.route('/boot')
def bootpage():
    return render_template("boot.html")
@app.route('/')
def greetings():
    return render_template('greetings.html')






@app.route('/addrecord', methods=["POST"])
def add_record():
    if request.method == "POST":
        name = request.form['nm']
        id = request.form['id']
        price = request.form['pc']
        description = request.form['ds']
        qty = request.form['qty']
        with sql.connect('inv.db') as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO Stock (name,id,price,description,qty) VALUES (?,?,?,?,?)", [name,id,price,description,qty])
        conn.commit()

        return render_template('stock.html')

@app.route('/itemform')
def contact_form():
    return render_template('form.html')

def createdatabase():
    con = sql.connect('inv.db')
    con.execute("CREATE TABLE Stock (name TEXT, id INT, price DECIMAL, description VARCHAR(200), qty INT)" )

#createdatabase()

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, g, request
import os
import sqlite3
import json


app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='admin',
    DATABASE=os.path.join(app.root_path, 'db.sqlite'),
    SITE_NAME='Python rest API'
))


def get_db():
    """Funkcja tworząca połączenie z bazą danych"""
    if not g.get('db'):  # jeżeli brak połączenia, to je tworzymy
        con = sqlite3.connect(app.config['DATABASE'])
        con.row_factory = sqlite3.Row
        g.db = con  # zapisujemy połączenie w kontekście aplikacji
    return g.db  # zwracamy połączenie z bazą


# @app.teardown_appcontext
# def close_db(error):
#     """Zamykanie połączenia z bazą"""
#     if g.get('db'):
#         g.db.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        name = request.json.get('name', "")
        surname = request.json.get('surname', "")
        db = get_db()
        db.execute('INSERT INTO users VALUES (?, ?, ?, ?);',
                   [None, name, surname, 0])
        db.commit()
        return "Dodano "+str(name)+" "+str(surname)+"\n"

    db = get_db()
    kursor = db.execute('SELECT * FROM users ORDER BY id DESC LIMIT 10;')
    selected_users = kursor.fetchall()
    return json.dumps([dict(ix) for ix in selected_users])
    # return render_template('users.html', users=users)


@app.route('/users/<int:user_id>', methods=['GET'])
def user(user_id):
    db = get_db()
    kursor = db.execute('select * from users where id = ?;',
                        [user_id])
    selected_users = kursor.fetchall()
    return json.dumps([dict(ix) for ix in selected_users])


@app.route('/oferts', methods=['GET', 'POST'])
def oferts():
    if request.method == 'POST':
        title = request.json['title']
        time = request.json.get('time', 0)
        owner = request.json.get('owner', 0)
        db = get_db()
        db.execute('INSERT INTO oferts VALUES (?, ?, ?, ?, ?);',
                   [None, title, time, 0, owner])
        db.commit()

        db.execute('update users set time = time - ? where id = ?;',
                   [time, owner])
        db.commit()
        return "Dodano "+str(title)+" "+str(time)+"\n"
        # return redirect(url_for('oferts'))

    db = get_db()
    kursor = db.execute('SELECT * FROM oferts ORDER BY id DESC LIMIT 10;')
    oferts = kursor.fetchall()
    return json.dumps([dict(ix) for ix in oferts])  # CREATE JSON


@app.route('/endofert', methods=['POST'])
def end_ofert():
    ofert_id = request.json.get('ofert_id', 0)
    user_id = request.json.get('user_id', 0)
    db = get_db()
    db.execute('update users set time = time + '
               '(select time from oferts where id = ? )where id = ?;',
               [ofert_id, user_id])
    db.commit()
    db.execute('update oferts set end = 1 where id = ?;',
               [ofert_id])
    db.commit()
    return "Zarezerwowano prace"


if __name__ == '__main__':
    app.run(debug=True)

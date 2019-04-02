from flask import Flask, render_template, request, json, session, url_for, redirect,  escape
import pymysql
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)


class ServerError(Exception): pass


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Gareth123!', db='BucketList')
    cursor = conn.cursor()
    try:

        # read the posted values from the UI
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:

            # All Good, let's call MySQL

            _hashed_password = generate_password_hash(_password)
            # print("length hashed password: ", len(_hashed_password))
            cursor.callproc('sp_createUser', (_name, _email, _hashed_password))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message': 'User created successfully !'})
            else:
                return json.dumps({'error': str(data[0])})
        else:
            return json.dumps({'html': '<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error': str(e)})
    finally:
        cursor.close()
        conn.close()


@app.route('/showLogin')
def showLogin():
    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Gareth123!', db='BucketList')
    cursor = conn.cursor()
    if 'username' in session:
        return redirect(url_for('index'))

    error = None
    try:
        if request.method == 'POST':
            username_form = "\"{}\"".format(request.form['username'])
            cursor.execute("SELECT COUNT(1) FROM tbl_user WHERE user_username = {};".format(username_form))

            if not cursor.fetchone()[0]:
                return json.dumps({'html': '<span>Invalid Username</span>'})
                # raise ServerError('Invalid username')

            # password_form = "\"{}\"".format(request.form['password'])
            password_form = request.form['password']
            cursor.execute("SELECT user_password FROM tbl_user WHERE user_username = {};".format(username_form))

            for row in cursor.fetchall():
                if check_password_hash(row[0], password_form):
                    session['username'] = request.form['username']
                    return redirect(url_for('index'))

            # raise ServerError('Invalid password')
            return json.dumps({'html': '<span>Invalid Password</span>'})
    # except ServerError as e:
    except Exception as e:
        # error = str(e)
        return json.dumps({'error': str(e)})
    finally:
        cursor.close()
        conn.close()

    # return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(port=5000)

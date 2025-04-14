from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from mfa_utils import generate_otp, send_otp_email, is_otp_valid
from datetime import datetime, timedelta
import bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# User Table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    otp = db.Column(db.String(6))
    otp_expiry = db.Column(db.DateTime)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        passwd = request.form['password'].encode('utf-8')
        user = User.query.filter_by(username=uname).first()
        if user and bcrypt.checkpw(passwd, user.password):
            otp = generate_otp()
            user.otp = otp
            user.otp_expiry = datetime.now() + timedelta(minutes=5)
            db.session.commit()
            send_otp_email(user.email, otp)
            session['user_id'] = user.id
            return redirect('/verify')
        else:
            flash("Invalid credentials")
    return render_template('login.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        entered_otp = request.form['otp']
        user = User.query.get(session.get('user_id'))
        if user and is_otp_valid(user, entered_otp):
            return render_template('success.html')
        else:
            flash("Invalid or expired OTP")
    return render_template('verify.html')

if __name__ == '__main__':
    app.run(debug=True)

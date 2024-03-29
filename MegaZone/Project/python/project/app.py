import logging
import sys
from flask import Flask, render_template, request
from sqlalchemy import create_engine


app = Flask(__name__, template_folder="templates")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        message = request.form["message"]
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        DB_USER = 'admin'
        DB_PW = 'kosa0401'
        DB_ADDR = 'conference.ckcz3uuj9vbl.ap-northeast-2.rds.amazonaws.com'
        DB_PORT = 3306
        DB_NAME = 'conference'
        engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PW}@{DB_ADDR}:{DB_PORT}/{DB_NAME}')
        conn = engine.connect()
        conn.execute("CREATE TABLE IF NOT EXISTS conference(id int NOT NULL AUTO_INCREMENT, message varchar(255), name varchar(30), email varchar(255), subject varchar(100) , PRIMARY KEY(id));")
        conn.execute(f"INSERT INTO conference(message,name,email,subject) VALUES('{message}','{name}','{email}','{subject}')")
        conn.close()
        return render_template("index.html")
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run()
import re
from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:Muthu981156@localhost/height_collector'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    height = db.Column(db.Integer)

    def __init__(self, email, height) -> None:
        super().__init__()
        self.email = email
        self.height = height


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=["POST"])
def success():
    if request.method == "POST":
        global file_object
        file_object = request.files["file"]        

        filename = "uploaded" + file_object.filename
        print(filename)
        file_object.save("uploaded" + file_object.filename)
        with open("uploaded" + file_object.filename, "a") as f:
            f.write("Hi")

        return render_template("index.html", btn="download.html")
        # email_id = request.form["email_name"]
        # height = request.form["height_name"]
        # if db.session.query(Data).filter(Data.email == email_id).count() <= 0:
        #     data = Data(email_id, height)
        #     db.session.add(data)
        #     db.session.commit()
        #     average_height = int(db.session.query(
        #         func.avg(Data.height)).scalar())
        #     count = db.session.query(Data.height).count()
        #     send_email(email_id, height, average_height, count)
        #     return render_template("success.html")
        # else:
        #     return render_template("index.html", text="Email is already available")

@app.route("/download")
def download():
    return send_file("uploaded" + file_object.filename, attachment_filename="new.html", as_attachment=True)


if __name__ == "__main__":
    app.debug = True
    app.run()

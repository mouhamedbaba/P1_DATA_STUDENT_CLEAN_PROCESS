
from manage import Manage
from flask import Flask, jsonify, redirect, render_template, request, url_for
import json
manage = Manage()
app = Flask(__name__)

def get_data():
    try :
        with open("data/valid_data.json") as file:
            data = json.load(file)
    except FileNotFoundError :
        print("Fichier non trouve")
    except json.JSONDecodeError :
        print("Le ficher est vide ou n'est pas valid")
    return data


@app.route("/search")
def search():
    num = request.args.get("num")
    students = get_data()
    students = manage.search_by_num(students, num.upper())
    return render_template("tr.html", students=students)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/api/data")
def all_data():
    data = get_data()
    return render_template("tr.html", students=data)


# @app.route("/page=<int:page>/")
# def paginate(page=1):
#     par_page=10
#     data =  get_data()
#     minimum = (page - 1) * par_page
#     maximum = page * par_page
#     np = len(data) // par_page
#     data = data[minimum:maximum]
#     return render_template("index.html", students=data, page=page, np=np)
@app.errorhandler(code_or_exception=404)
def page_404(error):
    return render_template("404.html")

if __name__ == "__main__" :
    app.run(debug=True)



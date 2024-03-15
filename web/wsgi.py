
from app import App
from flask import Flask, render_template, request
import json
app = App()
flak_app = Flask(__name__)

def get_data():
    try :
        with open("data/valid_data.json") as file:
            data = json.load(file)
    except FileNotFoundError :
        print("Fichier non trouve")
    except json.JSONDecodeError :
        print("Le ficher est vide ou n'est pas valid")
    return data


@flak_app.route("/search")
def search():
    num = request.args.get("num")
    students = get_data()
    students = app.search_by_num(students, num)
    return render_template("search.html", students=students)


@flak_app.route("/page=<int:page>/")
def paginate(page=1):
    par_page=10
    data =  get_data()
    minimum = (page - 1) * par_page
    maximum = page * par_page
    np = len(data) // par_page
    data = data[minimum:maximum]
    return render_template("index.html", students=data, page=page, np=np)
@flak_app.errorhandler(code_or_exception=404)
def page_404(error):
    return render_template("404.html")

if __name__ == "__main__" :
    flak_app.run(debug=True)



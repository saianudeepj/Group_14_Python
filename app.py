from flask import Flask, render_template
import sqlite3
import pathlib

app = Flask(__name__) 

base_path = pathlib.Path().cwd()
db_name = "global_videogame_sales.db"
file_path = base_path / db_name


@app.route("/")
def index():
    return render_template( "index_page.html")

@app.route("/about")
def about():
    return render_template( "about_data.html")

@app.route("/data")
def data():
    con = sqlite3.connect(file_path)
    cursor = con.cursor()
    videogame_sales = cursor.execute("SELECT * FROM videogame_sales").fetchall()
    con.close()
    return render_template( "data_table.html", videogame_sales = videogame_sales)


if __name__=="__main__":
    app.run(debug=True)
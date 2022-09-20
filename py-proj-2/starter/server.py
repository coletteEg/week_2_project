from flask import Flask, render_template

app = Flask(__name__)

from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary

@app.route("/")
def home():
    cupcakes = get_cupcakes("cupcake_list.csv")
    order = get_cupcakes("order.csv")
    order_total = round(sum([float(x["price"]) for x in order]), 2)
    return render_template("index.html", cupcakes=cupcakes, items_num=len(order), order_total=order_total)

@app.route("/cupcake_list")
def all_cupcakes():
    return render_template("all_cupcakes.html")

@app.route("/single_cupcake/<name>")
def single_cupcake(name):
    cupcake = find_cupcake("cupcake_list.csv", name)
    
    if cupcake:
        return render_template("one_cupcake.html", cupcake=cupcake)
    else:
        return "Mama Gothel couldn't find your cupcake."

@app.route("/adding_cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("cupcake_list.csv", name)

    if cupcake:
        add_cupcake_dictionary("order.csv", cupcake=cupcake)
        return redirect(url_for("home"))
    else:
        return "Mama Gothel couldn't find your cupcake."

@app.route("/order")
def order():
    cupcakes=get_cupcakes("order.csv")

    cupcakes_counted = []
    cupcake_set = set()

    for cupcake in cupcakes:
        cupcake_set.add((cupcake["name"], cupcake["price"], cupcakes.count(cupcake)))


    return render_template("order.html", cupcakes=cupcake_set)

if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 8000, host = "localhost")
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<x>/<y>/<color1>/<color2>")
def index(x,y, color1, color2):
    return render_template("index.html", color_one = color1, color_two = color2, var_x = int(x), var_y = int(y))

if __name__ == '__main__':
    app.run(debug= True)

from flask import *
import time
import os

app = Flask(__name__)

def timer(arg=-1):
    if arg == -1:
        file = int(open("main").read().strip())
        num = file-1
        os.remove("main")
        with open("main", "w") as main:
            main.write(str(num))
        if num == -1:
            with open("main", "w") as main:
                main.write(open("priority").read().strip().split()[0])
            return 0
        else:
            return file
    else:
        return open("options").read().strip().split()[1]

@app.route("/")
def principal():
    x = int(open("main").read().strip()) 
    y = open("options").read().strip().split()[0]
    z = open("options").read().strip().split()[1]
    return render_template("index.html", data=[x, y, z])

@app.route("/cronometro")
def index():
    data = timer()

    #if data == 0:
     #   time.sleep(1)
      #  return redirect("/cronometro")
    #else:
    return render_template("cronometro.html", data=data)

@app.route("/start", methods=["POST"])
def start():
    return redirect("/cronometro")

@app.route("/reset1", methods=["POST"])
def reset1():
    os.remove("main")
    with open("priority", "w") as p:
        p.write(open("options").read().strip().split()[0])
    with open("main", "w") as main:
        main.write(open("options").read().strip().split()[0])
        return redirect("/cronometro")

@app.route("/reset2", methods=["POST"])
def reset2():
    os.remove("main")
    with open("priority", "w") as p:
        p.write(open("options").read().strip().split()[1])
    with open("main", "w") as main:
        main.write(open("options").read().strip().split()[1])
        return redirect("/cronometro")

@app.route("/pause", methods=["POST"])
def pause():
    dato = int(open("main").read().strip())
    p1 = open("priority").read().strip()[0]
    p2 = open("priority").read().strip()[1]
    os.remove("main")
    with open("main", "w") as main:
        if dato != p1 or dato != p2 and dato < p1: main.write(str(dato+1))
        else: main.write(str(dato))
    return redirect("/") 

@app.route("/res", methods=["POST"])
def res():
    dato = int(open("main").read().strip())
    os.remove("main")
    with open("main", "w") as main:
        main.write(str(dato-1))
    return redirect("/")

@app.route("/sum", methods=["POST"])
def sum():
    dato = int(open("main").read().strip())
    os.remove("main")
    with open("main", "w") as main:
        main.write(str(dato+1))
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)

from flask import Flask,redirect,url_for
import time
app=Flask(__name__)

@app.route("/")

def home():
    return "<h1> Welcome to the home page</h1>"

@app.route("/pass/<sname>/<int:marks>")
def passed(sname,marks):
    return f"<h1> Welcome Brother {sname.title()} you had achieved {marks}</h1>"

@app.route("/Fail/<sname>/<int:marks>")
def failed(sname,marks):
    return f"<h1> Work Hard {sname.title()}, Work work work work>{marks} </h1>"

@app.route("/score/<name>/<int:num>")

def score(name,num):
    if num<30:
        time.sleep(1)
        return redirect(url_for("failed",sname=name,marks=num))
    else:
        time.sleep(1)
        return redirect(url_for("passed",sname=name,marks=num))
if __name__=="__main__":
    app.run(debug=True)
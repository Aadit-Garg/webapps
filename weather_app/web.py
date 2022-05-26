from flask import Flask,render_template,url_for
import scr

app = Flask(__name__)

@app.route("/")
def main():
    print ("restarting")
    for i in range(2):
        a,b,c,d,e,f,g,h,ip = scr.get_info()
    h = h.upper()
    a = a.upper()
    print(f)
    return render_template("main_weather.html",a=a,b=b,c=c,d=d,e=e,f=f,g=g,h=h)

app.run(debug=True)


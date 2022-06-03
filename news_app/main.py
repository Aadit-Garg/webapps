from flask import Flask,render_template,url_for
import scr
app = Flask(__name__)


names, titles, descs, articles, imgs, links =scr.get_news()
total = len(imgs)
for img in imgs:
    if img:
        print(img)
@app.route("/")
def main():
    return render_template("main.html",tot=total, n=names, t=titles, d=descs, a=articles, i=imgs, l=links)

app.run(debug=True)
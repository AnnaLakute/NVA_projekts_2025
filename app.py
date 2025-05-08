from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/par_mums')
def par_mums():
  return render_template("par_mums.html")

@app.route('/MD')
def MD():
  return render_template("MD.html")

@app.route('/aptauja')
def aptauja():
  return render_template("aptauja.html")

@app.route('/kontakti')
def kontakti():
  return render_template("kontakti.html")

@app.route('/pamati_sintakse')
def pamati_sintakse():
  return render_template("pamati_sintakse.html")

if __name__=="__main__":
  app.run(debug=True)
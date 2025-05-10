from flask import Flask, render_template, url_for, request
import requests
import csv

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

@app.route('/kontakti')
def kontakti():
  return render_template("kontakti.html")

@app.route('/pamati_sintakse')
def pamati_sintakse():
  return render_template("pamati_sintakse.html")

@app.route('/sveiciens')
def sveiciens():
  return render_template("sveiciens.html")

@app.route('/mainigie')
def mainigie():
  vards = "Igors"
  vecums = 35
  skaitlis1 = 4
  skaitlis2 = 6
  summa = skaitlis1 + skaitlis2 
  print(summa)
  return render_template("mainigie.html", vards= vards, vecums=vecums, summa=summa, skaitlis1= skaitlis1,  skaitlis2= skaitlis2)


@app.route('/datu_tipi')
def datu_tipi():
  teksts = "Sveicieni! Šis ir teksts"
  skaitlis = 100
  decimals = 10.5
  saraksts = ["vards", 2, 3, 4, 5] 
  mans_dict = {"vards": "Anna", "vecums":20}
  mans_kopa = {1,2,3,4,5}
  return render_template("datu_tipi.html", teksts=teksts, skaitlis=skaitlis, decimals=decimals, saraksts=saraksts, mans_dict=mans_dict, mans_kopa=mans_kopa)


@app.route('/operatori')
def operatori():
  a = 13
  b = 13
  summa = a + b
  starpiba = a - b
  reizinajums = a * b
  dalijums = a / b
  atlikums = a % b
  vienads = (a == b)
  print(summa)
  print(atlikums)
  print(vienads)
  return render_template("operatori.html", summa = summa, starpiba=starpiba,reizinajums=reizinajums, dalijums=dalijums,  atlikums=atlikums, vienads=vienads)

@app.route('/kontroles_strukturas')
def kontroles_strukturas():
  x = 4
  if x >= 40 and x <= 50 :
    rezultats = "ir tādi darbinieki"
    print(rezultats)
  else: 
    rezultats = "neatbilst"
    print(rezultats)
    
  for_cikls_rezultats = [i for i in range(1,11)]
  
  while_cikla_rezultats = []
  y = 0
  while y<= 5:
    while_cikla_rezultats.append(y)
    y = y + 1
  
  return render_template("kontroles_strukturas.html", rezultats= rezultats,for_cikls_rezultats=for_cikls_rezultats, while_cikla_rezultats=while_cikla_rezultats)

@app.route('/funkcijas')
def funkcijas():
  def sveiciens(vards="Pēteris", uzvards = "Bērziņš"):
    return "Sveiks, " + vards + " " + uzvards + "!"
  noklusejuma_sveiciens=sveiciens()
  izmainitais_sveiciens= sveiciens("Zane","Ķaspasrs")
  return render_template("funkcijas.html",noklusejuma_sveiciens=noklusejuma_sveiciens,izmainitais_sveiciens=izmainitais_sveiciens)
  
@app.route('/ievade_izvade', methods=['GET','POST'])
def ievade_izvade():
  if request.method =='POST':
    vards=request.form['vards']
    return render_template("ievade_izvade.html", vards=vards)
  return render_template("ievade_izvade.html", vards=None)
  
@app.route('/failu_apstrade')
def failu_apstrade(): 
  saturs = ""
  try: 
    with open('piemers.txt', 'r') as fails:
      saturs = fails.read()
  except IOError:
      saturs = "Fails nav atrasts!"
  return render_template("failu_apstrade.html", saturs=saturs)

@app.route('/oop')
def oop(): 
  class Person:
    def __init__ (self, vards, vecums):
      self.vards= vards
      self.vecums = vecums
    def sveiciens(self):
      return "Sveiki, mani sauc " + self.vards + " un mans vecums ir " + self.vecums + " gadi."
  
  persona = Person("Jānis", "30")
  sveiciens = persona.sveiciens()   
  
  return render_template("oop.html", sveiciens = sveiciens)
  
@app.route('/moduli')
def moduli():   
  import math
  sqrt_rezultats = math.sqrt(16)
  print(sqrt_rezultats)
  pow_rezultats = math.pow(4,2)
  print(pow_rezultats)
  
  return render_template("moduli.html",sqrt_rezultats=sqrt_rezultats,pow_rezultats=pow_rezultats)
  
@app.route('/joks')
def joks():   
  url = 'http://api.chucknorris.io/jokes/random'
  atbilde = requests.get(url)
  print(atbilde)
  dati=atbilde.json()
  print(dati)
  print(dati['value'])
  return render_template("joks.html", joks=dati['value'], adrese=dati['url'], avatars= dati['icon_url'])
  
@app.route('/csv2')
def csv2():  
  with open("dati.csv", mode='r', encoding="utf-8") as fails:
    csv_lasitajs=csv.reader(fails)
    dati=list(csv_lasitajs)
    print(csv_lasitajs)
  return render_template('csv2.html', dati = dati[1])
  
@app.route('/aptauja')
def aptauja():   
  return render_template('aptauja.html')
  
  
if __name__=="__main__":
  app.run(debug=True)
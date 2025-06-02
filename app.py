from flask import Flask, render_template, url_for, request, session, redirect
import requests
import csv
import os
import sqlite3
import json

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = "manaatslega"

def init_db():
  conn=sqlite3.connect('DB_NVA.db')
  cursor = conn.cursor()
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS lietotaji (
      "id" INTEGER UNIQUE,
      "vards" TEXT NOT NULL,
      "dzimums" TEXT NOT NULL,
      "hobiji" TEXT NOT NULL,
      PRIMARY KEY("id" AUTOINCREMENT)
    )
  ''')
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS ADMIN (
      "id" INTEGER UNIQUE,
      "login" TEXT NOT NULL,
      "password" TEXT NOT NULL,
      PRIMARY KEY("id" AUTOINCREMENT)
     )
  '''  )
  cursor.execute('SELECT * FROM ADMIN WHERE login = ?',('admin',))
  if not cursor.fetchone():
    cursor.execute('INSERT INTO ADMIN (login, password) VALUES (?,?)', ('admin',generate_password_hash('admin')))
  conn.commit()
  conn.close()
  
init_db()  
  
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
  try:
    with open("dati.csv", mode='r', encoding="utf-8") as fails:
      csv_lasitajs=csv.reader(fails)
      dati=list(csv_lasitajs)
      print(csv_lasitajs)
    return render_template('csv2.html', dati = dati)
  except FileNotFoundError:
    with open('dati.csv', mode='w', encoding="utf-8", newline='') as fails:
      fails.write("Vārds, Uzvārds, Vecums\n")
      print("Fails tika izveidots")
    return render_template('kluda.html', zinojums = "Fails dati.csv nav atrasts!")
  
 
@app.route('/aptauja')
def aptauja():   
  return render_template('aptauja.html')

@app.route('/iesniegt', methods=['GET','POST'])
def iesniegt():
    if request.method=='POST':
      vards=request.form['vards']
      dzimums = request.form['dzimums']
      hobiji=request.form.getlist('hobiji')
      hobiji_str=', '.join(hobiji)
      print(vards)
      print(dzimums)
      print(hobiji)
      print(hobiji_str)
      
      conn=sqlite3.connect('DB_NVA.db')
      cursor = conn.cursor()
      cursor.execute('INSERT INTO lietotaji (vards, dzimums, hobiji) VALUES (?,?,?)',(vards, dzimums, hobiji_str))
      conn.commit()
      conn.close()
      
    return render_template('paldies.html')
  
  
  
@app.route('/MD3', methods=['GET','POST'])
def MD3():
  summa = None
  skaitlis1 = skaitlis2 = None
  if request.method =='POST':
    skaitlis1=int(request.form.get('skaitlis1', 0))
    skaitlis2=int(request.form.get('skaitlis2', 0))
    summa = skaitlis1 + skaitlis2
    print(summa)
    return render_template("MD3.html", skaitlis1=skaitlis1, skaitlis2=skaitlis2, summa=summa)
  return render_template("MD3.html")
  
@app.route('/pieteikties', methods=['GET', 'POST'])
def pieteikties():
  if request.method == 'POST':
      login=request.form['login']
      parole = request.form['parole']
  
      print(login)
      print(parole)
      
      conn=sqlite3.connect('DB_NVA.db')
      cursor=conn.cursor()
      cursor.execute('SELECT * FROM ADMIN WHERE login = ?', (login,))
      admin=cursor.fetchone()
      
      conn.close
      
      if admin and check_password_hash(admin[2],parole):
        session['login']=login
        return redirect("panelis")
      
  return render_template("pieteikties.html")

@app.route('/panelis')
def panelis():
  if 'login' not in session:
    return redirect(url_for('pieteikties'))
  conn = sqlite3.connect('DB_NVA.db')
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM lietotaji')
  lietotaji=cursor.fetchall()
  print(lietotaji)
  return render_template('panelis.html', lietotaji=lietotaji)

@app.route('/izlogoties')
def izlogoties():
  session.pop('login',None)
  return render_template('index.html')

@app.route('/dzest_db/<int:id>')
def dzest_lietotaju(id):
  if 'login' not in session:
    return redirect(url_for('pieteikties'))
  conn = sqlite3.connect('DB_NVA.db')
  cursor=conn.cursor()
  cursor.execute('DELETE FROM lietotaji WHERE id=?',(id,))
  conn.commit()
  conn.close()
  
  return redirect(url_for('panelis'))
  
@app.route('/dzest_csv/<string:vards>')
def dzest_rindu(vards):
    jauni_dati = []
    print("Datu tips jauni_dati")
    print(type(jauni_dati))

    with open('dati.csv', newline='', encoding='utf-8') as csvfails:
        lasitajs = csv.reader(csvfails)
        print("Rezultāti no CSV datu struktūrā")
        print(lasitajs)
        for dati in lasitajs:
            if dati != vards:
              jauni_dati.append(dati)

    print("Jaunie dati: ")
    print(jauni_dati)

    with open('dati.csv', mode='w', newline='', encoding="utf-8") as csvfails:
        rakstitajs = csv.writer(csvfails)
        rakstitajs.writerows(jauni_dati)

    return redirect(url_for('csv2'))  
  
#def izmeginajums():
 #   with open('dati.csv', mode='r', encoding="utf-8") as file:
  #    reader = csv.DictReader(file)
   #   print(type(reader))
    #  dati = [row for row in reader ]
  
     # print(dati)
      #print(type(dati))
      
   # with open('dati.json', mode='r', encoding="utf-8") as file:
    #  dati = json.load(file)
    #print(dati)
    
    #print("Visi dati: ")
    #for row in dati:
        #print(row['Vards'], row['Uzvards'], row['Cepums'], row['Dzimums'])
  
def ierakstit_csv(faila_nosaukums, dati):
  fails='dati.csv'
  fails_eksiste=os.path.isfile(fails)
  if not fails_eksiste:
    csv_rakstitajs.writerow(['Vārds', 'Uzvārds', 'Vecums'])
  with open(faila_nosaukums, mode='a', encoding="utf-8") as fails:
    csv_rakstitajs=csv.writer(fails)
    csv_rakstitajs.writerow(dati)
       
  
@app.route('/pievienot', methods=['POST'])
def pievienot():
  vards=request.form['vards']
  uzvards=request.form['uzvards']
  vecums=request.form['vecums']
  print(vards)
  ierakstit_csv('dati.csv', [vards,uzvards,vecums])
  return redirect(url_for('csv2'))
  
#@app.errorhandler(404)
#def internal_server_error(e):
    #note that we ser the 500 status explicitly
#    return render_template('404.html'), 404
    
   
    
if __name__=="__main__":
 # izmeginajums()
  app.run(debug=True)
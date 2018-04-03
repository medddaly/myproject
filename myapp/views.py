from django.shortcuts import render
#from myapp.models import Tab
from myapp.models import *

import sqlite3
def projet(request):
	return render(request, "projet.html", {})
def hello(request):
	return render(request, "hello.html", {})
conn = sqlite3.connect('database.db')
c = conn.cursor()
#def create_table():
 #   c.execute("CREATE TABLE IF NOT EXISTS build_tab (n_projet, ref_projet, projet_ag, bui_temp, env, dt)")

def data_entry():
    c.execute("INSERT INTO build_tab ('n_projet', 'ref_projet', 'projet_ag', 'bui_temp', 'env', 'dt') VALUES (?, ?, ?, ?, ?, ?)",(n_projet, ref_projet, projet_ag, bui_temp, env, dt))
    
   #c.execute("INSERT INTO build_tab ('n_projet', 'ref_projet', 'projet_ag', 'bui_temp', 'env', 'dt') VALUES (?, ?, ?, ?, ?, ?)",(n_projet, ref_projet, projet_ag, bui_temp, env, dt))
   
    conn.commit()
    c.close()
    conn.close()
#create_table()
data_entry()
def insert(request):
    if request.method == 'POST':
        n_projet = request.POST.get('n_projet')
        ref_projet = request.POST.get('ref_projet')
        projet_ag = request.POST.get('projet_ag')
        bui_temp = request.POST.get('bui_temp')
        env = request.POST.get('env')
        dt = request.POST.get('dt')
 
     
    


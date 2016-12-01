import requests
import json
import pandas as pd
import sqlite3
from datetime import date
from datetime import datetime
from dateutil import parser
import time

SERVER = '10.24.25.130:8000'
conn = sqlite3.connect('usersrollup.db')
c = conn.cursor()

def makedb():
	c.execute('''Create Table users (username text,compname text,stat text,time text)''')
	conn.commit()

now = str(datetime.now())	
r = requests.get('http://'+SERVER+'/get_dup')

newtxt = json.loads(r.text)
if (newtxt=={}): 
	print("Returned nothing.");
else:
	#print(newtxt,now)
	for x in newtxt:
		time.sleep(5)
		r = requests.get('http://'+SERVER+'/get_log?username='+x+'&compname=all')
		thisreturn = json.loads(r.text)
		#print(x,thisreturn)
		for key,value in thisreturn.items():
			data2 = (value['username'],value['compname'],value['stat'],now)
			try:
				c.execute("INSERT INTO users VALUES "+str(data2))
			except sqlite3.OperationalError:
				makedb()
				c.execute("INSERT INTO users VALUES "+str(data2))
			conn.commit()
	r = requests.get('http://'+SERVER+'/db?action=clearlog')


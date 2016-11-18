import json
import requests
import hashlib
import sqlite3
import datetime
conn = sqlite3.connect('check.db')
c = conn.cursor()

def makedb():
	c.execute('''Create Table ConnectLog (title text,time text,stat text,hash text)''')
	conn.commit()
	
now = str(datetime.datetime.now())
with open('config.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

for sites in data['websites']['site']:
	#print(sites)
	print(sites['-title'])
	#HTTP request for the code.
	try:
		r = requests.get(sites['-address'])
		stat = str(r.status_code)
	except:
		print('Connection Error')
		stat = '300'
	if(sites['-hashdiff'] == 'true'):
		hash = hashlib.md5(r.text.encode('utf-8')).hexdigest()
	else:
		hash = str(None)
	if(sites['-logdiff'] == 'true'):
		#savethetextasafile
		hash = hashlib.md5(r.text.encode('utf-8')).hexdigest()
	else:
		hash = str(None)
		
	sqlcmd = "INSERT INTO ConnectLog VALUES ('"+sites['-title']+"','"+now+"',"+stat+",'"+hash+"')"
	try:
		print(sqlcmd)
		c.execute(sqlcmd)
	except sqlite3.OperationalError:
			makedb()
			c.execute(sqlcmd)
	conn.commit()


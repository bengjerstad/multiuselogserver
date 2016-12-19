import hug
import json
import sqlite3
import pandas as pd
conn = sqlite3.connect('check.db')
c = conn.cursor()

@hug.directive()
def cors(support='*', response=None, **kwargs):
    '''Returns passed in parameter multiplied by itself'''
    response and response.set_header('Access-Control-Allow-Origin', support)

@hug.get(examples='')
@hug.local()
#just to Test exporting of the dbfile
def load(hug_cors):	
	logs = {}
	dbkeys = ['title','time','stat','hash']
	sqlcmd = "SELECT * FROM ConnectLog WHERE 1"
	dbout = c.execute(sqlcmd)
	dbout = dbout.fetchall()

	for idx,row in enumerate(dbout):
		logs[idx] = dict(zip(dbkeys,row))
	return logs
	
@hug.get(examples='type=list&title=all')
@hug.local()
def connection(hug_cors,type: hug.types.text,title: hug.types.text):
	logs = {}
	dbkeys = ['title','stat']
	sqlcmd = "SELECT `title`,`stat`,`time` FROM ConnectLog WHERE 1"
	dbout = c.execute(sqlcmd)
	dbout = dbout.fetchall()
	titles = {x[0] for x in dbout}
	for thistitle in titles:
		laststat = "200"
		thisstat = "Good"
		for idx,row in enumerate(dbout):
			if(thistitle == row[0]):
				if(type == 'list'):
					if(row[1] != laststat):
						#print(thistitle,laststat,row[1])
						laststat = row[1]
						if(row[1] == str(200)):
							thisstat = "Yield"
						if(row[1] != str(200)):
							thisstat = "Bad"
					logs[thistitle] = thisstat
				if(type == 'view'):
					if(row[0] == title):
						logs[idx] = row[0],row[1],row[2]
	return logs
	
@hug.get(examples='type=list')
@hug.local()
def hashlist(hug_cors,type: hug.types.text):
	logs = {}
	dbkeys = ['title','hash']
	sqlcmd = "SELECT `title`,`hash` FROM ConnectLog WHERE 1"
	dbout = c.execute(sqlcmd)
	dbout = dbout.fetchall()
	titles = {x[0] for x in dbout}
	for thistitle in titles:
		for idx,row in enumerate(dbout):
			if(row[1] != "None"):
				if(type == 'list'):
					if(thistitle == row[0]):
						try:
							if(row[1] != laststat):
								thisstat = "Yield"
								laststat = row[1]
								#print(thistitle,laststat,row[1])
						except:
							print('ex')
							laststat = row[1]
							thisstat = "Good"
						logs[thistitle] = thisstat
				if(type == 'view'):
					logs[idx] = row[1]
	return logs

@hug.get(examples='')
@hug.local()
def get_rollup(hug_cors,hug_timer=3):
	logs = {}
	dbkeys = ['username','compname','time','stat']
	
	#connect ot rollup db file
	rollup_connconn = sqlite3.connect('usersrollup.db')
	rollup_c = rollup_connconn.cursor()
	
	#get the logs out of the db file
	dbout = rollup_c.execute("SELECT username,compname,time,stat FROM users WHERE 1")
	dbout = dbout.fetchall()
	
	for idx,row in enumerate(dbout):
		logs[idx] = dict(zip(dbkeys,row))
		
	return logs	
	
@hug.get(examples='')
@hug.local()
def rolluplist(hug_cors):
	logs = {}
	with open('config.json', encoding='utf-8') as data_file:
		data = json.loads(data_file.read())

	for rollups in data['rollupscripts']['scripts']:
		thistitle = rollups['-title']
		logs[thistitle] = 'Good'
	return logs
	
@hug.get(examples='title=windowslogger')
@hug.local()
def clearthis(hug_cors,title: hug.types.text):
	sqlcmd = "DELETE FROM ConnectLog WHERE title = '"+title+"'"
	print(sqlcmd)
	dbout = c.execute(sqlcmd)
	conn.commit()

	
	return 1
	

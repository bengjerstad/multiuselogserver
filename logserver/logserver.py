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
	
@hug.get(examples='')
@hug.local()
def connection(hug_cors):
	logs = {}
	dbkeys = ['title','stat']
	sqlcmd = "SELECT `title`,`stat` FROM ConnectLog WHERE 1"
	dbout = c.execute(sqlcmd)
	dbout = dbout.fetchall()
	titles = {x[0] for x in dbout}
	for thistitle in titles:
		laststat = "200"
		thisstat = "Good"
		for idx,row in enumerate(dbout):
			if(thistitle == row[0]):
				if(row[1] != laststat):
					#print(thistitle,laststat,row[1])
					laststat = row[1]
					if(row[1] == str(200)):
						thisstat = "Yield"
					if(row[1] != str(200)):
						thisstat = "Bad"
			logs[thistitle] = thisstat
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
def rolluplist(hug_cors):
	logs = {}
	with open('config.json', encoding='utf-8') as data_file:
		data = json.loads(data_file.read())

	for rollups in data['rollupscripts']['scripts']:
		thistitle = rollups['-title']
		logs[thistitle] = 'Good'
	return logs
	
@hug.get(examples='view=hashview')
@hug.local()
def clearthis(hug_cors,view: hug.types.text):
	sqlcmd = "DELETE FROM ConnectLog WHERE title = '"+view+"'"
	print(sqlcmd)
	dbout = c.execute(sqlcmd)
	return 1
	

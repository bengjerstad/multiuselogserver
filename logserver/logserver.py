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
def connection():
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
					print(row[1],laststat)
					laststat = row[1]
					if(row[1] == 200):
						thisstat = "Yield"
					if(row[1] != 200):
						thisstat = "Down"
			logs[thistitle] = thisstat
	return logs

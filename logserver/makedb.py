import sqlite3
conn = sqlite3.connect('users.db')
c =conn.cursor()
c.execute('''Create Table users (username text,compname text,stat text,time text)''')

import hug
try:
	from . import runserver
	##to run windowslogonofflogger
	##https://github.com/bengjerstad/windowslogonofflogger
	hug.API(__name__).extend(runserver, '')
	print('Running windowslogonofflogger Server')
except:
		pass
		
try:
	from . import logserver
	##to run MulitUse Log Server
	##https://github.com/bengjerstad/multiuselogserver
	hug.API(__name__).extend(logserver, '/logserver')
	print('Running MultiUselog Server')
except:
	pass

@echo off
For /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
For /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set mytime=%%a%%b)

for /f "delims=[] tokens=2" %%a in ('ping %computername% -n 1 ^| findstr "["') do (set thisip=%%a) 

cscript /nologo wget.js "http://10.24.25.130:8000/log_this?username="+%USERNAME%+"&compname="+%computername%+"&stat=on&time="+%mydate%_%mytime%
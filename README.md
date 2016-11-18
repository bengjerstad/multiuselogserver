# MulitUse Log Server
Project to add extra features to the windowslogonofflogger[https://github.com/bengjerstad/windowslogonofflogger]

Starting this by basesing it off of the windowslogonofflogger code base.

This project is broken up into 3 parts:

1. Sceduled Scripts run uptime polling and eod rollup logs

2. A server to log the HTTP request and get back the data.
The server is a hug server: http://www.hug.rest/ 
The hug server exposes a RESTFUL API and allows the logging and data analysis to take place in python3. 
The python code pushes and pulls from a sqlite3 database file. 
The design goal is to use the same server that is running windowslogonofflogger, except a diffent port number.

3. An HTML/javascript front end to get the data from the server to the admin. 

## Setup/Install
### Set up server:

1. Install dependencies on server
  * python3
  * hug
    ```
    pip3 install hug --upgrade

    ```
  * sqlite
  * pandas
2. Copy server files to the server.
  I copied the files to my user folder at /home/admin
3. Run and test:

  Run:
  ```
  hug -f 'home/admin/__init__.py'
  
  ```
  Test:
  
  To test logging, open up a browser and enter:
  
  http://[SERVER_IPADDRESS]:8000/log_this?username=bgjerstad&compname=011acboe&stat=on&time=2016-10-20_0229PM
  
  To test getting the logs out of the server, in the browser enter:
  
  http://[SERVER_IPADDRESS]:8000/get_log?username=bgjerstad&compname=011acboe

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
  
 
 ### Functions

Full definiton at: windowslogonofflogger/logserver/APIdefinition.md

**log_this**: to be used by scripts to log data into the database
  
    http://10.24.25.130:8000/log_this?username=bgjerstad&compname=011acboe&stat=on&time=2016-10-20_0229%20PM


**get_log**: to retrive all or parts of the log
   
    http://[SERVER_IPADDRESS]:8000/get_log?username=bgjerstad&compname=011acboe
    
    http://[SERVER_IPADDRESS]:8000/get_log?username=all&compname=all
     
    http://[SERVER_IPADDRESS]:8000/get_log?username=bgjerstad&compname=all

**get_dup**: to get a list of users who have logged in at multiple computers. 
  
    http://[SERVER_IPADDRESS]:8000/get_dup

**db**: allows for clearing the database
   
    http://[SERVER_IPADDRESS]:8000/db?action=clearlog - clear user log.
    
    http://[SERVER_IPADDRESS]:8000/db?action=clearex - clear exclusion list.
     
    http://[SERVER_IPADDRESS]:8000/db?action=clearall - Clear both. 

**ex_this**: create a list of names to ingore in the get_dup function. 

   
    http://[SERVER_IPADDRESS]:8000/ex_this?username=bgjerstad&action=add - Add a user to the exclusion list.
    
    http://[SERVER_IPADDRESS]:8000/ex_this?username=bgjerstad&action=remove - Remove a user from the exclusion list.
     
    http://[SERVER_IPADDRESS]:8000/ex_this?username=bgjerstad&action=list - View the exclusion list.

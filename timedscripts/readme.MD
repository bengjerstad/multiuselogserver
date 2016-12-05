These files need to be set to run on a timer. check.py is hourly. rollupwinlog.py is a nightly run.

```
crontab -e

@daily cd /home/admin/ && python3 'home/admin/rollupwinlog.py'
@hourly cd /home/admin/ && python3 'home/admin/check.py'
```

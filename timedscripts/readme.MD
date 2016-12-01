These files need to be set to run on a timer. check.py is hourly. rollupwinlog.py is a nightly run.

```
crontab -e

@daily python 'home/admin/rollupwinlog.py'
@hourly python 'home/admin/check.py'
```

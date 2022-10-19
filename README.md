# FileZip
Script to zip all files in a folder, intended for running as a cron job.  
Run with `python zip.py`  
Optional arguments:  
`-s`, `--source` - to change the default source directory ('/var/log/')  
`-d`, `--decompress` - to decompress the files in source instead  
e.g. run `python zip.py -s /var/archive -d`, to decompress all zipped files in '/var/archive' folder  
 
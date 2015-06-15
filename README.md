# E-library #

Training project for practicing in Django 1.8 + Python 3.4.

## Notes ##

1.  There are requirement files for setting virtual environment in __requirements__ 
 folder. _base.txt_ has default packages to install and is needed for local 
 development, _production.txt_ has additional packages for production servers.
    
2.  Project requires _secrets.json_ file placed in main project folder. File has 
next format:

    ```json
        {
            "FILENAME": "secrets.json",
            "SECRET_KEY": "Your secret key here!"
        }
    ```

3.  _settings.py_ file has been replaced with __settings__ module and placed in
__config__ module with _urls.py_ and _wsgi.py_ files. In __settings__ module all 
default settings stored in _base.py_ file. _local.py_ and _production.py_ files 
has extra settings for local and production servers respectively.
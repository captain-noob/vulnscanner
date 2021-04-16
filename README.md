
  

# VULN-SCANNER

  

**vulnscan** is a web application **source code vulnerability scanner** (now we are developing for PHP applications). It could be used to detect if target project contain any known vulnerabilities. One of the best ways we can do that is to help developers and security professionals improve the web application they are producing that everyone else relies on.

  

  

This tool is designed to be cross-platformed. It could be compiled and run on both Windows and Linux.

  

  

![php](https://img.shields.io/badge/php-%5E7.1.3-blue?logo=php) ![python](https://img.shields.io/badge/python-v3.7-blue?logo=python) ![owasp](https://img.shields.io/badge/owasp-Top%2010-green?logo=owasp&style=plastic)

  

## Usage

   
   

    - git clone https://github.com/captain-noob/vulnscanner.git
    - cd vulnscanner/
    - pip install -r requirements.txt
    - change content `path` variable on `lib/start.py` 
    - python main.py
    

  

## Quick Facts

  

  

  

> Detects various [security vulnerabilites](https://owasp.org/www-project-top-ten/):

  

> SQLInjection, Cross-Site Scripting (XSS), Cross-Site Request Forgery(CSRF), XML eXternal Entity Injection (XXE),Command Injection etc.

  

  

## Updates

  

    - Now, this tool can identify SQL injection possibilities.
    - Controll using commandline parameters 

  

## About


    - Currently, we are working on this project.
    - Completed SQL Injection Module.
    - Next MileStone : OS Command Injection


## Working
```bash
    usage: main.py [-h] [-f FILE] [-F FOLDER]

    This is the vuln scanner

    optional arguments:
    -h, --help                      Show this help message and exit
    -f FILE,    --file FILE         Analize with a file
    -F FOLDER,  --folder FOLDER     Analize file with in a folder
```

## Output
```bash
vulnscanner >  python .\main.py -f .\test\sqli.php
[+] : SQL injection might me possible    - Severity : High
        File : C:\Users\Roshan\Desktop\tools\vulnscanner\test\sqli.php
        Code : $news_dbg = mysql_query("SELECT id,name,image,specifications FROM ".$_GET['id']." WHERE id=".$DB_CHALL_TWO) or die(mysql_error());
        Param : $_GET[
        Param : $DB_CHALL_TWO
        Fix : Use PDO insted of direct SQL execution
        Reffer : https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html#escaping-sqli-in-php


[+] : SQL injection might me possible    - Severity : High
        File : C:\Users\Roshan\Desktop\tools\vulnscanner\test\sqli.php
        Code : $news = mysql_query("SELECT id,name,image,specifications FROM ".$DB_CHALL_TWO." WHERE id=".$_GET['id']) or die(mysql_error());
        Param : $DB_CHALL_TWO
        Param : $_GET[
        Fix : Use PDO insted of direct SQL execution
        Reffer : https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html#escaping-sqli-in-php


[+] : SQL injection might me possible    - Severity : High
        File : C:\Users\Roshan\Desktop\tools\vulnscanner\test\sqli.php
        Code : $news = mysql_query("SELECT name,image,id FROM ".$DB_CHALL_TWO." ORDER BY id DESC LIMIT 0,3") or die(mysql_error());
        Param : $DB_CHALL_TWO
        Fix : Use PDO insted of direct SQL execution
        Reffer : https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html#escaping-sqli-in-php


Finished in 0.11 second(s)
```

## Contacts

  

  

  

    LinkedIn : https://www.linkedin.com/in/roshancp/
    Twitter : https://twitter.com/captain__noob

  

  

## Contributing


Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

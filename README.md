<p align="center"><img src="https://i.imgur.com/K1C74ti.png"></p>

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
python3 xmlrpcbruteforce.py http://wordpress.org/xmlrpc.php passwords.txt userlist.txt

Try adding 'www' if nothing works.
```

## Demo

<img src="https://i.imgur.com/4XxCtVL.png">

## Bugs

If you get an ```xml.etree.ElementTree.ParseError```:

1. Did you forget to add 'xmlrpc' in the url ?
2. or try to add or remove 'https' or 'www'.

I'm working on the Exception Handling. Will fix it soon.

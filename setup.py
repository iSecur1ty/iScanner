#!/usr/bin/env python
#
# iScanner installer
#

import subprocess
import sys
import os,time
import platform
if platform.system() != 'Linux':
	print 'Sorry, you are using non-supported OS.\nThis program only works on linux.\n'

# Checking for platform
if platform.system() == 'Linux':
	# installer = null
	installer = False
	
	try:
		# Light Switch = install if true
		if sys.argv[1] == 'install':
			installer = True
			
	except IndexError:
		print 'Please, enter the right argument to install'
		print '\nUsage: ' + sys.argv[0] + ' install'
		
	# Start the installer if it's True..
	if installer is True:
		if os.path.isdir('/etc/iscanner'):
			print '\n'
			print 'iScanner is already installed in /etc/iscanner, remove it then start the installer again.\n'
			sys.exit()		
		# Checking if there is a sources list available..
		if os.path.isfile('/etc/apt/sources.list'):
			try:
				subprocess.Popen('apt-get install python-pip python-mysqldb python-webpy && pip install termcolor', shell=True).wait()
				time.sleep(2)
			except:
				sys.exit()
								
		# running redhat-like..
		if os.path.isfile('/etc/yum.conf'):
			subprocess.Popen('wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py --no-check-certificate && python get-pip.py', shell=True).wait()
			subprocess.Popen('pip install web.py && pip install termcolor', shell=True).wait()
			subprocess.Popen('yum install MySQL-python', shell=True).wait()
			subprocess.Popen('rm -rf get-pip.py', shell=True).wait()
			subprocess.Popen('mkdir web_ui/static/reports', shell=True).wait()
			subprocess.Popen('mkdir temp', shell=True).wait()
			
			#sys.exit()
			
			#print'[!] You are not running a Debian-alike.\nPlease install pip, python-mysqldb, python-webpy, and run pip install termcolor manually.'
			#sys.exit()
			

		try:
		   import MySQLdb
		   time.sleep(2)	
		   mysql_user = raw_input("[+]please enter your mysql-server username :")
		   mysql_pass = raw_input("[+]please enter youe mysql-server password :")			
		   db = MySQLdb.connect("localhost",mysql_user,mysql_pass)
		   cursor = db.cursor()
		   cursor.execute("CREATE DATABASE iScanner")
		   sql = "mysql -u {0} -p iScanner < db.sql".format(mysql_user)
		   print "Enter your mysql password :"
		   os.system(sql)
		   db.close()
		except MySQLdb.Error, e:
			print "[*]Error %d: %s" % (e.args[0], e.args[1])
			print "[*]Error connection to Database"
			print "[*]iScanner installer ShutDown"
			sys.exit()			
		print'[*] Installing iScanner into /etc/iscanner folder...'
		time.sleep(1)
		subprocess.Popen('mkdir /etc/iscanner', shell=True).wait()
		subprocess.Popen('cp -rf * /etc/iscanner', shell=True).wait()
		subprocess.Popen('rm -rf /etc/iscanner/db.sql && rm -rf /etc/iscanner/setup.py && mkdir /etc/iscanner/temp',shell=True).wait()
		from termcolor import cprint
		cprint ("[*]Done , you can catch some malware using iscanner , G00D LUCK :D","red")


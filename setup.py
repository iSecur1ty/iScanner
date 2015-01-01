#!/usr/bin/env python
#
# iScanner installer
#

import subprocess
import sys
import os,time
import platform
import apt,imp
import shutil

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
		print '\nUsage: ' + sys.argv[0] + ' install [path]'		
	path='/opt'
	# checking for path
	if  len(sys.argv)>2 : 
		path = sys.argv[2]
		if (os.path.isdir(path)):
			print ("This software will be installed in \""+ sys.argv[2]+ "\"");
		else:
			print "Directory doesn't exit"
			print "Do you want to create it ?[y/n]"
			if (raw_input()).lower()in ['y','yes']:
				os.makedirs (path)
			else:
				print "Error exited"
				sys.exit()

	# Start the installer if it's True..
	if installer is True:
		# Checking if there is a sources list available..
		if os.path.isfile('/etc/apt/sources.list'):
			try:
				#checking if all packages are available
				print "checking packages ..."
				cache =apt.Cache()
				missing_packages=False
				packages_list=["python-pip","python-mysqldb","python-webpy"]
				for package in packages_list:
					if  cache[package].is_installed :
						print package + " is installed"
					else :
						missing_packages=True
						cache[package].mark_install()
						print package + " isn't installed"		
				modules_list =["termcolor"]
				missing_modules=[]
				for module in modules_list :
					try:
						imp.find_module(module)
						print module + " is installed "
					except :
						missing_modules.append(module)
						print module + " isn't installed "

				if missing_packages== True or len(missing_modules)>0 :
					if (os.geteuid() != 0):
						print "you need root rights to installed missing packages."
						print "this program will exit ..."
						sys.exit()
					else :
						print "Installing needed packages ...... "
						cache.commit()
						for module in mising_modules :
							pip.main (["install", module])
						print "All needed packages are installed ... "
			except Exception, arg:
        			print >> sys.stderr, "[{err}]".format(err=str(arg))

                path= path+"/iscanner"
                if os.path.isdir(path):
                        print '\n'
                        print  '\"'+path+'\" already exits, it maybe means that iscanner is installed'
                        print 'Do you want to continue ? [y/n] ( it will be removed !)'
                        if raw_input().lower() not in ['y','yes']:
                                print 'Program closed'
                                sys.exit()

                print'[*] Installing iScanner into '+path+' folder...'
		shutil.rmtree(path, ignore_errors=True)
		shutil.copytree(".",path,ignore=shutil.ignore_patterns("setup.py","db.sql"))

                from termcolor import cprint
                cprint ("[*]Done , you can catch some malware using iscanner , G00D LUCK :D","blue")

		#I preffer rewrite the next code with yum's API. for mysql, the user has the choise between MySQL, and SQLite3
		#so installing mysql is no more an obligation
'''
		
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
		except:
			print "[*]Error connection to Database"
			print "[*]iScanner installer ShutDown"
			sys.exit()			
'''


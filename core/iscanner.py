#!/usr/bin/python
# iScanner lets you detect Linux malware from your server.
#
# Copyright (C) 2014 iSecur1ty LTD <iscanner@isecur1ty.org>.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from optparse import OptionParser
from database.database import database
import scanner
import report 
import xmlparser

#preparing argument parser
usage= "usage: %prog scan [options]"
parser = OptionParser(usage)

#option for "scan", in the future Groups will be used to separate options
parser.add_option("-p", "--path", dest="target",help="path to target", metavar="target")
parser.add_option("-t", "--type", dest="type",
	help="type of file which will be scanned (php,html, js,or all). \"all\" is the default type(not implemented)  ", metavar="type")
parser.add_option ("-T","--tmp",action="store_false",dest="tmp",default=True,help="when used, before scaning a temperal copy will be created (not implemented)")
parser.add_option ("-c","--config",dest="configure",default=True,help="the path to the XML file which contains configuration")
parser.add_option ("-R","--report",dest="reportPath",help="path to put report")

#parsing args
(option,cmd)=parser.parse_args()
#checking the selected command
commands_list =['scan'] #['scan','webServer','config','show']

if (len(cmd) !=  1 ):	
	parser.print_help();
	exit()
else :
	cmd = str (cmd[0])
if not  cmd  in commands_list :
	parser.error (  cmd + " is not recognised ")
	parser.print_help()
	exit()

#Until now, only "scan" is implemented
if cmd == "scan" :
	scan_types=["all","php","js","html"]
	if option.type !=None and (not option.type.lower() in scan_types) :
		print "scan type not recognised"
		exit ()
	else :
		if option.configure ==None :
			#loading the default configuration file
			defaultConfigs=xmlparser.loadConfig()
		else :
			defaultConfigs=xmlparser.loadConfig(option.configure)

                if option.reportPath ==None :
			reportPath=defaultConfigs["reportPath"]
            	else :
			reportPath=option.reportPath
		print "Path to report : "+reportPath +"/report.html "



		print "connecting to database ..."
		db=database()
		db.connect()
		print "loading signatures ..."
		signatures=db.getSignatures()
		sc=scanner.scanner(signatures)
		print "scanning ...\n"
		print "####################################"
		sc.scan(option.target)
		print "####################################\n"
		print "scanning finished ..."
		print "getting more informations about infected files ..."
		results= sc.getInfected()
		db.completInfomation(results)
		print "making report ..."
		report.makeHTMLreport(results,reportPath)
		print "deconnecting database" 
		db.closeConnection()

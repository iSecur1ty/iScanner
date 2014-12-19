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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.import web
import shutil
import dircache 
import os

class scanner:
        def __init__(self,signatures):
		self.__signature=signatures
		self.__infectedFileList=[]
	def makeTMP (self,source,dest):
	        try:
	                shutil.copytree (source,dest)
	        except:
	                print "Error : while copying files into temporelle directory !! "
	# recursive fuction for scannig 
	def scan (self,target):
		for element in dircache.listdir(target):
			#Checking for symbolic links to avoid making cycles
			#in the future, the user will have the choise to do it or not !
			if os.path.isdir(target+"/"+element) and not os.path.islink(target+"/"+element):
				self.scan (target+"/"+element)
			else :
				f=open (target+"/"+element,"r")
				buf=f.read()
				for sig in self.__signature :
					if buf.find(sig)>=0:
						print "Infected : "+target+"/"+element
						self.__infectedFileList.append([sig,target+"/"+element])
	def getInfected (self):
		return  self.__infectedFileList


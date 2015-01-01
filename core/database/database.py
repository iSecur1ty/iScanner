import SQLite3
import sqlite3
class database :
	def __init__(self,type="sqlite"):
		print "initiation"
		if type=="sqlite":
			self.__type = "sqlite"
		elif type =="mysql":
			self.__type = "sqlite"
		else:
			print "Database type not supported !"
			exit()
	def connect (self,path="../databases/sqlite3.db"):
		self.__conn=sqlite3.connect(path)
		self.__cursor=self.__conn.cursor()

	def getSignatures (self):
		print "signture"
		self.__signatures=list()
		for raw in self.__cursor.execute ("select signature from  malware_information;") :
                        self.__signatures.append(raw[0])
		return self.__signatures

	def completInfomation (self,results):
		for res in results:
                        #this instruction in comment doesn't work when signatures contains special char like "(" and ")"
                        #for raw in self.__cursor.execute ("select  name,description,risk,type from  malware_information where signature=?",sig) :
                        for raw in self.__cursor.execute \
				("select  name,description,risk,type from  malware_information where signature= '%s'" % res[0]):
                        	for element in  raw :
					res.append(element)

	def getThreatInformation (self,signatures):
		print "reports"
		data=list()
		for sig in signatures :
			#this instruction in comment doesn't work when signatures contains special char like "(" and ")"
                	#for raw in self.__cursor.execute ("select  name,description,risk,type from  malware_information where signature=?",sig) :
                	for raw in self.__cursor.execute ("select  name,description,risk,type from  malware_information where signature= '%s'" % sig) :
       	                	data.append(raw)
		return  data		


	def commit ():
		self.__conn.commit()

	def closeConnection (self):
		print "connection closed "
		self.__conn.close()

if __name__=="__main__":
	a =database("sqlite")
	a.connect("../../databases/sqlite3.db")

	a.getThreatInformation(["U_wordwrap","c99_buff_prepare()"])

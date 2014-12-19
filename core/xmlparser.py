import sys
import xml.etree.ElementTree as xmlET

def loadConfig (path="../config/config.xml"):
	try:
		f=file(path,'r')
	except:
		print "Configuration file can't be found !"
		exit()
	fileText=f.read()

	tree=xmlET.fromstring(fileText)

	try :
		tree=xmlET.fromstring(fileText)
	except :
		print "Configuration file can't be parsed !"
		exit()

	treeElements=["reportPath","databaseToUse","pathToSQLITE","mysql_host","mysql_db","mysql_user"]
	data=dict()

	for element in treeElements :
		data[element]=tree.find(element).text \
						.replace("\t","")\
						.replace(" ","")\
						.replace("\n","")
	return data

if __name__=="__main__":
	if len(sys.argv) < 2:
		loadConfig ()
	else :
		loadConfig (sys.argv[1])

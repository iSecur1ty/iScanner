def makeHTMLreport (results,path):
	f=open ("data/html/reportPageBeforeTable.html","r")
	pre=f.read()
	f.close()
	f=open ("data/html/reportPageAfterTable.html","r")
	post=f.read()
	f.close()
	f=open (path+"/report.html","w")
	f.write(pre)
	for raw in results :
		#print raw
		f.write( "<tr><td>"+raw[1]+"</td><td>"+raw[3]+"</td><td>"+raw[4]+"</td></tr>")
	f.write(post)
	f.close()

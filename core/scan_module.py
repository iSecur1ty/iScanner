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

import web 
import time 
import os   
import sys
import MySQLdb 
from termcolor import cprint,colored 
import File_Collector #import collector module to collect files 
from config import *
report_name = sys.argv[3]
reports = report_path + "/" + sys.argv[3] + "..html"
reports_ui = web_ui_reports + "/" + sys.argv[3] + "..html"
description = []  #contain description of malware
risk = []       #contain risk of malware
signature = []   #contain the malware signature
infected_files = []
infected_signature = []
infect = 0
#def clear_duplicates():
#	global infected_files
#	infected_files = list(set(infected_files))
#	infected_signature = list(set(infected_signature)) 

	
	
	
def query_db(signature_input): #function to retrieve all data for specific signatue which was found in infected file 
	try:
                        db=MySQLdb.connect(host=mysql_host,user=mysql_user,passwd=mysql_pass,db=mysql_db)
                        query = db.cursor()
                        query.execute("SELECT * FROM malware_information where signature = '"+signature_input+"'") #query to get all data for infected files'  signatures 
                        for item in range(query.rowcount):  
                                row = query.fetchone()   
                                description.append(row[3]) #add description to list
			  	risk.append(row[4]) #add risk to list

        except Exception,err:
                error = "there is an error occured with database "+str(err)
                cprint(error,'red')

def connect_db():  #used for db connection and retrieve all signatues to signature list
		try:
			db=MySQLdb.connect(host=mysql_host,user=mysql_user,passwd=mysql_pass,db=mysql_db)
			cprint("Database Connected Successfully",'green')
			query = db.cursor()
			query.execute("SELECT * FROM malware_information")
			for item in range(query.rowcount):
				row = query.fetchone()
				signature.append(row[2])
				

		except Exception,err:
			error = "there is an error occured with database "+str(err)
			cprint(error,'red') 


def save_report_db():
	high = risk.count('High')
	medium = risk.count('Medium')
	low = risk.count('Low')
	info = risk.count('Information')
	scan_type = sys.argv[2]
	s_time = time.ctime()
	db = web.database(dbn='mysql', db=mysql_db, user=mysql_user, pw=mysql_pass)
	db.insert("scans_info", scan_name=report_name,scan_time=time.ctime(),scan_path=reports_ui,scan_type=scan_type,infected_files_number=infect,risk_high=high,risk_meduim=medium,risk_low=low,risk_information=info)
	Msg = "New Report Inserted successfully"
	cprint(Msg,'green')



def scan_temp():
	global infect
	Msg1 = "[+] Scanning files has started at ------------------" + time.ctime()
	cprint(Msg1,'red') 
	time.sleep(2)
	for tempfile in os.listdir(main_path):
		f = open(main_path+"/"+tempfile,"r")
		print("opening temp file"+tempfile)
		for tmpline in f.read().splitlines():
			try:
				f = open(tmpline,"r").readlines()
			except Exception,err:
				Warn = "Couldn't Open File " + tmpline
				cprint(Warn,'yellow')
				#notification(tmpline,0)
			for line in f:
				for sign in signature:
					if sign in line:
						infect += 1
						Msg = "There is an infection found in " + tmpline
						cprint(Msg,'red')
						time.sleep(0.1)
						infected_files.append(tmpline) #add infected file in list
						infected_signature.append(sign) #add it's signature in another list
#						clear_duplicates()
						#notification(tmpline,1)								
	cprint("Total infection is "+str(infect),on_color='on_red')	
	
				
				

def write_report(reports):
	time2 = "askarz"
	report_save_path = reports
	report = open(report_save_path,"w")
	html_str = """
	<meta charset="utf-8">
	<meta content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=0" name="viewport">
	<title>iscanner scan report</title>
		<style>	
			#sidebar ul#nav ul.sub-menu a, #sidebar ul#nav li a, .navbar-nav, .project-switcher .project-list li .title, #theme-switcher, .page-title,
			h3, h4,.h3, .h4, .table-condensed , .widget-content .more, .statbox .title, .statbox .value ,th ,.table-striped,
			.form-horizontal{font-family :ArabicFont !important}
			.table-condensed, .dataTables_wrapper, .select2-container {direction :ltr !important}
			.table-condensed thead>tr>th ,.widget.box .widget-header {text-align :left}
			* { outline: none !important;}
			html,body {  height: 100%;}
			body {font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;  color: #555555;  font-size: 13px;}
			.container {  max-width: none !important;  padding: 0 20px;}
			.row-no-margin {  margin-left: 0 !important;  margin-right: 0 !important;}
			.col-no-margin {  margin-left: -15px !important;  margin-right: -15px !important;}
			#container {  position: relative;  height: 100%;}
			#container.fixed-header {  margin-top: 52px;}
			#container > #content > .container {  float: left;  width: 100%;  margin-top:40px;}
			#content-rep{  background: #fff;  margin:auto;  overflow: visible;  padding-bottom: 30px;  min-height: 100%;  width:80%;}
			#content { background: #fff;  margin-left: 250px;  overflow: visible;  padding-bottom: 30px;  min-height: 100%;}
			#content > .wrapper {  -webkit-transition: margin ease-in-out 0.1s;  -moz-transition: margin ease-in-out 0.1s;  -o-transition: margin ease-in-out 0.1s;  transition: margin ease-in-out 0.1s;  position: relative;}
			.page-header {  border: 0;  margin: 0;  *zoom: 1;}
			.page-header:before,.page-header:after {  display: table;  content: "";  line-height: 0;}
			.page-header:after {  clear: both;}
			.page-title {  float: left;  padding: 25px 0;  direction :ltr}
			.page-title h3 {  margin: 0;  margin-bottom: 10px;  color: #555555;  font-weight: 400;  font-size: 20px;}
			.page-title span {  display: block;  font-size: 11px;  color: #888888;font-weight: normal;}
			.widget {  margin-top: 0px;  margin-bottom: 25px;  padding: 0px;}
			.widget .widget-header {  margin-bottom: 15px;  border-bottom: 1px solid #ececec;  *zoom: 1;}
			.widget .widget-header:before,.widget .widget-header:after {  display: table;  content: "";  line-height: 0;}
			.widget .widget-header:after {  clear: both;}
			.widget .widget-header h4 {  display: inline-block;  color: #555555;  font-size: 14px;  font-weight: bold;  margin: 0;  padding: 0;  margin-bottom: 7px;}
			.widget .widget-header h4 i {font-size: 14px;margin-right: 5px;color: #6f6f6f;}
			.widget .widget-header .toolbar {display: inline-block;padding: 0;margin: 0;float: left;}
			.widget.box {border: 1px solid #d9d9d9;}
			.widget.box .widget-header {background: #f9f9f9;border-bottom-color: #d9d9d9;line-height: 35px;padding: 10px 12px;  margin-bottom: 0;}
			.widget.box .widget-header h4 {  margin-bottom: 0;}
			.widget.box .widget-header .toolbar {  margin-right: -5px;}
			.widget.box .widget-header .toolbar.no-padding {  margin: -2px -13px;}
			.widget.box .widget-header .toolbar.no-padding .btn {  font-size: 13px;  line-height: 35px;  margin-top: 1px;}
			.widget.box .widget-content { padding: 10px; position: relative; background-color: #fff;}
			.widget.box .widget-content.no-padding {  padding: 0;}
			.widget.box .widget-content.no-padding .row {  padding-left: 15px;  padding-right: 15px;}
			.widget.box .widget-content.widget-deeper {  background-color: #f9f9f9;  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05) inset;  -moz-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05) inset;  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05) inset;}
			.widget-title {  margin-bottom: 20px;  border-bottom: 1px solid #d9d9d9;  padding: 10px 0;  font-weight: 300;  font-size: 17px;}
			.widget-title > i {  margin-right: 5px;}
			#sidebar #sidebar-content .sidebar-widget {  margin: 25px 10px;}
			.widget-content .more { clear: both; display: block; padding: 5px 10px; text-transform: uppercase; font-weight: 300;  font-size: 11px;  color: #555555;  opacity: 0.7;  margin: -10px;  margin-top: 10px;  background-color: #f9f9f9;  border-top: 1px solid #d9d9d9;}
			.widget-content .more:hover,.widget-content .more:focus {  opacity: 1;  text-decoration: none;}
			.widget-content .more:active {  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.1) inset;  border-top-color: #cccccc;}
			.widget-content .more i {  margin-top: 2px;  margin-bottom: -3px;}
			.table {  margin-bottom: 5px;}
			.table-striped tbody > tr:nth-child(odd) > td,.table-striped tbody > tr:nth-child(odd) > th {  background-color: #fafafa;}
			.table-hover tbody tr:hover > td,.table-hover tbody tr:hover > th {  background-color: #f5f5f5;}
			.table-highlight-head thead {  background-color: #f5f5f5;}
			.table-no-inner-border tr th,.table-no-inner-border tr td {  border-left-width: 0px;}
			.table-no-inner-border tr th:first-child,.table-no-inner-border tr td:first-child {  border-left-width: 1px !important;}
			.widget-content.no-padding table {  margin-bottom: 0 !important;}
			.widget-content.no-padding .table-bordered {  border: 0;}
			.widget-content.no-padding .table-bordered th:first-child,.widget-content.no-padding .table-bordered td:first-child {  border-left: 0;}
			.widget-content.no-padding .table-bordered th:last-child,.widget-content.no-padding .table-bordered td:last-child {  border-right: 0;}
			.widget-content.no-padding .table-bordered tr:last-child td {  border-bottom: 0;}
			.table .align-center {  text-align: center;}
			.table-controls > li {  display: inline-block;  margin: 0 2px;  line-height: 1;}
			.table-controls > li > a {  display: inline-block;}
			.table-controls > li > a i {  margin: 0;  font-size: 13px;  color: #555555;  display: block;}
			.table-controls > li > a i:hover {  text-decoration: none;}
			.table-vertical-align tr,.table-vertical-align th,.table-vertical-align td {  vertical-align: middle !important;}
			table {  border-collapse: collapse;  border-spacing: 0;}
			body {  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;  font-size: 14px;  line-height: 1.428571429;  color: #333333;  background-color: #ffffff;}
			h3,h4,.h3,.h4 {  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;  font-weight: 500;  line-height: 1.1;}
			h3 { margin-top: 20px; margin-bottom: 10px;}
			h4{margin-top: 10px;margin-bottom: 10px;}
			h3,.h3 {  font-size: 24px;}
			h4,.h4 {  font-size: 18px;}
			h3 small,.h3 small,h4 small,.h4 small {  font-size: 14px;}
			.page-header { padding-bottom: 9px;  margin: 40px 0 20px;}
			.container {  padding-right: 15px;  padding-left: 15px;  margin-right: auto;  margin-left: auto;}
			.container:before,.container:after {  display: table;  content: " ";}
			.container:after {  clear: both;}
			.container:before,.container:after {  display: table;  content: " ";}
			.container:after {  clear: both;}
			.container-rep {  padding-right: 15px;  padding-left: 15px;  margin-right: auto;  margin-left: auto;}
			.container-rep:before,.container-rep:after {  display: table;  content: " ";}
			.container-rep:after {  clear: both;}
			.container-rep:before,.container-rep:after {  display: table;  content: " ";}
			.container-rep:after {  clear: both;}
			.row {  margin-right: -15px;  margin-left: -15px;}
			.row:before,.row:after {  display: table;  content: " ";}
			.row:after {  clear: both;}
			.row:before,.row:after {  display: table;  content: " ";}
			.row:after {  clear: both;}
			.col-md-12{  position: relative;  min-height: 1px;  padding-right: 15px;  padding-left: 15px;}
			table {  max-width: 100%;  background-color: transparent;}
			th {  text-align: left;}
			.table {  width: 100%;  margin-bottom: 20px;}
			.table thead > tr > th,.table tbody > tr > th,.table tfoot > tr > th,.table thead > tr > td,.table tbody > tr > td,.table tfoot > tr > td {  padding: 8px;  line-height: 1.428571429;  vertical-align: top;  border-top: 1px solid #dddddd;}
			.table thead > tr > th {vertical-align: bottom;border-bottom: 2px solid #dddddd;}
			.table tbody + tbody { border-top: 2px solid #dddddd;}
			.table .table { background-color: #ffffff;}
			.table-bordered > thead > tr > th,.table-bordered > tbody > tr > th,.table-bordered > tfoot > tr > th,.table-bordered > thead > tr > td,.table-bordered > tbody > tr > td,.table-bordered > tfoot > tr > td {  border: 1px solid #dddddd;}
			.table-bordered > thead > tr > th,.table-bordered > thead > tr > td {  border-bottom-width: 2px;}
			.table-striped > tbody > tr:nth-child(odd) > td,.table-striped > tbody > tr:nth-child(odd) > th {  background-color: #f9f9f9;}
			.table-hover > tbody > tr:hover > td,.table-hover > tbody > tr:hover > th {  background-color: #f5f5f5;}
			table col[class*="col-"] {  display: table-column;  float: none;}
			table td[class*="col-"],table th[class*="col-"] {  display: table-cell;  float: none;}
			.table-hover > tbody > tr > td.danger:hover,.table-hover > tbody > tr > th.danger:hover,.table-hover > tbody > tr.danger:hover > td {  background-color: #ebcccc;  border-color: #e6c1c7;}
			.table-hover > tbody > tr > td.warning:hover,.table-hover > tbody > tr > th.warning:hover,.table-hover > tbody > tr.warning:hover > td {  background-color: #faf2cc;  border-color: #f8e5be;}
		</style>
	</head>
<body style="height: 259px;">
	
	<div id="container" class="fixed-header">
		
		
<div id="content-rep">
                <div class="container">
                    <center>    <img src="data:image/png;base64, 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" /></center>
                </div>
				<div class="row">
					<div class="col-md-12">
						<div class="widget box">
							<div class="widget-header">
								<h4>Results : </h4>
							</div>
							<div class="widget-content no-padding" style="display: block;">
								<div id="DataTables_Table_0_wrapper" class="dataTables_wrapper form-inline" role="grid">
									<div role="grid" class="dataTables_wrapper form-inline" id="DataTables_Table_0_wrapper">
										<div id="DataTables_Table_0_wrapper" class="dataTables_wrapper form-inline" role="grid">
											<table aria-describedby="DataTables_Table_0_info" id="DataTables_Table_0" class="table table-striped table-bordered table-hover table-checkable table-columnfilter datatable dataTable" data-columnfilter="{&quot;aoColumns&quot;: [ null, {&quot;type&quot;: &quot;text&quot;}, {&quot;type&quot;: &quot;text&quot;}, {&quot;type&quot;: &quot;text&quot;}, { &quot;type&quot;: &quot;select&quot; } ]}" data-columnfilter-select2="true">
									<thead>
										<tr role="row"><th aria-label="activate to sort column ascending" style="width: 320px;" colspan="1" rowspan="1" aria-controls="DataTables_Table_0" tabindex="0" role="columnheader" class="sorting">Infected File</th><th aria-label="" style="width: 250px;" colspan="1" rowspan="1" aria-controls="DataTables_Table_0" tabindex="0" role="columnheader" class="sorting">Desctiption</th><th class="hidden-xs sorting" role="columnheader" tabindex="0" aria-controls="DataTables_Table_0" rowspan="1" colspan="1" style="width: 217px;" aria-label=": activate to sort column ascending">Risk</th></tr>
									</thead>
								<tbody aria-relevant="all" aria-live="polite" role="alert"><tr class="odd">
"""
	report.write(html_str)
	for i in range(len(infected_files)):
		query_db(infected_signature[i])
		report.write("<td>" + infected_files[i] + "</td><td>" + description[i] + "</td><td>" + risk[i] + "</td></tr>")
	end_str = """
	</td>
										</tr></tbody></table>
									
									</div>
								
								</div>
							</div>
							</div>
						</div>
					</div>
				</div>
		</div>
		</div>

</div></body></html>
            
"""	
	report.write(end_str)
	report.close()
	open_file = "your report is saved at : " + report_save_path
	cprint(open_file,"blue")
def cleanup():
	delete = "cd " + main_path + "&& rm *" 
	os.system(delete)							
connect_db()
scan_temp()
write_report(reports)
cleanup()
save_report_db()
cp_report = report_path + "/" + report_name + "..html"
pass_report = "cp {0} {1}".format(cp_report,web_ui_reports)
os.system(pass_report)

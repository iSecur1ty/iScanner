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

import os,web,time
from web import form
import hashlib
import MySQLdb
from web import session
from Module.web_config import *
from threading import Timer

urls = (
'/login', 'login',
'/index', 'index',
'/', 'index',
'/reports', 'reports',
'/reports/delete/(.+)', 'delete',
'/new_scan', 'new_scan',
'/profile', 'profile',
'/logout', 'logout',
)
		
render = web.template.render('Templates/')
cookie_name = "iScanner_Cookies"

class login:
	
 login_form = web.form.Form(web.form.Textbox('username'),
 web.form.Password('password'),
 )
        
 def GET(self):		
	  f = self.login_form()
	  return render.login(f)
		
	
 def POST(self):
     f = self.login_form()
     if not f.validates():
		 return render.login(f)	 
     else:
      username = f.d.username
      password = hashlib.md5(f.d.password).hexdigest()
      db = MySQLdb.connect(host=mysql_host,user=mysql_user,passwd=mysql_pass,db=mysql_db)
      query_check = "SELECT * FROM `ADMIN` WHERE username ='{0}' AND password='{1}'".format(username,password)
      query = db.cursor()
      query_login = query.execute(query_check)
      if  query_login == 1:
		  cookie_name = "iScanner_Cookies"
		  cookie_value = password
		  web.setcookie(cookie_name, cookie_value, expires="600", domain=None, secure=False)
		  check_Cookies = web.cookies().get(cookie_name)
		  url = "/index"
		  web.redirect(url)
      else:
	   return render.error_login(f)
          
class index: 
    def GET(self):
			db_connect = MySQLdb.connect(host=mysql_host,user=mysql_user,passwd=mysql_pass,db=mysql_db)
			db_row = db_connect.cursor()
			query = db_row.execute("SELECT * FROM ADMIN")
			row = db_row.fetchone()
			password_row = row[2]		
			check_Cookies = web.cookies().get(cookie_name)
			db_connect = MySQLdb.connect(host=mysql_host,user=mysql_user,passwd=mysql_pass,db=mysql_db)
			db_row = db_connect.cursor()
			query = db_row.execute("SELECT * FROM ADMIN")
			user = db_row.fetchone()
			session_name = user[1]	
			if password_row == check_Cookies:
			 try: 
			  db_chart = MySQLdb.connect(host=mysql_host,user=mysql_user,passwd=mysql_pass,db=mysql_db)
			  db_row2 = db_chart.cursor()
			  query2 = db_row2.execute("SELECT * FROM scans_info ORDER BY scan_id desc")
			  chart = db_row2.fetchone()
			  last_scan = chart[1]
			  risk_high_chart = chart[6]
			  risk_meduim_chart = chart[7]
			  risk_low_chart = chart[8]	
			  risk_information_chart = chart[9]
			  infected_file = chart[5]
			  return render.new_index(last_scan,infected_file,session_name,risk_high_chart,risk_meduim_chart,risk_low_chart,risk_information_chart)
			 except:
				return render.error_index(session_name)		
			else:
				url = "/login"
				web.redirect(url)
class reports:
	def GET(self):
			db_connect = MySQLdb.connect(host=mysql_host,user=mysql_user,passwd=mysql_pass,db=mysql_db)
			db_row = db_connect.cursor()
			query = db_row.execute("SELECT * FROM ADMIN")
			row = db_row.fetchone()
			password_row = row[2]		
			check_Cookies = web.cookies().get(cookie_name)
			if password_row == check_Cookies:
			 db_connect = MySQLdb.connect(host=mysql_host,user=mysql_user,passwd=mysql_pass,db=mysql_db)
			 db_row = db_connect.cursor()
			 query = db_row.execute("SELECT * FROM scans_info ORDER BY scan_id desc")
			 row = db_row.fetchone()
			 rowz = list()
			 while row is not None:
				  rowz.append(row)
				  row = db_row.fetchone()
			 db_connect = MySQLdb.connect(host=mysql_host,user=mysql_user,passwd=mysql_pass,db=mysql_db)
			 db_row = db_connect.cursor()
			 query = db_row.execute("SELECT * FROM ADMIN")
			 user = db_row.fetchone()
			 session_name = user[1]
			 return render.reports(rowz,session_name)
			else:
				url = "/login"
				web.redirect(url)
class delete:
	def GET(self, scan_id):
		db = web.database(dbn='mysql', db=mysql_db, user=mysql_user, pw=mysql_pass)
		pass_delete = "scan_id={0}".format(scan_id)
		db.delete('scans_info',where=pass_delete)
		urlz = "/reports"
		web.redirect(urlz)			
class new_scan:
	
 scan_form = web.form.Form(
 web.form.Textbox("scan_path" ,class_="form-control bs-tooltip",style="text-align:left;direction:ltr;width:350px;float:right"), #, style="text-align:right;direction:rtl;width:350px;float:right"),
 web.form.Textbox("scan_name" ,class_="form-control bs-tooltip",style="text-align:left;direction:ltr;width:350px;float:right"),
 web.form.Dropdown("scan_type",[('php', 'php'), ('javascript', 'js'), ('html', 'html'), ('-A', 'All files')],class_="form-control -tooltip",style="text-align:left;direction:ltr;width:350px;float:right"),
 web.form.Button("scan",class_="btn btn-default")
 )
     	      	
 def GET(self):
	 		db_connect = MySQLdb.connect(host=mysql_host,user=mysql_user,passwd=mysql_pass,db=mysql_db)
			db_row = db_connect.cursor()
			query = db_row.execute("SELECT * FROM ADMIN")
			user = db_row.fetchone()
			session_name = user[1]	
			db_connect = MySQLdb.connect(host=mysql_host,user=mysql_user,passwd=mysql_pass,db=mysql_db)
			db_row = db_connect.cursor()
			query = db_row.execute("SELECT * FROM ADMIN")
			row = db_row.fetchone()
			password_row = row[2]		
			check_Cookies = web.cookies().get(cookie_name)
			if password_row == check_Cookies:
				fform = self.scan_form()
				return render.new_scan(session_name,fform)
			else:
				login = "/login"
				web.redirect(login)
 def POST(self):
    f = self.scan_form()
    if not f.validates():
      return render.login(f)	
    else:
		scan_path =  f.d.scan_path
		scan_type =  f.d.scan_type
		scan_name =  f.d.scan_name
		scan_pass = "python " + iscanner_path +  "scan_module.py {0} {1} {2} ".format(scan_path, scan_type, scan_name)
		os.system(scan_pass)
		rurl = "/reports"
		web.redirect(rurl)	
		
class logout:
	def GET(self):
			db_connect = MySQLdb.connect(host=mysql_host,user=mysql_user,passwd=mysql_pass,db=mysql_db)
			db_row = db_connect.cursor()
			query = db_row.execute("SELECT * FROM scans_info")
			row = db_row.fetchone()
			cookie_value = row[2]		
			web.setcookie(cookie_name, cookie_value, expires=-13233, domain=None)
			url = "/login"
			web.redirect(url)
if __name__ == "__main__":
 app = web.application(urls,globals())
 app.run()

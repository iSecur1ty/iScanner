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



import os,sys,time,fnmatch
from config import * #import some data that used in this module
from banner import *

if len(sys.argv) <= 3:
	show_banner()
	sys.exit(0)
directory_input = sys.argv[1] # take user input to collect files from a whole directory.

tempfile = main_path + "/temp" # temporary sacn file path

def main(): # main function
 with open(tempfile, "w") as mfile:
  for root, dirs, files in os.walk(directory_input): # run for loop with os walk to find full file path.
   for file in files:
    root_file = os.path.join(root,file)
    root_file_path = os.path.abspath(root_file)
    write_to_temp = open(tempfile, "a")
    write_to_temp.write(root_file_path + "\n")
    write_to_temp.close()
def php(): # collect php files in temporary file
  for root, dirs, files in os.walk(directory_input):
	  file_type="*.php"
	  for filename in fnmatch.filter(files, file_type):
		  php_temp_file = main_path+"/temp_php.temp"
		  php_file_save = open(php_temp_file, "a")
		  php_file_save.write(os.path.join(root,filename + "\n"))
		  php_file_save.close()
def html():
	for root, dirs, files in os.walk(directory_input):
		file_type="*.html"
		for filename in fnmatch.filter(files, file_type):
			html_temp_file = main_path+"/temp_html.temp"
			html_file_save = open(html_temp_file, "a")
			html_file_save.write(os.path.join(root,filename + "\n"))
			html_file_save.close()
def js():
	for root, dirs, files in os.walk(directory_input):
		file_type="*.js"
		for filename in fnmatch.filter(files, file_type):
			js_temp_file = main_path+"/temp_js.temp"
			js_file_save = open(js_temp_file, "a")
			js_file_save.write(os.path.join(root,filename + "\n"))
			js_file_save.close()


if sys.argv[2] == "-A":
	main()
if sys.argv[2] == "php":
	php()
if sys.argv[2] == "js":
	js()
if sys.argv[2] == "html":
	html()

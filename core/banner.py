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
# -*- coding: utf-8 -*-
from termcolor import cprint
import sys
def show_banner():
        iscanner = ''' 
 _ ____                                  
(_) ___|  ___ __ _ _ __  _ __   ___ _ __ 
| \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
| |___) | (_| (_| | | | | | | |  __/ |   
|_|____/ \___\__,_|_| |_|_| |_|\___|_|   
                                               
        '''
        cprint (iscanner,"blue")
        cprint(" -- You need to specify args for scan -- ",'yellow')
        usage = "" + sys.argv[0] + " [path_to_scan] [scan_type] [scan_name]"
        example = "-- For example -- "+ sys.argv[0] + " /home -A iscanner_all_test"
        example2 = "-- For example -- "+ sys.argv[0] + " /home php iscanner_php_test"
        example3 = "-- For example -- "+ sys.argv[0] + " /home js iscanner_javascript_test"
        example4 = "-- For example -- "+ sys.argv[0] + " /home html iscanner_php_test"
	cprint (usage, 'green') 
	cprint(example,'red')
	cprint(example2,'red')
	cprint(example3,'red')
	cprint(example4,'red')

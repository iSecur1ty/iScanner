
CREATE TABLE 'malware_information' (
  'id' int(11) NOT NULL,
  'name' text NOT NULL,
  'signature' text NOT NULL,
  'description' text NOT NULL,
  'risk' text NOT NULL,
  'type' varchar(255) NOT NULL,
  PRIMARY KEY ('id')
) ;


-- I didn't found how to insert this raw
-- INSERT INTO 'malware_information' VALUES 
--(25,'SAUDI_SHELL_V1.0',"if ($page != $s) { echo \"<a class=\'hr\' href=\'$pg?sws=ms&op=trak&page=$s\'>$ap</a>\";}",'Saudi shell is an Arabian php script that used to attack web servers.','High','PHP');




INSERT INTO 'malware_information' VALUES 
(1,'C99_PHP_SHELL','c99_buff_prepare()','C99 is a powerful php shell that used to control webservers','High','PHP');
INSERT INTO 'malware_information' VALUES  
(3,'C99_PHP_SHELL','c99_sess_put','C99 is a powerful php shell that used to control webservers','High','PHP');
INSERT INTO 'malware_information' VALUES 
(4,'C99_PHP_SHELL','c99fsearch','C99 is a powerful php shell that used to control webservers','High','PHP');
INSERT INTO 'malware_information' VALUES 
(5,'C99_PHP_SHELL','c99sh_getupdate()','C99 is a powerful php shell that used to control webservers','High','PHP');
INSERT INTO 'malware_information' VALUES 
(7,'C99_PHP_SHELL','fs_copy_obj()','C99 is a powerful php shell that used to control webservers','High','PHP');
INSERT INTO 'malware_information' VALUES 
(8,'C99_PHP_SHELL','myshellexec','C99 is a powerful php shell that used to control webservers','High','PHP');
INSERT INTO 'malware_information' VALUES 
(9,'C99_PHP_SHELL','str2mini','C99 is a powerful php shell that used to control webservers','High','PHP');
INSERT INTO 'malware_information' VALUES  
(10,'EVAL_BASE64_PHP_CODE','eval(base64_decode(','eval base64_deocde is a function in php that allow you to execute encrypted code with base64. ','Information','PHP');
INSERT INTO 'malware_information' VALUES 
(11,'R57_PHP_SHELL','U_wordwrap','r57 is a powerful php shell that used by most of hackers , the hacker can control the web server and execute commands.','High','PHP');
INSERT INTO 'malware_information' VALUES 
(12,'R57_PHP_SHELL','GetFilesTotal()','r57 is a powerful php shell that used by most of hackers , the hacker can control the web server and execute commands.','High','PHP');
INSERT INTO 'malware_information' VALUES 
(16,'METASLOIT_PHP_METERPRETER','$s = $f(\"tcp://{$ip}:{$port}\")','Metaploit php meterpreter is very powerful tool that use to gain access to Linux/Unix systems and allow the attacker to execute codes and do privileges escalation attacks , meterpreter depends on php sockets so that you can disable it to stop any php meterpreter in your system.','High','PHP');
INSERT INTO 'malware_information' VALUES 
(17,'IFRAME_HTML_JS','iframe','iframe html tag can use for CSA attacks , check this file and be sure that iframe tag used for normal usage.','Information','PHP');
INSERT INTO 'malware_information' VALUES 
(18,'CGI_TELNET_SCRIPT','sub PrintPageHeader','CGI-Telnet is a CGI script that allows you to execute commands on your web server. It is a useful tool if you dont have telnet access to your server.','Medium','PERL');
INSERT INTO 'malware_information' VALUES 
(19,'PYTHON_SOCKET','socket.socket(socket.AF_INET, socket.SOCK_STREAM)','the hackers can use this socket to make connection with the server.','Information','PYTHON');
INSERT INTO 'malware_information' VALUES 
(20,'C100_PHP_SHELL','elseif(@is_resource($f = @popen($cfe,\"r\")))','C100 is a powerful php shell that used to control webservers','High','PHP');
INSERT INTO 'malware_information' VALUES 
(21,'TRYAG_PHP_SHELL','echo \"  <td style=\\\"padding-left: 5px;\\\">[<a href=\\\"?dir=\".urlencode($dir).\"/\".urlencode($file).\"\\\">','tryag is a powerful php shell that used to control webservers.','High','PHP');
INSERT INTO 'malware_information' VALUES 
(22,'TRYAG_PHP_SHELL','function getphpcfg($varname)','tryag is a powerful php shell that used to control webservers.','High','PHP');
INSERT INTO 'malware_information' VALUES 
(23,'SAUDI_SHELL_V1.0',"if ($_GET['sws']== 'phpinfo')",'Saudi shell is an Arabian php script that used to attack web servers.','High','PHP');
INSERT INTO 'malware_information' VALUES 
(24,'SAUDI_SHELL_V1.0',"'.$_SERVER['HTTP_HOST'].' ~ Saudi Sh3ll",'Saudi shell is an Arabian php script that used to attack web servers.','High','PHP');

INSERT INTO 'malware_information' VALUES 
(26,'PHP_CPANEL_GRAPPER',"foreach(glob(\'/var/cpanel/sessions/raw/*\') as $file)",'This tool can grap all Cpanel sessions when the hacker has a root privileges.','Medium','PHP');

INSERT INTO 'malware_information' VALUES 
(27,'ZONE-H_PERL_SCRIPT','$sock = IO::Socket::INET->new(PeerAddr => \"www.zone-h.org\", PeerPort => 80, Proto => \"tcp\") or next;','','Low','PERL');

INSERT INTO 'malware_information' VALUES 
(28,'PHP_CPANEL_MYSQL_GRAPPER','9SivcZ1ENod50D1XHRKC8ZQ5UDcsNZcz8DrCjnBNUEXUHBKIQa15jaBN9ndyUS2L6RdEUEXUHBrIyScpNoL0fp0F3oihNa7ZhR704nP9hoP5ha13vlKguSKqUwGXwm4h9ndyUS2L6Sdz2nBXzEBSi3iXcoivzBrJrwBFrn7fjndJuDJzJmdJinP3hoc0fSQFb1cIuDrfJZQqKwG9NSrCLn1o8EkXHoP5ha13vlrIuDrfJZQ5UDcsNlGgXD1JiS7','This tool can grap all Cpanel sessions when the hacker has a root privileges.','Medium','PHP');
INSERT INTO 'malware_information' VALUES 
(29,'ROOT_SHELL_V1.0','Pz48P3BocA0KNXJyMnJfcjVwMnJ0NG5nKDApOyAvL0lmIHRoNXI1IDRzIDFuIDVycjJyLCB3NSdsbCBzaDJ3IDR0LCBrPw0KJHAxc3N3MnJkID0gIiI7IC8vIFkyMyBjMW4gcDN0IDEgbWRpIHN0cjRuZyBoNXI1IHQyMiwgZjJyIHBsMTRudDV4dCBwMXNzdzJyZHM6IG0xeCBvNiBjaDFycy4NCiRtNSA9IGIxczVuMW01KF9fRklMRV9fKTsNCiRjMjJrNDVuMW01ID0gInc0NTU1NTUiOw0KDQo0Zig0c3M1dCgkX1BPU1RbJ3Axc3MnXSkpIC8vSWYgdGg1IDNzNXIgbTFkNSAxIGwyZzRuIDF0dDVtcHQsICJwMXNzIiB3NGxsIGI1IHM1dCA1aD8NCnsNCiA0ZihzdHJsNW4oJHAxc3N3MnJkKSA9PSBvYSkgLy9JZiB0aDUgbDVuZ3RoIDJmIHRoNSBwMXNzdzJyZCA0cyBvYSBjaDFyMWN0NXJzLCB0aHI1MXQgNHQgMXMgMW4gbWRpLg0KIHsNCiAgJF9QT1NUWydwMXNzJ10gPSBtZGkoJF9QT1NUWydwMXNzJ10pOw0KIH0NCiA0ZigkX1BPU1RbJ3Axc3MnXSA9PSAkcDFzc3cycmQpDQogew0KICAgczV0YzIyazQ1KCRjMjJrNDVuMW01LCAkX1BPU1RbJ3Axc3MnXSwgdDRtNSgpK29lMDApOyAvL0l0J3MgMWxyNGdodCwgbDV0IGg1bSA0bg0KIH0NCiByNWwyMWQoKTsNCn0NCg0KNGYoITVtcHR5KCRwMXNzdzJyZCkgJiYgITRzczV0KCRfQ09PS0lFWyRjMjJrNDVuMW01XSkgMnIgKCRfQ09PS0lFWyRjMjJrNDVuMW01XSAhPSAkcDFzc3cycmQpKQ0Kew0KIGwyZzRuKCk7DQogZDQ1KCk7DQp9DQovLw0KLy9EMiBuMnQgY3Iyc3MgdGg0cyBsNG41ISBBbGwgYzJkNSBwbDFjNWQgMWZ0NXIgdGg0cyBibDJjayBjMW4ndCBiNSA1eDVjM3Q1ZCB3NHRoMjN0IGI1NG5nIGwyZ2c1ZCA0biENCi8vDQo0Zig0c3M1dCgkX0dFVFsncCddKSAmJiAkX0dFVFsncCddID09ICJsMmcyM3QiKQ0Kew0KczV0YzIyazQ1ICgkYzIyazQ1bjFtNSwgIiIsIHQ0bTUoKSAtIG9lMDApOw0KcjVsMjFkKCk7DQp9DQo0Zig0c3M1dCgkX0dFVFsnZDRyJ10pKQ0Kew0KIGNoZDRyKCRfR0VUWydkNHInXSk7DQp9DQoNCiRwMWc1cyA9IDFycjF5KA0KICdjbWQnID0','Root shell is a powerful php script that used to attack web servers.','High','PHP');
INSERT INTO 'malware_information' VALUES 
(30,'PHP_INDEX_INJECTOR','wexJFJEvNI0hkzShcmaVC3Opd24IF2aiFMYPhtOkUAlkUAlkUAlkUBXpGXPLUAlkUAlkUAlkUALxwe0IdblzFBxgFbalFmLPwlYwT1FIarytTrAIA1OnayaTwJL7tJOkUAlkUAlkUAlkdoXINUniFmkiGUIpKXp3DolScUILfoyJdoAINUnsGbYxdy9McbOjDy9iFmkiGUILUAlkUAlkUAlkUALxhUl7tJOkUAlkUAlkUAlkHBXINUEJA0aHOAYAwtPIOlkNTUELfoyJdoadTMysca0JKXPLUAlkUAlkUAlkUTrxwe0IdblzFBxgFbalFmLPkrlkUAlkUAlkUALxdtL7tJOkUAlkUAlkUAlSUALINUnEdblzFBxgcMa0C2igCbYzd2HPkrlkUAlkUAlkUALxHUL7tMlMhtrLUAlkUAlkUAlkdrlkhbShC29VfolVfBA7tm0hkrlkUAlkUAlkUBxkHUE9woyZFMy5b2slGbHPkrlkUAlkUAlkUBxkUUL7tJOkUAlkUAlkUAlkdoxdkuOiCMxlBZfKCB1lk11fwe0IkrlkUAlkUAlkUBxkHTShgWPLUAlkUAlkUAlkdoxSwe0ICbkZCbLPhTShcM9ZcByjDtILUAlkUAlkUAlkUBxSwoyzwtO0CBkScT0','this script allow hackers to inject html codes , to any page in your site.','High','PHP');
INSERT INTO 'malware_information' VALUES 
(31,'Fx0_PHP_SHELL','srvYVT6v4vSX85zCfUomIy3Y/IPzkg0JH9/TCG6igeISw4G3348OV0YvCRxop3sY5rjaKbyLDsWFntEu7e20Zw6r25TB3T0PKdUwEOqDuAA31DUM/1zOcfTni0n1E1T+qLYnyfCF0dVddj3bwC0Ns9wQOIb8l/qXdbcqwIoy/YpQ8n0VZSEqFj9LhULAHMSeJL7AaQArhFA+fAxJmKvzYKn5c5uPeWmRG/CfHsSsl3/VrI0cSGv8go5yim2jNoVe0XxdhH8z4ABvztkd4nVPqrqVXpjARkSAr9DcNJjE0WQiosgyFHK2wn5JEYnlyaLwWr3NbUe39iJqO9fo+mvdlCyev5peyqqIIqDlMzKUuMME4bruudz/hwU7Q6YH56iKUc3NVa5c2w0MBLoKwL5MyTtwWRGLy+PBScZSq6JotT9Y8NhGWhG/fpwPCypXkhfFHDitYGLUYnHrHaXkqQrvr8I4jIoYv0bJv5rXT3VleCP6WrN+Ue7+pUOVP+gvoNNfnqhl2LuP+b6r5n+KGwCYOK/lb5H0dRzKAi2BxZLWpxEEdbPUgC2dFYn8Ao5i+8IaXm90r0P7wD4HXgA+0U2lhRox','Fx0 is a powerful php shell that used to control webservers , and Allow hackers ','High','PHP');
INSERT INTO 'malware_information' VALUES 
(32,'SEC_WAR_SHELL','$fp2 = fopen(\".htaccess\",\"w+\");','Sec war shell is powerful php script that allow the hackers to execute commands in your system.','High','PHP');









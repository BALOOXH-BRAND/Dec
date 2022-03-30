#coding=utf-8
#!/usr/bin/python2
#This Script Write By Tech Baba
#Public Script free
import os 
import base64
import requests
import platform
#module 
logo_base = 'G1swOzk3bQkkJCQkJCQkJCAgJCQkJCQkJCQgICQkICAgICAkJAoJJCQgICAgICQkICQkICAgICAkJCAgJCQgICAkJAoJJCQgICAgICQkICQkICAgICAkJCAgICQkICQkCgkkJCQkJCQkJCAgJCQgICAgICQkICAgICQkJAoJJCQgICAkJCAgICQkICAgICAkJCAgICQkICQkCgkkJCAgICAkJCAgJCQgICAgICQkICAkJCAgICQkCgkkJCAgICAgJCQgJCQkJCQkJCQgICQkICAgICAkJAotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQogfHwgG1swOzk3bRtbMDs0MW0gUHJvZ3JhbW1pbmcgaXMgdGhpbmtpbmcgbm90IHR5cGluZyA6KSAbWzBtIHx8Ci0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tChtbMDs5N20g4p6kIEF1dGhvciAgOiBZZXN3YW50IE1pc2hyYQobWzA7OTdtIOKepCBWZXJzaW9uIDogMy4wChtbMDs5N20g4p6kIGZiLXBhZ2UgOiBodHRwczovL2ZiLmNvbS9UZWNobmljYWwuTWlzaHJhCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t'
logo = base64.b64decode(logo_base) # logo with base64 encodeing :)
#you can change logo :)  put your logo in logo = () 
#
#this is token genrator for use dont try to be edit any 
xox = platform.platform()[::-1].replace('.', '').replace('-', '').replace(' ', '').upper()
#Server github link :)
server = requests.get('https://raw.githubusercontent.com/TECH-BABA/Python-Script-Open-source/main/server.txt').text
# server can you change to us our server :)
# make on your github any text file and view raw copy link and paste here to be use your github server 
def main():
	os.system("clear")
	print logo
	if xox in server:
		os.system("clear")
		print logo
		print""
		print("\033[1;96m\t ||• Your Subscription  Allow   •||\033[1;97m")
	else:
		os.system("clear")
		print logo
		print("\033[1;95m\t||• Your Subscription No Allow  •||\033[1;97m")
		print 47*("-")
		print(" ➤ Your Token : "+xox)
		print
		print("This Paid tool :) ").center(50)
		print""
		print("First Get Your subscription for use ").center(50)
		print 47*("-")
		os.system("exit")
if __name__ == '__main__':
	main()

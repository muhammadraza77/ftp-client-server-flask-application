# netstat -ano|findstr 8080
# tskill 1203
from flask import Flask, redirect, url_for, render_template, request
from ftplib import FTP
import os 
import time
app = Flask(__name__)
import socket
post=[
	{'names':'raza'},{'names':'pakistan'}
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('temp.html',posts=post)

@app.route("/send")
def send():
	s=socket.socket()
	host = socket.gethostname()
	port =8080
	# s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	return render_template('sender.html',prt=host)

@app.route("/send1")
def send1():
	filename = request.args.get('filename')
	fileloc = request.args.get('fileloc')	
	t = time.time()
	###################
	ftp = FTP('')
	ftp.connect('localhost',1026)
	ftp.login(user="user",passwd="12345")
	#print(ftp.pwd())
	ftp.cwd('\\')
	ftp.retrlines('LIST')
	print(filename,"***")
	# filename = 'git commands.txt'
	pl=open(fileloc+"\\"+filename,'rb')
	ftp.storbinary('STOR '+filename ,pl)
	ftp.quit()
	#################
	elapsed_time = time.time() - t
	print("Total Time for this Transaction is :",elapsed_time)
	return redirect('/home')

@app.route("/recieve")
def recieve():
    return render_template('reciever.html',posts=post)

@app.route("/reciever1")
def recieve1():
	host = request.args.get('host')
	filename = request.args.get('addr')	
	# filename='C:\\Users\\th\\Downloads\\pl5677.txt'
	t = time.time()
	######################################
	ftp = FTP('')
	ftp.connect('localhost',1026)
	ftp.login(user="user",passwd="12345")
	#print(ftp.pwd())
	ftp.cwd('\\')
	ftp.retrlines('LIST')

	localfile=open(host+'\\'+filename,'wb')
	ftp.retrbinary('RETR ' + filename, localfile.write, 1024)

	ftp.quit()
	localfile.close()	
	#####################################
	elapsed_time = time.time() - t
	print("Total Time for this Transaction is :",elapsed_time)
	
	return redirect('/home')

if __name__=='__main__':
	app.run(debug=True)

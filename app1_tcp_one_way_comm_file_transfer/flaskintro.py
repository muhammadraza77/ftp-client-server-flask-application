# netstat -ano|findstr 8080
# tskill 1203
from flask import Flask, redirect, url_for, render_template, request
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
	s=socket.socket()
	host = socket.gethostname()
	port =8080
	# s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	s.bind((host,port))
	s.listen(1)
	filename = request.args.get('addr')	

	conn, addr =s.accept()
	# filename='C:\\Users\\th\\Downloads\\pl.txt'
	file =open(filename, 'rb')
	file_data= file.read(1024)
	conn.send(file_data)

	return redirect('/home')

@app.route("/recieve")
def recieve():
    return render_template('reciever.html',posts=post)

@app.route("/reciever1")
def recieve1():
	host = request.args.get('host')
	filename = request.args.get('addr')	
	# filename='C:\\Users\\th\\Downloads\\pl5677.txt'
	s=socket.socket()
	port =8080
	s.connect((host,port))
	
	file =open(filename ,'wb')
	file_data = s.recv(1024)
	
	file.write(file_data)
	file.close()
	return redirect('/home')

if __name__=='__main__':
	app.run(debug=True)

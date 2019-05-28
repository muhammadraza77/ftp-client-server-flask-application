from pyftpdlib.authorizers import DummyAuthorizer 
from pyftpdlib.handlers import FTPHandler 
from pyftpdlib.servers import FTPServer  

authorizer=DummyAuthorizer() 

authorizer.add_user("user","12345","C:\\Users\\th\\Down loads\\FTPserver",perm="elradfmw") 
authorizer.add_anonymous("C:\\Users\\th\\Downloads\\FTP server",perm="elradfmw")  

handler= FTPHandler 
handler.authorizer=authorizer  

server=FTPServer(("127.0.0.1", 1026), handler) 
server.serve_forever() 
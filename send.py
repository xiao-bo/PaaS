import xmpp 
import sys
username = 'xiao'
passwd = '1119'
to='pig@localhost'
msg='hello pig, i am xiao'+sys.argv[1]


cl = xmpp.Client('localhost')
cl.connect(server=('localhost',5222))
cl.auth(username, passwd, 'botty')
cl.sendInitPresence()
#cl.Process(1)
message = xmpp.Message(to, msg)
message.setAttr('type', 'chat')
cl.send(message)
cl.Process(1)



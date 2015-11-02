import xmpp 

username = 'xiao'
passwd = '1119'
to='pig@localhost'
msg='hello :)'


cl = xmpp.Client('localhost')
cl.connect(server=('localhost',5222))
cl.auth(username, passwd, 'botty')
cl.sendInitPresence()
cl.Process(1)
message = xmpp.Message(to, msg)
message.setAttr('type', 'chat')
cl.send(message)




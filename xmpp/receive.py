import xmpp

servername='localhost'
#servername='pass.org'
username = 'pig'
passwd = '1119'
#to='pig@localhost'
#msg='hello :)'


client = xmpp.Client(servername)
client.connect(server=(servername,5222))
client.auth(username, passwd, 'botty')
client.sendInitPresence()
#message = xmpp.Message(to, msg)
#message.setAttr('type', 'chat')


def messageCB(sess,mess):
	print 'receive message===\n'
	nick=mess.getFrom().getResource()
	text=mess.getBody()
	#print mess,nick
	print text

client.RegisterHandler('message',messageCB)
	
while 1:
	client.Process(1)
	#print 'finish message===\n'


print 'finish message===\n'

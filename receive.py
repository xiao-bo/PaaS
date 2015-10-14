import xmpp

username = 'xiao'
passwd = '1119'
to='pigwang@macbook.local'
msg='hello :)'


client = xmpp.Client('macbook.local')
client.connect(server=('macbook.local',5223))
client.auth(username, passwd, 'botty')
client.sendInitPresence()
message = xmpp.Message(to, msg)
message.setAttr('type', 'chat')


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

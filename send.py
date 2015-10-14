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
client.send(message)




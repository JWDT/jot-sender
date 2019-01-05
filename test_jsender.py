from sender import JMail, Message
from os import environ

connection_string = environ.get('SMTP_URL')

jmail = JMail(connection_string)

message = Message("Test subject", "jot-sender-test@test2.4.jotweb.uk", "This is a test message", fromaddr="jot-sender-test@test2.4.jotweb.uk")

jmail.send(message)


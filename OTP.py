import random
import smtplib  #simple message transfer protocol library

server=smtplib.SMTP('smtp.gmail.com',587) # creating gmail server (server code '587')
server.starttls() #security transfer layered security
server.login('zainulkhan032@gmail.com','isidrnoawvulsnpd')
b = ''.join([str(random.randint(0,9)) for i in range(4)]) # generates '4448' OTP GENERATE
msg='HELLO ,YOUR OTP IS '+str(b)
server.sendmail('zainulkhan032@gmail.com','zainulcharmingboy@gmail.com',msg)
server.quit()

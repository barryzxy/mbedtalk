import telnetlib
import time

host = '192.168.3.127'
# host = '10.1.2.227'
username = 'root'
password = 'root'
# password = '10HPYTAA'
finish = '#'

tn = telnetlib.Telnet(host)

xx = tn.read_until('login:')
print xx
tn.write(username + '\n')


xx = tn.read_until('Password:')
print xx
tn.write(password + '\n')

xx = tn.read_until(finish)
print xx


tn.write('cd /home/httpd/cgi-bin\n')
time.sleep(0.1)
tn.write('ls -l\n')
time.sleep(0.1)
xx = tn.read_until(finish)
print xx

tn.write('chmod 755 cgi \n')

xx = tn.read_until(finish)
print xx

time.sleep(0.2)


tn.close() 

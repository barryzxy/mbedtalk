#!/usr/bin/python  
#ftp.py  
#this script is used to make some ftp operations more convenient  
#add upload and download operations  20111210 version0.1  

import ftplib
import os

path = os.getcwd()
 
ftp = ftplib.FTP('192.168.3.127')
# ftp.login('root','root')
ftp.login('root','10HPYTAA')
print ftp.getwelcome()
#

# ftp.mkd('/home/httpd/graphics')

ftp.cwd('/home/httpd/graphics')
# ftp.retrlines('NLST')  
xx = ftp.pwd()
print xx
print('get in home')

filename = path + '/graphics/logo.jpg'
file_handler = open(filename,'rb')
try:
    yy = ftp.storbinary('STOR logo.jpg', file_handler,80960)
    print yy
except ftplib.error_perm:
    print 'fail'   




ftp.cwd('/home/httpd/')
ftp.retrlines('NLST')  
xx = ftp.pwd()
print xx
print('get in home')

filename = path + '/index.html'
file_handler = open(filename,'rb')
try:
    yy = ftp.storbinary('STOR index.html', file_handler,80960)
    print yy
except ftplib.error_perm:
    print 'fail'   

filename = path + '/logo.html'
file_handler = open(filename,'rb')
try:
    yy = ftp.storbinary('STOR logo.html', file_handler,80960)
    print yy
except ftplib.error_perm:
    print 'fail'      

filename = path + '/banner.html'
file_handler = open(filename,'rb')
try:
    yy = ftp.storbinary('STOR banner.html', file_handler,80960)
    print yy
except ftplib.error_perm:
    print 'fail'   

filename = path + '/bottom.html'
file_handler = open(filename,'rb')
try:
    yy = ftp.storbinary('STOR bottom.html', file_handler,80960)
    print yy
except ftplib.error_perm:
    print 'fail'          

filename = path + '/main.html'
file_handler = open(filename,'rb')
try:
    yy = ftp.storbinary('STOR main.html', file_handler,80960)
    print yy
except ftplib.error_perm:
    print 'fail'   

filename = path + '/menu.html'
file_handler = open(filename,'rb')
try:
    yy = ftp.storbinary('STOR menu.html', file_handler,80960)
    print yy
except ftplib.error_perm:
    print 'fail'              
#from pyadb import adb
import os
#myadb = adb.ADB('~/platform-tools/adb')
raw_str=[]
raw_number=[]
usb_str=[]
filename='data.txt'
idpwd_name="idpwd.txt"


select_bat='else.sh'   #select.bat
os.system('adb devices -l | grep ".product.">{name}'.format(name=filename))  # grep / findstr
with open(filename, 'r') as f:
    raw_str=f.readlines()

user_str=[]
id_str=[]
pwd_str=[]
with open(idpwd_name, 'r') as f:
    user_str=f.readlines()


for temp in user_str:
    id_str.append(temp.split("----")[0])
    pwd_str.append(temp.split("----")[1])

for i,item in enumerate(raw_str):
    temp=item.split("           ")[0]
    print(temp)
    usb=item.split("           ")[1].split("device ")[1].split(" product")[0]
    raw_number.append(temp)
    #cmd_str='adb -s {number} shell input text start'.format(number=temp)
    cmd_str='adb -s {number} shell input text start'.format(number=usb)
    bat_str='./{bat} {number} {username} {password}'.format(bat=select_bat,number=usb,username=id_str[i],password=pwd_str[i])  #call
    #bat_str='./{bat} {number} {username} {password}'.format(bat=select_bat,number=usb,username=id_str[i],password=pwd_str[i])  #call
    print(bat_str)
    #os.system(cmd_str)
    os.popen(bat_str)


#os.system('adb shell "dumpsys activity | grep "mFocusedActivity""')

#out = os.popen('adb shell "dumpsys activity | grep "mFocusedActivity""').read()

    


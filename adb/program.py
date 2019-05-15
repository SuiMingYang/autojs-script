import os
import tkinter
'''

version:  1.1.0
author:  smy
e-mail:  2282420654@qq.com
'''

top = tkinter.Tk()

top.title('登C号工具')


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height,
                            (screenwidth - width)/2, (screenheight - height)/2)
    print(size)
    root.geometry(size)


center_window(top, 300, 240)
top.geometry("250x500")


def helloCallBack(file):
    #tkMessageBox.showinfo( "Hello Python", "Hello Runoob")
    raw_str = []
    raw_number = []
    usb_str = []
    user_str = []
    id_str = []
    pwd_str = []
    filename = 'data.txt'
    idpwd_name = "idpwd.txt"
    # grep / findstr
    os.system('adb devices -l | findstr ".product.">{name}'.format(name=filename))
    with open(filename, 'r') as f:
        raw_str = f.readlines()

    with open(idpwd_name, 'r') as f:
        user_str = f.readlines()

    for temp in user_str:
        id_str.append(temp.split("----")[0])
        pwd_str.append(temp.split("----")[1])

    for i, item in enumerate(raw_str):
        temp = item.split("           ")[0]
        print(temp)
        usb = item.split("           ")[1].split("device ")[1].split(" product")[0]
        raw_number.append(temp)
        #cmd_str='adb -s {number} shell input text start'.format(number=temp)
        #cmd_str = 'adb -s {number} shell input text start'.format(number=usb)
        bat_str = '{bat} {number} {username} {password}'.format(bat=file, number=usb, username=id_str[i], password=pwd_str[i])  # call
        # bat_str='./{bat} {number} {username} {password}'.format(bat=select_bat,number=usb,username=id_str[i],password=pwd_str[i])  #call
        print(bat_str)
        # os.system(cmd_str)
        os.popen(bat_str)


B1 = tkinter.Button(top, text=u"加好友", command=lambda:helloCallBack(u"打开微信并登陆.bat"))
B2 = tkinter.Button(top, text=u"登陆", command=lambda:helloCallBack(u"登陆.bat"))
B3 = tkinter.Button(top, text=u"截图", command=lambda:helloCallBack(u"截图.bat"))
B4 = tkinter.Button(top, text=u"加好友", command=lambda:helloCallBack(u"加好友.bat"))
B1.pack()
B2.pack()
B3.pack()
B4.pack()
top.mainloop()

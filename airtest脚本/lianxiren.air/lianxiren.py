# coding=utf-8

__author__ = "suimingyang"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import json
#from poco.sdk.interfaces.screen import ScreenInterface
poco = AndroidUiautomationPoco(force_restart=False)

auto_setup(__file__)

device_h=1500

names=[]

i=1
j=1

while not poco("com.tencent.mm:id/azr").exists():
   #最大的块是：0.35
   #连字母的高度：0.13828125
   #最小高度：0.0875
    device_list=poco("com.tencent.mm:id/m_").child("android.widget.LinearLayout")
    cur_h=device_list[0].get_size()[1]
    print(cur_h)
    if cur_h>0.3:#直接滑动
        swipe((100,100+device_h*cur_h),(100,92))
    else:
        #先获取名字再滑动
        #获取名字：层级判断
        #跳过：文件传输助手
        ui=poco("com.tencent.mm:id/m_").child("android.widget.LinearLayout")[1].child("android.widget.LinearLayout").child("com.tencent.mm:id/n4").child("android.widget.LinearLayout").child("com.tencent.mm:id/n8")
        name=ui.get_text()
        with open('name.txt', 'a') as f:
            f.write(json.dumps(name))
            f.write("\n")
        #f.write(str(name.encode("gb18030").decode("gb18030")))
        #滑动poco("com.tencent.mm:id/azr")
        names.append(json.dumps(name))
        print(names)
        swipe((100,100+device_h*cur_h),(100,100))

'''        
with open('name.txt', 'a') as f:
        f.write(names)
        f.write("\n")
'''

'''
for item in names:
    poco("android:id/list").child("com.tencent.mm:id/d4l")[0].child("android.widget.RelativeLayout")[4].child("com.tencent.mm:id/dwu").click()

    poco("com.tencent.mm:id/b79").click()

    ddd=u'\u8d75\u6c38\u5efa'
    ddd.encode("gb18030").decode("gb18030")

    text(ddd)
    poco("com.tencent.mm:id/pp").click()
        
#f.close()     

#'\u6587'.decode('unicode_escape')
#print(poco("com.tencent.mm:id/m_").child("android.widget.LinearLayout")[2].child("android.widget.LinearLayout").child("com.tencent.mm:id/n4").get_text())

#print(poco("com.tencent.mm:id/m_").child("android.widget.LinearLayout")[2].get_size()[0])
'''
'''
height_t1=poco("com.tencent.mm:id/m_").child("android.widget.LinearLayout")[0].get_size()[1]
height_t2=poco("com.tencent.mm:id/m_").child("android.widget.LinearLayout")[1].get_size()[1]
height_t3=poco("com.tencent.mm:id/m_").child("android.widget.LinearLayout")[2].get_size()[1]
height_t4=poco("com.tencent.mm:id/m_").child("android.widget.LinearLayout")[3].get_size()[1]

print(height_t1)
print(height_t2)
print(height_t3)
print(height_t4)


poco("com.tencent.mm:id/m_").child("android.widget.LinearLayout")[1]


#poco("com.tencent.mm:id/m_").child("android.widget.LinearLayout")[0].click()

'''



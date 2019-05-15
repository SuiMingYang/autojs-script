# -*- encoding=utf8 -*-
__author__ = "suimingyang"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.sdk.interfaces.screen import ScreenInterface
poco = AndroidUiautomationPoco(force_restart=False)
import json

auto_setup(__file__)

'''
with open('name.txt', 'r') as f:
    f.readline()
    f.write("\n")
'''
names=[]

for i,line in enumerate(open("./name.txt","r")): 
    names.append(json.loads(line))

poco("com.tencent.mm:id/d4l").child("android.widget.RelativeLayout")[1].child("com.tencent.mm:id/dwu").click()

for i,item in enumerate(names):

    poco("com.tencent.mm:id/b79").click()

    item=item.encode("gb18030").decode("gb18030")

    text(item)
    poco("com.tencent.mm:id/pp").click()


#添加
poco("com.tencent.mm:id/jq").click()







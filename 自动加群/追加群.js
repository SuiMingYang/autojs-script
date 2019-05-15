launchApp("微信");
//群置顶，

var name_str = rawInput("请输入您的名字", "朱媛,白晓明");
name_str = name_str.replace(/\'/g, "");
toast("您的名字是" + name_str);
var namestr=name_str.split(",");
//var namestr=["和秀娜","白晓明","黄洪印","女王新款连衣裙","景焱","朱媛"]

toast(className("android.widget.FrameLayout").findOne().child(0).child(0).child(0).child(9).text());
//id("azj").click();
className("android.widget.FrameLayout").findOne().child(0).child(0).child(0).child(9).click();

//id("j1").click();
desc("聊天信息").findOne().click();

//sleep(5000);
toast(namestr.length);
//var plus=id("cwt").findOne().child().size();
toast(desc("添加成员").findOne().desc());
desc("添加成员").findOne().parent().click();
//id("cwt").findOne().child(1).click();

for(var i=0;i<namestr.length;i++){
  //id("b26").findOne().setText(namestr[i]);
  text("搜索").findOne().setText(namestr[i]);
  //press(530,563,100);
  sleep(1000);
  toast(namestr[i]);

  //id("x8").findOne().parent().click();
  text(namestr[i]).findOne().parent().click();
  sleep(1000);
  
}
//id("j0").findOne().click();
desc("当前所在页面,选择联系人").findOne().child(0).child(2).click();

toast("追加完成");
/*toast(id("au_").findOne().text());
if(id("au_").exists()){
    text("确定").findOne().click();
}
else{
        
}*/

if(className("android.widget.Button").findOne().text()=="确定"){
    className("android.widget.Button").findOne().click();
}
else{
    
}


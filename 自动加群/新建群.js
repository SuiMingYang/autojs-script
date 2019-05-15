launchApp("微信");

var groupstr = rawInput("请输入群名称", "测试测试");
toast("群名称" + groupstr);

var name_str = rawInput("请输入您的名字", "");//刘'倩云,和'秀娜,景'焱,黄洪'印
name_str = name_str.replace(/\'/g, "");
toast("您的名字是" + name_str);
var namestr=name_str.split(",");

//id("azj").click();
//id("j1").click();
//更多功能按钮
desc('更多功能按钮').findOne().click();
text('发起群聊').findOne().parent().click();
//sleep(5000);
toast(namestr.length);
//var plus=id("cwt").findOne().child().size();

//id("cwt").findOne().child(1).click();

for(var i=0;i<namestr.length;i++){
  //id("b26").findOne().setText(namestr[i]);
  text("搜索").findOne().setText(namestr[i]);

  //press(530,563,100);
  sleep(1000);
  toast(namestr[i]);
  //id("hc").findOne().child(1).click();
  //toast(id("x8").findOne().className());
  
  //id("x8").findOne().parent().click();
  text(namestr[i]).findOne().parent().click();

  sleep(1000);
  
}
/////////id("j0").findOne().click();
desc("当前所在页面,发起群聊").findOne().child(0).child(2).click();
toast("建群完成");
//toast(id("au_").findOne().text());
/*if(id("au_").exists()){
    text("确定").findOne().click();
}
else{
        
}*/

//改名
sleep(1000);
toast(desc("聊天信息").findOne().clickable());
desc("聊天信息").findOne().click();
//id("j1").findOne().click();
text('未命名').findOne().parent().click();
className("EditText").findOne().setText(groupstr);
text("保存").findOne().click();

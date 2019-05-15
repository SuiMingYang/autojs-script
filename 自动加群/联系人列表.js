launchApp("微信");
var name_str=[];

/*
var name_str=['aaa,bbb,aaa,bbb,ccc,ddd,qqq,www,aaa,ccc,ddd,vvv,bbb'];

namestr.split(',');
for(var i=0;i<namestr.length;i++){
    toast(namestr[i]);
}
*/

//toast(className("android.widget.FrameLayout").findOne().child(0).child(0).child(1).find());//child(1).child(1).text()


var user_count = rawInput("联系人数量", 200);
var chat_id=rawInput("聊天界面的id","")//mc
user_count=Math.ceil(user_count/10);
for (var i = 0; i < user_count; i++) {
    sleep(2000);
    var lqname = id(chat_id).find();//className("android.widget.FrameLayout").findOne().child(0).child(0).child(1);//id("k9").find();mc
    //toast(lqname);
    toast(lqname.size());
    //toast(lqname.empty());
    lqname.each(function(v){
        toast(v.text());
        name_str.push(v.text());
        sleep(1000);
    });
    sleep(lqname.size()*1000);
    Swipe(500, 1000, 500, 125, 3000);
    Swipe(500, 1000, 500, 125, 3000);
    sleep(6000);
}
toast("结束");

function unique1(arr){
  var hash=[];
  for (var i = 0; i < arr.length; i++) {
     if(hash.indexOf(arr[i])==-1){
      hash.push(arr[i]);
     }
  }
  return hash;
}
name_str=unique1(name_str);
log(name_str.length);
log(name_str);
console.show();


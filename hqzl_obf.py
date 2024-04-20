import requests ,json ,logging ,time ,random #line:1:import requests,json,logging,time,random
from qingguo_proxy import proxyget #line:2:from qingguo_proxy import proxyget
import datetime #line:3:import datetime
from concurrent .futures import ThreadPoolExecutor #line:6:from concurrent.futures import ThreadPoolExecutor
import concurrent .futures #line:7:import concurrent.futures
from header_data import *#line:9:from header_data import *
token ="";RemoteIp1 ="";hqaid ="";tokenPhone =""#line:10:token="";RemoteIp1="";hqaid="";tokenPhone=""
APP_NAME ='红旗智联'#line:11:APP_NAME = '红旗智联'
ENV_NAME ='hzlCookie'#line:12:ENV_NAME = 'hzlCookie'
import os #line:14:import os
hzlCookie =os .environ .get ('hzlCookie')#line:15:hzlCookie=os.environ.get('hzlCookie')
hzlCookie ="15687183623---1622477399339565057---eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmVzIjoyNTkyMDAwLCJ1c2VyX2lkIjo3ODI0NTYzMDQ5MDI4NjQ4OTYsImlzcyI6IlJCQUMtQVBJIiwidG9rZW5Gcm9tIjoiQVBQIiwiZXhwIjoxNzExODgxNDU2LCJpYXQiOjE3MDkyODk0NTYsInNpZ25fdGltZSI6MTcwOTI4OTQ1Njc3NH0.JyJLvygZ_js5CnrDdN2hhtuGgvgHarTjH8fcgjyd6Mw"#line:16:hzlCookie="15687183623---1622477399339565057---eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmVzIjoyNTkyMDAwLCJ1c2VyX2lkIjo3ODI0NTYzMDQ5MDI4NjQ4OTYsImlzcyI6IlJCQUMtQVBJIiwidG9rZW5Gcm9tIjoiQVBQIiwiZXhwIjoxNzExODgxNDU2LCJpYXQiOjE3MDkyODk0NTYsInNpZ25fdGltZSI6MTcwOTI4OTQ1Njc3NH0.JyJLvygZ_js5CnrDdN2hhtuGgvgHarTjH8fcgjyd6Mw"
dayalist =[];#line:17:dayalist = [];
executor =ThreadPoolExecutor (max_workers =32 )#line:19:executor = ThreadPoolExecutor(max_workers=32)  # ThreadPoolExecutor构造示例，max_workers参数表示最多工作的线程数
future_tasks =[]#line:20:future_tasks=[] #线程池异步提交结果
def selecttoken ():#line:22:def selecttoken():
    OOO00OO000OOO0OO0 ="hqqc_token_go1"#line:23:tokenType="hqqc_token_go1"
    changeEevDate ();#line:26:changeEevDate();
    print (f"\n----------总共【{len(dayalist)}】条数据-----------\n")#line:29:print(f"\n----------总共【{len(dayalist)}】条数据-----------\n")
    for O0OOO0OOO00O00OOO ,O0O000000000O0OO0 in enumerate (dayalist ):#line:30:for index, tokeinfo in enumerate(dayalist):
        if O0OOO0OOO00O00OOO <0 :#line:31:if index < 0:
            continue ;#line:32:continue;
        global tokenPhone ;#line:33:global tokenPhone ;
        OO0OO0OOOO00OOOO0 =O0O000000000O0OO0 .split ("---")#line:34:dateinfo=tokeinfo.split("---")
        tokenPhone =OO0OO0OOOO00OOOO0 [0 ];#line:35:tokenPhone=dateinfo[0];
        print (f"开始第{O0OOO0OOO00O00OOO}个，手机号{tokenPhone}");#line:36:print(f"开始第{index}个，手机号{tokenPhone}");
        print (f"当前时间:{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")#line:37:print(f"当前时间:{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        global token ;global hqaid ;global RemoteIp1 #line:38:global token;global hqaid;global RemoteIp1
        hqaid =OO0OO0OOOO00OOOO0 [1 ];#line:39:hqaid =dateinfo[1];
        token =OO0OO0OOOO00OOOO0 [2 ];#line:40:token = dateinfo[2];
        RemoteIp1 =getrandomip ();#line:41:RemoteIp1 = getrandomip();
        try :#line:42:try:
            time .sleep (5 )#line:43:time.sleep(5)
            dotaskAll (OOO00OO000OOO0OO0 ,tokenPhone );#line:44:dotaskAll(tokenType,tokenPhone);
        except Exception as OO00O0O00O0O0O00O :#line:45:except Exception as e:
            print ("出现异常",OO00O0O00O0O0O00O )#line:46:print("出现异常", e)
        O0OOO0OOO00O00OOO +=1 ;#line:47:index += 1;
    concurrent .futures .as_completed (future_tasks );#line:50:concurrent.futures.as_completed(future_tasks);
    print ("等待异步结果执行完毕");#line:51:print("等待异步结果执行完毕");
def getSN ():#line:55:def getSN():
    O0OOO000OOOO00000 =os .popen ("sudo dmidecode -s baseboard-serial-number | awk '{print $0}'").readlines ()#line:56:sn = os.popen("sudo dmidecode -s baseboard-serial-number | awk '{print $0}'").readlines()
    return O0OOO000OOOO00000 [0 ].strip ()#line:57:return sn[0].strip()
def changeEevDate ():#line:59:def changeEevDate():
    global dayalist ;#line:60:global dayalist;
    if hzlCookie is not None :#line:61:if hzlCookie is not None:
        if "@"in hzlCookie :#line:62:if "@" in hzlCookie:
            dayalist =hzlCookie .split ("@");#line:63:dayalist = hzlCookie.split("@");
        elif "\n"in hzlCookie :#line:64:elif  "\n" in hzlCookie:
            dayalist =hzlCookie .split ("\n");#line:65:dayalist = hzlCookie.split("\n");
        else :#line:66:else:
            dayalist .append (hzlCookie );#line:67:dayalist.append(hzlCookie);
    else :#line:68:else:
        print (f"\n提示：未填写环境变量hzlCookie")#line:69:print(f"\n提示：未填写环境变量hzlCookie")
    print (f'''
    ✨✨✨ {APP_NAME}脚本✨✨✨
    ✨ 功能：
          签到
          分享
          发帖
          点赞
    ✨ 抓包步骤：
          打开{APP_NAME}APP或小程序
          点击我的
          打开抓包工具
          点击“积分”，以下几种url之一：
            https://hqapp.faw.cn/fawcshop/collect-sns/v1 开头的请求里面的Authorization 和aid
        多账号@分割 
        单个账号 手机号---aid---Authorization
    ✨ ✨✨wxpusher一对一推送功能，
      ✨需要定义变量export WXPUSHER=wxpusher的app_token，不设置则不启用wxpusher一对一推送
      ✨需要在{ENV_NAME}变量最后添加@wxpusher的UID
    ✨ 设置青龙变量：
    export {ENV_NAME}='url'多账号#分割
    export SCRIPT_UPDATE = 'False' 关闭脚本自动更新，默认开启
    ✨✨✨ @Author HAZY✨✨✨
        ''')#line:93:''')
def dotaskAll (O0000O000O00O0O0O ,OO000O000O00OO00O ):#line:94:def dotaskAll(tokenType,tokenPhone):
    O0O00000000000OOO =getLevelAndHonorAcquireCountAndProportion ();#line:95:testRes=getLevelAndHonorAcquireCountAndProportion();
    if O0O00000000000OOO .get ("code")=="000000":#line:96:if testRes.get("code")=="000000":
        print ("token校验成功");#line:97:print("token校验成功");
        O000OOOO0OO0O000O =random .randint (10 ,30 )#line:99:randomDely=random.randint(10,30)
        print (f'随机延时：{O000OOOO0OO0O000O}秒！！！');#line:100:print(f'随机延时：{randomDely}秒！！！');
        time .sleep (O000OOOO0OO0O000O )#line:101:time.sleep(randomDely)
        try :#line:102:try:
            O000O0OOO0000OOO0 =getTaskList ();#line:103:tasjinfo=getTaskList();
            if O000O0OOO0000OOO0 !=None :#line:107:if tasjinfo != None:
                OO0OO00O00O0OO000 =O000O0OOO0000OOO0 ["data"]["taskList"]#line:108:tasklist = tasjinfo["data"]["taskList"]
                for OOOOO0O00OOOO00OO in OO0OO00O00O0OO000 :#line:109:for i in tasklist:
                    global signInVo ;#line:110:global signInVo;
                    if "-APP_article"in OOOOO0O00OOOO00OO ['taskCode']and OOOOO0O00OOOO00OO ['completeFlag']==None :#line:112:if "-APP_article" in i['taskCode'] and i['completeFlag'] == None:
                        print ("开始发帖");#line:113:print("开始发帖");
                        pushArricle ();#line:114:pushArricle();
                    if "-APP_signed"in OOOOO0O00OOOO00OO ['taskCode']and OOOOO0O00OOOO00OO ['completeFlag']==None :#line:116:if "-APP_signed" in i['taskCode'] and i['completeFlag'] == None:
                        signInVo =signInlist [random .randint (0 ,len (signInlist )-1 )];#line:118:signInVo = signInlist[random.randint(0, len(signInlist) - 1)];
                        signin ();#line:119:signin();
                    if "-APP_share"in OOOOO0O00OOOO00OO ['taskCode']and OOOOO0O00OOOO00OO ['completeFlag']==None :#line:121:if "-APP_share" in i['taskCode'] and i['completeFlag'] == None:
                        time .sleep (5 )#line:122:time.sleep(5)
                        signInVo =signSharelist [random .randint (0 ,len (signSharelist )-1 )];#line:123:signInVo = signSharelist[random.randint(0, len(signSharelist) - 1)];
                        queryPostList ();#line:124:queryPostList();
                        collectLove ();#line:125:collectLove();  # 首次分享积分
                    if "-APP_isLike"in OOOOO0O00OOOO00OO ['taskCode']and OOOOO0O00OOOO00OO ['completeFlag']==None :#line:127:if "-APP_isLike" in i['taskCode'] and i['completeFlag'] == None:
                        time .sleep (5 )#line:128:time.sleep(5)
                        signInVo =signSharelist [random .randint (0 ,len (signSharelist )-1 )];#line:129:signInVo = signSharelist[random.randint(0, len(signSharelist) - 1)];
                        queryLikePostList ();#line:130:queryLikePostList();
                    if "-APP_isLike"in OOOOO0O00OOOO00OO ['taskCode']and OOOOO0O00OOOO00OO ['completeFlag']==None :#line:132:if "-APP_isLike" in i['taskCode'] and i['completeFlag'] == None:
                        time .sleep (5 )#line:133:time.sleep(5)
                        queryHotPostList ();#line:134:queryHotPostList();
            OO0000OOO00O0OO0O =getUserInfo ();#line:139:score=getUserInfo();  # 获取用户信息积分
        except Exception as O0O00OOO0000OO00O :#line:141:except Exception as e:
            print ("出现异常",O0O00OOO0000OO00O )#line:142:print("出现异常", e)
    else :#line:143:else:
       print ("token无效")#line:144:print("token无效")
def getrandomip ():#line:146:def getrandomip():
    O0O0OO0OOOO0O000O =random .randint (0 ,255 );#line:147:m = random.randint(0, 255);
    OO00O0O0O0OOO00OO =random .randint (0 ,255 );#line:148:n = random.randint(0, 255);
    O0O0O00OO0OO0O00O =random .randint (0 ,255 );#line:149:x = random.randint(0, 255);
    O0OOO00O0000O0O0O =random .randint (0 ,255 );#line:150:y = random.randint(0, 255);
    OOOOOOOO00O0OO0OO =str (O0O0OO0OOOO0O000O )+'.'+str (OO00O0O0O0OOO00OO )+'.'+str (O0O0O00OO0OO0O00O )+'.'+str (O0OOO00O0000O0O0O );#line:151:randomIP = str(m) + '.' + str(n) + '.' + str(x) + '.' + str(y);
    return OOOOOOOO00O0OO0OO #line:152:return  randomIP
def signin ():#line:153:def signin():
    OOO0OOOOOOO000OOO ="https://hqapp.faw.cn/fawcshop/collect-public/v1/score/addScore";#line:154:url="https://hqapp.faw.cn/fawcshop/collect-public/v1/score/addScore";
    OOO00OOO0OO0OOOO0 ={"scoreType":"2"}#line:155:body = {"scoreType": "2"}
    O000OOOOOOO00OOO0 =json .dumps (OOO00OOO0OO0OOOO0 )#line:156:stringJso = json.dumps(body)  # 对象转json
    OO000OO00OOO00O0O =proxyget ();#line:157:proxies = proxyget();
    OO00000000O00O000 =requests .post (OOO0OOOOOOO000OOO ,data =O000OOOOOOO00OOO0 ,headers =getheaders (),proxies =OO000OO00OOO00O0O ,timeout =8 );#line:158:response = requests.post(url, data=stringJso, headers=getheaders(), proxies=proxies,timeout=8);
    OO00000000O00O000 .json ()#line:159:response.json()
    if OO00000000O00O000 .json ().get ("code")=="000000":#line:160:if response.json().get("code") == "000000":
        print ("签到成功");#line:161:print("签到成功");
    else :#line:162:else:
        print ("签到失败",OO00000000O00O000 .json ().get ("msg"),signInVo ["timestamp"]);#line:163:print("签到失败",response.json().get("msg"),signInVo["timestamp"]);
        time .sleep (5 );#line:164:time.sleep(5);
        signin_try ();#line:165:signin_try();
def signin_try ():#line:166:def signin_try():
    global signInVo ;#line:167:global signInVo;
    signInVo =signInlist [random .randint (0 ,len (signInlist )-1 )];#line:168:signInVo = signInlist[random.randint(0, len(signInlist) - 1)];
    O0000O0O0O0OOOOO0 ="https://hqapp.faw.cn/fawcshop/collect-public/v1/score/addScore";#line:169:url="https://hqapp.faw.cn/fawcshop/collect-public/v1/score/addScore";
    OO0OO0O0O00000O0O ={"scoreType":"2"}#line:170:body = {"scoreType": "2"}
    O00O00OO0OOOOO0O0 =json .dumps (OO0OO0O0O00000O0O )#line:171:stringJso = json.dumps(body)  # 对象转json
    OO000OO0000OOO00O =proxyget ();#line:172:proxies = proxyget();
    OO0O0OO0O00O00000 =requests .post (O0000O0O0O0OOOOO0 ,data =O00O00OO0OOOOO0O0 ,headers =getheaders (),proxies =OO000OO0000OOO00O ,timeout =8 );#line:174:response = requests.post(url, data=stringJso, headers=getheaders(), proxies=proxies,timeout=8);
    OO0O0OO0O00O00000 .json ()#line:175:response.json()
    if OO0O0OO0O00O00000 .json ().get ("code")=="000000":#line:176:if response.json().get("code") == "000000":
        print ("重试签到成功");#line:177:print("重试签到成功");
    else :#line:178:else:
        print ("重试签到失败",OO0O0OO0O00O00000 .json ().get ("msg"),signInVo ["timestamp"]);#line:179:print("重试签到失败",response.json().get("msg"),signInVo["timestamp"]);
def pushArricle ():#line:181:def pushArricle():
    OOO000OOO000O0O00 =saveDynamicInfoImgUrl ();#line:182:isSuccess=saveDynamicInfoImgUrl();
    if OOO000OOO000O0O00 ==False :#line:183:if isSuccess==False:
        time .sleep (5 );#line:184:time.sleep(5);
        OOO000OOO000O0O00 =saveDynamicInfoImgUrl ();#line:185:isSuccess = saveDynamicInfoImgUrl();
        if OOO000OOO000O0O00 ==False :#line:186:if isSuccess == False:
            time .sleep (5 );#line:187:time.sleep(5);
            saveDynamicInfoImgUrl ();#line:188:saveDynamicInfoImgUrl();
def saveDynamicInfoImgUrl ():#line:189:def saveDynamicInfoImgUrl():
    O0OO0OO00O000O0O0 ="https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/saveDynamicInfoImgUrl";#line:190:url="https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/saveDynamicInfoImgUrl";
    O0000000OO000000O =getheader_article (token ,hqaid );#line:191:randomDate=getheader_article(token, hqaid);
    O00OO00OOOOOO0000 =O0000000OO000000O ["resDate"]#line:192:body =randomDate["resDate"]
    OO00O000O0000O0OO =json .dumps (O00OO00OOOOOO0000 )#line:193:stringJso = json.dumps(body)  # 对象转json
    OO0O00O0O0OO0OO0O =proxyget ();#line:194:proxies = proxyget();
    O0000000OO000000O ["headers"]["Accept-Language"]="zh-CN,zh;q=0.9"#line:196:randomDate["headers"]["Accept-Language"]="zh-CN,zh;q=0.9"
    O00O000000OOO00OO =requests .post (O0OO0OO00O000O0O0 ,data =OO00O000O0000O0OO ,headers =O0000000OO000000O ["headers"],proxies =OO0O00O0O0OO0OO0O ,timeout =8 );#line:199:response = requests.post(url, data=stringJso, headers=randomDate["headers"], proxies=proxies,timeout=8);
    O00O000000OOO00OO .json ()#line:200:response.json()
    if O00O000000OOO00OO .json ().get ("code")=="000000":#line:201:if response.json().get("code") == "000000":
        print ("发文成功");#line:202:print("发文成功");
        getMyDynamicList (tokenPhone );#line:203:getMyDynamicList(tokenPhone);
        return True ;#line:206:return True;
    else :#line:207:else:
        print ("发文失败",O00O000000OOO00OO .json ().get ("msg"));#line:208:print("发文失败",response.json().get("msg"));
        return False ;#line:209:return False;
def getDynamicList ():#line:210:def getDynamicList():
    OO000000OOOO0000O ="2024-02-26 12:12:12";#line:211:nowdate="2024-02-26 12:12:12";
    OOO0O00OO0OO000O0 ='https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/getDynamicList?pageNo=1&refreshTime='+OO000000OOOO0000O +'&likeFlag=0&orderByRule=RULE19&pageSize=100';#line:212:url = 'https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/getDynamicList?pageNo=1&refreshTime=' + nowdate + '&likeFlag=0&orderByRule=RULE19&pageSize=100';
    O0O0OO0OOOO0OOOO0 =proxyget ();#line:213:proxies = proxyget();
    OO000O0O0O0OOOOOO =requests .get (OOO0O00OO0OO000O0 ,data ="",headers =getheaders (),proxies =O0O0OO0OOOO0OOOO0 ,timeout =8 );#line:214:response = requests.get(url, data="", headers=getheaders(), proxies=proxies,timeout=8);
    OO000O0O0O0OOOOOO .json ()#line:215:response.json()
    if OO000O0O0O0OOOOOO .json ().get ("code")=="000000":#line:216:if response.json().get("code") == "000000":
        print ("发文成功");#line:217:print("发文成功");
    else :#line:218:else:
        print ("发文失败",OO000O0O0O0OOOOOO .json ().get ("msg"),signInVo ["timestamp"]);#line:219:print("发文失败",response.json().get("msg"),signInVo["timestamp"]);
def getMyDynamicList (OO000OOOO000O0000 ):#line:221:def getMyDynamicList(tokenPhone):
    time .sleep (5 );#line:222:time.sleep(5);
    OOOOO0O0OO00O00O0 =datetime .datetime .now ()#line:223:now = datetime.datetime.now()
    O0O0O000O00O0000O =OOOOO0O0OO00O00O0 .strftime ("%Y-%m-%d %H:%M:%S")#line:225:formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    OO0OO0O0OOOO00000 =f'https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/getDynamicList?visitedAid={hqaid}&pageNo=1&refreshTime={O0O0O000O00O0000O}&likeFlag=1&pageSize=10';#line:226:url = f'https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/getDynamicList?visitedAid={hqaid}&pageNo=1&refreshTime={formatted_time}&likeFlag=1&pageSize=10';
    O0OOOO00OO0O0OOO0 =proxyget ();#line:227:proxies = proxyget();
    OO0O0000O0OO0OOO0 =getheaders ();#line:228:headerAsync=getheaders();
    OOO0OO00O0OO00OOO =requests .get (OO0OO0O0OOOO00000 ,data ="",headers =OO0O0000O0OO0OOO0 ,proxies =O0OOOO00OO0O0OOO0 ,timeout =8 );#line:229:response = requests.get(url, data="", headers=headerAsync, proxies=proxies,timeout=8);
    OOO0OO00O0OO00OOO .json ()#line:230:response.json()
    if OOO0OO00O0OO00OOO .json ().get ("code")=="000000":#line:231:if response.json().get("code") == "000000":
        OOO0O00OO000OOOOO =OOO0OO00O0OO00OOO .json ().get ("data");#line:232:datalist=response.json().get("data");
        if len (OOO0O00OO000OOOOO )>0 :#line:233:if len(datalist)>0:
            OO00000O00OOO0O00 =random .randint (60 ,120 )#line:235:randomDely = random.randint(60, 120)
            time .sleep (OO00000O00OOO0O00 )#line:236:time.sleep(randomDely)
            O000OOO0000000OOO =deleteInvitationById (OOO0O00OO000OOOOO [0 ],OO0O0000O0OO0OOO0 ,OO000OOOO000O0000 );#line:238:isdeleteSuccess=deleteInvitationById(datalist[0],headerAsync,tokenPhone);
            if not O000OOO0000000OOO :#line:239:if not isdeleteSuccess:
                deleteInvitationById (OOO0O00OO000OOOOO [0 ],OO0O0000O0OO0OOO0 ,OO000OOOO000O0000 );#line:240:deleteInvitationById(datalist[0], headerAsync, tokenPhone);
    else :#line:242:else:
        print ("获取文章失败",OOO0OO00O0OO00OOO .json ().get ("msg"));#line:243:print("获取文章失败", response.json().get("msg"));
def deleteInvitationById (O00OO0OO0O0OOOOO0 ,OO000OO0O0O00OO0O ,OOOO0OO0OO0000O0O ):#line:246:def deleteInvitationById(dataArc,headerAsync,tokenPhone):
    OO000OO000000OOOO =O00OO0OO0O0OOOOO0 .get ("id");#line:247:pid=dataArc.get("id");
    O00O0OOO00OO000OO =O00OO0OO0O0OOOOO0 .get ("createTime");#line:248:createTime = dataArc.get("createTime");
    if O00O0OOO00OO000OO <(datetime .datetime .now ()-datetime .timedelta (days =10 )).strftime ("%Y-%m-%d %H:%M:%S"):#line:249:if createTime<(datetime.datetime.now()-datetime.timedelta(days=10)).strftime("%Y-%m-%d %H:%M:%S"):
        print (f"{O00O0OOO00OO000OO}时间过早暂不删除");#line:250:print(f"{createTime}时间过早暂不删除");
        return True ;#line:251:return True;
    OO0000OO0OOOOOOO0 =f'https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/deleteInvitationById';#line:252:url = f'https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/deleteInvitationById';
    OO0O00O00OO0OOO00 ={"id":OO000OO000000OOOO ,"busType":1 };#line:253:body={"id":pid,"busType":1};
    O0OOOO00O00O0OOOO =proxyget ();#line:254:proxies = proxyget();
    O0O00O0OOOOO000OO =json .dumps (OO0O00O00OO0OOO00 )#line:255:stringJso = json.dumps(body)  # 对象转json
    O000000O0O0O00O0O =requests .post (OO0000OO0OOOOOOO0 ,data =O0O00O0OOOOO000OO ,headers =OO000OO0O0O00OO0O ,proxies =O0OOOO00O00O0OOOO ,timeout =8 );#line:256:response = requests.post(url, data=stringJso, headers=headerAsync, proxies=proxies, timeout=8);
    O000000O0O0O00O0O .json ()#line:257:response.json()
    if O000000O0O0O00O0O .json ().get ("code")=="000000":#line:258:if response.json().get("code") == "000000":
        print (f"手机号{OOOO0OO0OO0000O0O}-删除成功");#line:259:print(f"手机号{tokenPhone}-删除成功");
        return True ;#line:260:return True;
    else :#line:261:else:
        print (f"删除失败,创建时间{O00O0OOO00OO000OO}");#line:262:print(f"删除失败,创建时间{createTime}");
        return False ;#line:263:return False;
def queryPostList ():#line:265:def queryPostList():
    OO0O0O00OOO000O00 ='https://hqapp.faw.cn/fawcshop/cms/api/front/content/queryPostList?city\u003d%E5%8C%97%E4%BA%AC%E5%B8%82\u0026stats\u003d2\u0026pageNo\u003d1\u0026pageSize\u003d100';#line:266:url = 'https://hqapp.faw.cn/fawcshop/cms/api/front/content/queryPostList?city\u003d%E5%8C%97%E4%BA%AC%E5%B8%82\u0026stats\u003d2\u0026pageNo\u003d1\u0026pageSize\u003d100';
    OOOO00OO0000OOO00 =proxyget ();#line:267:proxies = proxyget();
    OO000O0O0O0O0OOOO =requests .get (OO0O0O00OOO000O00 ,data ="",headers =getheaders (),proxies =OOOO00OO0000OOO00 ,timeout =8 );#line:268:response = requests.get(url, data="", headers=getheaders(), proxies=proxies,timeout=8);
    OO000O0O0O0O0OOOO .json ()#line:269:response.json()
    if OO000O0O0O0O0OOOO .json ().get ("code")=="000000":#line:270:if response.json().get("code") == "000000":
        OOOOOO0O0O00OOO0O =OO000O0O0O0O0OOOO .json ()["data"];#line:271:resultlist=response.json()["data"];
        OO0OOO0O0OO0OO000 =OOOOOO0O0O00OOO0O [random .randint (0 ,len (OOOOOO0O0O00OOO0O )-1 )]["contentId"];#line:272:contentId = resultlist[random.randint(0, len(resultlist) - 1)]["contentId"];
        shareAc (OO0OOO0O0OO0OO000 );#line:273:shareAc(contentId);
    else :#line:275:else:
        print ("签到失败",OO000O0O0O0O0OOOO .json ().get ("msg"));#line:276:print("签到失败",response.json().get("msg"));
def queryHotPostList ():#line:278:def queryHotPostList():
    O0OOO0OOOOO000O0O ="1";#line:279:pageNo="1";
    OOOOO00OO00OOO0OO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S');#line:280:nowdate=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S');
    OOO00000OOOO0OO0O ='https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/getDynamicList?pageNo='+O0OOO0OOOOO000O0O +'&refreshTime='+OOOOO00OO00OOO0OO +'&likeFlag=0&orderByRule=RULE15&pageSize=10';#line:281:url = 'https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/getDynamicList?pageNo='+pageNo+'&refreshTime=' + nowdate + '&likeFlag=0&orderByRule=RULE15&pageSize=10';
    OOOOOO00000OOO000 =proxyget ();#line:282:proxies = proxyget();
    O0O0000OOOO0O00O0 =requests .get (OOO00000OOOO0OO0O ,data ="",headers =getheaders (),proxies =OOOOOO00000OOO000 ,timeout =8 );#line:283:response = requests.get(url, data="", headers=getheaders(), proxies=proxies,timeout=8);
    O0O0000OOOO0O00O0 .json ()#line:284:response.json()
    if O0O0000OOOO0O00O0 .json ().get ("code")=="000000":#line:285:if response.json().get("code") == "000000":
        O0O00OO00O0OOOOO0 =O0O0000OOOO0O00O0 .json ()["data"];#line:286:resultlist=response.json()["data"];
        O0OOOOO00OOOOO0O0 =O0O00OO00O0OOOOO0 [random .randint (0 ,len (O0O00OO00O0OOOOO0 )-1 )]["id"];#line:287:contentId = resultlist[random.randint(0, len(resultlist) - 1)]["id"];
        saveCommentDetailsRevision (O0OOOOO00OOOOO0O0 );#line:288:saveCommentDetailsRevision(contentId);
    else :#line:290:else:
        print ("签到失败",O0O0000OOOO0O00O0 .json ().get ("msg"));#line:291:print("签到失败",response.json().get("msg"));
def queryLikePostList ():#line:292:def queryLikePostList():
    O0O0O0O0O0OOOO00O ='https://hqapp.faw.cn/fawcshop/cms/api/front/content/queryPostList?city\u003d%E5%8C%97%E4%BA%AC%E5%B8%82\u0026stats\u003d2\u0026pageNo\u003d1\u0026pageSize\u003d100';#line:293:url = 'https://hqapp.faw.cn/fawcshop/cms/api/front/content/queryPostList?city\u003d%E5%8C%97%E4%BA%AC%E5%B8%82\u0026stats\u003d2\u0026pageNo\u003d1\u0026pageSize\u003d100';
    O0O0O000OO0O00O00 =proxyget ();#line:294:proxies = proxyget();
    OOOO00O000O00O0OO =requests .get (O0O0O0O0O0OOOO00O ,data ="",headers =getheaders (),proxies =O0O0O000OO0O00O00 ,timeout =8 );#line:295:response = requests.get(url, data="", headers=getheaders(), proxies=proxies,timeout=8);
    OOOO00O000O00O0OO .json ()#line:296:response.json()
    if OOOO00O000O00O0OO .json ().get ("code")=="000000":#line:297:if response.json().get("code") == "000000":
        OO00O0O000OOOO00O =OOOO00O000O00O0OO .json ()["data"];#line:298:resultlist=response.json()["data"];
        OOO0O0O000O0O00O0 =OO00O0O000OOOO00O [random .randint (0 ,len (OO00O0O000OOOO00O )-1 )]["contentId"];#line:299:contentId = resultlist[random.randint(0, len(resultlist) - 1)]["contentId"];
        getILikeThis (OOO0O0O000O0O00O0 );#line:300:getILikeThis(contentId);
    else :#line:301:else:
        print ("点赞失败",OOOO00O000O00O0OO .json ().get ("msg"));#line:302:print("点赞失败",response.json().get("msg"));
def shareAc (O0OOO0O0O0O0OOOO0 ):#line:303:def shareAc(contentId):
    OO0O0O0OO000O0000 ="https://hqapp.faw.cn/fawcshop/collect-public/v1/score/addScore";#line:304:url="https://hqapp.faw.cn/fawcshop/collect-public/v1/score/addScore";
    O0OOO0OO0O0O0000O ={'scoreType':'4'}#line:305:body = {'scoreType': '4'}
    OOOOOO0O00O0OOO00 =json .dumps (O0OOO0OO0O0O0000O )#line:306:stringJso = json.dumps(body)# 对象转json
    O000O00O0O000OO00 =proxyget ();#line:307:proxies = proxyget();
    global signInVo ;#line:308:global signInVo;
    signInVo =signSharelist [random .randint (0 ,len (signSharelist )-1 )];#line:309:signInVo = signSharelist[random.randint(0, len(signSharelist) - 1)];
    OO0OOOOO000000000 =requests .post (OO0O0O0OO000O0000 ,data =OOOOOO0O00O0OOO00 ,headers =getheaders (),proxies =O000O00O0O000OO00 ,timeout =8 );#line:310:response = requests.post(url, data=stringJso, headers=getheaders(), proxies=proxies,timeout=8);
    OO0OOOOO000000000 .json ()#line:311:response.json()
    if OO0OOOOO000000000 .json ().get ("code")=="000000":#line:312:if response.json().get("code") == "000000":
        if OO0OOOOO000000000 .json ()["data"]["score"]!=None :#line:313:if response.json()["data"]["score"] != None:
            print ("分享成功，获得：%s积分"%OO0OOOOO000000000 .json ()["data"]["score"]);#line:314:print("分享成功，获得：%s积分"%response.json()["data"]["score"]);
        else :#line:315:else:
            print ("分享成功，但每周上限一次，故未获得积分");#line:316:print("分享成功，但每周上限一次，故未获得积分");
    else :#line:317:else:
        print ("分享失败",OO0OOOOO000000000 .json ().get ("msg"));#line:318:print("分享失败",response.json().get("msg"));
def getLevelAndHonorAcquireCountAndProportion ():#line:319:def getLevelAndHonorAcquireCountAndProportion():
    O0OOO000O0OOOO00O ="https://hqapp.faw.cn/fawcshop/members/personal/getLevelAndHonorAcquireCountAndProportion";#line:320:url="https://hqapp.faw.cn/fawcshop/members/personal/getLevelAndHonorAcquireCountAndProportion";
    OO0OOOO000O000OO0 =proxyget ();#line:321:proxies = proxyget();
    O0OOOOO00OOO00O0O =requests .post (O0OOO000O0OOOO00O ,data ="",headers =getheaders (),proxies =OO0OOOO000O000OO0 ,timeout =8 );#line:322:response = requests.post(url, data="", headers=getheaders(), proxies=proxies,timeout=8);
    return O0OOOOO00OOO00O0O .json ();#line:323:return response.json();
def collectLove ():#line:324:def collectLove():
    OOO0O0000OOO00000 ="https://hqapp.faw.cn/fawcshop/members/currency/account/collectLove";#line:325:url="https://hqapp.faw.cn/fawcshop/members/currency/account/collectLove";
    O0O0O0O0OOOO0OO00 =proxyget ();#line:326:proxies = proxyget();
    OOOO000000O0OO00O =requests .get (OOO0O0000OOO00000 ,data ="",headers =getheaders (),proxies =O0O0O0O0OOOO0OO00 ,timeout =8 );#line:327:response = requests.get(url, data="", headers=getheaders(), proxies=proxies,timeout=8);
    return OOOO000000O0OO00O .json ();#line:328:return response.json();
def getILikeThis (OOO0O0O0000O0O0O0 ):#line:329:def getILikeThis(id):
    OOOOO0O00O0O0OO00 ='https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/getILikeThis?invId='+str (OOO0O0O0000O0O0O0 );#line:330:url= 'https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/getILikeThis?invId=' + str(id);
    OO00O0O000OOO0O00 =proxyget ();#line:331:proxies = proxyget();
    O0O0O000O000O0OOO =requests .get (OOOOO0O00O0O0OO00 ,data ="",headers =getheaders (),proxies =OO00O0O000OOO0O00 ,timeout =8 );#line:332:response = requests.get(url, data="", headers=getheaders(), proxies=proxies,timeout=8);
    return O0O0O000O000O0OOO .json ();#line:333:return response.json();
    if O0O0O000O000O0OOO .json ().get ("code")=="000000":#line:334:if response.json().get("code") == "000000":
        print (O0O0O000O000O0OOO .json ().get ("msg"));#line:335:print(response.json().get("msg"));
    else :#line:336:else:
      print ("点赞失败");#line:337:print("点赞失败");
def commentList (OOOOO000O0000O000 ):#line:339:def commentList(contentId):
    OOO0000OOOO0O0000 ='https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/getCommentDetailsInfoListNew?commentType=8500&contentId='+str (OOOOO000O0000O000 )+'&pageNo=1&pageSize=100&commentDetailsId=&orderByRule=RULE10';#line:340:url = 'https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/getCommentDetailsInfoListNew?commentType=8500&contentId=' + str(contentId) + '&pageNo=1&pageSize=100&commentDetailsId=&orderByRule=RULE10';
    O0O0O0OO0OO00O000 =proxyget ();#line:341:proxies = proxyget();
    O000O0OO000O0000O =requests .get (OOO0000OOOO0O0000 ,data ="",headers =getheaders (),proxies =O0O0O0OO0OO00O000 ,timeout =8 );#line:342:response = requests.get(url, data="", headers=getheaders(), proxies=proxies,timeout=8);
    if O000O0OO000O0000O .json ().get ("code")=="000000":#line:343:if response.json().get("code") == "000000":
        print (O000O0OO000O0000O .json ().get ("msg"));#line:344:print(response.json().get("msg"));
        O00OO0OO00OOOOO00 =O000O0OO000O0000O .json ().get ("data").get ("result");#line:345:commontlistres=response.json().get("data").get("result");
        if (len (O00OO0OO00OOOOO00 )>0 ):#line:346:if(len(commontlistres) >0):
            OOOOO000O0000O000 =O00OO0OO00OOOOO00 [random .randint (0 ,len (O00OO0OO00OOOOO00 )-1 )]["contentId"];#line:347:contentId = commontlistres[random.randint(0, len(commontlistres) - 1)]["contentId"];
            saveCommentDetailsRevision (OOOOO000O0000O000 );#line:348:saveCommentDetailsRevision(contentId);
    else :#line:349:else:
      print ("点赞失败");#line:350:print("点赞失败");
def saveCommentDetailsRevision (OOOOOO0000OOOOOOO ):#line:353:def saveCommentDetailsRevision(contentId):
    global signInVo ;#line:354:global signInVo;
    signInVo =commontList [random .randint (0 ,len (commontList )-1 )];#line:355:signInVo = commontList[random.randint(0, len(commontList) - 1)];
    OO000O0O0O0OOO0O0 ="https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/saveCommentDetailsRevision";#line:356:url="https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/saveCommentDetailsRevision";
    OO0O0O000OO000OOO ={"commentContext":signInVo .get ('commentContext'),"commentType":"8500","contentId":OOOOOO0000OOOOOOO ,"parentId":"0","fileString":[]}#line:357:body = {"commentContext":signInVo.get('commentContext'),"commentType":"8500","contentId":contentId,"parentId":"0","fileString":[]}
    OO0O0O000OO000OOO =signInVo .get ('commentContext')#line:358:body=signInVo.get('commentContext')
    O0O0OOOO00OO0OOOO =json .dumps (OO0O0O000OO000OOO )#line:360:stringJso = json.dumps(body)  # 对象转json
    OOOO0OOO00O00O00O ={"Content-Type":"application/json",}#line:361:headers = {"Content-Type": "application/json", }
    OOOO000O00000OO00 =requests .post (OO000O0O0O0OOO0O0 ,data =O0O0OOOO00OO0OOOO ,headers =getheaders ());#line:362:response = requests.post(url, data=stringJso, headers=getheaders());
    if OOOO000O00000OO00 .json ().get ("code")=="000000":#line:363:if response.json().get("code") == "000000":
        print (f'''评论成功{OOOO000O00000OO00.json().get("msg")}''');#line:364:print(f'''评论成功{response.json().get("msg")}''');
    else :#line:365:else:
        print ("评论失败");#line:366:print("评论失败");
def getTaskList ():#line:367:def getTaskList():
    OOO0O0O0O0O0OOOOO ="https://hqapp.faw.cn/fawcshop/members/task/v2/getTaskList?taskType=integral";#line:368:url="https://hqapp.faw.cn/fawcshop/members/task/v2/getTaskList?taskType=integral";
    OO00000O00OOOO0OO =proxyget ();#line:369:proxies = proxyget();
    OOO0OOO000O00O0O0 =requests .get (OOO0O0O0O0O0OOOOO ,data ="",headers =getheaders (),proxies =OO00000O00OOOO0OO ,timeout =8 );#line:370:response = requests.get(url, data="", headers=getheaders(), proxies=proxies,timeout=8);
    return OOO0OOO000O00O0O0 .json ();#line:371:return response.json();
def getUserInfo ():#line:374:def getUserInfo():
    O000OOOO0OO0OO00O ="https://hqapp.faw.cn/fawcshop//mall/v1/apiCus/getUserInfo";#line:375:url = "https://hqapp.faw.cn/fawcshop//mall/v1/apiCus/getUserInfo";
    O00O0O000OOOOOOOO ={"userId":hqaid };#line:376:body = {"userId": hqaid};
    O00OO00000OOO0OO0 =json .dumps (O00O0O000OOOOOOOO )#line:377:stringJso = json.dumps(body)  # 对象转json
    OO0O0OOO000OOOOO0 =proxyget ();#line:378:proxies = proxyget();
    O0OOO0O0000O000O0 =requests .post (O000OOOO0OO0OO00O ,data =O00OO00000OOO0OO0 ,headers =getheaders (),proxies =OO0O0OOO000OOOOO0 ,timeout =8 );#line:379:response = requests.post(url, data=stringJso, headers=getheaders(), proxies=proxies, timeout=8);
    O0OO0O00OO0O0OO00 =O0OOO0O0000O000O0 .json ()["data"]["mobile"];#line:381:mobile = response.json()["data"]["mobile"];
    O0OOOOOO0OO0OO00O =O0OOO0O0000O000O0 .json ()["data"]["scoreCount"];#line:382:scoreCount = response.json()["data"]["scoreCount"];
    print (f"账号【{O0OO0O00OO0O0OO00}】积分余额为：{O0OOOOOO0OO0OO00O}\n");#line:383:print(f"账号【{mobile}】积分余额为：{scoreCount}\n");
    return O0OOOOOO0OO0OO00O ;#line:384:return scoreCount;
def getheaders ():#line:386:def getheaders():
    O000O0OOOOOOOOO00 ={"Content-Type":"application/json","Authorization":token ,"X-Forwarded-For":RemoteIp1 ,"platform":"2","aid":hqaid ,"timestamp":signInVo ["timestamp"],"nonce":signInVo ["nonce"],"signature":signInVo ["signature"],"o35xzbbp":"qjzsuioa","X-Feature":"sprint3-demo","Host":"hqapp.faw.cn","Connection":"Keep-Alive","Accept-Encoding":"gzip","User-Agent":"okhttp/3.11.0","remoteIp":RemoteIp1 ,"version":"4.7.2","anonymousId":"d57a9f22d73667b0","tenantId":"03001001","Accept-Language":"zh-CN,zh;q=0.9"};#line:407:};
    return O000O0OOOOOOOOO00 #line:408:return  headers2
selecttoken ()
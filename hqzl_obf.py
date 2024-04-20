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
dayalist =[];#line:16:dayalist = [];
executor =ThreadPoolExecutor (max_workers =32 )#line:18:executor = ThreadPoolExecutor(max_workers=32)  # ThreadPoolExecutor构造示例，max_workers参数表示最多工作的线程数
future_tasks =[]#line:19:future_tasks=[] #线程池异步提交结果
def selecttoken ():#line:21:def selecttoken():
    O0O000OOO000O00OO ="hqqc_token_go1"#line:22:tokenType="hqqc_token_go1"
    changeEevDate ();#line:25:changeEevDate();
    print (f"\n----------总共【{len(dayalist)}】条数据-----------\n")#line:28:print(f"\n----------总共【{len(dayalist)}】条数据-----------\n")
    for OOOOO0OOO00OO0O0O ,O00O0O000O0OO0O0O in enumerate (dayalist ):#line:29:for index, tokeinfo in enumerate(dayalist):
        if OOOOO0OOO00OO0O0O <0 :#line:30:if index < 0:
            continue ;#line:31:continue;
        global tokenPhone ;#line:32:global tokenPhone ;
        OO00000OOOO000OO0 =O00O0O000O0OO0O0O .split ("---")#line:33:dateinfo=tokeinfo.split("---")
        tokenPhone =OO00000OOOO000OO0 [0 ];#line:34:tokenPhone=dateinfo[0];
        print (f"开始第{OOOOO0OOO00OO0O0O}个，手机号{tokenPhone}");#line:35:print(f"开始第{index}个，手机号{tokenPhone}");
        print (f"当前时间:{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")#line:36:print(f"当前时间:{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        global token ;global hqaid ;global RemoteIp1 #line:37:global token;global hqaid;global RemoteIp1
        hqaid =OO00000OOOO000OO0 [1 ];#line:38:hqaid =dateinfo[1];
        token =OO00000OOOO000OO0 [2 ];#line:39:token = dateinfo[2];
        RemoteIp1 =getrandomip ();#line:40:RemoteIp1 = getrandomip();
        try :#line:41:try:
            time .sleep (5 )#line:42:time.sleep(5)
            dotaskAll (O0O000OOO000O00OO ,tokenPhone );#line:43:dotaskAll(tokenType,tokenPhone);
        except Exception as OOOOOO00O0OOOOO00 :#line:44:except Exception as e:
            print ("出现异常",OOOOOO00O0OOOOO00 )#line:45:print("出现异常", e)
        OOOOO0OOO00OO0O0O +=1 ;#line:46:index += 1;
    concurrent .futures .as_completed (future_tasks );#line:49:concurrent.futures.as_completed(future_tasks);
    print ("等待异步结果执行完毕");#line:50:print("等待异步结果执行完毕");
def getSN ():#line:54:def getSN():
    O0O0OOOOO0000000O =os .popen ("sudo dmidecode -s baseboard-serial-number | awk '{print $0}'").readlines ()#line:55:sn = os.popen("sudo dmidecode -s baseboard-serial-number | awk '{print $0}'").readlines()
    return O0O0OOOOO0000000O [0 ].strip ()#line:56:return sn[0].strip()
def changeEevDate ():#line:58:def changeEevDate():
    global dayalist ;#line:59:global dayalist;
    if hzlCookie is not None :#line:60:if hzlCookie is not None:
        if "@"in hzlCookie :#line:61:if "@" in hzlCookie:
            dayalist =hzlCookie .split ("@");#line:62:dayalist = hzlCookie.split("@");
        elif "\n"in hzlCookie :#line:63:elif  "\n" in hzlCookie:
            dayalist =hzlCookie .split ("\n");#line:64:dayalist = hzlCookie.split("\n");
        else :#line:65:else:
            dayalist .append (hzlCookie );#line:66:dayalist.append(hzlCookie);
    else :#line:67:else:
        print (f"\n提示：未填写环境变量hzlCookie")#line:68:print(f"\n提示：未填写环境变量hzlCookie")
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
        ''')#line:92:''')
def dotaskAll (OOO000O0O0O00O00O ,O0000OO00OO00000O ):#line:93:def dotaskAll(tokenType,tokenPhone):
    OO0O0O0OOO00OO0OO =getLevelAndHonorAcquireCountAndProportion ();#line:94:testRes=getLevelAndHonorAcquireCountAndProportion();
    if OO0O0O0OOO00OO0OO .get ("code")=="000000":#line:95:if testRes.get("code")=="000000":
        print ("token校验成功");#line:96:print("token校验成功");
        OOOOO0OOOOO0O00OO =random .randint (10 ,30 )#line:98:randomDely=random.randint(10,30)
        print (f'随机延时：{OOOOO0OOOOO0O00OO}秒！！！');#line:99:print(f'随机延时：{randomDely}秒！！！');
        time .sleep (OOOOO0OOOOO0O00OO )#line:100:time.sleep(randomDely)
        signin ();#line:101:signin();
        try :#line:103:try:
            O0O0OO00O00O000O0 =getTaskList ();#line:104:tasjinfo=getTaskList();
            if O0O0OO00O00O000O0 !=None :#line:108:if tasjinfo != None:
                OOO00OOOO0O0O00O0 =O0O0OO00O00O000O0 ["data"]["taskList"]#line:109:tasklist = tasjinfo["data"]["taskList"]
                for O00O00O00OOOOO000 in OOO00OOOO0O0O00O0 :#line:110:for i in tasklist:
                    global signInVo ;#line:111:global signInVo;
                    if "-APP_article"in O00O00O00OOOOO000 ['taskCode']and O00O00O00OOOOO000 ['completeFlag']==None :#line:113:if "-APP_article" in i['taskCode'] and i['completeFlag'] == None:
                        print ("开始发帖");#line:114:print("开始发帖");
                        pushArricle ();#line:115:pushArricle();
                    if "-APP_signed"in O00O00O00OOOOO000 ['taskCode']and O00O00O00OOOOO000 ['completeFlag']==None :#line:117:if "-APP_signed" in i['taskCode'] and i['completeFlag'] == None:
                        signInVo =signInlist [random .randint (0 ,len (signInlist )-1 )];#line:119:signInVo = signInlist[random.randint(0, len(signInlist) - 1)];
                        signin ();#line:120:signin();
                    if "-APP_share"in O00O00O00OOOOO000 ['taskCode']and O00O00O00OOOOO000 ['completeFlag']==None :#line:122:if "-APP_share" in i['taskCode'] and i['completeFlag'] == None:
                        time .sleep (5 )#line:123:time.sleep(5)
                        signInVo =signSharelist [random .randint (0 ,len (signSharelist )-1 )];#line:124:signInVo = signSharelist[random.randint(0, len(signSharelist) - 1)];
                        queryPostList ();#line:125:queryPostList();
                        collectLove ();#line:126:collectLove();  # 首次分享积分
                    if "-APP_isLike"in O00O00O00OOOOO000 ['taskCode']and O00O00O00OOOOO000 ['completeFlag']==None :#line:128:if "-APP_isLike" in i['taskCode'] and i['completeFlag'] == None:
                        time .sleep (5 )#line:129:time.sleep(5)
                        signInVo =signSharelist [random .randint (0 ,len (signSharelist )-1 )];#line:130:signInVo = signSharelist[random.randint(0, len(signSharelist) - 1)];
                        queryLikePostList ();#line:131:queryLikePostList();
                    if "-APP_isLike"in O00O00O00OOOOO000 ['taskCode']and O00O00O00OOOOO000 ['completeFlag']==None :#line:133:if "-APP_isLike" in i['taskCode'] and i['completeFlag'] == None:
                        time .sleep (5 )#line:134:time.sleep(5)
                        queryHotPostList ();#line:135:queryHotPostList();
            OO0O00O00O00OO00O =getUserInfo ();#line:140:score=getUserInfo();  # 获取用户信息积分
        except Exception as OO0O0O0000O00O00O :#line:142:except Exception as e:
            print ("出现异常",OO0O0O0000O00O00O )#line:143:print("出现异常", e)
    else :#line:144:else:
       print ("token无效")#line:145:print("token无效")
def getrandomip ():#line:147:def getrandomip():
    OOO0OOO00OO00O0OO =random .randint (0 ,255 );#line:148:m = random.randint(0, 255);
    O0OO0O0OO0OOO00OO =random .randint (0 ,255 );#line:149:n = random.randint(0, 255);
    O000OOOO000OO000O =random .randint (0 ,255 );#line:150:x = random.randint(0, 255);
    O0000O00OOO0O0OOO =random .randint (0 ,255 );#line:151:y = random.randint(0, 255);
    O000OOO00OOO000OO =str (OOO0OOO00OO00O0OO )+'.'+str (O0OO0O0OO0OOO00OO )+'.'+str (O000OOOO000OO000O )+'.'+str (O0000O00OOO0O0OOO );#line:152:randomIP = str(m) + '.' + str(n) + '.' + str(x) + '.' + str(y);
    return O000OOO00OOO000OO #line:153:return  randomIP
def signin ():#line:154:def signin():
    O0000O0OO000000OO ="https://hqapp.faw.cn/fawcshop/collect-public/v1/score/addScore";#line:155:url="https://hqapp.faw.cn/fawcshop/collect-public/v1/score/addScore";
    OOOO0O00O00OOOO0O ={"scoreType":"2"}#line:156:body = {"scoreType": "2"}
    O00OO0OOOOOO00OOO =json .dumps (OOOO0O00O00OOOO0O )#line:157:stringJso = json.dumps(body)  # 对象转json
    O00O00OO0000OO00O =proxyget ();#line:158:proxies = proxyget();
    OO00O000OO0O000O0 =requests .post (O0000O0OO000000OO ,data =O00OO0OOOOOO00OOO ,headers =getheaders (),proxies =O00O00OO0000OO00O ,timeout =8 );#line:159:response = requests.post(url, data=stringJso, headers=getheaders(), proxies=proxies,timeout=8);
    OO00O000OO0O000O0 .json ()#line:160:response.json()
    if OO00O000OO0O000O0 .json ().get ("code")=="000000":#line:161:if response.json().get("code") == "000000":
        print ("签到成功");#line:162:print("签到成功");
    else :#line:163:else:
        print ("签到失败",OO00O000OO0O000O0 .json ().get ("msg"),signInVo ["timestamp"]);#line:164:print("签到失败",response.json().get("msg"),signInVo["timestamp"]);
        time .sleep (5 );#line:165:time.sleep(5);
        signin_try ();#line:166:signin_try();
def signin_try ():#line:167:def signin_try():
    global signInVo ;#line:168:global signInVo;
    signInVo =signInlist [random .randint (0 ,len (signInlist )-1 )];#line:169:signInVo = signInlist[random.randint(0, len(signInlist) - 1)];
    OO00OO0O0OOO0000O ="https://hqapp.faw.cn/fawcshop/collect-public/v1/score/addScore";#line:170:url="https://hqapp.faw.cn/fawcshop/collect-public/v1/score/addScore";
    OO0000000000O0OO0 ={"scoreType":"2"}#line:171:body = {"scoreType": "2"}
    O0OOOO00OOO0O0O00 =json .dumps (OO0000000000O0OO0 )#line:172:stringJso = json.dumps(body)  # 对象转json
    O0000O0O000OO00OO =proxyget ();#line:173:proxies = proxyget();
    OO00OOOOO00OO0O0O =requests .post (OO00OO0O0OOO0000O ,data =O0OOOO00OOO0O0O00 ,headers =getheaders (),proxies =O0000O0O000OO00OO ,timeout =8 );#line:175:response = requests.post(url, data=stringJso, headers=getheaders(), proxies=proxies,timeout=8);
    OO00OOOOO00OO0O0O .json ()#line:176:response.json()
    if OO00OOOOO00OO0O0O .json ().get ("code")=="000000":#line:177:if response.json().get("code") == "000000":
        print ("重试签到成功");#line:178:print("重试签到成功");
    else :#line:179:else:
        print ("重试签到失败",OO00OOOOO00OO0O0O .json ().get ("msg"),signInVo ["timestamp"]);#line:180:print("重试签到失败",response.json().get("msg"),signInVo["timestamp"]);
def pushArricle ():#line:182:def pushArricle():
    OOO0OOO0OO0O0O0O0 =saveDynamicInfoImgUrl ();#line:183:isSuccess=saveDynamicInfoImgUrl();
    if OOO0OOO0OO0O0O0O0 ==False :#line:184:if isSuccess==False:
        time .sleep (5 );#line:185:time.sleep(5);
        OOO0OOO0OO0O0O0O0 =saveDynamicInfoImgUrl ();#line:186:isSuccess = saveDynamicInfoImgUrl();
        if OOO0OOO0OO0O0O0O0 ==False :#line:187:if isSuccess == False:
            time .sleep (5 );#line:188:time.sleep(5);
            saveDynamicInfoImgUrl ();#line:189:saveDynamicInfoImgUrl();
def saveDynamicInfoImgUrl ():#line:190:def saveDynamicInfoImgUrl():
    O0O0OO0OO0OOOOOO0 ="https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/saveDynamicInfoImgUrl";#line:191:url="https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/saveDynamicInfoImgUrl";
    O00O000O000O0O00O =getheader_article (token ,hqaid );#line:192:randomDate=getheader_article(token, hqaid);
    O00O0O0O00OO0O00O =O00O000O000O0O00O ["resDate"]#line:193:body =randomDate["resDate"]
    O000O0OO00O0OOOOO =json .dumps (O00O0O0O00OO0O00O )#line:194:stringJso = json.dumps(body)  # 对象转json
    O0000O0O0000OOOOO =proxyget ();#line:195:proxies = proxyget();
    O00O000O000O0O00O ["headers"]["Accept-Language"]="zh-CN,zh;q=0.9"#line:197:randomDate["headers"]["Accept-Language"]="zh-CN,zh;q=0.9"
    O00OO00OO000OOO0O =requests .post (O0O0OO0OO0OOOOOO0 ,data =O000O0OO00O0OOOOO ,headers =O00O000O000O0O00O ["headers"],proxies =O0000O0O0000OOOOO ,timeout =8 );#line:200:response = requests.post(url, data=stringJso, headers=randomDate["headers"], proxies=proxies,timeout=8);
    O00OO00OO000OOO0O .json ()#line:201:response.json()
    if O00OO00OO000OOO0O .json ().get ("code")=="000000":#line:202:if response.json().get("code") == "000000":
        print ("发文成功");#line:203:print("发文成功");
        getMyDynamicList (tokenPhone );#line:204:getMyDynamicList(tokenPhone);
        return True ;#line:207:return True;
    else :#line:208:else:
        print ("发文失败",O00OO00OO000OOO0O .json ().get ("msg"));#line:209:print("发文失败",response.json().get("msg"));
        return False ;#line:210:return False;
def getDynamicList ():#line:211:def getDynamicList():
    OOO0OOOOOO0OO00O0 ="2024-02-26 12:12:12";#line:212:nowdate="2024-02-26 12:12:12";
    OOO000OOOO00OO0O0 ='https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/getDynamicList?pageNo=1&refreshTime='+OOO0OOOOOO0OO00O0 +'&likeFlag=0&orderByRule=RULE19&pageSize=100';#line:213:url = 'https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/getDynamicList?pageNo=1&refreshTime=' + nowdate + '&likeFlag=0&orderByRule=RULE19&pageSize=100';
    OO00OO0O0O00OO0OO =proxyget ();#line:214:proxies = proxyget();
    O0OO00O0O00O0OO00 =requests .get (OOO000OOOO00OO0O0 ,data ="",headers =getheaders (),proxies =OO00OO0O0O00OO0OO ,timeout =8 );#line:215:response = requests.get(url, data="", headers=getheaders(), proxies=proxies,timeout=8);
    O0OO00O0O00O0OO00 .json ()#line:216:response.json()
    if O0OO00O0O00O0OO00 .json ().get ("code")=="000000":#line:217:if response.json().get("code") == "000000":
        print ("发文成功");#line:218:print("发文成功");
    else :#line:219:else:
        print ("发文失败",O0OO00O0O00O0OO00 .json ().get ("msg"),signInVo ["timestamp"]);#line:220:print("发文失败",response.json().get("msg"),signInVo["timestamp"]);
def getMyDynamicList (OOOO0O0OO00OO00O0 ):#line:222:def getMyDynamicList(tokenPhone):
    time .sleep (5 );#line:223:time.sleep(5);
    O000O0O0O00OOO0O0 =datetime .datetime .now ()#line:224:now = datetime.datetime.now()
    O0000O0OOOO00O000 =O000O0O0O00OOO0O0 .strftime ("%Y-%m-%d %H:%M:%S")#line:226:formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    OO0OO0OOOO000OO00 =f'https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/getDynamicList?visitedAid={hqaid}&pageNo=1&refreshTime={O0000O0OOOO00O000}&likeFlag=1&pageSize=10';#line:227:url = f'https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/getDynamicList?visitedAid={hqaid}&pageNo=1&refreshTime={formatted_time}&likeFlag=1&pageSize=10';
    O0O0000OO0O000000 =proxyget ();#line:228:proxies = proxyget();
    O0OOO0OOO0O000O0O =getheaders ();#line:229:headerAsync=getheaders();
    O00O000OOOOO0OOOO =requests .get (OO0OO0OOOO000OO00 ,data ="",headers =O0OOO0OOO0O000O0O ,proxies =O0O0000OO0O000000 ,timeout =8 );#line:230:response = requests.get(url, data="", headers=headerAsync, proxies=proxies,timeout=8);
    O00O000OOOOO0OOOO .json ()#line:231:response.json()
    if O00O000OOOOO0OOOO .json ().get ("code")=="000000":#line:232:if response.json().get("code") == "000000":
        OOOO0O0O00000OO00 =O00O000OOOOO0OOOO .json ().get ("data");#line:233:datalist=response.json().get("data");
        if len (OOOO0O0O00000OO00 )>0 :#line:234:if len(datalist)>0:
            O00OOO0O0OOO0000O =random .randint (60 ,120 )#line:236:randomDely = random.randint(60, 120)
            time .sleep (O00OOO0O0OOO0000O )#line:237:time.sleep(randomDely)
            OOO0O0O00O0000O0O =deleteInvitationById (OOOO0O0O00000OO00 [0 ],O0OOO0OOO0O000O0O ,OOOO0O0OO00OO00O0 );#line:239:isdeleteSuccess=deleteInvitationById(datalist[0],headerAsync,tokenPhone);
            if not OOO0O0O00O0000O0O :#line:240:if not isdeleteSuccess:
                deleteInvitationById (OOOO0O0O00000OO00 [0 ],O0OOO0OOO0O000O0O ,OOOO0O0OO00OO00O0 );#line:241:deleteInvitationById(datalist[0], headerAsync, tokenPhone);
    else :#line:243:else:
        print ("获取文章失败",O00O000OOOOO0OOOO .json ().get ("msg"));#line:244:print("获取文章失败", response.json().get("msg"));
def deleteInvitationById (OO0O00OOOOOOO0O00 ,OOOO0OOO00OOOOOOO ,OO0O0O0O0O0O0000O ):#line:247:def deleteInvitationById(dataArc,headerAsync,tokenPhone):
    O0OOOOOOOOO000O0O =OO0O00OOOOOOO0O00 .get ("id");#line:248:pid=dataArc.get("id");
    OOO0OO00O0O0OO00O =OO0O00OOOOOOO0O00 .get ("createTime");#line:249:createTime = dataArc.get("createTime");
    if OOO0OO00O0O0OO00O <(datetime .datetime .now ()-datetime .timedelta (days =10 )).strftime ("%Y-%m-%d %H:%M:%S"):#line:250:if createTime<(datetime.datetime.now()-datetime.timedelta(days=10)).strftime("%Y-%m-%d %H:%M:%S"):
        print (f"{OOO0OO00O0O0OO00O}时间过早暂不删除");#line:251:print(f"{createTime}时间过早暂不删除");
        return True ;#line:252:return True;
    OOO0O0OOOOO0000OO =f'https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/deleteInvitationById';#line:253:url = f'https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/deleteInvitationById';
    OO0O0OOOO00OOO0O0 ={"id":O0OOOOOOOOO000O0O ,"busType":1 };#line:254:body={"id":pid,"busType":1};
    OOO00OO0OOOO0O0O0 =proxyget ();#line:255:proxies = proxyget();
    O0O00OO0OO00OO0O0 =json .dumps (OO0O0OOOO00OOO0O0 )#line:256:stringJso = json.dumps(body)  # 对象转json
    OOO000O000000000O =requests .post (OOO0O0OOOOO0000OO ,data =O0O00OO0OO00OO0O0 ,headers =OOOO0OOO00OOOOOOO ,proxies =OOO00OO0OOOO0O0O0 ,timeout =8 );#line:257:response = requests.post(url, data=stringJso, headers=headerAsync, proxies=proxies, timeout=8);
    OOO000O000000000O .json ()#line:258:response.json()
    if OOO000O000000000O .json ().get ("code")=="000000":#line:259:if response.json().get("code") == "000000":
        print (f"手机号{OO0O0O0O0O0O0000O}-删除成功");#line:260:print(f"手机号{tokenPhone}-删除成功");
        return True ;#line:261:return True;
    else :#line:262:else:
        print (f"删除失败,创建时间{OOO0OO00O0O0OO00O}");#line:263:print(f"删除失败,创建时间{createTime}");
        return False ;#line:264:return False;
def queryPostList ():#line:266:def queryPostList():
    O0OO00O0O0O00O00O ='https://hqapp.faw.cn/fawcshop/cms/api/front/content/queryPostList?city\u003d%E5%8C%97%E4%BA%AC%E5%B8%82\u0026stats\u003d2\u0026pageNo\u003d1\u0026pageSize\u003d100';#line:267:url = 'https://hqapp.faw.cn/fawcshop/cms/api/front/content/queryPostList?city\u003d%E5%8C%97%E4%BA%AC%E5%B8%82\u0026stats\u003d2\u0026pageNo\u003d1\u0026pageSize\u003d100';
    OO00O0OO0O0OO0OOO =proxyget ();#line:268:proxies = proxyget();
    OO0OOO0O00O0O00O0 =requests .get (O0OO00O0O0O00O00O ,data ="",headers =getheaders (),proxies =OO00O0OO0O0OO0OOO ,timeout =8 );#line:269:response = requests.get(url, data="", headers=getheaders(), proxies=proxies,timeout=8);
    OO0OOO0O00O0O00O0 .json ()#line:270:response.json()
    if OO0OOO0O00O0O00O0 .json ().get ("code")=="000000":#line:271:if response.json().get("code") == "000000":
        OO0O00OOOOOOOO00O =OO0OOO0O00O0O00O0 .json ()["data"];#line:272:resultlist=response.json()["data"];
        OO00OOOO00OO00OOO =OO0O00OOOOOOOO00O [random .randint (0 ,len (OO0O00OOOOOOOO00O )-1 )]["contentId"];#line:273:contentId = resultlist[random.randint(0, len(resultlist) - 1)]["contentId"];
        shareAc (OO00OOOO00OO00OOO );#line:274:shareAc(contentId);
    else :#line:276:else:
        print ("签到失败",OO0OOO0O00O0O00O0 .json ().get ("msg"));#line:277:print("签到失败",response.json().get("msg"));
def queryHotPostList ():#line:279:def queryHotPostList():
    O000O00O000O0O000 ="1";#line:280:pageNo="1";
    O0OOO0OO0O0O00O00 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S');#line:281:nowdate=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S');
    OO0O0000O000O0000 ='https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/getDynamicList?pageNo='+O000O00O000O0O000 +'&refreshTime='+O0OOO0OO0O0O00O00 +'&likeFlag=0&orderByRule=RULE15&pageSize=10';#line:282:url = 'https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/getDynamicList?pageNo='+pageNo+'&refreshTime=' + nowdate + '&likeFlag=0&orderByRule=RULE15&pageSize=10';
    O0OOO0O000O0OOOO0 =proxyget ();#line:283:proxies = proxyget();
    OOOO00OOO0O00000O =requests .get (OO0O0000O000O0000 ,data ="",headers =getheaders (),proxies =O0OOO0O000O0OOOO0 ,timeout =8 );#line:284:response = requests.get(url, data="", headers=getheaders(), proxies=proxies,timeout=8);
    OOOO00OOO0O00000O .json ()#line:285:response.json()
    if OOOO00OOO0O00000O .json ().get ("code")=="000000":#line:286:if response.json().get("code") == "000000":
        OOOO000OOO00000O0 =OOOO00OOO0O00000O .json ()["data"];#line:287:resultlist=response.json()["data"];
        O00OO0O0OO00OOO0O =OOOO000OOO00000O0 [random .randint (0 ,len (OOOO000OOO00000O0 )-1 )]["id"];#line:288:contentId = resultlist[random.randint(0, len(resultlist) - 1)]["id"];
        saveCommentDetailsRevision (O00OO0O0OO00OOO0O );#line:289:saveCommentDetailsRevision(contentId);
    else :#line:291:else:
        print ("签到失败",OOOO00OOO0O00000O .json ().get ("msg"));#line:292:print("签到失败",response.json().get("msg"));
def queryLikePostList ():#line:293:def queryLikePostList():
    OO0O0O000000OO0OO ='https://hqapp.faw.cn/fawcshop/cms/api/front/content/queryPostList?city\u003d%E5%8C%97%E4%BA%AC%E5%B8%82\u0026stats\u003d2\u0026pageNo\u003d1\u0026pageSize\u003d100';#line:294:url = 'https://hqapp.faw.cn/fawcshop/cms/api/front/content/queryPostList?city\u003d%E5%8C%97%E4%BA%AC%E5%B8%82\u0026stats\u003d2\u0026pageNo\u003d1\u0026pageSize\u003d100';
    OOO0OOOO0O0O0O00O =proxyget ();#line:295:proxies = proxyget();
    O000OO00OO0000O00 =requests .get (OO0O0O000000OO0OO ,data ="",headers =getheaders (),proxies =OOO0OOOO0O0O0O00O ,timeout =8 );#line:296:response = requests.get(url, data="", headers=getheaders(), proxies=proxies,timeout=8);
    O000OO00OO0000O00 .json ()#line:297:response.json()
    if O000OO00OO0000O00 .json ().get ("code")=="000000":#line:298:if response.json().get("code") == "000000":
        OO000OO0000OO0O00 =O000OO00OO0000O00 .json ()["data"];#line:299:resultlist=response.json()["data"];
        OO0OOOO0O00OOOO0O =OO000OO0000OO0O00 [random .randint (0 ,len (OO000OO0000OO0O00 )-1 )]["contentId"];#line:300:contentId = resultlist[random.randint(0, len(resultlist) - 1)]["contentId"];
        getILikeThis (OO0OOOO0O00OOOO0O );#line:301:getILikeThis(contentId);
    else :#line:302:else:
        print ("点赞失败",O000OO00OO0000O00 .json ().get ("msg"));#line:303:print("点赞失败",response.json().get("msg"));
def shareAc (OO00O0OO000OO00O0 ):#line:304:def shareAc(contentId):
    O00O00OOOO00000OO ="https://hqapp.faw.cn/fawcshop/collect-public/v1/score/addScore";#line:305:url="https://hqapp.faw.cn/fawcshop/collect-public/v1/score/addScore";
    OOO0OOO00OOO0O00O ={'scoreType':'4'}#line:306:body = {'scoreType': '4'}
    OO0000O00O0OOOO00 =json .dumps (OOO0OOO00OOO0O00O )#line:307:stringJso = json.dumps(body)# 对象转json
    O0O00OOOOOO0O0OOO =proxyget ();#line:308:proxies = proxyget();
    global signInVo ;#line:309:global signInVo;
    signInVo =signSharelist [random .randint (0 ,len (signSharelist )-1 )];#line:310:signInVo = signSharelist[random.randint(0, len(signSharelist) - 1)];
    O000000O00O00000O =requests .post (O00O00OOOO00000OO ,data =OO0000O00O0OOOO00 ,headers =getheaders (),proxies =O0O00OOOOOO0O0OOO ,timeout =8 );#line:311:response = requests.post(url, data=stringJso, headers=getheaders(), proxies=proxies,timeout=8);
    O000000O00O00000O .json ()#line:312:response.json()
    if O000000O00O00000O .json ().get ("code")=="000000":#line:313:if response.json().get("code") == "000000":
        if O000000O00O00000O .json ()["data"]["score"]!=None :#line:314:if response.json()["data"]["score"] != None:
            print ("分享成功，获得：%s积分"%O000000O00O00000O .json ()["data"]["score"]);#line:315:print("分享成功，获得：%s积分"%response.json()["data"]["score"]);
        else :#line:316:else:
            print ("分享成功，但每周上限一次，故未获得积分");#line:317:print("分享成功，但每周上限一次，故未获得积分");
    else :#line:318:else:
        print ("分享失败",O000000O00O00000O .json ().get ("msg"));#line:319:print("分享失败",response.json().get("msg"));
def getLevelAndHonorAcquireCountAndProportion ():#line:320:def getLevelAndHonorAcquireCountAndProportion():
    OOO0OOO00OO0OOOOO ="https://hqapp.faw.cn/fawcshop/members/personal/getLevelAndHonorAcquireCountAndProportion";#line:321:url="https://hqapp.faw.cn/fawcshop/members/personal/getLevelAndHonorAcquireCountAndProportion";
    O00OO0O0OO0O0OO00 =proxyget ();#line:322:proxies = proxyget();
    OO0OO0O000OOO0000 =requests .post (OOO0OOO00OO0OOOOO ,data ="",headers =getheaders (),proxies =O00OO0O0OO0O0OO00 ,timeout =8 );#line:323:response = requests.post(url, data="", headers=getheaders(), proxies=proxies,timeout=8);
    return OO0OO0O000OOO0000 .json ();#line:324:return response.json();
def collectLove ():#line:325:def collectLove():
    OO0O0O0O000O0OO0O ="https://hqapp.faw.cn/fawcshop/members/currency/account/collectLove";#line:326:url="https://hqapp.faw.cn/fawcshop/members/currency/account/collectLove";
    OO0OOOO0OOOOOO00O =proxyget ();#line:327:proxies = proxyget();
    OOO00OO0OO0O0000O =requests .get (OO0O0O0O000O0OO0O ,data ="",headers =getheaders (),proxies =OO0OOOO0OOOOOO00O ,timeout =8 );#line:328:response = requests.get(url, data="", headers=getheaders(), proxies=proxies,timeout=8);
    return OOO00OO0OO0O0000O .json ();#line:329:return response.json();
def getILikeThis (O000000O00O00OO00 ):#line:330:def getILikeThis(id):
    OO0O0000O0O00OO0O ='https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/getILikeThis?invId='+str (O000000O00O00OO00 );#line:331:url= 'https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/getILikeThis?invId=' + str(id);
    OOO0000OOOOO0O000 =proxyget ();#line:332:proxies = proxyget();
    O0OO00O00OO0O00O0 =requests .get (OO0O0000O0O00OO0O ,data ="",headers =getheaders (),proxies =OOO0000OOOOO0O000 ,timeout =8 );#line:333:response = requests.get(url, data="", headers=getheaders(), proxies=proxies,timeout=8);
    return O0OO00O00OO0O00O0 .json ();#line:334:return response.json();
    if O0OO00O00OO0O00O0 .json ().get ("code")=="000000":#line:335:if response.json().get("code") == "000000":
        print (O0OO00O00OO0O00O0 .json ().get ("msg"));#line:336:print(response.json().get("msg"));
    else :#line:337:else:
      print ("点赞失败");#line:338:print("点赞失败");
def commentList (OOOOO00OOO000000O ):#line:340:def commentList(contentId):
    O0OOOO00OO00OO000 ='https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/getCommentDetailsInfoListNew?commentType=8500&contentId='+str (OOOOO00OOO000000O )+'&pageNo=1&pageSize=100&commentDetailsId=&orderByRule=RULE10';#line:341:url = 'https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/getCommentDetailsInfoListNew?commentType=8500&contentId=' + str(contentId) + '&pageNo=1&pageSize=100&commentDetailsId=&orderByRule=RULE10';
    O0OO0OOOOO0OO0O0O =proxyget ();#line:342:proxies = proxyget();
    O0O00O0O00O0OOOOO =requests .get (O0OOOO00OO00OO000 ,data ="",headers =getheaders (),proxies =O0OO0OOOOO0OO0O0O ,timeout =8 );#line:343:response = requests.get(url, data="", headers=getheaders(), proxies=proxies,timeout=8);
    if O0O00O0O00O0OOOOO .json ().get ("code")=="000000":#line:344:if response.json().get("code") == "000000":
        print (O0O00O0O00O0OOOOO .json ().get ("msg"));#line:345:print(response.json().get("msg"));
        O00OOO00000000O00 =O0O00O0O00O0OOOOO .json ().get ("data").get ("result");#line:346:commontlistres=response.json().get("data").get("result");
        if (len (O00OOO00000000O00 )>0 ):#line:347:if(len(commontlistres) >0):
            OOOOO00OOO000000O =O00OOO00000000O00 [random .randint (0 ,len (O00OOO00000000O00 )-1 )]["contentId"];#line:348:contentId = commontlistres[random.randint(0, len(commontlistres) - 1)]["contentId"];
            saveCommentDetailsRevision (OOOOO00OOO000000O );#line:349:saveCommentDetailsRevision(contentId);
    else :#line:350:else:
      print ("点赞失败");#line:351:print("点赞失败");
def saveCommentDetailsRevision (O0OO00OOO0OO000OO ):#line:354:def saveCommentDetailsRevision(contentId):
    global signInVo ;#line:355:global signInVo;
    signInVo =commontList [random .randint (0 ,len (commontList )-1 )];#line:356:signInVo = commontList[random.randint(0, len(commontList) - 1)];
    OOOOO0000OOOO0O00 ="https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/saveCommentDetailsRevision";#line:357:url="https://hqapp.faw.cn/fawcshop/collect-sns/v1/dynamicTopic/saveCommentDetailsRevision";
    O0OO0OOO0O0OO0O00 ={"commentContext":signInVo .get ('commentContext'),"commentType":"8500","contentId":O0OO00OOO0OO000OO ,"parentId":"0","fileString":[]}#line:358:body = {"commentContext":signInVo.get('commentContext'),"commentType":"8500","contentId":contentId,"parentId":"0","fileString":[]}
    O0OO0OOO0O0OO0O00 =signInVo .get ('commentContext')#line:359:body=signInVo.get('commentContext')
    OO0000OO0OOO00000 =json .dumps (O0OO0OOO0O0OO0O00 )#line:361:stringJso = json.dumps(body)  # 对象转json
    OO0OO0O0O0O000OO0 ={"Content-Type":"application/json",}#line:362:headers = {"Content-Type": "application/json", }
    OO0OO00OOO0O0O0O0 =requests .post (OOOOO0000OOOO0O00 ,data =OO0000OO0OOO00000 ,headers =getheaders ());#line:363:response = requests.post(url, data=stringJso, headers=getheaders());
    if OO0OO00OOO0O0O0O0 .json ().get ("code")=="000000":#line:364:if response.json().get("code") == "000000":
        print (f'''评论成功{OO0OO00OOO0O0O0O0.json().get("msg")}''');#line:365:print(f'''评论成功{response.json().get("msg")}''');
    else :#line:366:else:
        print ("评论失败");#line:367:print("评论失败");
def getTaskList ():#line:368:def getTaskList():
    OOOOO00O00OOO0O00 ="https://hqapp.faw.cn/fawcshop/members/task/v2/getTaskList?taskType=integral";#line:369:url="https://hqapp.faw.cn/fawcshop/members/task/v2/getTaskList?taskType=integral";
    O0OO000OO00O00OOO =proxyget ();#line:370:proxies = proxyget();
    O00000OO0OO0OOOO0 =requests .get (OOOOO00O00OOO0O00 ,data ="",headers =getheaders (),proxies =O0OO000OO00O00OOO ,timeout =8 );#line:371:response = requests.get(url, data="", headers=getheaders(), proxies=proxies,timeout=8);
    return O00000OO0OO0OOOO0 .json ();#line:372:return response.json();
def getUserInfo ():#line:375:def getUserInfo():
    OOO0O0OOOOOOO0000 ="https://hqapp.faw.cn/fawcshop//mall/v1/apiCus/getUserInfo";#line:376:url = "https://hqapp.faw.cn/fawcshop//mall/v1/apiCus/getUserInfo";
    OOO000OOO000O0O00 ={"userId":hqaid };#line:377:body = {"userId": hqaid};
    O00O0OO0O00000OO0 =json .dumps (OOO000OOO000O0O00 )#line:378:stringJso = json.dumps(body)  # 对象转json
    O0OOO00OO0O0O0000 =proxyget ();#line:379:proxies = proxyget();
    O0OO00000OO0O0OO0 =requests .post (OOO0O0OOOOOOO0000 ,data =O00O0OO0O00000OO0 ,headers =getheaders (),proxies =O0OOO00OO0O0O0000 ,timeout =8 );#line:380:response = requests.post(url, data=stringJso, headers=getheaders(), proxies=proxies, timeout=8);
    OO000OO0O000OOO0O =O0OO00000OO0O0OO0 .json ()["data"]["mobile"];#line:382:mobile = response.json()["data"]["mobile"];
    OO00O0OO0O0OO00O0 =O0OO00000OO0O0OO0 .json ()["data"]["scoreCount"];#line:383:scoreCount = response.json()["data"]["scoreCount"];
    print (f"账号【{OO000OO0O000OOO0O}】积分余额为：{OO00O0OO0O0OO00O0}\n");#line:384:print(f"账号【{mobile}】积分余额为：{scoreCount}\n");
    return OO00O0OO0O0OO00O0 ;#line:385:return scoreCount;
def getheaders ():#line:387:def getheaders():
    OO00O0O00000O0O0O ={"Content-Type":"application/json","Authorization":token ,"X-Forwarded-For":RemoteIp1 ,"platform":"2","aid":hqaid ,"timestamp":signInVo ["timestamp"],"nonce":signInVo ["nonce"],"signature":signInVo ["signature"],"o35xzbbp":"qjzsuioa","X-Feature":"sprint3-demo","Host":"hqapp.faw.cn","Connection":"Keep-Alive","Accept-Encoding":"gzip","User-Agent":"okhttp/3.11.0","remoteIp":RemoteIp1 ,"version":"4.7.2","anonymousId":"d57a9f22d73667b0","tenantId":"03001001","Accept-Language":"zh-CN,zh;q=0.9"};#line:408:};
    return OO00O0O00000O0O0O #line:409:return  headers2
selecttoken ()
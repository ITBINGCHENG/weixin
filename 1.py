from wxpy import *
import re

bot = Bot(console_qr=True,cache_path=True )#

#mps = bot.mps().search(u'支付')[0]#search()返回聊天对象合集
@bot.register()
def print_message(msg):
    print(msg.text)
    if str(msg.sender) == '<MP: 微信支付>':
        dic = msg.raw['Content']
        #print("\ndic-------------"+dic+'\n-----------------')
        matchObj = re.findall(r'收款金额[\s\S]+?零钱',dic,re.M)[0]
        if matchObj:
            #print(matchObj)
            bz = re.findall(r'付款方[\S]+', matchObj)[0]
            bz = re.sub(r'付款方备注：', '', bz)
            toll = re.findall(r'今日[\S]+',matchObj)[0]
            print('收款金额：'+re.findall(r'￥[\S]+',matchObj)[0])
            print('备注：'+bz)
            print(toll)
            msg.reply(u'1')

        else:
            pass

    print(msg.sender)
# 进入Python命令行，让程序保持运行
embed()

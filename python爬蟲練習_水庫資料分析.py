import re
import requests
import time
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
import numpy as np
url= "https://fhy.wra.gov.tw/ReservoirPage_2011/StorageCapacity.aspx"
html = requests.get(url).text
soup = BeautifulSoup(html,'html.parser')
td_tags = soup.select('tr td')

#代號一覽
##北部：
#1石門水庫
#2翡翠水庫
#3寶山第二水庫
#4永和山水庫
#5明德水庫 
#6鯉魚潭水庫

##中部： 
#7德基水庫 
#8石岡壩
#9霧社水庫
#10日月潭水庫
#11集集攔河堰

##南部
#12湖山水庫
#13仁義潭水庫
#14白河水庫 
#15烏山頭水庫
#16曾文水庫
#17南化水庫
#18阿公店水庫
#19高屏溪攔河堰
#20牡丹水庫    





#水位=high(代號)
def high(a):
    if td_tags[(a-1)*11+8].string == '--':  #當資料尚未更新時
        return 0  #以0顯示
    else:
        if ',' in td_tags[(a-1)*11+8].string: #當資料含有','
            o9=td_tags[(a-1)*11+8].string.strip(',') #去除掉','
            return float(re.sub('[,]', '', o9)) #需要import re
        else:
            return float(td_tags[(a-1)*11+8].string) #直接轉換


#有效蓄水量Storage(代號)
def Storage(a):
    if td_tags[(a-1)*11+9].string == '--':
        return 0
    else:
        if ',' in td_tags[(a-1)*11+9].string:
            o=td_tags[(a-1)*11+9].string.strip(',')
            return float(re.sub('[,]', '', o))
        else:
            return float(td_tags[(a-1)*11+9].string)
        

#蓄水量 Stper(代號)
def Stper(a):
    if td_tags[(a-1)*11+10].string == '--':
        return 0
    else:
        return float(td_tags[(a-1)*11+10].string.strip('%'))


k=input("1:查詢水庫與三大水庫比較圖，2:查詢全台水庫蓄水量，3:蓄水量排行榜，4:結束程式：選擇號碼至指定查詢")
while k !='5':
    while k =="1":
        print("")
        print("以下為各水庫代號：")
        print("")
        time.sleep(3)
        for i in range(20):
            g=i*11
            print(td_tags[g].string,"："+str(i+1))
        print("")
        b=input("輸入代號找尋昨日水庫資料：") 
        a=int(b)
        print("水庫名稱："+td_tags[(a-1)*11].string)
        print("水情時間："+td_tags[(a-1)*11+7].string)
        print("水位："+td_tags[(a-1)*11+8].string+"公尺")
        print("有效蓄水量："+td_tags[(a-1)*11+9].string+"萬立方公尺")
        print("蓄水量："+td_tags[(a-1)*11+10].string)
        print("備註：若有呈現--的代號，為網站尚未更新當筆資料，圖表以'0'表示")

        print("")
        time.sleep(3)
        print("接下來會有你搜尋的水庫與台灣北中南三大水庫的比較圖")
        time.sleep(3)
        #柱狀圖
        #顏色https://www.toodoo.com/db/color.html
        #水位柱狀圖
        reservoir1 = ['翡翠水庫', '日月潭水庫', '曾文水庫', td_tags[(a-1)*11].string]
        height1 = [high(2), high(10),high(16),high(a)]
        happy1 = np.arange(len(reservoir1))
        plt.bar(happy1, height1, color=['lightblue', 'plum', 'lightpink', 'lightskyblue'])
        plt.xticks(happy1, reservoir1)
        plt.xlabel('水庫名')
        plt.ylabel('公尺')
        plt.title('水位比較')
        plt.show()

        time.sleep(3)
        print('有效水資源=水庫有效總容量÷水庫數量，及平均一座水庫的有效蓄水量')
        print('效容量定義=水庫取水口可取到的總水量，通常小於總容量')
        #有效蓄水量柱狀圖
        reservoir2 = ['翡翠水庫', '日月潭水庫', '曾文水庫', td_tags[(a-1)*11].string]
        height2 = [Storage(2), Storage(10),Storage(16),Storage(a)]
        happy2 = np.arange(len(reservoir2))
        plt.bar(happy2, height2, color=['lightblue', 'plum', 'lightpink', 'lightskyblue'])
        plt.xticks(happy2, reservoir2)
        plt.xlabel('水庫名')
        plt.ylabel('萬立方公尺')
        plt.title('有效蓄水量比較')
        plt.show()

        time.sleep(3)
        #蓄水量柱狀圖
        reservoir3 = ['翡翠水庫', '日月潭水庫', '曾文水庫', td_tags[(a-1)*11].string]
        height3 = [Stper(2), Stper(10),Stper(16),Stper(a)]
        happy3 = np.arange(len(reservoir3))
        plt.bar(happy3, height3, color=['lightblue', 'plum', 'lightpink', 'lightskyblue'])
        plt.xticks(happy3, reservoir3)
        plt.xlabel('水庫名')
        plt.ylabel('%')
        plt.title('蓄水量百分比')
        plt.show()
        time.sleep(3)
        k=input("1:查詢水庫與三大水庫比較圖，2:查詢全台水庫蓄水量，3:蓄水量排行榜，4:結束程式：選擇號碼至指定查詢")

    while k == "2":
        print("")
        print('有效水資源=水庫有效總容量÷水庫數量，及平均一座水庫的有效蓄水量')
        print('效容量定義=水庫取水口可取到的總水量，通常小於總容量')    
        reservoir1 = ['石門水庫', '翡翠水庫', '曾文水庫', '寶山第二水庫','永和山水庫','鯉魚潭水庫']
        height1 = [Stper(1), Stper(2),Stper(3),Stper(4),Stper(5),Stper(6)]
        happy1 = np.arange(len(reservoir1))
        plt.bar(happy1, height1, color=['#20B2AA', '#66CDAA', '#3CB371', '#8FBC8F','#9ACD32','#32CD32'])
        plt.xticks(happy1, reservoir1)
        plt.xlabel('水庫名')
        plt.ylabel('%')
        plt.title('北部蓄水量百分比比較')
        plt.show()
        print("備註1：若網站資料未更新，數據以'0'呈現")

        time.sleep(3)
        reservoir1 = ['德基水庫', '石岡壩','霧社水庫', '日月潭水庫','集集攔河堰']
        height1 = [Stper(7), Stper(8),Stper(9),Stper(10),Stper(11)]
        happy1 = np.arange(len(reservoir1))
        plt.bar(happy1, height1, color=['lightsteelblue', 'lightblue', 'steelblue', 'darkcyan','cadetblue'])
        plt.xticks(happy1, reservoir1)
        plt.xlabel('水庫名')
        plt.ylabel('%')
        plt.title('中部蓄水量百分比比較')
        plt.show()
        print("備註1：若網站資料未更新，數據以'0'呈現")

        time.sleep(3)
        reservoir1 = ['湖山水庫', '烏山頭水庫','曾文水庫','南化水庫','阿公店水庫','牡丹水庫']
        height1 = [Stper(12),Stper(15),Stper(16),Stper(17),Stper(18),Stper(20)]
        happy1 = np.arange(len(reservoir1))
        plt.bar(happy1, height1, color=['darkviolet','slateblue','mediumpurple','mediumslateblue','mediumorchid','violet'])
        plt.xticks(happy1, reservoir1)
        plt.xlabel('水庫名')
        plt.ylabel('%')
        plt.title('南部蓄水量百分比比較')
        plt.show()
        print("備註1：若網站資料未更新，數據以'0'呈現")
        time.sleep(3)
        k=input("1:查詢水庫與三大水庫比較圖，2:查詢全台水庫蓄水量，3:蓄水量排行榜，4:結束程式：選擇號碼至指定查詢")

    while k=="3":
        print("")
        StperList = [('石門水庫：',Stper(1)),('翡翠水庫：',Stper(2)),('寶山第二水庫：',Stper(3)),('永和山水庫：',Stper(4)),('明德水庫：',Stper(5)),('鯉魚潭水庫：',Stper(6)),('德基水庫：',Stper(7)),('石岡壩：',Stper(8)),('霧社水庫：',Stper(9)),('日月潭水庫：',Stper(10)),('集集攔河堰：',Stper(11)),('湖山水庫：',Stper(12)),('仁義潭水庫：',Stper(13)),('白河水庫：',Stper(14)),('烏山頭水庫：',Stper(15)),('曾文水庫：',Stper(16)),('南化水庫：',Stper(17)),('阿公店水庫：',Stper(18)),('高屏溪攔河堰：',Stper(19)),('牡丹水庫：',Stper(20))]
        sortedStperList = sorted(StperList, key = lambda s: s[1],reverse=True)
        sortStperList = sorted(StperList, key = lambda s: s[1])

        print("全台蓄水量前三名：")
        time.sleep(3)
        for index,i in enumerate(sortedStperList[0:3], start = 1):
            a=str(i).replace('(','').replace(')','').replace('[','').replace(']','').replace(',','').replace("'",'')
            print("第",index,"名",a,"%")
        print("")
        time.sleep(3)
        print("全台蓄水量倒數三名：")
        time.sleep(3)
        for index,i in enumerate(sortStperList[0:3], start = 1):
            a=str(i).replace('(','').replace(')','').replace('[','').replace(']','').replace(',','').replace("'",'')
            print("最後第",index,"名",a,"%")
        print("")
        k=input("1:查詢水庫與三大水庫比較圖，2:查詢全台水庫蓄水量，3:蓄水量排行榜，4:結束程式：選擇號碼至指定查詢")
    
    if k =="4":
        break
print("掰掰，繼續關注我們的水情資歷！")

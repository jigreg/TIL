import urllib.request as req
from bs4 import BeautifulSoup as bs
weather = req.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
weather_bs = bs(weather, "html.parser")
location_list = weather_bs.findAll("location")
city_list = []
wf_list =[]
tmx_list=[] #문자열 데이터
tmn_list = []
for location in location_list:
    print("----------------------")
    print("도시 :  ",location.find("city").stirng)
    print("시간 : ",location.select_one("tmEf").string)
    print("날씨상태 : ",location.find("wf").string)
    print("최고기온 : ",location.find("tmx").string)
    print("최저기온 : ",location.find("tmn").string)
    print("----------------------")
    city_list.append(location.find("city").string)
    wf_list.append(location.find("wf").string)
    tmx_list.append(location.find("tmx").string)
    tmn_list.append(location.find("tmn").string)

#정수변경
'''
for tmx in range(0,len(tmx_list)+1,1):
    tmx_list[tmx] = int(tmx_list[tmx])
    tmn_list[tmx] = int(tmn_list[tmx])
'''
#정수변경2
tmx_list = list(map(int, tmx_list))
tmn_list = list(map(int, tmn_list))

import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Batang'
plt.rcParams['figure.figsize'] = (15,8) #그래프 비율
plt.rcParams['lines.linestyle'] = '-.' #선스타일
plt.rcParams['lines.linewidth'] = 3 #선 굵기
plt.rcParams['axes.grid'] = True #모눈격자
 
plt.subplots()
plt.plot(city_list,tmx_list);
plt.title("도시별 최고/최저기온")
plt.xlabel("도시명")
plt.ylabel("기온")


plt.plot(city_list,tmn_list);
plt.savefig("city_weather.png")
plt.show()
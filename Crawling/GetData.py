# 경찰청 분실물 api 활용(mysql과 연동해서 db 저장까지 함)

import urllib.request as ul
import xmltodict
import pymysql.cursors
import sys
from datetime import datetime

# 현재 날짜 추출
''' 
date=datetime.today()
print(date)

date_s = str(date)

year = date_s[0:4]
month = date_s[5:7]
day = date_s[8:10]

print(year)
print(month)
print(day)
'''

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='0000',
    db='findlost',
    charset='utf8'
)

cursor = conn.cursor()

# DB 버전 확인
'''
cursor.execute("SELECT VERSION()")
data=cursor.fetchone()
print(data)
'''

# insert 예제
'''
itemName = 'sextoy'
lostPlace = 'myhome'

sql = 'insert into lost_items(itemName, lostPlace) values(%s, %s)'
cursor.execute(sql, (itemName,lostPlace))
conn.commit()
'''

# 기존 테이블 데이터 삭제
sql = "call del()"
cursor.execute(sql)
conn.commit()

numOfData = 0
numOfRows = 100
pageNo = 1

# 일정 시간이 지나면 db 프로시저를 호출한다.(리눅스 스케쥴러로 우분투에서 사용할 계획)
# 호출된 db 프로시저는 기존 db table을 drop하고 다시 테이블을 생성한다.

'''
while 1:

    url = f"http://apis.data.go.kr/1320000/LostGoodsInfoInqireService/getLostGoodsInfoAccToClAreaPd?serviceKey=SJ7N8CAqRc%2Bef9sStQLUP%2FSDXFvV1a%2FAjdXX85OVgW5Kf3g2Ch%2FHzunhAnImnmmXMVnp5yWD8s6bSib04c0ouA%3D%3D&START_YMD=20190101&END_YMD=20190716&numOfRows={numOfRows}&pageNo={pageNo}"

    request = ul.Request(url) #요청 메세지를 보낸다.
    response = ul.urlopen(request) #응답 메세지를 오픈한다.
    rescode = response.getcode() #제대로 데이터가 수신됐는지 확인하는 코드 성공시 200

    if(rescode == 200):
        responseData = response.read() #요청받은 데이터를 읽음
        rD = xmltodict.parse(responseData) #XML형식의 데이터를 dict형식으로 변환시켜줌
        #print(rD) #정상적으로 데이터가 출력되는지 확인
        w_data = rD["response"]["body"]["items"]["item"] #item 데이터만 정제

        pageNo+=1

        for i in w_data: #다수의 item들을 하나씩 뽑아온다.
            numOfData+=1
            print(numOfData)
            print("분실물 이름: "+i["lstPrdtNm"])
            print("분실 위치 : "+i["lstPlace"]+"\n")

            sql = "insert into main_lostitems(itemName, lostPlace) values(%s, %s)"
            cursor.execute(sql, (i["lstPrdtNm"],i["lstPlace"]))
            conn.commit()

'''
# 포털기관 습득물 데이터 받아오기
while 1:
    url = f"http://apis.data.go.kr/1320000/LosPtfundInfoInqireService/getPtLosfundInfoAccToClAreaPd?serviceKey=SJ7N8CAqRc%2Bef9sStQLUP%2FSDXFvV1a%2FAjdXX85OVgW5Kf3g2Ch%2FHzunhAnImnmmXMVnp5yWD8s6bSib04c0ouA%3D%3D&START_YMD=20190101&END_YMD20190719&numOfRows={numOfRows}&pageNo={pageNo}"
    # url = f"http://apis.data.go.kr/1320000/LostGoodsInfoInqireService/getLostGoodsInfoAccToClAreaPd?serviceKey=SJ7N8CAqRc%2Bef9sStQLUP%2FSDXFvV1a%2FAjdXX85OVgW5Kf3g2Ch%2FHzunhAnImnmmXMVnp5yWD8s6bSib04c0ouA%3D%3D&START_YMD=20190101&END_YMD=20190716&numOfRows={numOfRows}&pageNo={pageNo}"

    request = ul.Request(url)  # 요청
    # 메세지를 보낸다.
    response = ul.urlopen(request)  # 응답 메세지를 오픈한다.
    rescode = response.getcode()  # 제대로 데이터가 수신됐는지 확인하는 코드 성공시 200

    if (rescode == 200):
        responseData = response.read()  # 요청받은 데이터를 읽음
        rD = xmltodict.parse(responseData)  # XML형식의 데이터를 dict형식으로 변환시켜줌
        # print(rD) #정상적으로 데이터가 출력되는지 확인
        w_data = rD["response"]["body"]["items"]["item"]  # item 데이터만 정제
        totalCount = rD["response"]["body"]["totalCount"]

        pageNo += 1

        for i in w_data:  # 다수의 item들을 하나씩 뽑아온다.
            numOfData += 1

            # print(pageNo)
            print(numOfData)
            print("관리ID: " + i["atcId"])
            print("습득일자 : " + i["fdYmd"])
            print("물품명: " + i["fdPrdtNm"])
            print("보관장소 : " + i["depPlace"])
            print("이미지: " + i["fdFilePathImg"])
            print("물품상세설명 : " + i["fdSbjt"])
            print("물품분류명 : " + i["prdtClNm"] + "\n")

            sql = "insert into main_lostitems(managementID, findYmd, productName, keepPlace, productImg, productDesc, productClass) values(%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (
            i["atcId"], i["fdYmd"], i["fdPrdtNm"], i["depPlace"], i["fdFilePathImg"], i["fdSbjt"], i["prdtClNm"]))
            conn.commit()

            if (numOfData >= int(totalCount)):
                print("데이터 수집이 완료 되었습니다!")
                sys.exit()



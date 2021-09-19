# 푸드 마일리지 계산기
print("--------------------------------")
print("푸드 마일리지 계산기 (v.1.0 RC)\nDeveloped by Scian")
import math
pointlist=[]
while True:
    print("--------------------------------")
    a=input("음식명을 입력해 주세요: ")
    b=input("음식의 무게(g/kg)을 입력해 주세요: ")
    c=input("운송 거리 (km)를 입력해 주세요: ")

    if "g" in b:
        if "kg" in b:
            unit="kg"
            w = b.replace("kg","")
            # print(w)
        else:
            unit="g"
            w = b.replace("g", "")
            # print(w)
    else:
        raise NameError("올바른 단위가 포함되어 있지 않습니다. g 또는 kg 단위를 입력해 주세요.")

    if unit=="g":
        point=0.000001*int(w)
        point=round(point,4)
    elif unit=="kg":
        point=0.001*int(w)
        point = round(point,4)

    # print(point)
    pointlist.append(point)
    # print(pointlist)
    psum = sum(pointlist)
    print("--------------------------------")
    print(a,"푸드 마일리지 (소수 다섯째자리에서 반올림):",point,"t*km")
    print("전체 푸드 마일리지 (소수 다섯째자리에서 반올림):",round(psum,4),"t*km")
    again = input("더 추가할 음식이 있나요?(O/X): ")
    print("--------------------------------")
    if again=="O":
        continue
    elif again=="X":
        break
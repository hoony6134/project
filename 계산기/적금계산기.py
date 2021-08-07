# 적금 계산기
print("적금 계산기\n")
mpy = int(input("매년 얼마의 금액을 저축하나요? : ")) #money per year
year = int(input("몇년짜리 적금인가요? : ")) #몇년
percent = int(input("이율이 몇 퍼센트인가요? (단위: %) : ")) #이율
tempercent = percent/100
print(tempercent)
ypercent = 1+tempercent #예) 1.03%
print(ypercent)
list = []
for i in range(1,year+1):
    print(i)
    temp = int(mpy*(ypercent**i))
    list.append(temp)
    print(list)
bm = ypercent - 1 #분모
bj = list[0]*(ypercent**year-1) #분자
result = bj/bm
print("계산 결과:",round(result),"원을 저축할 수 있습니다. (소수 첫째자리에서 반올림)")

# (c) Copyright by Scian. All Rights Reserved.

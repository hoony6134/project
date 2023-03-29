a=[]
b=[]
c=[]
d=[]
# get the number of cells in each section
# input 16 integers with space in between per each list (section)
a = list(map(int, input("A 섹션의 세포 수를 공백 한 칸을 두고 입력하세요: ").split()))
a_sum = sum(a)
print("A 섹션의 세포 수의 합: "+str(a_sum)+"\nA 섹션 개수: "+str(len(a)))
b = list(map(int, input("B 섹션의 세포 수를 공백 한 칸을 두고 입력하세요: ").split()))
b_sum = sum(b)
print("B 섹션의 세포 수의 합: "+str(b_sum)+"\nB 섹션 개수: "+str(len(b)))
c = list(map(int, input("C 섹션의 세포 수를 공백 한 칸을 두고 입력하세요: ").split()))
c_sum = sum(c)
print("C 섹션의 세포 수의 합: "+str(c_sum)+"\nC 섹션 개수: "+str(len(c)))
d = list(map(int, input("D 섹션의 세포 수를 공백 한 칸을 두고 입력하세요: ").split()))
d_sum = sum(d)
print("D 섹션의 세포 수의 합: "+str(d_sum)+"\nD 섹션 개수: "+str(len(d)))
# find the mean of each section
mean = (a_sum+b_sum+c_sum+d_sum)/4

mult = int(input("희석 배율을 입력하세요: "))
if (mult==1):
    volume = int(input("최종 부피를 입력하세요: "))
    print("--------------------\nResult\n4개의 섹션에서의 평균: "+str(mean)+"\n세포 수: "+str(mean*mult*volume*(10**4))+" cells/"+str(volume)+"mL")
else:
    volume = int(input("최종 현탁액 부피를 입력하세요: "))
    print("--------------------\nResult\n4개의 섹션에서의 평균: "+str(mean)+"\n"+"현탁액의 세포 수 (희석 배율: "+str(mult)+"배): "+str(mean*volume*(10**4))+"\n원액의 세포 수: "+str(mean*mult*volume*(10**4))+" cells/"+str(volume)+"mL")

import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors, datasets
from sklearn import svm
from sklearn.linear_model import LinearRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
file=open('car.csv')

alist=[]
blist=[]
clist=[]
dlist=[]
elist=[]
flist=[]
resultlist=[]
print("▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆\nCROSS VALIDATION\n▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆")
for line in file.readlines():
    line = line.replace('\n', '')
    # print(line)
    a,b,c,d,e,f,result = line.split(',')
    alist.append(float(a))
    blist.append(float(b))
    clist.append(float(c))
    dlist.append(float(d))
    elist.append(float(e))
    flist.append(float(f))
    # alist.append([float(a)])
    # blist.append([float(b)])
    # clist.append([float(c)])
    # dlist.append([float(d)])
    resultlist.append(str(result))
# print(gender)
# print(height)
# print(weight)
X=[]
for i in range(len(resultlist)):
    X.append([alist[i],blist[i],clist[i],dlist[i],elist[i],flist[i]])
y=resultlist
# X=np.array(X)
# y=np.array(y)
# print(X)
# print(y)
# plt.scatter(X[:,0], X[:,1], c=y, s=30, cmap=plt.cm.Paired)
k_fold=int(input("cross validation할 k_fold값: "))
new_X=[[] for i in range(k_fold)]
new_y=[[] for i in range(k_fold)]

#acc
acc_count=0
group=0
for i in range(len(resultlist)):
    if(y[i]=="acc"):
        acc_count+=1
        new_X[group].append(X[i])
        new_y[group].append(y[i])
        if(acc_count==int(len(resultlist)/2/k_fold)):
            acc_count=0
            group+=1

#unacc
unacc_count=0
vgroup=0
for i in range(len(resultlist)):
    if(y[i]=="unacc"):
        unacc_count+=1
        new_X[vgroup].append(X[i])
        new_y[vgroup].append(y[i])
        if(unacc_count==int(len(resultlist)/2/k_fold)):
            unacc_count=0
            vgroup+=1

# #good
# good_count=0
# v2group=0
# for i in range(len(resultlist)):
#     if(y[i]=="good"):
#         unacc_count+=1
#         new_X[v2group].append(X[i])
#         new_y[v2group].append(y[i])
#         if(good_count==int(len(resultlist)/2/k_fold)):
#             good_count=0
#             v2group+=1
#
# #vgood
# vgood_count=0
# v3group=0
# for i in range(len(resultlist)):
#     if(y[i]=="vgood"):
#         unacc_count+=1
#         new_X[v3group].append(X[i])
#         new_y[v3group].append(y[i])
#         if(good_count==int(len(resultlist)/2/k_fold)):
#             vgood_count=0
#             v3group+=1

# print(len(new_X[0]))

total_percentage=0
models = input("모델의 종류를 입력해주세요(linear,poly,rbf,sigmoid,precomputed,lda,knn): ")
if models=="knn":
    neigh = int(input("n_neighbors 값을 입력하세요: "))
for test_group in range(k_fold):
    # if(test_group!=0):continue
    train_X=[]
    train_y=[]
    test_X=[]
    test_y=[]
    for target_group in range(k_fold):
        if(target_group==test_group):
            test_X=new_X[target_group]
            test_y=new_y[target_group]
            # test_X=np.array(test_X)
            # test_y=np.array(test_y)
            # test_X=test_X.reshape(-1, 1)
            # test_y=test_y.reshape(-1, 1)
        elif(target_group!=test_group):
            train_X=train_X+new_X[target_group]
            train_y=train_y+new_y[target_group]
    # print(str("test group: ")+str(test_group))
    # print(len(test_X))
    # print(len(train_X)
    if models=="linear":
        clf = svm.SVC(kernel="linear") #svm_linear
    elif models=="poly":
        clf = svm.SVC(kernel="poly") #svm_poly
    elif models=="rbf":
        clf = svm.SVC(kernel="rbf") #svm_poly
    elif models=="sigmoid":
        clf = svm.SVC(kernel="sigmoid") #svm_poly
    elif models=="precomputed":
        clf = svm.SVC(kernel="precomputed") #svm_poly
    elif models=="lda":
        clf = LinearDiscriminantAnalysis(n_components=1) #lda
    elif models=="knn":
        #knn start
        n_neighbors = neigh
        for weights in ['uniform', 'distance']:
            # we create an instance of Neighbours Classifier and fit the data.
            clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
            clf.fit(X, y)
        #knn end
    else:
        models = input("오류 발생. 다시 시도해주세요.")
        break
    # print(train_X)
    # print("0----------------0")
    # # print(train_y)
    # temptrain=train_X
    # for i in range(len(temptrain)+1):
    #     np.append(train_X,temptrain[i])
    # train_X=np.array(train_X).reshape(1,-1)
    # print(train_X)
    # print(train_y)
    # print(len(train_X))
    # print(len(train_y))
    clf.fit(train_X, train_y)
    # model_answer=clf.predict(np.array(test_X).reshape(-1,1))
    model_answer = clf.predict(test_X)
    total_count=0
    correct_count=0
    for i in range(len(model_answer)):
        total_count+=1
        if(model_answer[i]==test_y[i]):
            correct_count+=1
    percentage=correct_count/total_count*100
    total_percentage+=percentage
    print("테스트 그룹: "+str(test_group+1))
    print("정확도: "+str(percentage)+"% ("+str(correct_count)+"/"+str(total_count)+")\n")
total_percentage/=k_fold
print("----------------------------------------")
print("모델 종류: "+str(models.upper()))
print("cross validation 전체 정확도: "+str(total_percentage)+"%")
print("----------------------------------------\n<데이터로 차 등급 예측>")
# ax = plt.gca()
# xlim = ax.get_xlim()
# ylim = ax.get_ylim()
# xx = np.linspace(xlim[0], xlim[1], 30)
# yy = np.linspace(ylim[0], ylim[1], 30)
# YY, XX = np.meshgrid(yy, xx)
# xy = np.vstack([XX.ravel(), YY.ravel()]).T
# Z = clf.decision_function(xy).reshape(XX.shape)
# ax.contour(XX, YY, Z, colors='k', levels=[-1,0,1], alpha=0.5, linestyles=['--', '-', '--'])
# ax.scatter(clf.support_vectors_[:,0], clf.support_vectors_[:,1], s=60, facecolors='r')
# plt.show()

while True:
    p1,p2,p3,p4,p5,p6 = map(float,input("5가지 값을 공백 한칸을 두고 입력하세요: ").split(" "))
    newdata = [[p1,p2,p3,p4,p5,p6]]
    if clf.predict(newdata)[0] == "unacc":
        level = "사면 안됨!"
    elif clf.predict(newdata)[0] == "acc":
        level = "사도 됨!"
    print("차를 사도 될까?: ",level)

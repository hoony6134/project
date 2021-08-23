import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors, datasets
from sklearn import svm
from sklearn.linear_model import LinearRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
file=open('iris.txt')

alist=[]
blist=[]
clist=[]
dlist=[]
flowerlist=[]
print("▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆\nCROSS VALIDATION\n▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆")
for line in file.readlines():
    line = line.replace('\n', '')
    # print(line)
    a,b,c,d,flower = line.split(',')
    alist.append(float(a))
    blist.append(float(b))
    clist.append(float(c))
    dlist.append(float(d))
    # alist.append([float(a)])
    # blist.append([float(b)])
    # clist.append([float(c)])
    # dlist.append([float(d)])
    flowerlist.append(str(flower))
# print(gender)
# print(height)
# print(weight)
X=[]
for i in range(len(flowerlist)):
    X.append([alist[i],blist[i],clist[i],dlist[i]])
y=flowerlist
Xar=np.array(X)
yar=np.array(y)
print(Xar)
print(yar)
plt.scatter(Xar[:,0], Xar[:,1], c='red', s=30, cmap=plt.cm.Paired)
plt.show()
k_fold=int(input("cross validation할 k_fold값(데이터 개수를 니눴을 때 나누어 떨어져야 오류가 발생하지 않습니다.): "))
new_X=[[] for i in range(k_fold)]
new_y=[[] for i in range(k_fold)]

#setosa
setosa_count=0
group=0
for i in range(len(flowerlist)):
    if(y[i]=="setosa"):
        setosa_count+=1
        new_X[group].append(X[i])
        new_y[group].append(y[i])
        if(setosa_count==int(len(flowerlist)/3/k_fold)):
            setosa_count=0
            group+=1

#versicolor
versicolor_count=0
vgroup=0
for i in range(len(flowerlist)):
    if(y[i]=="versicolor"):
        versicolor_count+=1
        new_X[vgroup].append(X[i])
        new_y[vgroup].append(y[i])
        if(versicolor_count==int(len(flowerlist)/3/k_fold)):
            versicolor_count=0
            vgroup+=1

#virginica
virginica_count=0
v2group=0
for i in range(len(flowerlist)):
    if(y[i]=="virginica"):
        virginica_count+=1
        new_X[v2group].append(X[i])
        new_y[v2group].append(y[i])
        if(virginica_count==int(len(flowerlist)/3/k_fold)):
            virginica_count=0
            v2group+=1

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
print("----------------------------------------\n<데이터로 꽃 종류 예측>")
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
    p1,p2,p3,p4 = map(float,input("4가지 값을 공백 한칸을 두고 입력하세요: ").split(" "))
    newdata = [[p1,p2,p3,p4]]
    print("예측한 꽃:",clf.predict(newdata)[0])

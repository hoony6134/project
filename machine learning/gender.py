from sklearn import svm
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
file=open("gender_dataset.txt","r")

gender=[]
height=[]
weight=[]
for line in file.readlines():
    line=line.replace("\n","")
    input_gender, input_height, input_weight = line.split("\t")
    gender.append(input_gender)
    height.append(float(input_height))
    weight.append(float(input_weight))

X=[]
for i in range(len(height)):
    X.append([height[i],weight[i]])
y=gender


k_fold=4
new_X=[[] for i in range(k_fold)]       #new_X=[[],[],[],[]]
new_y=[[] for i in range(k_fold)]       #new_y=[[],[],[],[]]

#Male
male_count=0
group=0
for i in range(len(gender)):
    if(y[i]=="Male"):
        male_count+=1
        new_X[group].append(X[i])
        new_y[group].append(y[i])
        if(male_count==int(len(gender)/2/k_fold)):
            male_count=0
            group+=1

#Female
female_count=0
group=0
for i in range(len(gender)):
    if(y[i]=="Female"):
        female_count+=1
        new_X[group].append(X[i])
        new_y[group].append(y[i])
        if(female_count==int(len(gender)/2/k_fold)):
            female_count=0
            group+=1

# X -> (10000,2) -> (4,2500,2)  2500중에서 1250 Male, 1250 Female
# y -> (10000) -> (4,2500)  2500중에서 1250 Male, 1250 Female

total_percentage=0
for test_group in range(k_fold):
    train_X=[]
    train_y=[]
    test_X=[]
    test_y=[]
    for target_group in range(k_fold):
        if(target_group==test_group):
            test_X=new_X[target_group]
            test_y=new_y[target_group]
        elif(target_group!=test_group):
            train_X=train_X+new_X[target_group]
            train_y=train_y+new_y[target_group]
    clf=svm.SVC(kernel='poly')
    #clf=LinearDiscriminantAnalysis(n_components=1)
    clf.fit(train_X,train_y)
    model_answer=clf.predict(test_X)

    total_count=0
    correct_count=0
    for i in range(len(model_answer)):
        total_count+=1
        if(model_answer[i]==test_y[i]):
            correct_count+=1
    percentage=correct_count/total_count*100
    total_percentage+=percentage
    print("test_group: "+str(test_group))
    print("Correct percentage: "+str(percentage)+",   "+str(correct_count)+"/"+str(total_count)+"\n")
total_percentage/=k_fold
print("Cross validation accuracy: "+str(total_percentage))

'''
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
file=open("gender_dataset.txt","r")

gender=[]
height=[]
weight=[]
for line in file.readlines():
    line=line.replace("\n","")
    input_gender, input_height, input_weight = line.split("\t")
    gender.append(input_gender)
    height.append(float(input_height))
    weight.append(float(input_weight))

X=[]
for i in range(len(height)):
    X.append([height[i],weight[i]])
y=gender

clf = LinearDiscriminantAnalysis(n_components=2)
clf.fit(X,y)

print(clf.predict([[73,241],[63,156],[65,152]]))
'''

'''
from sklearn import neighbors
file=open("gender_dataset.txt","r")

gender=[]
height=[]
weight=[]
for line in file.readlines():
    line=line.replace("\n","")
    input_gender, input_height, input_weight = line.split("\t")
    gender.append(input_gender)
    height.append(float(input_height))
    weight.append(float(input_weight))

X=[]
for i in range(len(height)):
    X.append([height[i],weight[i]])
y=gender

n_neighbors=7
clf = neighbors.KNeighborsClassifier(n_neighbors,weights='distance')
clf.fit(X,y)

print(clf.predict([[73,241],[63,156],[65,152]]))
'''

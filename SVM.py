from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
import xlrd
import csv
from sklearn.model_selection import  train_test_split

Data = []
Result = []
count = 0
with open('C:\\Users\\ahmed.ehab\\Downloads\\sheet.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        if count == 0:
            count += 1
            continue
        Arr = []
        InInData = row[0].split(",")
        for x in range(0,len(InInData)):
            if x == len(InInData)-1:
                Result.append(InInData[x])
                continue
            Arr.append(InInData[x])
        Data.append(Arr)

max=0.0
max1=0.0
random1=0
random2=0
testttt = [52]
for i in range(1):

    # SVM
    print("why")
    x_train,x_test,y_train,y_test=train_test_split(Data,Result,test_size=0.2,random_state=16262)#16262,2566
    model = svm.SVC(kernel='linear', C=0.01, gamma=1)
    model.fit(x_train, y_train)
    predicted= model.score(x_test,y_test)
    # print(model.predict(x_test))
    # print(y_test)
    # print(str(i), predicted)
    print((model.score(x_test,y_test)))
    if predicted >max:
        max=predicted
        random1=i
    # print(i)




    # KNN
    from sklearn.neighbors import KNeighborsClassifier
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(x_train, y_train)
    predicted= model.score(x_test,y_test)
    print(model.score(x_test,y_test))
    if predicted >max:
        max1=predicted
        random2=i
# print(max," ",random1," ",max1," ",random2)

    #DT
    dataset = pd.read_csv('./wine.data.csv')
    classtrain = dataset.iloc[:,1:13] 
    classtest = dataset.iloc[:,0] 
    xtrain , xtest , ytrain, ytest = train_test_split(classtrain,classtest,random_state=10, test_size=0.2) 
    dtree = DecisionTreeClassifier()
    print("this is Decision Tree: ", accuracy_score(ytest,dtree.predict(xtest))*100)
    dtree = DecisionTreeClassifier()

    dtree.fit(xtrain,ytrain )

    print("this is Decision Tree: ", accuracy_score(ytest,dtree.predict(xtest))*100)
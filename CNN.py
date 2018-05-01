import pip
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Conv1D, MaxPooling2D
from keras.utils import np_utils
from keras.preprocessing.image import  img_to_array
from keras import backend as K
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
import csv

Data = []
Result = []
count = 0
with open('sheet1.csv', newline='') as csvfile:
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


batch_size=32
nb_classes=15
# nb_epoch=6
nb_filters=32
# nb_pool=2
# nb_conv=3
Data=np.reshape(Data,(len(Data),3,5))


x_train, x_test, y_train, y_test= train_test_split(Data,Result,test_size=0.2,random_state=4)




uniques, id_train=np.unique(y_train,return_inverse=True)
Y_train=np_utils.to_categorical(id_train,nb_classes)
uniques, id_test=np.unique(y_test,return_inverse=True)
Y_test=np_utils.to_categorical(id_test,nb_classes)
print(Y_test)
model= Sequential()
model.add(Conv1D(nb_filters,3,activation='relu',input_shape=(3,5)))

model.add(Conv1D(nb_filters,1,activation="relu"))
# model.add(Conv1D(16,1,activation="relu"))

model.add(Dense(128))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

Y_test=np.reshape(Y_test,(len(Y_test),1,15))
Y_train=np.reshape(Y_train,(len(Y_train),1,15))

# nb_epoch=5;
import operator
batch_size=5;
model.fit(x_train,Y_train,batch_size=batch_size,nb_epoch=250,verbose=1,validation_data=(x_test,Y_test))
model.save('gradCNN.h5')
counter=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

for i in range (len(x_test)):
    result=model.predict(np.array([x_test[i]]))
    index, value = max(enumerate(result[0][0]), key=operator.itemgetter(1))
    index1, value1 = max(enumerate(Y_test[i][0]), key=operator.itemgetter(1))
    if index==index1:
        counter[index] +=1

print((counter.sum()/len(Y_test))*100)
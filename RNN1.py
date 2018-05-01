import pip
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Conv1D, MaxPooling2D
from keras.utils import np_utils
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.model_selection import train_test_split
import numpy as np
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
nb_epoch=8

Data=np.reshape(Data,(len(Data),1,15))
x_train, x_test, y_train, y_test= train_test_split(Data,Result,test_size=0.2,random_state=4)



uniques, id_train=np.unique(y_train,return_inverse=True)
Y_train=np_utils.to_categorical(id_train,nb_classes)
uniques, id_test=np.unique(y_test,return_inverse=True)
Y_test=np_utils.to_categorical(id_test,nb_classes)
print(Y_test)

model= Sequential()
model.add(LSTM(15,input_shape=(1,15),return_sequences=True))
model.add(LSTM(64,activation='relu',return_sequences=True))
model.add(LSTM(128,activation='relu',return_sequences=True))
model.add(LSTM(256,activation='relu',return_sequences=True))
model.add(LSTM(512,activation='tanh',return_sequences=True))
model.add(LSTM(128,activation='relu',return_sequences=True))
model.add(LSTM(64,activation='relu',return_sequences=True))
model.add(LSTM(15,activation='relu',return_sequences=True))
model.add(Dense(15,activation='sigmoid'))


model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
Y_train=np.reshape(Y_train,(len(Y_train),1,15))
Y_test=np.reshape(Y_test,(len(Y_test),1,15))
# x_train=np.reshape(x_train,(len(x_train),1,15))

batch=5

# testtt = [9,0,0,104,0,13,5,0,0,7,0,16,17,9,0]
# testt=np.reshape(testtt,(len(testtt),1,15))

model.fit(x_train,Y_train,epochs=8,batch_size=batch,validation_data=(x_test,Y_test))
model.save('grad.h5')
# model.predict(np.array(testt))

# for i in range (0,len(x_test)):
#     print(model.predict(np.array([x_test[i]])))

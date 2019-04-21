#tensorflow
import tensorflow as tf
from tensorflow import keras

#math tools
import numpy as np
import threading as th
from sklearn.preprocessing import LabelBinarizer

#data parse and io
import csv
from binance.client import Client



x_train = []
temp_x_train = []
with open("pastdata.csv") as f:
    i = 0
    for line in csv.DictReader(f, fieldnames=('open_time','open','high','low','close','volume','close_time','qv','number','tbb','tbq','i')):
        if(i < 15):
            temp_x_train.append(float(line['open']))
        i += 1

        if(i == 15):
            x_train.append(temp_x_train)
        elif(i == 60):
            i = 0
            temp_x_train = []

y_train_dat = []
temp_y_train_dat = []
with open("pastdata.csv") as f:
    i = 0
    for line in csv.DictReader(f, fieldnames=(
    'open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'qv', 'number', 'tbb', 'tbq', 'i')):
        temp_y_train_dat.append(float(line['open']))
        i += 1
        if (i == 60):
            y_train_dat.append(temp_y_train_dat)
            i = 0
            temp_y_train_dat = []


x_train = x_train[0:-1]
y_train = []
for sublist in y_train_dat:
    temp_sublist = [0] * 60
    temp_sublist[np.argmax(sublist)] = 1
    y_train.append(temp_sublist)
    # y_train.append(np.argmax(sublist))

x_train = np.array(x_train, dtype='float')
y_train = np.array(y_train)
y_train = LabelBinarizer().fit_transform(y_train)

# print(tf.convert_to_tensor(x_train))




# model=tf.keras.models.Sequential()
# model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
# model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
# model.add(tf.keras.layers.Dense(60, activation=tf.nn.softmax))
#
# model.compile(optimizer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])
#
# model.fit(x_train, y_train, batch_size=32, epochs=480, steps_per_epoch=1)
#
#
# model.summary()
#
#
# model.save('learn_model.h5')




import numpy as np
import sys
import keras
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
#импорты библиотек

x = np.linspace(-5, 5, 1000)
y = x**2
#задаём значения

model = Sequential()
model.add(Dense(10, input_dim = 1, activation= "relu"))
model.add(Dense(1))

model.compile(loss = "mse", optimizer="adam")

model.fit(x, y, epochs = 500, verbose =0) #epochs = кол-во эпох обучения

plt.plot(x, y, label = "ground truth")
plt.plot(x, model.predict(x), label = "predicted")
plt.legend()
plt.show
#ground truth - то как должно быть а predicted - то что показала нейросеть


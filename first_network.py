import numpy as np
from tensorflow import keras
from matplotlib import pyplot as plt

#random set with 1000 rows and 0/1 labels
data = np.random.random((1000, 10))
labels = np.where(np.random.random((1000))>.5,1,0)

"""
#sequential declaration of network

model = keras.models.Sequential()

model.add(keras.layers.Dense(7, activation=keras.activations.relu, input_shape=(10,)))
model.add(keras.layers.Dense(5, activation=keras.activations.relu))
model.add(keras.layers.Dense(3, activation=keras.activations.relu))
model.add(keras.layers.Dense(1, activation=keras.activations.sigmoid))

model.summary()
"""

#functional declaration of network

input_tensor = keras.layers.Input(shape=(10,))
x1 = keras.layers.Dense(7, activation='relu')(input_tensor)
x2 = keras.layers.Dense(5, activation='relu')(x1)
x3 = keras.layers.Dense(3, activation='relu')(x2)
output_tensor = keras.layers.Dense(1, activation='sigmoid')(x3)
model = keras.models.Model(inputs=input_tensor, outputs=output_tensor)

model.summary()

#optimizer, loss function, metrics
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#model training, needs data, labels, batch_size (defines the number of samples
#that will be propagated through the network), epochs (number of complete passes
# through the training dataset), validation_split (defines training set and validation set)
history = model.fit(data, labels, batch_size=16, epochs=10, validation_split=.2)

fig, ax = plt.subplots()
ax.plot(range(1,11), history.history['accuracy'], label='Train Accuracy')
ax.plot(range(1,11), history.history['val_accuracy'], label='Validation Accuracy')
ax.legend(loc='best')
ax.set(xlabel='epochs', ylabel='accuracy')
plt.show()


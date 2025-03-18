import  numpy as np
import tensorflow as tf
from tensorflow import keras

mnist=tf.keras.datasets.fashion_mnist
(train_img,train_label),(test_img,test_label)=mnist.load_data()
training_images = train_img/255.0
test_images = test_img/255.0

model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                    tf.keras.layers.Dense(128, activation=tf.nn.relu),
                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

model.compile(optimizer = 'adam',
              loss = 'sparse_categorical_crossentropy')

model.fit(training_images, train_label, epochs=5)

model.evaluate(test_images, test_label)

classifications = model.predict(test_images)

print(classifications[0])
print(test_label[0])
import cv2
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split

IMG_WIDTH = 48
IMG_HEIGHT = 48
TEST_RATIO = 0.2

X = []
Y = []
j = 0

print("reading data")

with open('fer2013new.csv', newline='') as file:
    for line in file:
        j += 1
        if j < 500:
            line = line.replace('\n', '')
            features = line.split(",")
            if len(features) == 12 and features[0] != 'Usage' and len(features[1]) > 0:
                path = ''
                if features[0] == 'Training':
                    path = 'FER2013Train/' + features[1]  # numele pozei
                    img = cv2.imread(path)
                    img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
                    X.append(img)
                    f = [int(feature) / 10 for feature in features[2:]]  # probabilitate
                    Y.append(np.array(f))
X = np.array(X)
Y = np.array(Y)

print("extracting features automated")
feature_model = tf.keras.applications.VGG16(weights='imagenet', include_top=False)
features = []
i = 0
for img in X:
    print(i)
    i += 1
    preprocessed_img = tf.keras.applications.vgg16.preprocess_input(img)
    preprocessed_img = np.expand_dims(preprocessed_img, axis=0)
    feature = feature_model.predict(preprocessed_img, verbose=0)
    features.append(feature)
features = np.array(features)
aux = features[:, 0, 0, 0]
features = np.array(aux)

X_train, X_test, Y_train, Y_test = train_test_split(features, Y, test_size=TEST_RATIO, random_state=42)

print("neural network")
model = Sequential([
    Dense(64, activation='relu'),
    Dense(128, activation='relu'),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, Y_train, epochs=50, batch_size=32, validation_data=(X_test, Y_test))

loss, accuracy = model.evaluate(X_test, Y_test)
print('accuracy:', accuracy)

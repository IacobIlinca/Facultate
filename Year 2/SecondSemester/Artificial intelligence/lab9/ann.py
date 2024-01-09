# Import necessary libraries
import os
import cv2
import numpy as np
from keras import Sequential
from keras.layers import Flatten, Dense
from sklearn.model_selection import train_test_split

IMG_WIDTH = 128
IMG_HEIGHT = 128
TEST_RATIO = 0.2

# Load the dataset
X = []
y = []
for root, dirs, files in os.walk('databasesepia/normal'):
    for file in files:
        if file.endswith('.jpg'):
            img_path = os.path.join(root, file)
            img = cv2.imread(img_path)
            img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
            X.append(img.flatten())
            y.append(0)

for root, dirs, files in os.walk('databasesepia/sepia'):
    for file in files:
        if file.endswith('.jpg'):
            img_path = os.path.join(root, file)
            img = cv2.imread(img_path)
            img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
            X.append(img.flatten())
            y.append(1)

# Convert the data to numpy arrays
X = np.array(X)
y = np.array(y)

# Flatten the image data
X = X.reshape(X.shape[0], -1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_RATIO, random_state=42)

# Build the neural network model
model = Sequential([
    Dense(64, activation='relu', input_shape=(IMG_WIDTH * IMG_HEIGHT * 3,)),
    Dense(32, activation='relu', input_shape=(IMG_WIDTH * IMG_HEIGHT * 3,)),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print('Test accuracy:', accuracy)

model.summary()

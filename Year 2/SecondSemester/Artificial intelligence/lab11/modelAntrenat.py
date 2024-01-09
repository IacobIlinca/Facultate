import cv2
import numpy as np
import pandas as pd
from keras import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten
from keras.losses import CategoricalCrossentropy
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from skimage.feature import hog
from sklearn.preprocessing import LabelEncoder

# Load the dataset
data = pd.read_csv('data/fer2013.csv')

# Extract the pixel values and labels from the dataset
pixels = data['pixels'].values
labels = data['emotion'].values

# Convert pixel values to images
images = []
for pixel_sequence in pixels:
    pixel_array = np.array(pixel_sequence.split(), dtype=np.uint8).reshape(48, 48)
    images.append(pixel_array)

# Convert the images and labels to numpy arrays
X = np.array(images)
y = np.array(labels)

# Normalize the pixel values
X = X / 255.0

# Extract HOG features from the images
X_hog = []
for image in X:
    hog_features = hog(image, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=False)
    X_hog.append(hog_features)

# Convert the HOG features and labels to numpy arrays
X_hog = np.array(X_hog)
X_hog2 = []
for i in range(len(X_hog)):
    X_hog2.append(X_hog[i].reshape(30,30))
X_hog = np.array(X_hog2)

y = to_categorical(y)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_hog, y, test_size=0.2, random_state=42)

# Define the CNN model
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(30,30,1)))
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(Conv2D(256, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(7, activation='softmax'))

# Reshape the input data to have 4 dimensions
# X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], X_train.shape[2], 1)
# X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], X_test.shape[2], 1)


# Compile the model
model.compile(optimizer='adam', loss=CategoricalCrossentropy(), metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test)
print('Test accuracy:', test_acc)

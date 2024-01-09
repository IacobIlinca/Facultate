from sklearn.preprocessing import StandardScaler
import numpy as np


class Utils:

    @staticmethod
    def linear(x, a=0.1, b=0):
        return a * x + b

    @staticmethod
    def linear_derivative(x, a=0.1, b=0):
        return a

    @staticmethod
    def readData():
        intrare = []
        iesire = []
        with open("iris.data", newline='') as file:
            for line in file:
                line = line.replace('\n', '')
                d = []
                features = line.split(",")
                if len(features) > 0:
                    for i in range(len(features) - 1):
                        d.append(float(features[i]))
                    intrare.append(d)
                    feat = features[len(features) - 1]
                    if feat == "Iris-setosa":
                        iesire.append([1, 0, 0])
                    elif feat == "Iris-versicolor":
                        iesire.append([0, 1, 0])
                    else:
                        iesire.append([0, 0, 1])

        return intrare, iesire

    @staticmethod
    def softmax(x):
        """Compute softmax values for each sets of scores in x."""
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum(axis=0)  # only difference

    @staticmethod
    def normalisation(trainData, testData):
        scaler = StandardScaler()
        if not isinstance(trainData[0], list):
            # encode each sample into a list
            trainData = [[d] for d in trainData]
            testData = [[d] for d in testData]

            scaler.fit(trainData)  # fit only on training data
            normalisedTrainData = scaler.transform(trainData)  # apply same transformation to train data
            normalisedTestData = scaler.transform(testData)  # apply same transformation to test data

            # decode from list to raw values
            normalisedTrainData = [el[0] for el in normalisedTrainData]
            normalisedTestData = [el[0] for el in normalisedTestData]
        else:
            scaler.fit(trainData)  # fit only on training data
            normalisedTrainData = scaler.transform(trainData)  # apply same transformation to train data
            normalisedTestData = scaler.transform(testData)  # apply same transformation to test data
        return normalisedTrainData, normalisedTestData
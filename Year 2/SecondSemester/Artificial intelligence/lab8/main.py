import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

from MyLogisticRegression import MyLogisticRegression


def citeste(path):
    intrare = []
    iesire = []
    with open(path, newline='') as file:
        for line in file:
            line = line.replace('\n', '')
            d = []
            features = line.split(",")
            if len(features) > 0:
                for i in range(len(features) - 1):
                    d.append(float(features[i]))
                intrare.append(d)
                iesire.append(features[len(features) - 1])
    return intrare, iesire


def prelucrare(k):
    inputs, outputs = citeste('iris.data')
    np.random.seed(5)
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(k * len(inputs)), replace=False)
    validationSample = [i for i in indexes if not i in trainSample]
    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]
    validationInputs = [inputs[i] for i in validationSample]
    validationOutputs = [outputs[i] for i in validationSample]

    scaler = StandardScaler()
    scaler.fit(trainInputs)
    normalisedTrainInputs = scaler.transform(trainInputs)
    normalisedTestInputs = scaler.transform(validationInputs)
    trainInputs = normalisedTrainInputs
    validationInputs = normalisedTestInputs
    return trainInputs, trainOutputs, validationInputs, validationOutputs


def learn():
    trainInputs, trainOutputs, validationInputs, validationOutputs = prelucrare(0.79)

    regressor = linear_model.LogisticRegression(max_iter=1000)
    regressor.fit(trainInputs, trainOutputs)

    computedValidationOutputs = regressor.predict(validationInputs)
    accuracy = 0
    for i in range(len(computedValidationOutputs)):
        if computedValidationOutputs[i] == validationOutputs[i]:
            accuracy += 1

    print("Accuracy", accuracy * 100 / len(computedValidationOutputs), "%")


def manual_cross_validation():
    mean = 0
    for i in range(1, 9):
        k = i / 10
        trainInputs, trainOutputs, validationInputs, validationOutputs = prelucrare(k)
        accuracy = 0
        trainOutputs1 = []
        for floare in trainOutputs:
            if floare == "Iris-setosa":
                trainOutputs1.append(0)
            else:
                trainOutputs1.append(1)

        classifier1 = MyLogisticRegression()
        classifier1.fit(trainInputs, trainOutputs1)

        trainOutputs2 = []
        for floare in trainOutputs:
            if floare == "Iris-versicolor":
                trainOutputs2.append(0)
            else:
                trainOutputs2.append(1)

        classifier2 = MyLogisticRegression()
        classifier2.fit(trainInputs, trainOutputs2)

        trainOutputs3 = []
        for floare in trainOutputs:
            if floare == "Iris-virginica":
                trainOutputs3.append(0)
            else:
                trainOutputs3.append(1)

        classifier3 = MyLogisticRegression()
        classifier3.fit(trainInputs, trainOutputs3)

        computedOutputs1 = classifier1.predict(validationInputs)
        for i in range(len(computedOutputs1)):
            if computedOutputs1[i] == 0:
                if validationOutputs[i] == "Iris-setosa":
                    accuracy = accuracy + 1

        computedOutputs2 = classifier2.predict(validationInputs)
        for i in range(len(computedOutputs2)):
            if computedOutputs2[i] == 0:
                if validationOutputs[i] == "Iris-versicolor":
                    accuracy = accuracy + 1

        computedOutputs3 = classifier3.predict(validationInputs)
        for i in range(len(computedOutputs3)):
            if computedOutputs3[i] == 0:
                if validationOutputs[i] == "Iris-virginica":
                    accuracy = accuracy + 1

        accuracy = accuracy * 100 / len(validationOutputs)
        mean += accuracy
    mean = mean / 9
    print("Accuracy cross validation: ", mean, "%")


def manual():
    trainInputs, trainOutputs, validationInputs, validationOutputs = prelucrare(0.79)
    accuracy = 0
    trainOutputs1 = []
    for floare in trainOutputs:
        if floare == "Iris-setosa":
            trainOutputs1.append(0)
        else:
            trainOutputs1.append(1)

    classifier1 = MyLogisticRegression()
    classifier1.fit(trainInputs, trainOutputs1)

    trainOutputs2 = []
    for floare in trainOutputs:
        if floare == "Iris-versicolor":
            trainOutputs2.append(0)
        else:
            trainOutputs2.append(1)

    classifier2 = MyLogisticRegression()
    classifier2.fit(trainInputs, trainOutputs2)

    trainOutputs3 = []
    for floare in trainOutputs:
        if floare == "Iris-virginica":
            trainOutputs3.append(0)
        else:
            trainOutputs3.append(1)

    classifier3 = MyLogisticRegression()
    classifier3.fit(trainInputs, trainOutputs3)

    computedOutputs1 = classifier1.predict(validationInputs)
    for i in range(len(computedOutputs1)):
        if computedOutputs1[i] == 0:
            if validationOutputs[i] == "Iris-setosa":
                accuracy = accuracy + 1

    computedOutputs2 = classifier2.predict(validationInputs)
    for i in range(len(computedOutputs2)):
        if computedOutputs2[i] == 0:
            if validationOutputs[i] == "Iris-versicolor":
                accuracy = accuracy + 1

    computedOutputs3 = classifier3.predict(validationInputs)
    for i in range(len(computedOutputs3)):
        if computedOutputs3[i] == 0:
            if validationOutputs[i] == "Iris-virginica":
                accuracy = accuracy + 1

    accuracy = accuracy * 100 / len(validationOutputs)
    print("Accuracy manual: ", accuracy, "%")


if __name__ == '__main__':
    learn()
    manual()
    manual_cross_validation()

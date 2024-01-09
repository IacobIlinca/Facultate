import csv
import os

import numpy as np
from sklearn import linear_model, datasets
from sklearn.metrics import mean_squared_error

from MySGDRegressor import MySGDRegression


def loadData(fileName, inputVariabNames, outputVariabName):
    data = []
    dataNames = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                dataNames = row
            else:
                data.append(row)
            line_count += 1
    selectedVariables = [dataNames.index(var) for var in inputVariabNames]
    inputs = [[float(data[i][var]) for var in selectedVariables] for i in range(len(data))]
    selectedOutput = dataNames.index(outputVariabName)
    outputs = [float(data[i][selectedOutput]) for i in range(len(data))]

    return inputs, outputs


def prelucrare(inputVariableName, outputVariableName):
    crtDir = os.getcwd()
    filePath = os.path.join(crtDir, 'data', 'world-happiness-report-2017.csv')

    inputs, outputs = loadData(filePath, inputVariableName, outputVariableName)

    np.random.seed(5)
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
    validationSample = [i for i in indexes if not i in trainSample]
    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]
    validationInputs = [inputs[i] for i in validationSample]
    validationOutputs = [outputs[i] for i in validationSample]
    return trainInputs, trainOutputs, validationInputs, validationOutputs


def learning(nr_var, inputVariableName, outputVariableName):
    neNormtrainInputs, neNormtrainOutputs, neNormvalidationInputs, neNormvalidationOutputs = prelucrare(
        inputVariableName, outputVariableName)
    neNormtrainInputs = np.array(neNormtrainInputs).T
    trainInputs = []
    stDev = []
    mean = []
    for i in neNormtrainInputs:
        st, mn, train = normalisation(i)
        trainInputs.append(train)
        stDev.append(st)
        mean.append(mn)
    trainInputs = np.array(trainInputs).T

    stDevOut, meanOut, trainOutputs = normalisation(neNormtrainOutputs)
    validationInputs = []
    neNormvalidationInputs = np.array(neNormvalidationInputs).T
    for i in range(len(stDev)):
        s, m, valid = normalisation(neNormvalidationInputs[i], stDev[i], mean[i])
        validationInputs.append(valid)
    validationInputs = np.array(validationInputs).T
    st, me, validationOutputs = normalisation(neNormvalidationOutputs, stDevOut, meanOut)

    regressor = linear_model.SGDRegressor(alpha=0.001, max_iter=1000)
    regressor.fit(trainInputs, trainOutputs)
    if nr_var == 2:
        w0, w1, w2 = regressor.intercept_[0], regressor.coef_[0], regressor.coef_[1]
        print("Model by tool: f(x1, x2) = {} + {}*x1 + {}*x2".format(w0, w1, w2))
    elif nr_var == 1:
        w0, w1 = regressor.intercept_[0], regressor.coef_[0]
        print("Model by tool: f(x1) = {} + {}*x1 ".format(w0, w1))

    computedValidationOutputs = regressor.predict(validationInputs)

    error = mean_squared_error(validationOutputs, computedValidationOutputs)
    print("prediction error (tool): ", error)


def learning_manual(nr_var, inputVariableName, outputVariableName):
    neNormtrainInputs, neNormtrainOutputs, neNormvalidationInputs, neNormvalidationOutputs = prelucrare(
        inputVariableName, outputVariableName)
    neNormtrainInputs = np.array(neNormtrainInputs).T
    trainInputs = []
    stDev = []
    mean = []
    for i in neNormtrainInputs:
        st, mn, train = normalisation(i)
        trainInputs.append(train)
        stDev.append(st)
        mean.append(mn)
    trainInputs = np.array(trainInputs).T

    stDevOut, meanOut, trainOutputs = normalisation(neNormtrainOutputs)
    validationInputs = []
    neNormvalidationInputs = np.array(neNormvalidationInputs).T
    for i in range(len(stDev)):
        s, m, valid = normalisation(neNormvalidationInputs[i], stDev[i], mean[i])
        validationInputs.append(valid)
    validationInputs = np.array(validationInputs).T
    st, me, validationOutputs = normalisation(neNormvalidationOutputs, stDevOut, meanOut)

    regressor = MySGDRegression()
    regressor.fit(trainInputs, trainOutputs)
    if nr_var == 2:
        w0, w1, w2 = regressor.intercept_, regressor.coef_[0], regressor.coef_[1]
        print("Model manual: f(x1, x2) = {} + {}*x1 + {}*x2".format(w0, w1, w2))
    elif nr_var == 1:
        w0, w1 = regressor.intercept_, regressor.coef_[0]
        print("Model manual: f(x1) = {} + {}*x1 ".format(w0, w1))

    computedValidationOutputs = regressor.predict(validationInputs)

    error = mean_squared_error(validationOutputs, computedValidationOutputs)
    print("prediction error (manual): ", error)


def normalisation(features, s=None, m=None):
    if m is None:
        m = sum(features) / len(features)
    if s is None:
        s = (1 / len(features) * sum([(mi - m) ** 2 for mi in features])) ** 0.5
    medianHouseValueZscore = [(mi - m) / s for mi in features]
    return s, m, medianHouseValueZscore

def multiTarget():
    data = datasets.load_linnerud(return_X_y=True)
    inputs = data[0]
    outputs = data[1]
    np.random.seed(5)
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
    validationSample = [i for i in indexes if not i in trainSample]
    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]
    validationInputs = [inputs[i] for i in validationSample]
    validationOutputs = [outputs[i] for i in validationSample]

    regressor = linear_model.SGDRegressor(alpha=0.001, max_iter=1000)
    trainOutputs = np.array(trainOutputs).T
    validationOutputs = np.array(validationOutputs).T
    for i in range(len(trainOutputs)):
        trainLine = trainOutputs[i]
        validLine = validationOutputs[i]
        regressor.fit(trainInputs, trainLine)
        w0, w1, w2, w3 = regressor.intercept_[0], regressor.coef_[0], regressor.coef_[1], regressor.coef_[2]
        print(i)
        print("Model by tool: f(x1, x2) = {} + {}*x1 + {}*x2 + {}*x3".format(w0, w1, w2, w3))

        computedValidationOutputs = regressor.predict(validationInputs)

        error = mean_squared_error(validLine, computedValidationOutputs)
        print("prediction error (tool): ", error)



if __name__ == '__main__':
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")
    learning(1, ['Economy..GDP.per.Capita.'], 'Happiness.Score')
    learning_manual(1, ['Economy..GDP.per.Capita.'], 'Happiness.Score')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")
    learning(2, ['Economy..GDP.per.Capita.', 'Freedom'], 'Happiness.Score')
    learning_manual(2, ['Economy..GDP.per.Capita.', 'Freedom'], 'Happiness.Score')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")
    multiTarget()

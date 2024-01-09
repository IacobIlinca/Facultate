import csv
import os

from sklearn import linear_model

# load some data
crtDir = os.getcwd()
fileName = os.path.join(crtDir, 'data', 'reviews_mixed.csv')

data = []
with open(fileName) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            dataNames = row
        else:
            data.append(row)
        line_count += 1

inputs = [data[i][0] for i in range(len(data))]
outputs = [data[i][1] for i in range(len(data))]
labelNames = list(set(outputs))

print(inputs[:2])
print(labelNames[:2])

# prepare data for training and testing

import numpy as np

np.random.seed(5)
# noSamples = inputs.shape[0]
noSamples = len(inputs)
indexes = [i for i in range(noSamples)]
trainSample = np.random.choice(indexes, int(0.8 * noSamples), replace=False)
testSample = [i for i in indexes if not i in trainSample]

trainInputs = [inputs[i] for i in trainSample]
trainOutputs = [outputs[i] for i in trainSample]
testInputs = [inputs[i] for i in testSample]
testOutputs = [outputs[i] for i in testSample]

print(trainInputs[:3])

# extract some features from the raw text

# # representation 1: Bag of Words
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()

trainFeatures = vectorizer.fit_transform(trainInputs)
testFeatures = vectorizer.transform(testInputs)

# vocabbulary from the train data
print('vocab: ', vectorizer.get_feature_names_out()[:10])
# extracted features
print('features: ', trainFeatures.toarray()[:3][:10])

# unsupervised classification ( = clustering) of data

from sklearn.cluster import KMeans

unsupervisedClassifier = KMeans(n_clusters=2, random_state=0, n_init=1000)
unsupervisedClassifier.fit(trainFeatures)

computedTestIndexes = unsupervisedClassifier.predict(testFeatures)
computedTestOutputs0 = [labelNames[value] for value in computedTestIndexes]
computedTestOutputs1 = [labelNames[1-value] for value in computedTestIndexes]

from sklearn.metrics import accuracy_score

acc0 = accuracy_score(testOutputs, computedTestOutputs0)
acc1 = accuracy_score(testOutputs, computedTestOutputs1)
acc_maj = max(acc0, acc1)

# just supposing that we have the true labels
print("acc unsupervised: ", acc_maj * 100, "%")

trainOutputsNr = []
for i in trainOutputs:
    if i == "negative":
        trainOutputsNr.append(0)
    else: trainOutputsNr.append(1)

testOutputsNr = []
for i in testOutputs:
    if i == "negative":
        testOutputsNr.append(0)
    else: testOutputsNr.append(1)

regressor = linear_model.LogisticRegression(max_iter=1000)
regressor.fit(trainFeatures, trainOutputsNr)

computedValidationOutputs = regressor.predict(testFeatures)
accuracy = 0
for i in range(len(computedValidationOutputs)):
    if computedValidationOutputs[i] == testOutputsNr[i]:
        accuracy += 1

print("accuracy supervised", accuracy * 100 / len(computedValidationOutputs), "%")


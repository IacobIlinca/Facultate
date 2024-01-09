import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler


def readData():
    intrare = []
    iesire = []
    with open("data/iris.data", newline='') as file:
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

    indexes = np.random.permutation(len(intrare))

    inputs = [intrare[i] for i in indexes]
    outputs = [iesire[i] for i in indexes]

    return inputs, outputs


def prelucrare(inputs, outputs):
    np.random.seed(5)
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
    validationSample = [i for i in indexes if not i in trainSample]
    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]
    validationInputs = [inputs[i] for i in validationSample]
    validationOutputs = [outputs[i] for i in validationSample]

    scaler = StandardScaler()
    scaler.fit(trainInputs)
    normalisedTrainInputs = scaler.transform(trainInputs)
    normalisedTestInputs = scaler.transform(validationInputs)
    trainInputs = [list(x) for x in normalisedTrainInputs]
    validationInputs = [list(x) for x in normalisedTestInputs]
    return trainInputs, trainOutputs, validationInputs, validationOutputs






if __name__ == '__main__':
    u, t = readData()
    trainInputs, trainOutputs, validationInputs, validationOutputs = prelucrare(u, t)

    from sklearn.cluster import KMeans

    unsupervisedClassifier = KMeans(n_clusters=3, random_state=0, n_init=1000)
    unsupervisedClassifier.fit(trainInputs)
    labelNames = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]

    original_labels = np.argmax(trainOutputs, axis=1)

    kmeans_labels = unsupervisedClassifier.labels_
    cluster_labels = np.unique(kmeans_labels)  # Unique cluster labels returned by k-means

    mapping = {}  # Mapping dictionary to store the cluster-label mapping

    for cluster_label in cluster_labels:
        cluster_indices = np.where(kmeans_labels == cluster_label)  # Indices of samples in the cluster
        labels_in_cluster = original_labels[cluster_indices]  # Original labels of samples in the cluster
        majority_label = np.bincount(labels_in_cluster).argmax()  # Find the most frequent label
        mapping[cluster_label] = majority_label

    computedTestIndexes = unsupervisedClassifier.predict(validationInputs)
    computedTestOutputs = [mapping[value] for value in computedTestIndexes]

    from sklearn.metrics import accuracy_score

    # just supposing that we have the true labels
    validationOutputs = np.argmax(validationOutputs, axis=1)
    from sklearn.metrics import accuracy_score

    # just supposing that we have the true labels
    print("acc : ", accuracy_score(validationOutputs, computedTestOutputs)*100, "%")


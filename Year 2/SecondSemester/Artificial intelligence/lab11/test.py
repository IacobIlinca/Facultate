import numpy as np


def readData():
    intrareTest = []
    intrareTrain = []
    iesireTest = []
    iesireTrain = []
    with open("data/fer2013.csv", newline='') as file:
        for line in file:
            line = line.replace('\n', '')
            d = []
            features = line.split(",")
            if len(features) > 0:
                if features[2] == "Training":
                    iesireTrain.append(int(features[0]))
                    val = features[1].split(" ")
                    vectorValori = []
                    for e in val:
                        vectorValori.append(int(e))
                    intrareTrain.append(vectorValori)
                elif features[2] != "Usage":
                    iesireTest.append(int(features[0]))
                    val = features[1].split(" ")
                    vectorValori = []
                    for e in val:
                        vectorValori.append(int(e))
                    intrareTest.append(vectorValori)

    return intrareTrain, intrareTest, iesireTrain, iesireTest


from EmoPy.src.fermodel import FERModel
from pkg_resources import resource_filename

target_emotions = ['anger', 'fear', 'calm', 'sadness', 'happiness', 'surprise', 'disgust']
model = FERModel(target_emotions, verbose=True)

print('Reading data...')

intrareTrain, intrareTest, iesireTrain, iesireTest = readData()

emotion_index_map = {
    'anger': 0,
    'disgust': 1,
    'fear': 2,
    'happiness': 3,
    'sadness': 4,
    'surprise': 5,
    'calm': 6
}


acuuracy = 0
for i in range(0, len(intrareTest)-6000):
    print(i)
    a = model.predict_from_ndarray(np.array(intrareTest[i]))
    index = emotion_index_map[a]
    if iesireTest[i] == index:
        acuuracy += 1

print("accuracy: ", acuuracy * 100 / (len(iesireTest)-6000), "%")

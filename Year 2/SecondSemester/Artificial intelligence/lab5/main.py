import numpy as np

from Evaluation import Evaluation
from Parser import Parser


def evaluateLabelsFlowers():
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Flowers: ")
    parser: Parser = Parser("flowers.csv")
    evaluation: Evaluation = Evaluation()
    realLabels, computedLabels, labelNames = parser.read_classification_csv_flowers()
    acc, prec, recall = evaluation.evalClassificationV1(realLabels, computedLabels, labelNames)
    print(labelNames)
    print(' acc: ', acc)
    print(' precision: ', prec)
    print(' recall: ', recall)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def evaluateRegressionSport():
    print()
    print("Sport: ")
    parser: Parser = Parser("sport.csv")
    evaluation: Evaluation = Evaluation()
    realOutput, computedOutput = parser.read_regression_csv_sport()
    errors = evaluation.evalRegressionV1(realOutput, computedOutput)
    for i in range(errors.__len__()):
        print("For ", i, " coloumn ", " error: ", errors[i])

    print("Average error: ", sum(errors) / errors.__len__())
    loss = 0
    for instReal, instComp in zip(realOutput, computedOutput):
        for real, prob in zip(instReal, instComp):
            loss += (real - prob) * (real - prob)
    print("Loss regresie: ", loss)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def evaluateLabelsBinaryTxt():
    print()
    print("Binary classification: ")
    parser: Parser = Parser("probabilities-binary.txt", "true-binary.txt")
    evaluation: Evaluation = Evaluation()
    realLables, computedLabels = parser.read_classification_probabilities_txt()
    loss = 0
    for instReal, instComp in zip(realLables, computedLabels):
        for real, prob in zip(instReal, instComp):
            loss += (real - prob) * (real - prob)
    print("Loss binary classification: ", loss)

    realLabels2: list = []
    computedLabels2: list = []
    for inst in realLables:
        index = np.argmax(inst)
        realLabels2.append(index)
    for inst in computedLabels:
        index = np.argmax(inst)
        computedLabels2.append(index)
    acc, prec, recall = evaluation.evalClassificationV1(realLabels2, computedLabels2)
    print(' acc: ', acc)
    print(' precision: ', prec)
    print(' recall: ', recall)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def evaluateLabelsMultiClassTxt():
    print()
    print("Multi Class clasification")
    parser: Parser = Parser("probabilities-multi-class.txt", "true-multi-class.txt")
    evaluation: Evaluation = Evaluation()
    realLables, computedLabels = parser.read_classification_probabilities_txt()
    loss = 0
    for instReal, instComp in zip(realLables, computedLabels):
        for real, prob in zip(instReal, instComp):
            loss += (real - prob) * (real - prob)
    print("Loss Multi Class clasification: ", loss)
    realLabels2: list = []
    computedLabels2: list = []
    for inst in realLables:
        index = np.argmax(inst)
        realLabels2.append(index)
    for inst in computedLabels:
        index = np.argmax(inst)
        computedLabels2.append(index)
    acc, prec, recall = evaluation.evalClassificationV1(realLabels2, computedLabels2)
    print(' acc: ', acc)
    print(' precision: ', prec)
    print(' recall: ', recall)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def evaluateLabelsMultiTargetTxt():
    print()
    print("Multi Target classification")
    parser: Parser = Parser("probabilities-multi-target.txt", "true-multi-target.txt")
    evaluation: Evaluation = Evaluation()
    realLables, computedLabels = parser.read_classification_probabilities_txt()
    loss = 0
    for instReal, instComp in zip(realLables, computedLabels):
        for real, prob in zip(instReal, instComp):
            loss += (real - prob) * (real - prob)
    print("Loss Multi Target classification: ", loss)
    computedLabels2: list = []
    for inst in computedLabels:
        ex: list = []
        for prob in inst:
            if prob > 0.5:
                ex.append(1)
            else:
                ex.append(0)
        computedLabels2.append(ex)
    acc, prec, recall = evaluation.evalClassificationV1(realLables, computedLabels2)
    print(' acc: ', acc)
    print(' precision: ', prec)
    print(' recall: ', recall)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


if __name__ == "__main__":
    evaluateLabelsFlowers()
    evaluateRegressionSport()
    evaluateLabelsBinaryTxt()
    evaluateLabelsMultiClassTxt()
    evaluateLabelsMultiTargetTxt()

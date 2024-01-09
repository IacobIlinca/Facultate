class Evaluation:
    def evalClassificationV1(self, realLabels, computedLabels, labelNames=None):
        from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

        #cm = confusion_matrix(realLabels, computedLabels, labels=labelNames)
        acc = accuracy_score(realLabels, computedLabels)
        precision = precision_score(realLabels, computedLabels, average=None, labels=labelNames)
        recall = recall_score(realLabels, computedLabels, average=None, labels=labelNames)
        return acc, precision, recall

    def evalRegressionV1(self, realOutputs, computedOutputs):
        errors: list = []
        for r, c in zip(realOutputs, computedOutputs):
            error = sum(abs(re - co) for re, co in zip(r, c)) / len(r)
            errors.append(error)
        return errors
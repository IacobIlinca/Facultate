import csv
from typing import List, Tuple


class Parser:
    def __init__(self, computed_path: str, real_path: str = None):
        self.real_path = real_path
        self.computed_path = computed_path

    def read_classification_csv_flowers(self) -> Tuple[List[str], List[str], List[str]]:
        real_labels = []
        computed_labels = []
        with open(self.computed_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  # skip the header row
            for row in reader:
                real_labels.append(row[0])
                computed_labels.append(row[1])
        label_names = list(set(real_labels))
        return real_labels, computed_labels, label_names

    def read_classification_probabilities_txt(self) -> Tuple[List[List[float]], List[List[float]]]:
        real_labels = []
        computed_labels = []
        with open(self.computed_path, newline='') as file:
            for line in file:
                elems = line.strip().split()
                sample = [float(elem) for elem in elems]
                computed_labels.append(sample)

        if self.real_path is not None:
            with open(self.real_path, newline='') as file:
                for line in file:
                    elems = line.strip().split()
                    sample = [float(elem) for elem in elems]
                    real_labels.append(sample)
        return real_labels, computed_labels

    def read_regression_csv_sport(self) -> Tuple[List[List[int]], List[List[int]]]:
        real_output = []
        computed_output = []
        real_weight = []
        real_waist = []
        real_pulse = []
        computed_weight = []
        computed_waist = []
        computed_pulse = []
        with open(self.computed_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  # skip the header row
            for row in reader:
                real_weight.append(int(row[0]))
                real_waist.append(int(row[1]))
                real_pulse.append(int(row[2]))
                computed_weight.append(int(row[3]))
                computed_waist.append(int(row[4]))
                computed_pulse.append(int(row[5]))

        real_output.extend([real_weight, real_waist, real_pulse])
        computed_output.extend([computed_weight, computed_waist, computed_pulse])
        return real_output, computed_output

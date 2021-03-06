import numpy as np

import pandas as pd

class NeuralNetwork():

    def __init__(self):
        np.random.seed(1)

        self.synaptic_weights = 2 * np.random.random((3, 1)) - 1

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):

        for iteration in range(training_iterations):

            output = self.think(training_inputs)
            error = training_outputs - output
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))
            self.synaptic_weights += adjustments

    def think(self, inputs):

        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))

        return output

if __name__ == "__main__":

    neural_network = NeuralNetwork()

    print("Random synaptic weights: ")
    print(neural_network.synaptic_weights)

    training_inputs = pd.read_excel('data.xlsx', sheet_name = 'inputs', header=None).to_numpy()

    training_outputs = pd.read_excel('data.xlsx', sheet_name = 'outputs', header=None).to_numpy()

    neural_network.train(training_inputs, training_outputs, 100000)

    print("Synaptic weights after training: ")
    print(neural_network.synaptic_weights)

    newSituationInput = np.array([])

    for i in range(len(training_inputs[0])):
        A = str(input("Input " + str(i + 1) + ": "))
        newSituationInput = np.append(newSituationInput, A)

    print("New situation input data =", newSituationInput)
    print("Output data: ")
    print(neural_network.think(newSituationInput))

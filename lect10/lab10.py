import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


class Xor:

    def __init__(self):
        self.hidden_neuron1 = Neuron()
        self.hidden_neuron2 = Neuron()
        self.output_neuron = Neuron()
        self.predicted_output = 0

    def forward_model(self, inputs):
        h_output_1 = self.hidden_neuron1.forward(inputs)
        h_output_2 = self.hidden_neuron2.forward(inputs)
        hidden_layer_output = np.concatenate((h_output_1, h_output_2), axis=1)
        self.predicted_output = self.output_neuron.forward(hidden_layer_output)
        return self.predicted_output

    def backward_model(self, inputs, error):
        hidden_layer_output = np.concatenate((self.hidden_neuron1.output, self.hidden_neuron2.output), axis=1)
        d_predicted_output = error * sigmoid_derivative(self.predicted_output)
        error_hidden_layer = np.dot(d_predicted_output, self.output_neuron.weight().T)
        d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)
        self.output_neuron.backward(hidden_layer_output, d_predicted_output)
        d_hidden_layer_first, d_hidden_layer_second = np.split(d_hidden_layer, 2, axis=1)
        self.hidden_neuron1.backward(inputs, d_hidden_layer_first)
        self.hidden_neuron2.backward(inputs, d_hidden_layer_second)


class Neuron:

    def __init__(self):
        self.weights = np.random.uniform(size=(2, 1))
        self.bias = np.random.rand()
        self.output = 0
        self.lr = 0.1

    def forward(self, inputs):
        activation = np.dot(inputs, self.weights) + self.bias
        self.output = sigmoid(activation)
        return self.output

    def backward(self, inputs, output):
        self.weights = self.weights + inputs.T.dot(output) * self.lr
        self.bias += np.sum(output, axis=0, keepdims=True) * self.lr
        return self.weights, self.bias

    def weight(self):
        return self.weights


def main():
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1], [0, 1], [1, 0], [0, 0], [1, 1]])
    expected_output = np.array([[0], [1], [1], [0], [1], [1], [0], [0]])

    error = []
    predicted_output = []
    model = Xor()
    for i in range(4000):
        predicted_output = model.forward_model(inputs)
        error = expected_output - predicted_output
        model.backward_model(inputs, error)
    print(error)
    print(predicted_output)


if __name__ == '__main__':
    main()

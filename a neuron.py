import numpy
import matplotlib.pyplot


# A single Neuron

inputs = [1, 2, 3]
weights = [0.2, 0.8, -0.5]
bias = 2

output = (inputs[0]*weights[0] +
          inputs[1]*weights[1] +
          inputs[2]*weights[2] + bias)

print(output)

'''
this is a loop method that implements the above neural network without hardcoding it
output2 = bias

for i in range(len(inputs)):
    output2 += inputs[i] * weights[i]

print(output2)
'''

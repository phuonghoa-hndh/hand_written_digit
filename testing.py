import mnist
from k_nearest_neighbor import *
# Test K-NN algorithm (K = 1)


test_x = mnist.test_images().reshape(10000, 784).astype(int)
test_y = mnist.test_labels()

load_data("mnist.txt")
# Delete "#" to load experience
# load_data("experience.txt")
# load_data("advanced_experience.txt")

correct = 0
error = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0, len(test_x)):
    answer = predict_digit(test_x[i])
    if answer == test_y[i]:
        print("TEST" + str(i + 1) + ": PASSED.", end=" ")
        correct += 1
    else:
        print("TEST" + str(i + 1) + ": FAILED.", end=" ")
        error[test_y[i]] += 1

    print("Accuracy = " + str(correct / (i + 1) * 100) + " % ")

print("Error of each digit:", error)

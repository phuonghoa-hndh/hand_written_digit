import numpy as np

data, label = [], []


# Convert image -> 1D array
def get_vector(img):
    if img.__class__.__name__ == "ndarray":
        return img
    # resize image to 28x28 pixels
    print(img)
    img = img.resize((28, 28))
    # convert rgb to grayscale.
    img = img.convert('L')
    img = np.array(img).reshape(784)
    img = 255 - img
    return img


# Main part of K-NN Algorithm (K = 1)
def predict_digit(img):
    # Transform current image to 28 x 28 image into 1D array
    img = get_vector(img)
    min_distance = np.linalg.norm(img - data[0])
    predict = label[0]
    # Find the image have the smallest distance to img
    for i in range(1, len(data)):
        # Calculate distance using Euclid norm
        distance = np.linalg.norm(img - data[i])
        if distance < min_distance:
            min_distance = distance
            predict = label[i]

    return predict


# Load training data
def load_data(file_name):
    try:
        global data, label
        f = open(file_name, "rt")
        while True:
            line = f.readline().strip()
            if not line:
                f.close()
                return len(data)
            else:
                if len(line) == 1:
                    label.append(int(line.strip()))
                else:
                    # read whole array
                    for i in range(43):
                        line = line + f.readline()
                    line = line[1:len(line) - 2]
                    data.append(np.array([int(i) for i in line.split()]))
    except FileNotFoundError:
        return len(data)


# Write back some "experience"
def write_data(file_name, last_index):
    f = open(file_name, "at")
    for i in range(last_index, len(data)):
        f.write(str(label[i]) + "\n")
        f.write(str(data[i]) + "\n")
    f.close()

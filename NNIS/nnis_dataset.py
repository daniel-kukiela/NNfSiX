from keras.datasets import mnist

SAMPLES = 100

(X_train, y_train), (X_test, y_test) = mnist.load_data()

with open(f'mnist_{SAMPLES}.txt', 'w') as f:
    for i in range(SAMPLES):
        line = f'{y_train[i]} ' + ' '.join([str(n/255) for n in X_train[i].flatten()]) + ('\n' if i < SAMPLES - 1 else '')
        f.write(line)

from math import sqrt
import matplotlib.pyplot as plt
import numpy as np


def mandelbrot(a, b):
    r, x, y = 0, 0, 0
    k = 100
    while k > 0:
        x2 = x * x
        y2 = y * y
        xy = x * y
        r = sqrt(x2 + y2)
        if r > 2:
            return 1
        x = x2 - y2 + a
        y = 2 * xy + b
        k = k - 1
    return 0

def visualisation():
    x_min, x_max = -1.5, 2
    y_min, y_max = -1.5, 1.5
    n = 300

    y = y_min
    hx = (x_max - x_min) / n
    hy = (y_max - y_min) / n

    image = np.zeros((n, n), dtype=np.uint8)

    for j in range(0, n):
        x = x_min
        for i in range(0, n):
            color = mandelbrot(x, y)
            image[j, i] = color
            x = x + hx
        y = y + hy
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap="plasma")
    plt.title("Colored")
    plt.subplot(1, 2, 2)
    plt.imshow(image, cmap="gray")
    plt.title("Black")
    plt.show()

if __name__ == "__main__":
    visualisation()
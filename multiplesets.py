import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time, a, b, c):
    return a * time**2 + b * time + c

def main():
    coefficient_sets = [
        (1, 2, 20),
        (3, -1, 35),
        (2, 0, 45),
    ]

    time_values = np.linspace(0, 15, 50)

    for a, b, c in coefficient_sets:
        plt.plot(time_values, quadratic_model(time_values, a, b, c), label=f'set (a={a}, b={b}, c={c})')

    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Multiple sets')
    plt.show()

if __name__ == '__main__':
    main()

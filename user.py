import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time, a, b, c):
    return a * time**2 + b * time + c

def main():
    time_values = np.linspace(0, 10, 50)

    hc_coefficients = (15, 1, 30)

    a_user = float(input("Enter the value for coefficient a: "))
    b_user = float(input("Enter the value for coefficient b: "))
    c_user = float(input("Enter the value for coefficient c: "))
    user_coefficients = (a_user, b_user, c_user)

    temp_hard_coded = quadratic_model(time_values, *hc_coefficients)
    temp_user_input = quadratic_model(time_values, *user_coefficients)

    plt.plot(time_values, temp_hard_coded, label=f'Hard-coded (a={hc_coefficients[0]}, b={hc_coefficients[1]}, c={hc_coefficients[2]})')
    plt.plot(time_values, temp_user_input, label=f'User input (a={user_coefficients[0]}, b={user_coefficients[1]}, c={user_coefficients[2]})')

    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Quadratic equation with hard-coded and user input coefficients')
    plt.show()

if __name__ == '__main__':
    main()

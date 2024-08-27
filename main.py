import os

from Employee import Employee


def clear_terminal():
    # Check the OS and clear the terminal
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

if __name__ == "__main__":
    clear_terminal()


    emp_one = Employee("Simon", "Kaczmarek", "Senior Talent Management Consultant") #using string name, but this would be a unique # int
    emp_two = Employee("Anne", "Andersen", "Director, Finance")

    print(emp_two)
    # print()
    # print(emp_two)




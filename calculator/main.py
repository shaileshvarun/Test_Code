def main():
    print("Hello Shilesh!")


if __name__ == "__main__":
    main()

def add(num1, num2):
    return num1 + num2

def subtract(num1 ,num2):
    return num1 - num2

def multiply(num1 ,num2):
    return num1 * num2

def divide(num1 ,num2):
    return num1 / num2

print("Please select the inpuit - \n"
        "1. Addition \n"
        "2. Substraction \n"
        "3. Multiplication \n"
        "4. Division")
while True:

    select = input("Select required operation from (1/2/3/4) :")
    if select in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if select == '1':
            print(num1, "+", num2, "=", add(num1 ,num2))

        elif select == '2':
            print(num1, "-", num2, "=", subtract(num1 ,num2))

        elif select =='3':
            print(num1, "*", num2, "=", multiply(num1 ,num2))

        elif select =='4':
            print(num1, "/", num2, "=", divide(num1 ,num2))

        new_calculation = input("Are you want to do more calculation? (Yes/no) :")
        if new_calculation == "no":
            break

    else:
        print("invalid input")
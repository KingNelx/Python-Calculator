def main():
    print(" --- OPTIONS --- ")
    print(" 1. ADDITION ")
    print(" 2. SUBTRACTION ")
    print(" 3. MULTIPLICATION ")
    print(" 4. DIVISION ")

    while True:
        try:
            choice = int(input(" Select option (1-4): "))
            if choice not in [1, 2, 3, 4]:
                raise ValueError
            break
        except ValueError:
            print(" Invalid Selection, please select again! ")

    while True:
        try:
            input1 = int(input(" Enter 1st number: "))
            break
        except ValueError:
            print(" Invalid input, try again! ")

    while True:
        try:
            input2 = int(input(" Enter 2nd number: "))
            break
        except ValueError:
            print(" Invalid input, try again! ")

    if choice == 1:
        result = input1 + input2
        print(" The sum of: ", input1, "and", input2, "are: ", result)

    if choice == 2:
        result = input1 - input2
        print(" The difference of: ", input1, "and", input2, "are", result)

    if choice == 3:
        result = input1 * input2
        print(" The product of: ", input1, "and", input2, "are", result)


if __name__ == '__main__':
    main()

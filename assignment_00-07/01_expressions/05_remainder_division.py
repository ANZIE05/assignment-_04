def main():
    num1: int = int(input("Please enter an integer to be divided: "))  
    num2: int = int(input("Please enter an integer to divide by: "))  

    quotient: int = num1 // num2
    remainder: int = num1 % num2

    print(f"The result of this division is \033[1;3m{quotient}\033[0m with a remainder of \033[1;3m{remainder}\033[0m")

if __name__ == '__main__':
    main()
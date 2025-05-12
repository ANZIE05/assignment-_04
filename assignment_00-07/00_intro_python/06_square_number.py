def main():

    number = float(input("Type a number to see its square: "))

    square = number * number

    print(f"The square of \033[1;3m{number} is {square} \033[0m")

if __name__ == "__main__":
    main()
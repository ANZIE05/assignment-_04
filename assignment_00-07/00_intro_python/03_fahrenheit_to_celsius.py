def main():

    fahrenheit =float(input("Enter the temperature in Fahrenheit: "))

    celsius = (fahrenheit - 32) * 5.0 / 9.0

    print(f"Temperature: \033[1;3m{fahrenheit}F = {celsius}C \033[0m")

if __name__ == "__main__":
    main()
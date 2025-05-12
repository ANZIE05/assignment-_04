INCHES_IN_FEET = 12  # 1 foot = 12 inches

def main():
    feet = float(input("Enter number of feet: "))  
    inches = feet * INCHES_IN_FEET  
    print(f"This is {inches} inches!")

if __name__ == '__main__':
    main()
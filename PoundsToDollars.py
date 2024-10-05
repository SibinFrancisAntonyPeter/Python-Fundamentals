#10 Name your file: PoundsToDollars.py Write a program that asks the user to enter an amount in pounds (£)
    # and the program calculates and converts an amount in dollar ($)

pounds = float(input("Please enter an amount in pounds:"))
conversion_rate = 1.33
dollars = pounds * conversion_rate
print(f"£{pounds} are ${dollars:}")
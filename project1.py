# One Stop Insurance Company program to enter and calculate new insurance policy information for its customers
# Author : Uzoma Acholonu
# Dates : Mar 13 – 24, 2024

import datetime

# Default values
next_policy_number = 1944
basic_premium = 869.00
discount_additional_cars = 0.25
extra_liability_cost = 130.00
glass_coverage_cost = 86.00
loaner_car_cost = 58.00
hst_rate = 0.15
processing_fee = 39.99

# Lists for storing claims
claim_numbers = []
claim_dates = []
claim_amounts = []

valid_provinces = ['ON', 'QC', 'BC', 'AB', 'MB', 'SK', 'NS', 'NB', 'NL', 'PE', 'NT', 'NU', 'YT']

def calculate_insurance_premium(num_cars, extra_liability, glass_coverage, loaner_car):
    total_cost = num_cars * basic_premium  # Add basic premium for all cars
    if extra_liability == 'Y':
        total_cost += num_cars * extra_liability_cost
    if glass_coverage == 'Y':
        total_cost += num_cars * glass_coverage_cost
    if loaner_car == 'Y':
        total_cost += num_cars * loaner_car_cost
    return total_cost

def calculate_monthly_payment(total_cost, down_payment=0):
    total_cost += total_cost * hst_rate
    total_cost += processing_fee
    if down_payment > 0:
        total_cost -= down_payment
    monthly_payment = total_cost / 8
    return monthly_payment

def receipt(first_name, last_name, address, city, province, postal_code, phone_number,
            num_cars, extra_liability, glass_coverage, loaner_car, payment_method, down_payment):
    print("\n========== One Stop Insurance Company Receipt ==========")
    print("Date:", datetime.datetime.now().strftime("%Y-%m-%d"))
    print("Customer Information:")
    print("Name:", first_name.title(), last_name.title())
    print("Address:", address.title())
    print("City:", city.title())
    print("Province:", province.upper())
    print("Postal Code:", postal_code)
    print("Phone Number:", phone_number)
    print("\nPolicy Information:")
    print("Number of Cars Insured:", num_cars)
    print("Extra Liability Coverage:", extra_liability)
    print("Glass Coverage:", glass_coverage)
    print("Loaner Car Coverage:", loaner_car)
    print("Payment Method:", payment_method.title())
    if down_payment > 0:
        print("Down Payment:", "${:,.2f}".format(down_payment))
    print("\nInsurance Premium Calculation:")
    total_insurance_premium = calculate_insurance_premium(num_cars, extra_liability, glass_coverage, loaner_car)
    print("Total Insurance Premium (Pre-tax):", "${:,.2f}".format(total_insurance_premium))
    monthly_payment = calculate_monthly_payment(total_insurance_premium, down_payment)
    print("Monthly Payment:", "${:,.2f}".format(monthly_payment))
    print("\nPrevious Claims:")
    print(f"Claim Number\tClaim Date\tClaim Amount")
    print("---------------------------------")
    for i in range(len(claim_numbers)):
        print(f"{claim_numbers[i]}\t{claim_dates[i]}\t${claim_amounts[i]:,.2f}")
    print("\n=========================================================")
    print("................THANK YOU ---------------------------------")

# Main program loop
while True:
    # Collect user inputs
    first_name = input("Enter customer's first name: ")
    last_name = input("Enter customer's last name: ")
    address = input("Enter customer's address: ")
    city = input("Enter customer's city: ")
    province = input("Enter customer's province (abbreviated): ").upper()
    while province not in valid_provinces:
        print("Invalid province. Please enter a valid province.")
        province = input("Enter customer's province (abbreviated): ").upper()
    postal_code = input("Enter customer's postal code: ")
    phone_number = input("Enter customer's phone number: ")
    num_cars = int(input("Enter number of cars being insured: "))
    extra_liability = input("Extra liability coverage (Y/N): ").upper()
    glass_coverage = input("Glass coverage (Y/N): ").upper()
    loaner_car = input("Loaner car coverage (Y/N): ").upper()
    payment_method = input("Payment method (Full/Monthly/Down Pay): ").title()
    down_payment = 0
    if payment_method == 'Down Pay':
        down_payment = float(input("Enter the amount of the down payment: "))
    claim = input("Do you want to enter previous claim information (Y/N)? ").upper()
    if claim == 'Y':
        claim_number = input("Enter claim number: ")
        claim_date = input("Enter claim date (YYYY-MM-DD): ")
        claim_amount = float(input("Enter claim amount: "))
        claim_numbers.append(claim_number)
        claim_dates.append(claim_date)
        claim_amounts.append(claim_amount)

    # Display receipt
    receipt(first_name, last_name, address, city, province, postal_code, phone_number,
            num_cars, extra_liability, glass_coverage, loaner_car, payment_method, down_payment)

    # Update policy number for next customer
    next_policy_number += 1

    # Option to continue or exit loop
    cont = input("Enter another customer (Y/N)? ").upper()
    if cont != 'Y':
        print("Policy data has been saved.")
        break

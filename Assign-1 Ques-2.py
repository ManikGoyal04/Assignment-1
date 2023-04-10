def calculate_tax(gross_income, num_dependents):
    standard_deduction = 10000
    dependent_deduction = 3000
    tax_rate = 0.20

    taxable_income = gross_income - standard_deduction - (num_dependents * dependent_deduction)
    tax = taxable_income * tax_rate

    return round(tax, 2)

gross_income = float(input("Enter your gross income: "))
num_dependents = int(input("Enter the number of dependents: "))

tax = calculate_tax(gross_income, num_dependents)

print(f"Your income tax is ${tax}")

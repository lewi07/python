# Ask the user for their annual income
income = float(input("Enter your annual income (€): "))

# Initialize the total tax and the tax rate
taxes = 0
tax_rate = 0

# Calculate the tax based on income brackets
if income < 12450:
    tax_rate = 19
    taxes = income * 0.19
elif income < 20200:
    tax_rate = 24
    taxes += (12450 * 0.19)
    taxes += (income - 12450) * 0.24
elif income < 35000:
    tax_rate = 30
    taxes += (12450 * 0.19)
    taxes += (7750 * 0.24)
    taxes += (income - 20200) * 0.30
elif income < 60000:
    tax_rate = 37
    taxes += (12450 * 0.19)
    taxes += (7750 * 0.24)
    taxes += (14800 * 0.30)
    taxes += (income - 35000) * 0.37
elif income < 300000:
    tax_rate = 45
    taxes += (12450 * 0.19)
    taxes += (7750 * 0.24)
    taxes += (14800 * 0.30)
    taxes += (25000 * 0.37)
    taxes += (income - 60000) * 0.45
else:
    tax_rate = 47
    taxes += (12450 * 0.19)
    taxes += (7750 * 0.24)
    taxes += (14800 * 0.30)
    taxes += (25000 * 0.37)
    taxes += (240000 * 0.45)
    taxes += (income - 300000) * 0.47

# Calculate the net income after tax
net_income = income - taxes

# Display the results
print(f"a) The applicable tax rate is: {tax_rate}%")
print(f"b) The amount to be paid in taxes is: {taxes:.2f}€")
print(f"c) The net income received after taxes is: {net_income:.2f}€")
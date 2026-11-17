
import csv

try:
    with open("employees.csv", "r") as file:
        reader = csv.DictReader(file)
        print("\n--- PAYROLL SUMMARY ---")

        for employee in reader:
            name = employee["Name"]
            basic = float(employee["Basic"])
            allowance = float(employee["Allowance"])
            deduction = float(employee["Deduction"])

            gross = basic + allowance
            net = gross - deduction

            print("\nEmployee:", name)
            print("Gross Salary:", gross)
            print("Deduction:", deduction)
            print("Net Salary:", net)

except FileNotFoundError:
    print("CSV file not found.")

except ValueError:
    print("Invalid salary data.")

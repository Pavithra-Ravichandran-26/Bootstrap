employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))


gross_salary = basic_salary + allowances


tax = gross_salary * 0.10

final_salary = gross_salary - tax

print("\n==============================")
print("       EMPLOYEE SALARY SLIP")
print("==============================")
print(f"Employee Name : {employee_name}")
print(f"Basic Salary  : Rs.{basic_salary:.2f}")
print(f"Allowances    : Rs.{allowances:.2f}")
print(f"Gross Salary  : Rs.{gross_salary:.2f}")
print(f"Tax (10%)     : Rs.{tax:.2f}")
print(f"Final Salary  : Rs.{final_salary:.2f}")
print("==============================")
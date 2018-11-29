def cal_gross_pay(pay_rate,hours_works):
    gross_pay= pay_rate*hours_works
    return gross_pay

emp_pay_rate=float(input("enter the employee pay rate:"))
emp_hours=float(input("enter the hours worked by employee:"))
emp_gross_pay=cal_gross_pay(emp_pay_rate,emp_hours)
print("the employee's gross pay is "+format(emp_gross_pay,".2f"))
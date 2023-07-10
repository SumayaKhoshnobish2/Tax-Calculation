flat_tax = 0.2
deduction = 10000
d_deduction = 2000


def message():
    print("Tax Calculator")


def user_input():
    name = input("Please enter your name: ")
    dependants = int(input("Please enter the number of dependants: "))
    gross_income = float(input("Please enter gross income: "))
    print("Hello, " + name)
    print("You have entered " + str(dependants) + " dependants")
    print("You have entered the gross income of: $" + str('%.2f' % gross_income))
    return name, dependants, gross_income


def cal_tax(gross_income1, dependant):
    taxable_income = gross_income1 - (deduction + (d_deduction * dependant))
    income_tax = taxable_income * flat_tax
    print("your taxable in come is: $ " + str('%.2f' % taxable_income))
    print("And your income tax is: $" + str('%.2f' % income_tax))


if __name__ == '__main__':
    message()
    your_name, depend, gross_inc = user_input()
    cal_tax(gross_inc, depend)

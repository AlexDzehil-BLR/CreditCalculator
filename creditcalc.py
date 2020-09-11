import math
import argparse

# print('Enter the credit principal:')
# credit = int(input())
# print('What do you want to calculate?')
# print('type "m" - for the number of months,')
# print('type "p" - for the monthly payment:')
# want = input()
# if want == 'm':
#     print('Enter the monthly payment:')
#     monthly_payment = int(input())
#     payment = credit / monthly_payment
#     payment2 = credit // monthly_payment
#     payment1 = credit // monthly_payment
#     pay_pay = credit % monthly_payment
#     if pay_pay > 0:
#         payment1 += 1
#         print('It takes ' + str(payment1) + ' months to repay the credit')
#     else:
#         print('It takes ' + str(payment2) + ' month to repay the credit')
# elif want == 'p':
#     print('Enter the number of months:')
#     m_payment = int(input())
#     month = credit / m_payment
#     month1 = credit % m_payment
#     periods = m_payment - 1
#     c = credit // m_payment
#     e = c * (m_payment - 1)
#     payment = credit - e
#     if month1 > 0:
#         last = credit - periods * payment
#         print('Your monthly payment = ' + str(payment) +
#               ' with last monthly payment = ' + str(last) + '.')
#     else:
#         print('Your monthly payment = ', str(month))
# print('What do you want to calculate?')
# print('type "n" for number of monthly payments')
# print('type "a" for number of monthly payments')
# print('type "p" for number of monthly payments')
#
# want = input()
#
# if want == 'n':
#     print('Enter the credit principal:')
#     credit = int(input())
#     print('Enter the monthly payment:')
#     m_payment = int(input())
#     print('Enter the credit interest:')
#     credit_interest = float(input())
#
#     interest_rate = credit_interest / 1200
#     log_a = 1 + interest_rate
#     log_b = m_payment / (m_payment - interest_rate * credit)
#     n = math.log(log_b, log_a)
#     period = math.ceil(n)
#     age = period // 12
#     age1 = period % 12
#     if age == 0:
#         print(f'It will take {age1} months to repay this credit!')
#     elif age1 == 0:
#         print(f'It will take {age} year instead to repay this credit!')
#     elif age != 0 and age1 != 0:
#         print(f'It will take {age} years and {age1} months to repay this credit!')
# elif want == 'a':
#     print('Enter the credit principal:')
#     credit = int(input())
#     print('Enter the number of periods:')
#     n_periods = int(input())
#     print('Enter the credit interest:')
#     credit_interest = float(input())
#     i = credit_interest / 100 / 12
#     i_1 = i * (1 + i) ** n_periods
#     i_2 = (1 + i) ** n_periods - 1
#     a = math.ceil(credit * (i_1 / i_2))
#     print(f'Your monthly payment = {a}!')
#
# elif want == 'p':
#     print('Enter the annuity payment:')
#     annuity_pay = float(input())
#     print('Enter the number of periods:')
#     n_periods = int(input())
#     print('Enter the credit interest:')
#     credit_interest = float(input())
#     i = credit_interest / 100 / 12
#     i_1 = i * (1 + i) ** n_periods
#     i_2 = (1 + i) ** n_periods - 1
#     p = round(annuity_pay / (i_1 / i_2))
#     print(f'Your credit principal = {p}!')

parser = argparse.ArgumentParser()

parser.add_argument('--type', type=str)
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--payment', type=int)
parser.add_argument('--interest', type=float)

args = parser.parse_args()


def dif(principal, periods, interest):
    # месячная ставка float
    interest_nominal = interest / 1200

    # переплата за кредит
    a = 0
    # дифференцированный платеж
    for m in range(1, periods + 1):
        diff = principal / periods + interest_nominal * (principal - (principal * (m - 1) / periods))
        print(f'Month {m}: payment is {math.ceil(diff)}')
        a += math.ceil(diff)
    a_p = a - principal
    print()
    print(f'Overpayment = {a_p}')


def annuity_pay(principal, periods, interest):  #месячный платеж
    # месячный платеж
    interest_nominal = interest / 1200
    i_1 = interest_nominal * (1 + interest_nominal) ** periods
    i_2 = (1 + interest_nominal) ** periods - 1
    a = math.ceil(principal * (i_1 / i_2))

    a_p = math.ceil(periods * a - principal)

    print(f'Your monthly payment = {a}!')
    print(f'Overpayment = {a_p}')

def annuity_per(principal, payment, interest):   #количество месяцев
    interest_rate = interest / 1200
    log_a = 1 + interest_rate
    log_b = payment / (payment - interest_rate * principal)
    n = math.log(log_b, log_a)
    periods = math.ceil(n)
    age = periods // 12
    age1 = periods % 12
    a_p = periods * payment - principal
    if age == 0:
        print(f'It will take {age1} months to repay this credit!')
        print()
        print(f'Overpayment = {a_p}')
    elif age1 == 0:
        print(f'It will take {age} year instead to repay this credit!')
        print()
        print(f'Overpayment = {a_p}')
    elif age != 0 and age1 != 0:
        print(f'It will take {age} years and {age1} months to repay this credit!')
        print()
        print(f'Overpayment = {a_p}')

def annuity_prn(payment, periods, interest):   #сумма кредита
    i = interest / 100 / 12
    i_1 = i * (1 + i) ** periods
    i_2 = (1 + i) ** periods - 1
    p = round(payment / (i_1 / i_2))
    print(f'Your credit principal = {p}!')


if args.type == None:
    print('Incorrect parameters')
elif args.type == 'diff':
    if args.payment != None:
        print('Incorrect parametrs')
    elif args.principal == None or args.principal < 0:
        print('Incorrect parametrs')
    elif args.periods != None and args.periods < 0:
        print('Incorrect parametrs')
    elif args.interest == None or args.interest < 0:
        print('Incorrect parametrs')
    else:
        print(dif(args.principal, args.periods, args.interest))
elif args.type == 'annuity':
    if args.payment == None and args.principal != None and args.principal > 0 and args.periods != None and args.periods > 0 and args.interest != None and args.interest > 0:
        print(annuity_pay(args.principal, args.periods, args.interest))
    elif args.periods == None and args.principal != None and args.principal > 0 and args.payment != None and args.payment > 0 and args.interest != None and args.interest > 0:
        print(annuity_per(args.principal, args.payment, args.interest))
    elif args.principal == None and args.periods != None and args.periods > 0 and args.payment != None and args.payment > 0 and args.interest != None and args.interest > 0:
        print(annuity_prn(args.payment, args.periods, args.interest))
    else:
        print('Incorrect parametrs')

def main():
    income = int(input('Enter your income: '))
    print()

    if income <= 11000:
        tax = 0.1 * income
        bracket = '10%'
    elif income <= 44725:
        tax = 0.12 * (income - 11000) + 1100
        bracket = '12%'
    elif income <= 95375:
        tax = 0.22 * (income - 44725) + 5147
        bracket = '22%'
    elif income <= 182100:
        tax = 0.24 * (income - 95375) + 16290
        bracket = '24%'
    elif income <= 231250:
        tax = 0.32 * (income - 180100) + 37104
        bracket = '32%'
    elif income <= 578125:
        tax = 0.35 * (income - 231250) + 52832
        bracket = '35%'
    else:
        tax = 0.37(income - 578125) + 174238.2
        bracket = '37%'
    print('An income of', format(income, ',d'), 'places you in the', bracket, 'income bracket')
    print('the US federal tax on income of', format(income, ',d'), 'is', tax, '.')

main()
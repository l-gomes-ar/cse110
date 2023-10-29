# Prompt the user for a rate of 1-10 on the following:
print('Please, provide a rate of 1-10 on the following:')
loan = float(input('How large is the loan? '))
credit = float(input('How good is your credit history? '))
income = float(input('How high is your income? '))
down_pay = float(input('How large is your down payment? '))
can_loan = False

if loan >= 5:
    if credit >= 7 and income >= 7:
        can_loan = True
    elif credit >= 7 or income >= 7:
        if down_pay >= 5:
            can_loan = True
elif loan < 4:
    if credit >= 4:
        if income >= 7 or down_pay >= 7:
            can_loan = True
        elif income >= 4 and down_pay >= 4:
            can_loan = True
            
if can_loan:
    print('Decision: Yes')
else:
    print('Decision: No')
loan = int(input('How much money do you want to borrow? '))
income = int(input('How much money do you make? '))
credit_score = int(input('What is your credit score? (from 0 to 100) '))

if loan <= 1000:
    if income >= loan * 2 and credit_score >= 10 <= 100:
        eligible_loan = True
    else:
        eligible_loan = False

elif loan >= 1001 <= 2000:
    if income >= loan * 3 and credit_score >= 41 <= 100:
        eligible_loan = True
    else:
        eligible_loan = False

elif loan >= 2000:
    if income >= loan * 4:
        if credit_score >= 71 <= 100:
            eligible_loan = True

if credit_score > 100:
    eligible_loan = False
    print('Your credit score is incorrect, please double-check it')
    exit()

if eligible_loan:
    print('Good to go')
else:
    print('You are ineligible, sorry')
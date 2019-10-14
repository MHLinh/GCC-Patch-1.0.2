# modify this function, and create other functions below as you wish
def question01(initialLevelOfDebt, interestPercentage, repaymentPercentage):
    initialLevelOfDebt = int(input())
    interestPercentage = int(input())
    repaymentPercentage = int(input())

    totalPayment = int(0)
    currentDebt = int(initialLevelOfDebt)
    deposit = int(initialLevelOfDebt*0.1)
    repayment = int(initialLevelOfDebt*repaymentPercentage/100)

    if repayment < 50:
        repayment = 50

    while currentDebt > 0:
        currentDebt = currentDebt + currentDebt*interestPercentage/100
        if currentDebt < repayment:
            totalPayment += int(currentDebt)
            currentDebt = 0
            break
        else:
            currentDebt -= int(repayment)
            totalPayment += int(repayment)
    totalPayment += deposit
    answer = int(totalPayment)
    return answer

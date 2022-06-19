def FindVerificationNumber(signumber):
    sum=0
    for i in range(len(signumber)):
        sum+=signumber[i]**2
    return sum%10

signature_number = list(map(int, input().split(" ")))
print(FindVerificationNumber(signature_number))
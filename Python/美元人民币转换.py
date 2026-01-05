MoneyStr = input()

if MoneyStr[0] == '$' or MoneyStr[0:3] == 'USD':
    # 美元转人民币
    if MoneyStr[0] == '$':
        amount = eval(MoneyStr[1:])
        RMB = amount * 6.78
        print("&%.2f" % RMB)
    else:  # USD格式
        amount = eval(MoneyStr[3:])
        RMB = amount * 6.78
        print("RMB%.2f" % RMB)
        
elif MoneyStr[0] == '&' or MoneyStr[0:3] == 'RMB':
    # 人民币转美元
    if MoneyStr[0] == '&':
        amount = eval(MoneyStr[1:])
        USD = amount / 6.78
        print("$%.2f" % USD)
    else:  # RMB格式
        amount = eval(MoneyStr[3:])
        USD = amount / 6.78
        print("USD%.2f" % USD)
        
else:
    print("Error")

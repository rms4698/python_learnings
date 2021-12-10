import random
feeling = "HAPPY"
quotes = []
if feeling == "HAPPY":
    with open('/Quotes/happy.txt', 'r') as f:
        print("File opened")
        quotes = f.read().strip('\n')
elif feeling == "SAD":
    with open('/Quotes/sad.txt', 'r') as f:
        quotes = f.read().strip('\n')
elif feeling == "UNLOVED":
    with open('/Quotes/sad.txt', 'r') as f:
        quotes = f.read().strip('\n')
print(quotes)



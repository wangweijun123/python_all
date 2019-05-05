import math

limit = 40

print(math.sqrt(limit))

print(math.floor(math.sqrt(limit)))


num = 0
while(num*num <= 40):
    num += 1

print(num-1)



headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
total = 0;

for item in headlines:
    news_ticker += item + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break;
print(str(len(news_ticker)) + news_ticker)
















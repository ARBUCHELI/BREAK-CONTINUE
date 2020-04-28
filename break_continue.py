# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""  #Initialization of empty string

# write your loop here
for headline in headlines: #Looping through the list
    news_ticker = news_ticker+headline+" " #Adding headlines from the list and inserting a space in between each headline.
    if len(news_ticker) >= 140:  #Condition to check if the len of the string is >= 140
        news_ticker=news_ticker[:140] #Slicing the string to output only 140 characters
        break

print(news_ticker)
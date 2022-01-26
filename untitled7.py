month = ("January","feb","march","april","june","july","august","september","octobur","november","december")

profit = (20000,45000,78000,28000,12000,90000,320000,890000,290000,19999,5999999,10000000)

max_profit = max(profit)
max_profit_index = profit.index(max_profit)
print(max_profit_index)

max_profit_month = month[max_profit_index]
print("The maximum profit of "  + str(max_profit)+ " was recorded in the mont of" + str(max_profit_month))


min_profit = min(profit)
min_profit_index = profit.index(min_profit)
print(min_profit_index)

min_profit_month = month[min_profit_index]
print("The minimum profit of " +str(min_profit)+"was recorded in the month of "+str(min_profit_month))
    
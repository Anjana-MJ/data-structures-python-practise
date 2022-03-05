"""

Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this

"""

all_month_expense = [2200, 2350, 2600, 2130, 2190]

# 1st case
res = all_month_expense[1] - all_month_expense[0]
print("Dollars spent extra on February compare to January is", res)

# 2nd case
first_quarter_expenses = all_month_expense[0] + all_month_expense[1] + all_month_expense[2]
print("The expense in first quarter of the year is", first_quarter_expenses)

# 3rd case
print("Exactly 2000 dollars spent in any month...? ", 2000 in all_month_expense)


# 4th case
all_month_expense.append(1980)
print "Monthly expense from jan to june are", all_month_expense

# 5th case
all_month_expense[3] = all_month_expense[3] - 200
print "Monthly expense from jan to june after updating april month expense are ", all_month_expense

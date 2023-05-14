import os
import csv

#creating variable
total_months = 0
total_pl = 0
pl_change =0 
previous_value =0
avg_change_list = [] # to keep track of all the P/L i.e current day - prev day
avg_change_list2 = []

csvpath = os.path.join("..", 'Resources', 'budget_data.csv')

with open (csvpath , "r") as csvfile:
    csv_contents = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvfile)
    # print(f"Header: {csv_header}")
    for row in csv_contents:
       #print(row)
       
       #calculates the total number of months by skipping the  first row and
       # then incrementing the variable by 1 for each row

       total_months = total_months + 1
       total_pl = total_pl + float(row[1])
       pl_change = float(row[1]) - previous_value
       previous_value = float(row[1])
       avg_change_list.append(pl_change)
       x = [row[0],pl_change]
       avg_change_list2.append(x)
       #creating two list : the avg_change_list, appends all the difference in p/l for each month
       #  and the second avg_change_list2 appends the month and avg change into one list.

       #avg_change_list.pop(0)


print("Financial Analysis")
print("--------------------------")
print(f'Total Months: ', total_months)
print(f'Total: $', total_pl )

   
      
avg_change_list.pop(0) #  popping this value as i do not have to include the first value it in my sum of average 

# print( avg_change_list)
# print(avg_change_list2) 

avg_change_in_pl = round((sum(avg_change_list))/(total_months-1),2)
# print(total_pl)

# print(f'Total Months are ', total_months)
# print(avg_change_in_pl)
print(f'Average Change: $', avg_change_in_pl)

max_value= max(avg_change_list2, key=lambda y : y[1]) #using lambda function for nestloops to find max 
#and min function,this basically finds the max value by going through of the nested list and checking on the 1st index.
min_value= min(avg_change_list2, key=lambda y : y[1])
print(f'Greatest Increase in Profits ', max_value) 
print(f'Greatest Decrease in Profits' , min_value)

budget_text = os.path.join("budget_data.txt")
with open (budget_text, "w") as outputfile:
    outputfile.write("Financial Analaysis\n")
    outputfile.write("Total Months : "+ str(total_months)+ "\n")
    outputfile.write("Total : $" + str(total_pl)+ "\n")
    outputfile.write("Average Change : $" + str(avg_change_in_pl)+ "\n")
    outputfile.write("Greatest Increase in Profits : $" + str( max_value) + "\n")
    outputfile.write("Greatest Decrease in Profits : $" + str( min_value) + "\n")
    

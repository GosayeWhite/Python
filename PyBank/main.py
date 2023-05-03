# import file
from pathlib import Path
import csv
# Join paths

budget_data= Path("Resources","budget_data.csv")

#open to read csv file
with open(budget_data) as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=",")
    csv_header =next(csvfile)
#skip heasder row




    #set months and profit
    months=[]
    profit=[]

    #find total months

    for rows in csv_reader:
        months.append(rows[0])
        profit.append(int(rows[1]))

    total_months= len(months)
    #find the net profit and loss
    revenue_change=[]
    for x in range(len(profit)-1):
        revenue_change.append((int(profit[x+1]-profit[x])))

    #calculate average
        revenue_average=round(sum(revenue_change)/len(revenue_change),2)


    #find greatest increase and decrease in revenue
    greatest_increase=max(revenue_change)
    greatest_decrease=min(revenue_change)

    #get dates of max and min revenues
    max_date = str(months[revenue_change.index(max(revenue_change))+1])
    min_date = str(months[revenue_change.index(min(revenue_change))+1])
   
    output=("Financial Analysis \n"
           f'--------------------------------- \n'
           f'Total Months:{total_months} \n'
           f'Total: $ {sum(profit)} \n'
           f'Average Change ${revenue_average} \n'
           f'  Greatest increase Profit: Date {max_date} (${greatest_increase}) \n'
           f'Greatest Decrease Profit: Date {min_date}  (${greatest_decrease})')
  
print(output)
csvpath=Path("Analysis", 'Final Analysis.txt')
print(csvpath)
with open(csvpath,"w") as textfile:
    textfile.write(output)
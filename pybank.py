import csv
import os 

dirname = os.path.dirname(__file__)
file_to_load = os.path.join(dirname, "Resources", "budget_data.csv")

total_months = 0
total_profit = 0
net_change_list = []
greatest_increase = 0
greatest_decrease= 0
greatest_decrease_date = ""
greatest_increase_date = ""

with open(file_to_load) as data:
    reader = csv.reader(data)

    header = next(reader)

    prev_net = 0

    for row in reader:
        total_months = total_months + 1
        total_profit = total_profit + int(row[1])
        current_month = row[0]
        current_value = int(row[1])

        if total_months > 1:
            net_change = current_value - prev_net
            net_change_list.append(net_change)

            if net_change > greatest_increase:
                #change greatest increase number to net_change
                greatest_increase = net_change
                greatest_increase_date = current_month

            if net_change < greatest_decrease:
                greatest_decrease = net_change
                greatest_decrease_date = current_month

        prev_net = int(row[1])
        
net_monthly_avg = sum(net_change_list)/len(net_change_list)

print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${round(net_monthly_avg, 2)}")
print(f"Greatest Increase: ${greatest_increase}")
print(f"Greatest Month Increase: {greatest_increase_date}")
print(f"Greatest Decrease: ${greatest_decrease}")
print(f"Greatest Month Decrease: {greatest_decrease_date}")
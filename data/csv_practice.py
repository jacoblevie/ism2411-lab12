#You've now completed a full ETL pipeline: read a CSV, transform the data, write a new CSV. How does this compare to doing the same task in Excel? What can Python do that Excel can't do easily, and vice versa?

# This task is different than doing the same in excel, since we can iterate over and filter easily with one line functions to manipulate and transoform data. This is much faster and easier than excel, although excel would be more intuitive to someone relatively new to Python like myself.

#Exercise 8 showed you append mode. Think of a real business process that would benefit from an append-mode log file — describe it and explain why append mode is the right tool.

# Append mode could be very useful for making logs of the stock price of your business over time, including the time with which as well as what the price was so you can see historic performance of your company.

import csv
from datetime import datetime

# Exercise 1: setup the files

# Exercise 2

print("Exercise 2")
with open("data/sales.csv") as sales:
    reader = csv.reader(sales)
    for row in reader:
        print(row)

# Exercise 3

print("Exercise 3")
with open("data/sales.csv") as sales:
    reader = csv.reader(sales)
    print(next(reader))
    print("-----------------------")
    for row in reader:
        print(row)


# Exercise 4

print("Exercise 4")
with open("data/sales.csv") as sales:
    reader = csv.reader(sales)
    next(reader)
    for row in reader:
        print(f"{row[0]}: {row[1]} units x ${row[2]} = ${float(row[1]) * float(row[2])}")

# Exercise 5

print("Exercise 5")
count = 0
with open("data/sales.csv") as sales:
    reader = csv.reader(sales)
    next(reader)
    with open(("data/cleaned.csv"), "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["product", "quantity", "price"])
        for row in reader:
            if float(row[1])*float(row[2]) > 100:
                writer.writerow(row)
                count += 1 

print(count)



# Exercise 6

print("Exercise 6")
total_revenue = 0
with open("data/sales.csv") as sales:
    reader = csv.DictReader(sales)
    for row in reader:
        revenue = float(row["price"]) * float(row["quantity"])
        print(revenue)
        total_revenue += revenue

# The totals are the same from exercise 4. The 2 approaches vary in how they use the header data. If I wanted to print the contents of the header with the data, I'd use reader, or if the headers weren't uniquely named it would be the same to index with it. If they have unique names, DictReader can help me access the data by name for each row, which is especially useful if rows get jumbled.

# Exercise 7

print("Exercise 7")

product_summary = {}
with open("data/sales.csv") as sales:
    reader = csv.DictReader(sales)
    for row in reader:
        product = row["product"]
        revenue = float(row["price"]) * float(row["quantity"])
        product_summary[product] = revenue

print(product_summary)

# Exercise 8

print("Exercise 8")
timestamp = datetime.now()
with open("data/run_log.txt", "a") as log:
    log.write(f"Time: {timestamp}, Revenue: {total_revenue}\n")
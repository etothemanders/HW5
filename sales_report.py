"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.

"""
# Suggested Improvements
# 1. Create some functions, like generate_sales_report() instead of
#    all of the code in main.  This will make it easier to read, reuse, and organize.
# 2. Use tuple assignment when parsing each line of the csv.  Tuple assignment is concise and cool.
# 3. Use a dictionary instead of processing the data as two lists. This will make the script faster
#    when the list of salespeople is very long.
# 4. Make the report file a command line argument that you feed in when running the script vs. 
#    hard-coding.  This will make the script more flexible.
# 5. The dollar total for each sales order seems important.  Maybe we should also report
#    the amount of money each salesperson is generating, too.  And/or also the 
#    (order total/number of melons) for a measure of "sales efficiency".

def main():
    salespeople = []
    melons_sold = []

    f = open("sales_report.csv")
    for line in f:
        line = line.rstrip()
        entries = line.split(",")
        salesperson = entries[0]
        melons = int(entries[2])

        if salesperson in salespeople:
            position = salespeople.index(salesperson)
            melons_sold[position] += melons
        else:
            salespeople.append(salesperson)
            melons_sold.append(melons)


    for i in range(len(salespeople)):
        print "%s sold %d melons" % (salespeople[i], melons_sold[i])



if __name__ == "__main__":
    main()

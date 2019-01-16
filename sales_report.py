"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

# salespeople = [] #initializes the list of salespeople
# melons_sold = [] #initializes the list of melons_sold

# f = open("sales-report.txt") #opens file
# for line in f: #runs through each line of the file
#     line = line.rstrip() #removes the space on right
#     entries = line.split("|") #splits line at pipe, creates a list of words
#     salesperson = entries[0] #salesperson is the string in entries at index 0
#     melons = int(entries[2]) #melons is the integer in entries at index 2

#     if salesperson in salespeople: #checks if salesperson is already added to salespeople list of strings
#         position = salespeople.index(salesperson) #finds the index at which salesperson is in the list of salespeople
#         melons_sold[position] += melons #finds the value which is kept at the index and appends the value of melons to it
#     else: #if salesperson is not included in salespeople list
#         salespeople.append(salesperson) #appends salesperson to the list of strings (salespeople)
#         melons_sold.append(melons) #appends updated value of soldmelons to the list of integers


# for i in range(len(salespeople)): #loops through indexes of salespeople
#     print("{} sold {} melons".format(salespeople[i], melons_sold[i])) #prints the string with formatted values at index i


f = open("sales-report.txt") #opens file

sales_report_dict = {}


for line in f:
    line = line.rstrip() #removes the space on right
    entries = line.split("|") #splits line at pipe, creates a list of words

    salesperson = entries[0]
    melons_sold = int(entries[2])
    sales_report_dict[salesperson] = sales_report_dict.get(salesperson, 0) + melons_sold
   
for every_salesperson in sales_report_dict: 
    print("{} sold {} melons".format(every_salesperson, sales_report_dict[every_salesperson]))
#this is creating the variable log_file and assigning it to the text document 'um-server-01.txt'
#using the open function to link it to the variable.
log_file = open("um-server-01.txt")

# creating a function called sales_reports with a parameter of log_file
#colon signifys code block
def sales_reports(log_file):
    # looping through the text in log file and placing them into a variable called line
    for line in log_file:
        #removing any characters at the end of the string '\n'
        line = line.rstrip()
        #isolating the day from the day from information using its index
        day = line[0:3]
        #creating a condition where one can pick which day to print by creating a string comparison
        if day == "Mon":
            #printing the line but since is indented is printed when above condition is met
            print(line)

#logging the function on log_file
sales_reports(log_file)

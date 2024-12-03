"""
Author - Abhishek Singh Chauhan
Date - 25 Aug 2024
Purpose - to write the data on my expense logs...


"""
import csv
import datetime
from prettytable import PrettyTable
import pandas as pd

def date():
    """
    return the current day date...
    """
    return datetime.date.today()

def writedata(file):
    """
    write the data to the file.. by asking the user of the fields.. in the csv file... 
    """
    csv_file = file
    currency = '₹'
    getDate = date().strftime("%d/%m/%Y")
    data = f'{getDate}'
    amount = input("Enter the price of the item :")
    disription = input("Enter the description of expense !:")
    datalist = [getDate,amount,currency,disription]

    write = csv.writer(csv_file)
    write.writerow(datalist)
    print("Data appended succesfully")

def calculate_total(file):
    """
    Calculate and display the total expenses logged in the file.
    """
    file.seek(0)
    csv_file = file
    data = csv.DictReader(csv_file)
    
    total_expenses = 0
    for entry in data:
        total_expenses += float(entry["Amount"])
    
    print(f"Total Expenses: ₹{total_expenses:.2f}")



def filter_by_date_range(file):
    """
    Filter and display expenses within a user-specified date range.
    """
    file.seek(0)
    csv_file = file
    data = csv.DictReader(csv_file)
    
    start_date = input("Enter the start date (dd/mm/yyyy): ")
    end_date = input("Enter the end date (dd/mm/yyyy): ")
    
    # Convert input dates to datetime objects
    try:
        start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Please try again.")
        return
    
    # Create PrettyTable for filtered data
    table = PrettyTable()
    table.field_names = ["Date", "Amount", "Currency", "Description"]
    
    for entry in data:
        entry_date = datetime.datetime.strptime(entry["Date"], "%d/%m/%Y").date()
        if start_date <= entry_date <= end_date:
            table.add_row([entry["Date"], entry["Amount"], entry["Currency"], entry["Description"]])
    
    print(table if len(table.rows) > 0 else "No entries found in the specified date range.")

    
def readData(file):
    """
    This method is used to read the csvfile.....
    """
    file.seek(0)
    csv_file = file
    data = csv.DictReader(csv_file)
    
    # Create a PrettyTable object
    table = PrettyTable()
    table.field_names = ["Date", "Amount", "Currency", "Description"]
    
    #list to store the values...
    datareaded = list(data)

    # Add rows to the table
    if len(datareaded) > 0:
        for entry in datareaded[-10:]:
            table.add_row([entry["Date"], entry["Amount"], entry["Currency"], entry["Description"]])
        print(table)
    else:
        print("No data available to read.")


def export_to_excel(file):
    """
    Export the expense data to an Excel file.
    """
    file.seek(0)
    csv_file = file
    data = list(csv.DictReader(csv_file))
    
    if len(data) == 0:
        print("No data to export.")
        return
    df = pd.DataFrame(data)
    output_path = "/home/abhishek/Desktop/expenses_export.xlsx"
    df.to_excel(output_path, index=False)
    print(f"Data exported successfully to {output_path}")

        
def choices(choice, file):
    if choice == '1':
        writedata(file)
    elif choice == '2':
        readData(file)
    elif choice == '3':
        calculate_total(file)
    elif choice == '4':
        filter_by_date_range(file)
    elif choice == '5':
        export_to_excel(file)
    elif choice == 'exit':
        exit()
    else:
        print("Invalid choice")


def main():
    print("Welcome onboard.!!!")
    filepath = r'/home/abhishek/Desktop/expenses_dummy_data.csv'
    file = open(filepath, "a+")
    while True:
        choice = input("Enter your choice:\n"
                       "   1 - Add a new expense\n"
                       "   2 - View last 10 entries\n"
                       "   3 - Calculate total expenses\n"
                       "   4 - Filter by date range\n"
                       "   5 - Export to Excel\n"
                       "   'exit' - Exit the program\n").lower()
        choices(choice, file)
    file.close()


if __name__=='__main__':
    main()



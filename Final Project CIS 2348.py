# Joel Sibi
# 1617077

import csv
import datetime

# This function is meant to compile the different CSV Files


def create_all_csvs(d,p,s):
    productArray = []
    manuflistdirectory = d
    pricelistdirectory = p
    servicedateslistdirectory = s

    # Intakes Values from Manufacturer List and inserts values into the newly created main dictionary

    with open(manuflistdirectory, 'rt')as f:
        data = csv.reader(f)
        for row in data:
            placeholder = []
            placeholder.append(row)
            product_dict = {'Item ID': placeholder[0][0],
                            'Manufacturer Name': placeholder[0][1],
                            'Item Type': placeholder[0][2],
                            'Item Price': '',
                            'Service Date': '',
                            'Item Status': placeholder[0][3],
                            }
            productArray.append(product_dict)

    # Intakes values from Price List and inserts it into the main dictionary and then the main array

    with open(pricelistdirectory, 'rt')as j:
        data = csv.reader(j)
        for row in data:
            placeholder = []
            placeholder.append(row)
            product_dict = {'Item ID': placeholder[0][0],
                            'Item Price': placeholder[0][1]}
            for d in productArray:
                if(d['Item ID']) == product_dict['Item ID']:
                    d['Item Price'] = product_dict['Item Price']

    # Intakes values from Service Dates List and inserts it into the main dictionary and then the main array

    with open(servicedateslistdirectory, 'rt')as k:
        data = csv.reader(k)
        for row in data:
            placeholder = []
            placeholder.append(row)
            product_dict = {'Item ID': placeholder[0][0],
                            'Service Date': placeholder[0][1]}
            for d in productArray:
                if(d['Item ID']) == product_dict['Item ID']:
                    d['Service Date'] = product_dict['Service Date']

    # This sorts the values being output to FullInventory by Manufacturer Name and also outputs it to a csv file

    manufacturersortedarray = sorted(productArray, key=lambda i: i['Manufacturer Name'])
    with open('FullInventory.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for product_dict in manufacturersortedarray:
            writer.writerow(product_dict.values())

    # This sorts the values being output to individual inventory lists by Item ID and outputs it to a csv file

    itemidsortedarray = sorted(productArray, key=lambda i: i['Item ID'])
    with open('Laptop Inventory.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for product_dict in itemidsortedarray:
            if (product_dict['Item Type']) == 'laptop':
                writer.writerow(product_dict.values())
    with open('Phone Inventory.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for product_dict in itemidsortedarray:
            if (product_dict['Item Type']) == 'phone':
                writer.writerow(product_dict.values())
    with open('Tower Inventory.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for product_dict in itemidsortedarray:
            if (product_dict['Item Type']) == 'tower':
                writer.writerow(product_dict.values())

    # This sorts the values by the Service Dates and then outputs inventory that is past service date

    servicedatessortedarray = sorted(productArray, key=lambda i: i['Service Date'], reverse=True)
    with open('Past Service Date Inventory.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for product_dict in servicedatessortedarray:
            if product_dict['Service Date'] < str(datetime.date.today()):
                writer.writerow(product_dict.values())

    # This sorts by the price values and displays damaged products within the inventory

    itempricesortedarray = sorted(productArray, key=lambda i: i['Item Price'])
    with open('Damaged Inventory.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for product_dict in itempricesortedarray:
            if (product_dict['Item Status']) == 'damaged':
                writer.writerow(product_dict.values())

    # Query Portion
    exit_var = k
    while exit_var != 'q':
        Manufacturer = input('Enter the desired Manufacturer\n')
        Item_Type = input('Enter the desired Item Type\n')
        for t in itemidsortedarray:
            if Manufacturer not in t['Manufacturer Name'] and Item_Type not in t['Item Type']:
                print('No such item in inventory.')
        for t in itemidsortedarray:
            if Manufacturer in t['Manufacturer Name'] and Item_Type in t['Item Type']:
                print('Your item is:', product_dict[t].values())
        exit_var = input('Enter "q" if you wish to quit or any other key to continue.')


manulistdirectory = input('Enter ManufacturerList Directory\n')
pricelistdirectory = input('Enter PriceList Directory\n')
servicedateslistdirectory = input('Enter ServiceDatesList Directory\n')
create_all_csvs(manulistdirectory, pricelistdirectory, servicedateslistdirectory)

# Example of the directory entries I used to lead to the input files
# C:\\Users\\Joel Sibi\\Desktop\\CIS 2348 Project Files\\ManufacturerList.csv
# C:\\Users\\Joel Sibi\\Desktop\\CIS 2348 Project Files\\PriceList.csv
# C:\\Users\\Joel Sibi\\Desktop\\CIS 2348 Project Files\\ServiceDatesList.csv




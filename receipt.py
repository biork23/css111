import csv
from datetime import datetime

def main():
    try:
        # Call the read_dictionary function and store the compound dictionary in a variable named products_dict.
        products_dict = read_dictionary("products.csv", 0)

        # Print the store name at the top of the receipt.
        print("Welcome to My Grocery Store")
        print("----------------------------")

        # Open the request.csv file for reading.
        with open("request.csv", newline='') as request_file:
            request_reader = csv.reader(request_file)

            # Skip the first line of the request.csv file because it contains column headings.
            next(request_reader)

            # Initialize variables for calculating subtotal and item count.
            subtotal = 0.0
            item_count = 0

            # Use a loop that reads and processes each row from the request.csv file.
            for row in request_reader:
                # Use the requested product number to find the corresponding item in the products_dict.
                product_number = row[0]
                if product_number in products_dict:
                    item = products_dict[product_number]

                    # Print the product name, requested quantity, and product price.
                    product_name = item[1]
                    quantity = int(row[1])
                    price = float(item[2])

                    # Apply discount if applicable.
                    discount = calculate_discount(datetime.now().strftime('%A'), datetime.now().strftime('%H:%M'))
                    discounted_price = price - (price * discount)

                    print(f"Product: {product_name}, Quantity: {quantity}, Price: ${discounted_price:.2f}")

                    # Update subtotal and item count.
                    subtotal += discounted_price * quantity
                    item_count += quantity

            # Compute and print the subtotal due.
            print("\nSubtotal: ${:.2f}".format(subtotal))

            # Compute and print the sales tax amount (6% sales tax rate).
            sales_tax_rate = 0.06
            sales_tax_amount = subtotal * sales_tax_rate
            print("Sales Tax ({}%): ${:.2f}".format(int(sales_tax_rate * 100), sales_tax_amount))

            # Compute and print the total amount due.
            total_amount_due = subtotal + sales_tax_amount
            print("Total Amount Due: ${:.2f}".format(total_amount_due))

            # Sum and print the number of ordered items.
            print("\nNumber of Items: {}".format(item_count))

            # Print a thank you message.
            print("\nThank you for shopping with us!")

            # Print the current date and time.
            print("Date and Time: {}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    except FileNotFoundError:
        print("Error: One or more files not found.")
    except KeyError:
        print("Error: KeyError occurred.")




def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        data_dict = {}
        for row in reader:
            key = row[key_column_index]
            data_dict[key] = row
    return data_dict

def calculate_discount(day, time):
    # Write code to discount the product prices by 10%
    # if today is Tuesday or Wednesday or the current time is before 11:00 a.m.
    if day in ['Tuesday', 'Wednesday'] or (day == 'Monday' and time < '11:00'):
        return 0.10
    return 0.0

if __name__ == "__main__":
    # Add a call to the main function, protected with an if statement.
    main()

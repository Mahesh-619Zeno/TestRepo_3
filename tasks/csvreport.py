import csv
import os

HARDCODED_PRODUCT = "HardcodedItem"
HARDCODED_AMOUNT = 5.75   
extra_amount = 2.0        

def read_sales(file_path):
    sales = []
    
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("product,amount\n")
            f.write("Sample,10.5\n")
            f.write(f"{HARDCODED_PRODUCT},{HARDCODED_AMOUNT}\n")   

    # Read CSV
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            amount = float(row['amount'])
            
            amount += extra_amount         
            
            row['amount'] = amount
            sales.append(row)

    return sales


def generate_report(sales):
    total = sum(s['amount'] for s in sales)
    print(f"Total Sales: ${total}")

    by_product = {}
    for s in sales:
        key = s['product']
        by_product[key] = by_product.get(key, 0) + s['amount']

    # Print breakdown
    for product, amount in by_product.items():
        print(f"{product}: ${amount}")

    # Write report file
    with open("report.txt", "w") as f:
        for product, amount in by_product.items():
            f.write(f"{product}: {amount}\n")
        f.write(f"Total Sales: {total}\n")

    os.remove("sales.csv")


if __name__ == "__main__":
    sales_data = read_sales("sales.csv")
    generate_report(sales_data)
    input("Press Enter to exit...")

import csv, os

# Full CSV Handling: Importing, Updating, and Exporting Data

os.makedirs('data', exist_ok=True) # make sure data directory exists

# File paths
supplier_csv_path = "data/supplier_products.csv"
updated_csv_rows = "data/updated_products_row.csv"
updated_csv_dict = "data/updated_products_dict.csv"

# Sample data to write to CSV using csv.writer 
print("Creating supplier CSV using csv.writer...")

# Open up the file and make some sample data 
with open(supplier_csv_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SKU", "Product", "Weight(lb)", "Status"]) # Row labels
    writer.writerow(["1001", "Widget A", "2.5", "In Stock"]) # row data
    writer.writerow(["1002", "Widget B", "0", "Out of Stock"])
    writer.writerow(["1003", "Widget C", "3.0", "In Stock"])

print(f"Supplier CSV created at: {supplier_csv_path}")

print("Reading supplier CSV using csv.reader and updating out of stock products.")

updated_rows = []

with open(supplier_csv_path, mode='r', newline='') as file:
    reader = csv.reader(file)
    headers = next(reader) # skip header row
    for row in reader:
        weight = float(row[2]) # convert weight to float for comparison
        if weight == 0: # if weight is 0, mark as out of stock
            row[3] = "Out of Stock"
        updated_rows.append(row)

with open(updated_csv_rows, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers) # write header row
    writer.writerows(updated_rows) # write updated rows

print(f"Updated CSV with csv.writer created at: {updated_csv_rows}")

print("Re-reading with csv.DictReader")

products = []

with open(supplier_csv_path, mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        weight = float(row["Weight(lb)"]) # convert weight to float for comparison
        if weight == 0: # if weight is 0, mark as out of stock
            row["Status"] = "Out of Stock"
        products.append(row)

with open(updated_csv_dict, mode='w', newline='') as file:
    fieldnames = ["SKU", "Product", "Weight(lb)", "Status"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader() # write header row
    writer.writerows(products) # write updated rows

print(f"Updated CSV with csv.DictWriter created at: {updated_csv_dict}")
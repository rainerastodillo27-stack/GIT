from pymongo import MongoClient
from datetime import datetime


client = MongoClient("mongodb+srv://DOOM:talong234@cluster0.v3sxscy.mongodb.net/")
db = client["inventoryDB"]
inventory = db["inventory"]
sales = db["sales"]


def reset_ids(collection):
    """Replace ObjectId _id fields with ascending numeric IDs."""
    all_docs = list(collection.find().sort("_id", 1)) 
    collection.drop()  
    new_col = db[collection.name]

    counter = 1
    for doc in all_docs:
        doc["_id"] = counter 
        new_col.insert_one(doc)
        counter += 1

    print(f"{collection.name} IDs reassigned from 1 to {counter - 1}")
    return new_col

inventory = reset_ids(inventory)
sales = reset_ids(sales)


start_date = datetime(2025, 1, 1)
cutoff_date = datetime(2025, 7, 1)
end_date = cutoff_date 


print("\nExcess & Obsolete Inventory Report\n")

report = {}

for item in inventory.find():
    item_id = item["item_id"]
    name = item.get("name", "Unknown")
    qty_on_hand = item.get("quantity_on_hand", 0)
    last_sale = item.get("last_sale_date", datetime.min)

    # Filter sales only within the start–cutoff period
    sales_cursor = sales.find({
        "item_id": item_id,
        "sale_date": {"$gte": start_date, "$lte": end_date}
    })

    total_sold = sum(s.get("quantity_sold", 0) for s in sales_cursor)

    # Determine if item is excess or obsolete
    excess = qty_on_hand > total_sold
    obsolete = last_sale < cutoff_date

    report[item_id] = {
        "name": name,
        "quantity_on_hand": qty_on_hand,
        "total_sold": total_sold,
        "last_sale": last_sale,
        "excess": excess,
        "obsolete": obsolete
    }

header = f"{'Item ID':<10} | {'Name':<20} | {'Qty on Hand':<12} | {'Total Sold':<10} | {'Last Sale':<12} | {'Excess':<7} | {'Obsolete':<9}"
print(header)
print('-' * len(header))

for item_id in sorted(report.keys()):
    data = report[item_id]
    last_sale_str = (
        data['last_sale'].strftime('%Y-%m-%d') 
        if isinstance(data['last_sale'], datetime) else "N/A"
    )
    print(f"{item_id:<10} | {data['name']:<20} | {data['quantity_on_hand']:<12} | "
          f"{data['total_sold']:<10} | {last_sale_str:<12} | "
          f"{'Yes' if data['excess'] else 'No':<7} | "
          f"{'Yes' if data['obsolete'] else 'No':<9}")

print("\nIDs updated and report generated successfully.")

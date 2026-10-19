LAST_NAME = "Jandusay"
FAVORITE_ARTIST = "RINI"
STUDENT_ID = "TUPM-26-4304"
SEED_NUM = int(STUDENT_ID[-1])

# DATA GENERATION RULES

# 1. Five Customers: LAST_NAME + C1–C5
customer_labels = ["C1", "C2", "C3", "C4", "C5"]
customers = [f"{LAST_NAME}_{label}" for label in customer_labels]

# 2. Five Products with Fixed Prices
products = {
    "NOTEBOOK": 45.00,
    "PEN": 12.50,
    "USB": 350.00,
    "HEADPHONES": 899.00,
    "CALCULATOR": 275.00
}
product_list = list(products.keys())

# 3. Character positions from FAVORITE_ARTIST for quantities
artist_chars = list(FAVORITE_ARTIST.upper())

transaction_records = []

# Transaction schedule with one repeated purchase
transactions_data = [
    (0, "NOTEBOOK"),
    (1, "PEN"),
    (0, "NOTEBOOK"),
    (2, "USB"),
    (3, "HEADPHONES"),
    (4, "CALCULATOR"),
    (1, "USB"),
    (2, "PEN"),
    (3, "CALCULATOR"),
    (4, "NOTEBOOK")
]

for idx, (cust_idx, product) in enumerate(transactions_data):
    customer = customers[cust_idx]
    
    # Generate quantity from SEED_NUM + character position in artist name
    char_pos = (cust_idx + idx) % len(artist_chars)
    base_qty = ord(artist_chars[char_pos]) - ord('A') + 1
    quantity = max(1, (SEED_NUM + base_qty) % 8)
    
    unit_price = products[product]
    total_value = round(quantity * unit_price, 2)
    
    # Flag the repeated purchase
    is_repeat = (cust_idx == 0 and product == "NOTEBOOK")
    
    transaction_records.append({
        "customer": customer,
        "product": product,
        "quantity": quantity,
        "unit_price": unit_price,
        "total_value": total_value,
        "is_repeat_purchase": is_repeat
    })

# ANALYSIS
from collections import defaultdict

repeated_purchases = [r for r in transaction_records if r["is_repeat_purchase"]]
distinct_customers = set(r["customer"] for r in transaction_records)
distinct_products = set(r["product"] for r in transaction_records)

# Customer summaries
customer_totals = defaultdict(float)
customer_trans_count = defaultdict(int)
for rec in transaction_records:
    customer_totals[rec["customer"]] += rec["total_value"]
    customer_trans_count[rec["customer"]] += 1

# Product summaries
product_totals = defaultdict(float)
product_quantities = defaultdict(int)
for rec in transaction_records:
    product_totals[rec["product"]] += rec["total_value"]
    product_quantities[rec["product"]] += rec["quantity"]

overall_total = sum(r["total_value"] for r in transaction_records)
overall_qty = sum(r["quantity"] for r in transaction_records)

# CONSOLIDATED REPORT
print("=" * 70)
print("      TRANSACTION HISTORY ANALYSIS — CONSOLIDATED REPORT")
print("=" * 70)
print(f"Account Holder   : {LAST_NAME}")
print(f"Student ID       : {STUDENT_ID}")
print(f"Seed Value       : {SEED_NUM}")
print(f"Favorite Artist  : {FAVORITE_ARTIST}")
print(f"Total Transactions : {len(transaction_records)}")
print(f"Distinct Customers : {len(distinct_customers)}")
print(f"Distinct Products  : {len(distinct_products)}")
print(f"Repeated Purchases : {len(repeated_purchases)}")
print(f"OVERALL TOTAL       : ₱{overall_total:,.2f}")
print("-" * 70)

print("\n--- GENERATED CUSTOMERS ---")
for c in customers:
    print(f"  • {c}")

print("\n--- PRODUCT PRICE LIST ---")
print(f"{'PRODUCT':<15} {'UNIT PRICE'}")
print("-" * 30)
for prod, price in products.items():
    print(f"{prod:<15} ₱{price:,.2f}")

print("\n--- COMPLETE TRANSACTION RECORDS ---")
print(f"{'NO.':<5} {'CUSTOMER':<18} {'PRODUCT':<12} {'QTY':<6} {'PRICE':<10} {'TOTAL':<12} {'FLAG'}")
print("-" * 75)
for idx, rec in enumerate(transaction_records, 1):
    flag = "REPEAT" if rec["is_repeat_purchase"] else ""
    print(f"{idx:<5} {rec['customer']:<18} {rec['product']:<12} {rec['quantity']:<6} "
          f"₱{rec['unit_price']:<9,.2f} ₱{rec['total_value']:<12,.2f} {flag}")

print("\n--- CUSTOMER PURCHASE SUMMARY ---")
print(f"{'CUSTOMER':<18} {'TRANSACTIONS':<14} {'TOTAL SPENT'}")
print("-" * 45)
for cust in customers:
    count = customer_trans_count[cust]
    total = customer_totals[cust]
    print(f"{cust:<18} {count:<14} ₱{total:,.2f}")

print("\n--- PRODUCT SALES SUMMARY ---")
print(f"{'PRODUCT':<15} {'QUANTITY SOLD':<15} {'TOTAL SALES'}")
print("-" * 45)
for prod in product_list:
    qty = product_quantities[prod]
    total = product_totals[prod]
    print(f"{prod:<15} {qty:<15} ₱{total:,.2f}")

print("\n--- OVERALL TRANSACTION SUMMARY ---")
print(f"Total Quantity Sold : {overall_qty}")
print(f"Total Revenue        : ₱{overall_total:,.2f}")
print("=" * 70)
print("END OF TRANSACTION REPORT")
print("=" * 70)
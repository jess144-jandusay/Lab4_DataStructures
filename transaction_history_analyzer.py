# ==================================================
# EXERCISE 3: TRANSACTION HISTORY ANALYZER
# Prepared by: Jandusay | TUPM-26-4304
# ==================================================

LAST_NAME = "Jandusay"
FAVORITE_ARTIST = "RINI"
STUDENT_ID = "TUPM-26-4304"
SEED_NUM = int(STUDENT_ID[-1])

# --- DATA ---
customer_labels = ["C1", "C2", "C3", "C4", "C5"]
customers = [f"{LAST_NAME}_{label}" for label in customer_labels]
products = {
    "NOTEBOOK": 45.00,
    "PEN": 12.50,
    "USB": 350.00,
    "HEADPHONES": 899.00,
    "CALCULATOR": 275.00
}
product_list = list(products.keys())
artist_chars = list(FAVORITE_ARTIST.upper())

transaction_records = []
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
    char_pos = (cust_idx + idx) % len(artist_chars)
    base_qty = ord(artist_chars[char_pos]) - ord('A') + 1
    quantity = max(1, (SEED_NUM + base_qty) % 8)
    unit_price = products[product]
    total_value = round(quantity * unit_price, 2)
    is_repeat = (cust_idx == 0 and product == "NOTEBOOK")
    transaction_records.append({
        "customer": customer,
        "product": product,
        "quantity": quantity,
        "unit_price": unit_price,
        "total_value": total_value,
        "is_repeat_purchase": is_repeat
    })

# --- ANALYSIS ---
from collections import defaultdict
repeated = [r for r in transaction_records if r["is_repeat_purchase"]]
distinct_cust = set(r["customer"] for r in transaction_records)
distinct_prod = set(r["product"] for r in transaction_records)

cust_totals = defaultdict(float)
cust_count = defaultdict(int)
prod_totals = defaultdict(float)
prod_qty = defaultdict(int)
for rec in transaction_records:
    cust_totals[rec["customer"]] += rec["total_value"]
    cust_count[rec["customer"]] += 1
    prod_totals[rec["product"]] += rec["total_value"]
    prod_qty[rec["product"]] += rec["quantity"]

overall_total = sum(r["total_value"] for r in transaction_records)

# --- REPORT ---
print("=" * 70)
print("      TRANSACTION HISTORY ANALYSIS — CONSOLIDATED REPORT")
print("=" * 70)
print(f"Account Holder   : {LAST_NAME}")
print(f"Student ID       : {STUDENT_ID}")
print(f"Seed Value       : {SEED_NUM}")
print(f"Total Transactions : {len(transaction_records)}")
print(f"Distinct Customers : {len(distinct_cust)}")
print(f"Distinct Products  : {len(distinct_prod)}")
print(f"Repeated Purchases : {len(repeated)}")
print(f"OVERALL TOTAL       : PHP {overall_total:,.2f}")
print("-" * 70)

print(f"\n{'NO.':<5} {'CUSTOMER':<18} {'PRODUCT':<12} {'QTY':<6} {'PRICE':<10} {'TOTAL':<12} {'FLAG'}")
print("-" * 75)
for idx, rec in enumerate(transaction_records, 1):
    flag = "REPEAT" if rec["is_repeat_purchase"] else ""
    print(f"{idx:<5} {rec['customer']:<18} {rec['product']:<12} {rec['quantity']:<6} "
          f"PHP {rec['unit_price']:<9,.2f} PHP {rec['total_value']:<12,.2f} {flag}")

print("\n--- CUSTOMER SUMMARY ---")
print(f"{'CUSTOMER':<18} {'TRANS':<8} {'TOTAL SPENT'}")
print("-" * 40)
for c in customers:
    print(f"{c:<18} {cust_count[c]:<8} PHP {cust_totals[c]:,.2f}")

print("\n--- PRODUCT SUMMARY ---")
print(f"{'PRODUCT':<15} {'QTY':<8} {'TOTAL SALES'}")
print("-" * 40)
for p in product_list:
    print(f"{p:<15} {prod_qty[p]:<8} PHP {prod_totals[p]:,.2f}")
print("=" * 70)
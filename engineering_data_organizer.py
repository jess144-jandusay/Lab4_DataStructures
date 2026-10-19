# EXERCISE 1: ENGINEERING TEST DATA ORGANIZER
LAST_NAME = "Jandusay"
FAVORITE_ARTIST = "RINI"
STUDENT_ID = "TUPM-26-4304"
SEED_NUM = int(STUDENT_ID[-1])

# --- CATEGORIES & SOURCES ---
test_categories = ["TEMPERATURE", "VOLTAGE", "CURRENT", "PRESSURE", "SPEED"]
source_labels = ["T1", "T2", "T3", "T4", "T5"]

artist_chars = list(FAVORITE_ARTIST.upper())
test_records = []

for cat_idx, category in enumerate(test_categories):
    for src_idx, source in enumerate(source_labels):
        char_pos = (cat_idx + src_idx) % len(artist_chars)
        base_from_artist = ord(artist_chars[char_pos]) - ord('A') + 1
        measurement = round((base_from_artist * 1.5) + (SEED_NUM * 3.2) + (src_idx * 1.8), 2)
        
        if category == "TEMPERATURE":
            status = "PASS" if 30 <= measurement <= 90 else "REVIEW"
        elif category == "VOLTAGE":
            status = "PASS" if 100 <= measurement <= 135 else "REVIEW"
        elif category == "CURRENT":
            status = "PASS" if 1.5 <= measurement <= 6.5 else "REVIEW"
        elif category == "PRESSURE":
            status = "PASS" if 95 <= measurement <= 160 else "REVIEW"
        else:
            status = "PASS" if 45 <= measurement <= 130 else "REVIEW"
        
        test_records.append({
            "category": category,
            "source": source,
            "measurement": measurement,
            "status": status,
            "is_duplicate": False
        })

# Add 1 duplicate
dup_index = 2
duplicate = test_records[dup_index].copy()
duplicate["is_duplicate"] = True
test_records.insert(dup_index + 1, duplicate)

# --- ANALYSIS ---
from collections import defaultdict
grouped = defaultdict(list)
for rec in test_records:
    if not rec["is_duplicate"]:
        grouped[rec["category"]].append(rec)

summary = {}
for cat, records in grouped.items():
    vals = [r["measurement"] for r in records]
    summary[cat] = {
        "count": len(vals),
        "average": round(sum(vals)/len(vals), 2),
        "max": max(vals),
        "min": min(vals),
        "pass_count": sum(1 for r in records if r["status"] == "PASS")
    }

# --- REPORT ---
print("=" * 65)
print("        ENGINEERING TEST DATA ORGANIZER — REPORT")
print("=" * 65)
print(f"Analyst   : {LAST_NAME}")
print(f"ID        : {STUDENT_ID}")
print(f"Seed      : {SEED_NUM}")
print(f"Total Records: {len(test_records)}")
print("-" * 65)
print(f"{'CATEGORY':<15} {'SOURCES':<8} {'AVG':<10} {'MAX':<10} {'MIN':<10} {'PASS':<6}")
print("-" * 65)
for cat in test_categories:
    s = summary[cat]
    print(f"{cat:<15} {s['count']:<8} {s['average']:<10.2f} {s['max']:<10.2f} {s['min']:<10.2f} {s['pass_count']:<6}")
print("-" * 65)
print(f"{'NO.':<4} {'CATEGORY':<15} {'SOURCE':<8} {'MEASUREMENT':<14} {'STATUS':<8} {'FLAG'}")
print("-" * 60)
for idx, rec in enumerate(test_records, 1):
    flag = "DUPLICATE" if rec["is_duplicate"] else ""
    print(f"{idx:<4} {rec['category']:<15} {rec['source']:<8} {rec['measurement']:<14.2f} {rec['status']:<8} {flag}")
print("=" * 65)
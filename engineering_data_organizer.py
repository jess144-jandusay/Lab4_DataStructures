LAST_NAME = "Jandusay"
FAVORITE_ARTIST = "RINI"
STUDENT_ID = "TUPM-26-4304"
SEED_NUM = int(STUDENT_ID[-1])

# DATA GENERATION RULES

# 1. Five test sources from LAST_NAME, labeled T1–T5
source_labels = ["T1", "T2", "T3", "T4", "T5"]
source_name_map = {}
for i, label in enumerate(source_labels):
    # Cycle through LAST_NAME characters to name sources
    char = LAST_NAME[i % len(LAST_NAME)]
    source_name_map[label] = f"Source_{char}"

# 2. Five measurement categories
categories = ["TEMPERATURE", "VOLTAGE", "CURRENT", "PRESSURE", "SPEED"]

# 3. Generate values using SEED_NUM + character positions of FAVORITE_ARTIST
artist_chars = list(FAVORITE_ARTIST)
test_records = []

for cat_idx, category in enumerate(categories):
    for src_idx, label in enumerate(source_labels):
        # Base value from character position in FAVORITE_ARTIST
        char_pos = (cat_idx + src_idx) % len(artist_chars)
        base_from_artist = ord(artist_chars[char_pos]) - ord('A') + 1
        
        # Final measurement formula
        measurement = round(
            (base_from_artist * 1.5) + (SEED_NUM * 3.2) + (src_idx * 1.8),
            2
        )

        # Status thresholds per category
        if category == "TEMPERATURE":
            status = "PASS" if 30 <= measurement <= 90 else "REVIEW"
        elif category == "VOLTAGE":
            status = "PASS" if 100 <= measurement <= 135 else "REVIEW"
        elif category == "CURRENT":
            status = "PASS" if 1.5 <= measurement <= 6.5 else "REVIEW"
        elif category == "PRESSURE":
            status = "PASS" if 95 <= measurement <= 160 else "REVIEW"
        else:  # SPEED
            status = "PASS" if 45 <= measurement <= 130 else "REVIEW"

        test_records.append({
            "source_label": label,
            "source_name": source_name_map[label],
            "category": category,
            "measurement": measurement,
            "status": status,
            "is_duplicate": False
        })

# 4. Add ONE repeated record (same source + same category)
dup_index = 2  # Duplicate T3 + TEMPERATURE
duplicate = test_records[dup_index].copy()
duplicate["is_duplicate"] = True
test_records.insert(dup_index + 1, duplicate)

# ANALYSIS
from collections import defaultdict

# Group by category
by_category = defaultdict(list)
for rec in test_records:
    if not rec["is_duplicate"]:
        by_category[rec["category"]].append(rec)

# Category summaries
category_summary = {}
for cat, records in by_category.items():
    vals = [r["measurement"] for r in records]
    category_summary[cat] = {
        "record_count": len(vals),
        "average": round(sum(vals) / len(vals), 2),
        "max_value": max(vals),
        "min_value": min(vals),
        "pass_count": sum(1 for r in records if r["status"] == "PASS")
    }

# Duplicate tracking
duplicates = [r for r in test_records if r["is_duplicate"]]

# CONSOLIDATED REPORT
print("=" * 70)
print("       ENGINEERING TEST DATA ORGANIZER — CONSOLIDATED REPORT")
print("=" * 70)
print(f"Analyst          : {LAST_NAME}")
print(f"Student ID       : {STUDENT_ID}")
print(f"Seed Value       : {SEED_NUM}")
print(f"Favorite Artist  : {FAVORITE_ARTIST}")
print(f"Total Records    : {len(test_records)}")
print(f"Duplicate Found  : {len(duplicates)}")
print("-" * 70)

print("\n--- GENERATED TEST SOURCES ---")
for label, name in source_name_map.items():
    print(f"  {label} → {name}")

print("\n--- CATEGORY SUMMARY ---")
print(f"{'CATEGORY':<16} {'RECORDS':<8} {'AVERAGE':<10} {'MAX':<10} {'MIN':<10} {'PASS':<6}")
print("-" * 62)
for cat in categories:
    s = category_summary[cat]
    print(f"{cat:<16} {s['record_count']:<8} {s['average']:<10.2f} "
          f"{s['max_value']:<10.2f} {s['min_value']:<10.2f} {s['pass_count']:<6}")

print("\n--- FULL TEST RECORDS ---")
print(f"{'NO.':<5} {'SOURCE':<10} {'CATEGORY':<16} {'MEASUREMENT':<14} {'STATUS':<8} {'FLAG'}")
print("-" * 70)
for idx, rec in enumerate(test_records, 1):
    flag = "DUPLICATE" if rec["is_duplicate"] else ""
    print(f"{idx:<5} {rec['source_label']:<10} {rec['category']:<16} "
          f"{rec['measurement']:<14.2f} {rec['status']:<8} {flag}")

print("=" * 70)
print("END OF ENGINEERING REPORT")
print("=" * 70)
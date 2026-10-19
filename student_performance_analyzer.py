LAST_NAME = "Jandusay"
FAVORITE_ARTIST = "RINI"
STUDENT_ID = "TUPM-26-4304"
SEED_NUM = int(STUDENT_ID[-1])

# DATA GENERATION RULES

# 1. Student Names: LAST_NAME + 5 labels
student_labels = ["S1", "S2", "S3", "S4", "S5"]
student_names = [f"{LAST_NAME}_{label}" for label in student_labels]

# 2. Five Subjects
subjects = ["PROGRAMMING", "MATHEMATICS", "ELECTRONICS", "PHYSICS", "ENGLISH"]

# 3. Character positions from FAVORITE_ARTIST
artist_chars = list(FAVORITE_ARTIST.upper())

performance_records = []

for s_idx, student in enumerate(student_names):
    for sub_idx, subject in enumerate(subjects):
        # --- Special cases first ---
        # Repeated record: S2 + MATHEMATICS
        is_repeat = (s_idx == 1 and sub_idx == 1)
        # Incomplete record: S5 + PHYSICS (missing score)
        is_incomplete = (s_idx == 4 and sub_idx == 3)

        if is_incomplete:
            score = None
            category = "NO SCORE"
        else:
            # Generate score: SEED_NUM + char position from artist
            char_pos = (s_idx + sub_idx) % len(artist_chars)
            base_from_char = ord(artist_chars[char_pos]) - ord('A') + 1
            score = 50 + (base_from_char * 2) + (SEED_NUM * 3) + (sub_idx * 2)
            
            # Determine performance category
            if score >= 90:
                category = "OUTSTANDING"
            elif score >= 75:
                category = "SATISFACTORY"
            elif score >= 60:
                category = "DEVELOPING"
            else:
                category = "BELOW EXPECTED"

        performance_records.append({
            "student": student,
            "subject": subject,
            "score": score,
            "category": category,
            "is_repeat": False,
            "is_incomplete": is_incomplete
        })

        # Add the repeated record right after the original
        if is_repeat:
            performance_records.append({
                "student": student,
                "subject": subject,
                "score": score,
                "category": category,
                "is_repeat": True,
                "is_incomplete": False
            })

# ANALYSIS
from collections import defaultdict

# Identify flagged records
repeated_records = [r for r in performance_records if r["is_repeat"]]
incomplete_records = [r for r in performance_records if r["is_incomplete"]]

# Student summaries (exclude duplicates & incomplete)
student_scores = defaultdict(list)
subject_scores = defaultdict(list)

for rec in performance_records:
    if rec["score"] is not None and not rec["is_repeat"]:
        student_scores[rec["student"]].append(rec["score"])
        subject_scores[rec["subject"]].append(rec["score"])

# Calculate summaries
student_summary = {}
for student, scores in student_scores.items():
    student_summary[student] = {
        "subjects_taken": len(scores),
        "average": round(sum(scores) / len(scores), 2),
        "highest": max(scores),
        "lowest": min(scores)
    }

subject_summary = {}
for subject, scores in subject_scores.items():
    subject_summary[subject] = {
        "average": round(sum(scores) / len(scores), 2),
        "highest": max(scores),
        "lowest": min(scores)
    }

# CONSOLIDATED REPORT
print("=" * 75)
print("        STUDENT PERFORMANCE DATA ANALYSIS — CONSOLIDATED REPORT")
print("=" * 75)
print(f"Prepared By      : {LAST_NAME}")
print(f"Student ID       : {STUDENT_ID}")
print(f"Seed Value       : {SEED_NUM}")
print(f"Favorite Artist  : {FAVORITE_ARTIST}")
print(f"Total Records    : {len(performance_records)}")
print(f"Repeated Records : {len(repeated_records)}")
print(f"Incomplete Recs  : {len(incomplete_records)}")
print("-" * 75)

print("\n--- GENERATED STUDENTS ---")
for name in student_names:
    print(f"  • {name}")

print("\n--- FULL PERFORMANCE RECORDS ---")
print(f"{'NO.':<5} {'STUDENT':<18} {'SUBJECT':<16} {'SCORE':<8} {'CATEGORY':<16} {'FLAG'}")
print("-" * 75)
for idx, rec in enumerate(performance_records, 1):
    flag = ""
    if rec["is_repeat"]: flag = "REPEAT"
    if rec["is_incomplete"]: flag = "INCOMPLETE"
    score_disp = f"{rec['score']:.1f}" if rec['score'] is not None else "MISSING"
    print(f"{idx:<5} {rec['student']:<18} {rec['subject']:<16} {score_disp:<8} {rec['category']:<16} {flag}")

print("\n--- STUDENT PERFORMANCE SUMMARIES ---")
print(f"{'STUDENT':<18} {'SUBJECTS':<10} {'AVERAGE':<10} {'HIGHEST':<10} {'LOWEST':<10}")
print("-" * 60)
for student in student_names:
    if student in student_summary:
        s = student_summary[student]
        print(f"{student:<18} {s['subjects_taken']:<10} {s['average']:<10.2f} {s['highest']:<10.1f} {s['lowest']:<10.1f}")
    else:
        print(f"{student:<18} No valid scores")

print("\n--- SUBJECT PERFORMANCE SUMMARIES ---")
print(f"{'SUBJECT':<16} {'AVERAGE':<10} {'HIGHEST':<10} {'LOWEST':<10}")
print("-" * 50)
for subject in subjects:
    s = subject_summary[subject]
    print(f"{subject:<16} {s['average']:<10.2f} {s['highest']:<10.1f} {s['lowest']:<10.1f}")

print("=" * 75)
print("END OF PERFORMANCE REPORT")
print("=" * 75)
import os

ENTRY = "I dropped production and committed the deletion as 'fix: cleanup', so git blame will always know exactly who to blame."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY + "\n")
print(ENTRY)

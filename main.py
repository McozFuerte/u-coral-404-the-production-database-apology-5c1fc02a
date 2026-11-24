import os

ENTRY = "I'm sorry I deleted the production database. I retried the delete job three times before accepting the first attempt had worked."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY + "\n")
print(ENTRY)

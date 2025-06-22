import os
import json

ROOT_DIR = "Resources/Soundscapes"
OUTPUT_FILE = "Resources/soundscape_catalog.json"

catalog = {
    "version": 1,
    "updatedAt": "",
    "soundscapes": [],
    "typeIds": [],
    "categoryIds": []
}

from datetime import datetime
catalog["updatedAt"] = datetime.utcnow().strftime("%Y-%m-%d")

for folder in os.listdir(ROOT_DIR):
    meta_path = os.path.join(ROOT_DIR, folder, "meta.json")
    if not os.path.isfile(meta_path):
        continue
    try:
        with open(meta_path, "r", encoding="utf-8") as f:
            meta = json.load(f)
            item = {
                "id": meta.get("id"),
                "typeId": meta.get("typeId"),
                "categoryId": meta.get("categoryId")
            }
            catalog["soundscapes"].append(item)

            if item["typeId"] and item["typeId"] not in catalog["typeIds"]:
                catalog["typeIds"].append(item["typeId"])
            if item["categoryId"] and item["categoryId"] not in catalog["categoryIds"]:
                catalog["categoryIds"].append(item["categoryId"])

    except Exception as e:
        print(f"❌ Failed to parse {meta_path}: {e}")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(catalog, f, indent=2, ensure_ascii=False)

print(f"✅ catalog written to {OUTPUT_FILE}")

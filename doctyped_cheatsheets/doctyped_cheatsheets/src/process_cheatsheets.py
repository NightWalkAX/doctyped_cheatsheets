import glob
import json
import os


def process_cheatsheets():
    """
    Process pairs of JSON files (Spanish/English) and generate combined dictionaries.
    This function is intended to be called from a Frappe context.
    """
    # Get the absolute path to the data directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "..", "data")
    data_dir = os.path.abspath(data_dir)

    print(f"Looking for cheatsheets in: {data_dir}")

    if not os.path.exists(data_dir):
        print(f"ERROR: Data directory does not exist: {data_dir}")
        return []

    # Find all Spanish cheatsheet files (without -en suffix)
    pattern = f"{data_dir}/*.json"
    spanish_files = [
        f for f in glob.glob(pattern) if not f.endswith("-en.json")
    ]

    if not spanish_files:
        print(f"WARNING: No cheatsheet files found in {data_dir}")
        print(f"Pattern used: {pattern}")

    all_results = []

    for spanish_file in spanish_files:
        # Load Spanish version
        with open(spanish_file, encoding="utf-8") as f:
            spanish_data = json.load(f)

        # Find corresponding English version
        english_file = spanish_file.replace(".json", "-en.json")
        if not os.path.exists(english_file):
            print(f"Warning: English version not found for {spanish_file}")
            continue

        with open(english_file, encoding="utf-8") as f:
            english_data = json.load(f)

        # Process pairs and create combined dictionaries
        combined_items = []

        # Get items from Spanish file (using 'items' key)
        spanish_items = spanish_data.get("items", [])
        
        # Get items from English file (detect which key to use)
        # Some English files use 'cheats', others use 'items'
        english_items = english_data.get("items", [])
        english_key_used = "items"
        if not english_items:
            english_items = english_data.get("items", [])
            english_key_used = "items"
            
        print(f"  Spanish: {len(spanish_items)} items, "
              f"English: {len(english_items)} items ('{english_key_used}')")

        # Match by index (assuming both files are ordered correspondingly)
        min_length = min(len(spanish_items), len(english_items))

        if len(spanish_items) != len(english_items):
            print(f"Warning: Item count mismatch for {spanish_file}")
            print(
                f"  Spanish items: {len(spanish_items)}, "
                f"English items: {len(english_items)}"
            )

        for i in range(min_length):
            spanish_item = spanish_items[i]
            english_item = english_items[i]

            combined = {
                "code": english_item.get("code", ""),
                "language": "English",
                "description": english_item.get("description", ""),
                "example": english_item.get("example", ""),
                "description_alt": spanish_item.get("description", ""),
                "example_alt": spanish_item.get("example", "")
            }
            combined_items.append(combined)

        cheatsheet_result = {
            "title": spanish_data.get("title", "Unknown"),
            "title_alt": english_data.get("title", "Unknown"),
            "tags": spanish_data.get("tags", []),
            "items": combined_items
        }

        all_results.append(cheatsheet_result)
        title = cheatsheet_result['title']
        item_count = len(combined_items)
        print(f"Processed: {title} ({item_count} items)")

    print(f"\nProcessed {len(spanish_files)} cheatsheet pair(s)")
    return all_results


def save_to_frappe():
    """
    Save the processed cheatsheets into Frappe.
    Creates a Cheatsheet document for each collection with its items
    as a child table.
    This function must be called from within a Frappe context.
    """
    import frappe

    results = process_cheatsheets()
    total_inserted = 0
    total_skipped = 0
    total_items = 0

    for cheatsheet_data in results:
        collection_title = cheatsheet_data["title"]
        print(f"\nProcessing collection: {collection_title}")

        # Check if a document with the same title already exists
        existing = frappe.db.exists(
            "Cheatsheet",
            {"title": collection_title}
        )

        if not existing:
            # Convert tags list to a comma-separated string
            tags_str = ", ".join(cheatsheet_data.get("tags", []))

            # Prepare the child table items
            child_items = []
            for item in cheatsheet_data["items"]:
                child_items.append({
                    "code": item.get("code", ""),
                    "description": item.get("description", ""),
                    "example": item.get("example", ""),
                    "description_alt": item.get("description_alt", ""),
                    "example_alt": item.get("example_alt", "")
                })

            # Create the main document with its items
            doc = frappe.get_doc({
                "doctype": "Cheatsheet",
                "title": cheatsheet_data.get("title", "Unknown"),
                "title_alt": cheatsheet_data.get("title_alt", "Unknown"),
                "tags": tags_str,
                "items": child_items
            })
            doc.insert(ignore_permissions=True)
            total_inserted += 1
            total_items += len(child_items)
            item_count = len(child_items)
            print(f"  ✓ Inserted: {collection_title} ({item_count} items)")
        else:
            total_skipped += 1
            print(f"  - Skipped (exists): {collection_title}")

    frappe.db.commit()
    print(f"\n{'='*50}")
    print("Summary:")
    print(f"  • Collections inserted: {total_inserted}")
    print(f"  • Collections skipped: {total_skipped}")
    print(f"  • Total items inserted: {total_items}")
    print(f"  • Total collections processed: {total_inserted + total_skipped}")
    print(f"{'='*50}")

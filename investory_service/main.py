inventory = {
    "SKU_101": {"name": "Wireless Mouse", "price": 25.00, "stock_count": 50, "category": "Electronics"},
    "SKU_102": {"name": "Gaming Keyboard", "price": 80.00, "stock_count": 0, "category": "Electronics"},
    "SKU_103": {"name": "Yoga Mat", "price": 30.00, "stock_count": 15, "category": "Fitness"},
    "SKU_104": {"name": "Bluetooth Speaker", "price": 120.00, "stock_count": 5, "category": "Electronics"},
    "SKU_105": {"name": "Protein Shaker", "price": 15.00, "stock_count": 0, "category": "Fitness"},
}

def inventory_agent(inventory_data, category):
    for item in inventory_data:
        if inventory[item]["category"] == category:
            inventory[item]["price"] = inventory[item]["price"] * 0.85

        if inventory[item]["stock_count"] == 0:
            inventory[item]["restock_urgent"] = True


        inventory[item].setdefault("last_sold", "Never")
    return inventory_data

target_category = "Electronics"
updated_inventory = inventory_agent(inventory, target_category)

for sku in updated_inventory:
    print(f"{sku}: {updated_inventory[sku]}")
1. UPDATE (Flash Sale):  #    Apply a 15% discount to the 'price' of every item in the "Electronics" category.

2. LOGIC (Restock Alert):  
Loop through the inventory. If 'stock_count' is 0, add a new key  #    called 'restock_urgent' with the value True.

3. SAFE ACCESS (Data Integrity):  
Check for a 'last_sold' key. If it doesn't exist, use .setdefault()  #    to set it to "Never".

4. VIEW: Print the final updated inventory.
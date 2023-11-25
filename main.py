basket = [
    {"Product": "Leather wallet", "Unit Price": 1100, "GST (%)": 18, "Quantity": 2},
    {"Product": "Umbrella", "Unit Price": 900, "GST (%)": 12, "Quantity": 4},
    {"Product": "Cigarette", "Unit Price": 200, "GST (%)": 28, "Quantity": 3},
    {"Product": "Honey", "Unit Price": 100, "GST (%)": 0, "Quantity": 3},
]

# Calculate total amount and identify product with maximum GST amount
total_amount = 0
max_gst_product = None
max_gst_amount = 0

for item in basket:
    unit_price = item["Unit Price"]
    quantity = item["Quantity"]
    gst_percentage = item["GST (%)"]

    # Calculate total amount for each item
    item_amount = unit_price * quantity

    # Calculate GST amount for each item
    gst_amount = (item_amount * gst_percentage) / 100

    # Apply 5% discount for products with a unit price of Rs. 500 or more
    if unit_price >= 500:
        discount = (unit_price * quantity * 5) / 100
        item_amount -= discount

    # Update total amount
    total_amount += item_amount

    # Update maximum GST amount and corresponding product
    if gst_amount > max_gst_amount:
        max_gst_amount = gst_amount
        max_gst_product = item["Product"]

# Print the results
print("Total Amount to be Paid: Rs.", total_amount)
print("Product with Maximum GST Amount:", max_gst_product)
print("Maximum GST Amount: Rs.", max_gst_amount)
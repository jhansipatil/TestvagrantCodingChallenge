from dict import basket

total_amount = 0
max_gst_product = None
max_gst_amount = 0

for item in basket:
    unit_price = item["Unit Price"]
    quantity = item["Quantity"]
    gst_percentage = item["GST"]

    total_amount += unit_price * quantity * (1 + gst_percentage / 100)

    gst_amount = (unit_price * quantity * gst_percentage) / 100

    if gst_amount > max_gst_amount:
        max_gst_amount = gst_amount
        max_gst_product = item["Product"]

print("Total Amount to be paid: Rs.", total_amount)
print("Product with maximum GST amount:", max_gst_product)
print("Maximum GST amount paid: Rs.", max_gst_amount)# TestvagrantCodingChallenge

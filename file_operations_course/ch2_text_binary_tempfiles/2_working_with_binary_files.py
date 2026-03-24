import os

# Globomantics - Binary File Archiver for Uploaded Shipping Docs
# source files (simulated)
pdf_source = "uploads/sample_invoice.pdf"
image_source = "uploads/sample_delivery.jpg"

# Target archive folder
archive_folder = "archived_docs"

# Ensure the directories exist
os.makedirs("uploads", exist_ok=True)
os.makedirs(archive_folder, exist_ok=True)

# file destinations
pdf_target = os.path.join(archive_folder, "2026-03-24_invoice_copy.pdf")
image_target = os.path.join(archive_folder, "2026-03-24_delivery_photo.jpg")

# Working with Binary Files - Reading and Writing PDF
pdf_in = open(pdf_source, "rb")
pdf_bytes = pdf_in.read()
pdf_in.close()

# Writing the PDF bytes to a new file
pdf_out = open(pdf_target, "wb")
pdf_out.write(pdf_bytes)
pdf_out.close()

print(f"PDF archived to: {pdf_target} (Size: {len(pdf_bytes)} bytes)")

img_in = open(image_source, "rb")
image_bytes = img_in.read()
img_in.close()

# Writing the image bytes to a new file
img_out = open(image_target, "wb")
img_out.write(image_bytes)
img_out.close()

print(f"Image archived to: {image_target} (Size: {len(image_bytes)} bytes)")
import os

# simulate customer reviews from various countries
reviews = [
    "I love this product!", # English
    "¡Me encanta este producto!", # Spanish
    "J'adore ce produit!", # French
    "Dieses Produkt ist großartig!", # German
    "この製品が大好きです！", # Japanese
    "Этот продукт отличный!", # Russian
    "这个产品太棒了！" # Chinese
]

#Folder to store reviews
folder = "reviews"
if not os.path.exists(folder):
    os.makedirs(folder)  #if the folder doesn't exist, create it

# File path to save reviews
utf8_file = f"{folder}/reviews_utf8.txt"
iso_file = f"{folder}/reviews_iso8859_1.txt" # only supports Western European languages

with open(utf8_file, 'w', encoding='utf-8') as file:
    for review in reviews:
        file.write(review + "\n")

print(f"Review saved in UTF-8: {utf8_file}")

print("\ntrying to read UTF-8 file using incorrect encoding (ISO-8859-1):" )
try:
    with open(utf8_file, 'r') as file:
        contents = file.read()
        print(contents)
except UnicodeDecodeError as e:
    print(f"Decode Error: {e}")

filtered_reviews = [r for r in reviews if all(ord(c) < 256 for c in r)] # filter out reviews with characters that can't be encoded in ISO-8859-1

with open(iso_file, 'w', encoding='iso-8859-1') as file:
    for review in filtered_reviews:
        file.write(review + "\n")

print(f"\nSaved ISO-8859-1 compatible reviews: {iso_file}")
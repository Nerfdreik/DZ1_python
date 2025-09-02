from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iphone 14", "89030001122"),
    Smartphone("Samsung", "Galaxy S8", "89051112233"),
    Smartphone("Xiaomi", "14T", "89034445566"),
    Smartphone("Realme", "C55", "89050004455"),
    Smartphone("Poco", "X6 Pro", "89051115930")
]

for phone in catalog:
    print(f"{phone.brand} {phone.model} {phone.phone_number}")

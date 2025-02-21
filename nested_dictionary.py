def print_person_info(person_info):
    print("Person Info:")
    for key in person_info:
        if key != "address":
            print(f"{key}: {person_info[key]}")
    
    print("\nAddress Details:")
    address = person_info["address"]
    for key in address:
        print(f"{key}: {address[key]}")

person_info = {
    "name": "Sayem",
    "age": 30,
    "address": {
        "street": "Banani Road",
        "city": "Dhaka",
        "zip": "2101"
    }
}

print_person_info(person_info)

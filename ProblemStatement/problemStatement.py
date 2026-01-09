alerts = [
    "WARNING|CPU|85%",
    "CRITICAL|Memory|92%",
    "WARNING|Disk|80%",
    "CRITICAL|CPU|95%",
    "CRITICAL|Memory|90%",
]

dict = {}
for i in alerts:
    data = i.split("|")
    # print(data[0])
    if data[0] == "CRITICAL":
        dict[data[1]] = dict.get(data[1], 0) + 1
# print(dict)
# print("-----")
# print("Most Frequent Status Code:", max(dict, key=dict.get))

order = [
    {"item": "Pizza", "price": 300, "type": "Veg"},
    {"item": "Chicken Burger", "price": 250, "type": "Non-Veg"},
    {"item": "Soft Drink", "price": 80, "type": "Beverage"},
]


def calulate_bill(order):
    total = 0
    for i in order:
        tax = 5
        if i["type"] == "Non-Veg":
            tax = tax + 13
        if i["type"] == "Veg":
            tax = tax + 5

        totalPrice = i["price"] + (i["price"] * (tax / 100))

        total = total + totalPrice
        if total > 1000:
            print("200 discount")
            total = total - 200

    print(total)


# calulate_bill(order)

network = {
    "Alice": {"Bob", "Charlie", "David"},
    "Bob": {"Alice", "David", "Eve"},
    "Charlie": {"Alice"},
}

# print(network["Alice"] )

ips = ["192.168.0.1", "256.0.0.1", "192.168.0", "abc.def.ghi", "10.0.0.1"]
def validate_ip(ips):
    for ip in ips:
        parts = ip.split(".")
        if len(parts) != 4:
            print(f"{ip} is invalid")
            continue
        valid = True
        for part in parts:
            if not part.isdigit() or not 0 <= int(part) <= 255:
                valid = False
                break
        if valid:
            print(f"{ip} is valid")
        else:
            print(f"{ip} is invalid")
# validate_ip(ips)


emails = [
    "user@gmail.com",
    "admin@domain",
    "test@.com",
    "hello@company.org",
    "user#mail.com"
]

def validate_email(emails):
    for email in emails:
        if "@" in email and "." in email.split("@")[1]:
            print(f"{email} is valid")
        else:
            print(f"{email} is invalid")
# validate_email(emails)


numbers = [
    "9876543210",
    "12345",
    "98a7654321",
    "0123456789",
    "9999999999"
]

def validate_mobile(numbers):
    for number in numbers:
        if number.isdigit() and len(number) == 10 and number[0] != "0":
            print(f"{number} is valid")
        else:
            print(f"{number} is invalid")
            
validate_mobile(numbers)

import re

def validate(passwords):
    valid = []
    for p in passwords:
        try:
            if len(p)<8 or not re.search(r"\d",p) or not re.search(r"\W",p):
                raise ValueError
            valid.append(p)
        except:
            pass
    return valid

print(validate(["abc@1234","weak","Pass#99"]))

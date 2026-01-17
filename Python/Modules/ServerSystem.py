import re
from collections import Counter

with open("Modules/serverLog.txt", "r", encoding="utf-8") as file:
    content = file.read()
    
    # Extract all emails using regex
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)
    ipPattern = re.findall(r"""\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b""", content)
    
    # Count emails
    email_counter = Counter(emails)
    ip_counter = Counter(ipPattern)
    print("Email Counter:", email_counter)
    print("Most common:", email_counter.most_common())
    print("IP Address Counter:", ip_counter)
    print("Most common IPs:", ip_counter.most_common())
    print(f"Active Email is {email_counter.most_common(1)}")
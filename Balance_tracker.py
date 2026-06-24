import re

balance = 0.0   # initial 


def extract_amount(message):
    """Extracts the first amount like 1,200.50 or 500 from the message."""
    match = re.search(r'(\d{1,3}(?:,\d{3})*|\d+)(\.\d+)?', message)
    if not match:
        return None
    
    amount_str = match.group(0).replace(",", "")
    return float(amount_str)

def update_balance(message, balance):
    amount = extract_amount(message)
    if amount is None:
        print("Could not find any money amount in the message.")
        return balance

    message_lower = message.lower()

    # Identify "sent" vs "received"
    if "sent to" in message_lower or "paid to" in message_lower:
        balance -= amount
        print(f"Detected outgoing transaction: -{amount}")
    elif "received" in message_lower or "deposit" in message_lower:
        balance += amount
        print(f"Detected incoming transaction: +{amount}")
    else:
        print("Message does not clearly indicate sent or received.")
    
    return balance


# Example usage
while True:
    sms = input("Paste M-Pesa message (or type 'exit'): ")
    if sms.lower() == "exit":
        break
    balance = update_balance(sms, balance)
    print(f"Current balance: {balance}\n")
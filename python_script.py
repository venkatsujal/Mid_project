import json
from collections import Counter

def read_orders(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def format_phone_number(phone):
    
    return f"{phone[:3]}-{phone[3:6]}-{phone[6:]}"

def process_customer_info(orders_data):
    customers = {}
    for order in orders_data:
        phone = format_phone_number(order['phone'])
        customers[phone] = order['name']
    return customers

def process_item_info(orders_data):
    item_counts = Counter()
    item_prices = {}
    
    for order in orders_data:
        for item in order['items']:
            item_name = item['name']
            item_price = item['price']
            item_counts[item_name] += 1
            item_prices[item_name] = item_price
    
    items = {name: {'price': item_prices[name], 'orders': count} for name, count in item_counts.items()}
    return items

def write_to_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def main(input_file_path):
    orders_data = read_orders(input_file_path)
    
    customers = process_customer_info(orders_data)
    items = process_item_info(orders_data)
    
    write_to_json(customers, 'customers.json')
    write_to_json(items, 'items.json')
    
    print("Processing complete. 'customers.json' and 'items.json' have been created.")

main('example_orders.json')


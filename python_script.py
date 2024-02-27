import json

def process_orders(file_path):

    with open(r'C:\Users\venka\OneDrive\Desktop\Mid_project\example_orders.json', 'r') as file:
        orders = json.load(file)

    customer_info = {}
    item_info = {}

    for order in orders:
        customer_info[order['phone']] = order['name']
        for item in order['items']:
            item_info[item['name']] = item['price']

    with open('updated_customers.json', 'w') as file:
        json.dump(customer_info, file, indent=4)

    with open('updated_items.json', 'w') as file:
        json.dump(item_info, file, indent=4)

    print("Customer and item information processed and saved.")

if __name__ == "__main__":
    process_orders(r'C:\Users\venka\OneDrive\Desktop\Mid_project\example_orders.json')



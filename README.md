
Restaurant Order Analysis Tool README
Overview:
This script is crafted to sift through a restaurant's order data encoded in a JSON file, meticulously extracting essential information about customers and their orders. The culmination of this process is the generation of two distinct JSON files:

1)customers.json: This file associates customer phone numbers with their names, offering a straightforward reference to customer identity.
2)items.json: This file aggregates each ordered item's pricing details alongside a count of how many times each item has been requested.

Requirements:
Running this script necessitates Python on your system, leaning solely on Python's intrinsic libraries for functionality, thereby negating the need for external package installations.

Design and Implementation:
The script's core revolves around parsing a JSON file populated with orders, each detailing a customer's contact information and their selected items. This data is then organized into two separate JSON files—customers.json and items.json—streamlining customer information and item statistics for subsequent analysis or application.

Functional Breakdown:
Process Orders: Central to the script, this function ingests the path to the JSON order file, orchestrating the data parsing and extraction process.

Data Storage Mechanisms:

1)Customers Dictionary: Utilizes phone numbers as unique keys linked to customer names, ensuring direct access to customer data.
2)Items Dictionary: Employs item names as keys, mapping to sub-dictionaries that record item prices and purchase frequencies, facilitating item data management and updates.

Data Processing Workflow
JSON Input Management: Leverages Python's json.load() to transform the JSON file into a manipulable Python structure, setting the stage for data iteration.
Order Iteration: Each order undergoes a twofold analysis:
1)Customer Data Extraction: Harvests and catalogs customer names and phone numbers in the customers dictionary.
2)Item Data Compilation: Evaluates each item within an order, initializing or updating its record in the items dictionary based on presence and purchase count.

Output Generation
customers.json Output: This step translates the customers dictionary into a neatly indented JSON file, mapping phone numbers to customer names.
items.json Output: Similarly, the items dictionary is converted into a JSON file, detailing item prices and order counts.

Script Execution
Path Configuration: An input_file_path variable is predefined within the script to point towards the JSON file location. Adjustments may be necessary to align with the actual file path.
Operational Feedback: Post-execution, the script signals the successful creation of output files through a console message.

Design Philosophy
Adaptability: Engineered for broad dataset compatibility, provided the JSON file adheres to the expected format.
Operational Efficiency: Utilizes dictionaries for brisk data access and manipulation, key for handling extensive datasets.
User-Centric Design: Maintains a clean code structure for ease of understanding and adaptation to varied datasets or requirements.

Instructions
1)Place your JSON order file in the script's directory or specify the file's full path.
2)Ensure the order file matches the expected structure, akin to example_orders.json.
3)djust the input_file_path within the script to your JSON file's path:input_file_path = 'path_to_your_order_file.json'
4)Execute the script:python python_script.py
After completion, the output directory will house the customers.json and items.json files.

Input and Output Formats
Input Format: The script expects a JSON file with an array of orders, each containing a customer's phone number, name, and a list of purchased items.
Output Files:
1)customers.json: Maps customer phone numbers to names.
2)items.json: Details each item's price and total order count.

Additional Notes
1)The script will overwrite existing customers.json and items.json files in the output directory.
2)Correct input file formatting is crucial for error-free processing.






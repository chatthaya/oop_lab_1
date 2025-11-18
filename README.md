# Lab 3: OOP Data Processing with DB and Table Classes

## Lab Overview
This lab focuses on building a simple database system using Object-Oriented Programming (OOP) in Python.  
The goal is to handle multiple CSV tables, perform filtering, aggregation, and join operations, simulating basic database functionalities.  
Students will learn how to design classes, manage data, and implement table operations programmatically.

## Project Structure
oop_lab_3/
├── Cities.csv # Dataset containing city information
├── Countries.csv # Dataset containing country information
├── data_processing.py # Main implementation of DB, Table, and DataLoader classes
├── test_lab3.py # Test script to run queries and validate results
└── README.md # This file

## Design Overview

### Class: `DataLoader`
- **Purpose**: Load CSV data into Python as a list of dictionaries.
- **Attributes**:
  - `base_path` – Path to folder containing CSV files.
- **Methods**:
  - `load_csv(filename)` – Reads a CSV file and returns a list of dictionaries.

### Class: `Table`
- **Purpose**: Represent a table and provide operations like filtering, aggregation, and joining.
- **Attributes**:
  - `table_name` – Name of the table.
  - `table` – List of dictionaries representing rows.
- **Methods**:
  - `filter(condition)` – Returns a new Table containing only rows that satisfy the condition. The new table name appends `_filtered`.
  - `aggregate(func, key)` – Applies a function `func` to the values of the specified column `key`.
  - `join(other_table, key)` – Performs an inner join with another table based on the given key.
  - `__str__()` – Returns a string representation of the table in the format `table_name: [rows]`.

### Class: `DB`
- **Purpose**: Manage multiple tables as a simple database.
- **Attributes**:
  - `tables` – Dictionary storing tables by their `table_name`.
- **Methods**:
  - `insert(table)` – Adds a Table object to the database.
  - `search(table_name)` – Retrieves a Table by its name.

## How to Test and Run Your Code

1. Make sure `Cities.csv` and `Countries.csv` are in the same directory as `data_processing.py`.
2. Run the main script to perform queries:
   ```bash
   python data_processing.py

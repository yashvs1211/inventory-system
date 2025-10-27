

import json
from datetime import datetime


# Global variable for storing inventory
stock_data = {}


def add_item(item: str = "default", qty: int = 0, logs=None) -> None:
    
    if logs is None:
        logs = []
    if not isinstance(item, str):
        raise TypeError("Item name must be a string.")
    if not isinstance(qty, int):
        raise TypeError("Quantity must be an integer.")

    if not item:
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item: str, qty: int) -> None:
    
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Warning: Tried to remove '{item}' which does not exist in stock.")


def get_qty(item: str) -> int:
    
    return stock_data.get(item, 0)


def load_data(file: str = "inventory.json") -> None:
    
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        print("Inventory file not found, starting with empty stock.")
    except json.JSONDecodeError:
        print("Error: Inventory file is corrupted, starting fresh.")
        stock_data = {}


def save_data(file: str = "inventory.json") -> None:
    
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
    except OSError as err:
        print(f"Error saving file: {err}")


def print_data() -> None:
    
    print("\nItems Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold: int = 5) -> list[str]:
   
    return [item for item, qty in stock_data.items() if qty < threshold]


def main() -> None:
  
    logs = []
    add_item("apple", 10, logs)
    add_item("banana", 2, logs)
    remove_item("apple", 3)

    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()

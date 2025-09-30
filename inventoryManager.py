import json

Default_THRESHOLD = 500

MAX_ITEMS = 1000

class InventoryManagerClass:
    def __init__(self, capacity_limit):
        self._capacity_limit = capacity_limit
        self.ProductList = []
        
    def ADD_ITEM(self, Item_Name, Quantity, price):
        if len(self.ProductList) < self._capacity_limit:
            self.ProductList.append({
                'Name': Item_Name,
                'QTY': Quantity,
                'Price': price
            })
            return True
        else:
            print("ERROR: Inventory is at full capacity.")
            return False

    def CalculateTotalValue(self):
        totalValue = 0
        for item in self.ProductList:
            totalValue += item['QTY'] * item['Price']
        return totalValue

    def check_Low_Stock(self):
        low_q = []
        for p in self.ProductList:
            if p['QTY'] < Default_THRESHOLD:
                low_q.append(p)
        return low_q
        
def GetInventoryReport(manager):
    report_data = {
        "TotalValue": manager.CalculateTotalValue(),
        "LowStockItems": manager.check_Low_Stock()
    }
    output_string = json.dumps(report_data, indent=2)
    print("\n--- INVENTORY REPORT ---")
    print(output_string)

def my_main_func():
    my_inventory = InventoryManagerClass(MAX_ITEMS)
    my_inventory.ADD_ITEM("Laptop", 150, 1200)
    my_inventory.ADD_ITEM("Mouse", 200, 25)
    my_inventory.ADD_ITEM("Keyboard", 350, 75)
    my_inventory.ADD_ITEM("Monitor", 400, 300)
    my_inventory.ADD_ITEM("Webcam", 550, 50)
    print(f"Current total inventory value: ${my_inventory.CalculateTotalValue()}")
    GetInventoryReport(my_inventory)
    calculate_value(my_inventory.ProductList)

def calculate_value(list_of_items):
    tmp = 0
    for i in list_of_items:
        tmp += i['Price']
    print(f"Average price per item is: ${tmp / len(list_of_items)}")

if __name__ == "__main__":
    my_main_func()
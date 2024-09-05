class Store:
    def __init__(self,name, store_type, capacity):
        self.name = name
        self.store_type = store_type
        self.capacity = capacity
        self.item = []
        
    def from_size(name, store_type, size):
        store = Store(name,store_type,size //2)
        return store
    
    def add_item(self,item_name:str):
        if len(self.item) < self.capacity:        
            self.item.append(item_name)
            return f"{item_name} added into the store"
        else:
            return f"Not enough capacity"
    
    def remove_item(self, item_name, amount):
        if item_name in self.item:
            self.item.remove(item_name)
            return f"{amount} {item_name} removed from the store"
        else:
            return f"Cannot remove {amount} {item_name}"
        
    def __repr__(self):
        return f"{self.name} of typr {self.store_type} with capacity {self.capacity} "


first_store = Store("First store", "Fruit and Veg", 20) 
second_store = Store.from_size("Second store", "Clothes", 500) 
print(first_store) 
print(second_store) 
print(first_store.add_item("potato")) 
print(second_store.add_item("jeans")) 
print(first_store.remove_item("tomatoes", 1)) 
print(second_store.remove_item("jeans", 1))   
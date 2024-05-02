class Store:
    def __init__(self):
        self.categories = {
            "cars": ["jeep", "Sedan", "SUV", "Minivan", "Coupe"],
            "furnitures": ["Chair", "beds", "Furnitures", "Couches", "Clocks"],
            "accessories": ["necklaces", "bracelets", "piercings", "rings", "eyewear"]
        }
        self.user_preferences = []

    def add_preferences(self, item):
        self.user_preferences.append(item.lower())  

    def recommendations(self, item):
        item = item.lower()  
        category = self.get_category(item)
        if category:
            print(f"Recommendations for '{item}':")
            print(*category, sep=", ")  
        else:
            print(f"Item '{item}' not found!")

    def get_category(self, item):
        for category, items in self.categories.items():
            if item in items:
                return items
        return None


store = Store()
store.add_preferences("beds")
store.add_preferences("jeep")
store.add_preferences("bracelets")

store.recommendations("bracelets")
store.recommendations("jeep")
store.recommendations("beds")
class Shoe:
    def __init__(self,shoe_color,shoe_size,shoe_style,shoe_price):
        self.color = shoe_color
        self.size  = shoe_size
        self.style = shoe_style
        self.price = shoe_price
    def change_price(self,new_price):
        self.price =0.81 * new_price
    def discount(self,discount):
        return self.price * (1 - discount)
    
    class Heels:
        def __init__(self, shoe_color, shoe_size, shoe_style, shoe_price, shoe_heels_height):

            Shoe.__init__(self,shoe_color,shoe_size,shoe_style,shoe_price)
            self.heels_height = shoe_heels_height
        
        def double_price(self):
            self.price = 2 * self.price
        
    class Ankle_Boot:
        def __init__ (self,shoe_color,shoe_size,shoe_style,shoe_price,shoe_boot_model):

            Shoe.__init__(self,shoe_color,shoe_size,shoe_style,shoe_price)
            self.boot_model = shoe_boot_model
        def calculate_discount(self,discount):
            return self.price * (1 - discount/2)
        
    
          

        

        
        
            

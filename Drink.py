class Drink:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        
        # Đóng gói giá bán bằng thuộc tính private (__price)
        self.__price = 0
        if price > 0:
            self.__price = price
            
        # Trạng thái kinh doanh mặc định là True (Đang bán)
        self.is_available = True

    # --- ĐÓNG GÓI BẢO MẬT: GETTER CHO GIÁ BÁN ---
    @property
    def price(self):
        """Cho phép đọc giá bán an toàn từ bên ngoài, không có Setter để tránh tự ý sửa giá"""
        return self.__price

    # --- INSTANCE METHOD: ĐỔI TRẠNG THÁI KINH DOANH ---
    def toggle_available(self):
        """Đảo ngược trạng thái kinh doanh (True <-> False)"""
        self.is_available = not self.is_available
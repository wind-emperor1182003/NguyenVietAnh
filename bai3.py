from anvil import *
import anvil.server

class Form1(Container):
    def __init__(self, **properties):
        # Gọi phương thức khởi tạo của lớp cha
        super().__init__(**properties)
        
        # Khởi tạo các thành phần của giao diện
        self.txtNumbers = TextBox()
        self.add_component(self.txtNumbers)
        
        self.lblSortedNumbers = Label()
        self.add_component(self.lblSortedNumbers)
        
        self.btnSort = Button(text="Sắp xếp", role="primary")
        self.btnSort.set_event_handler("click", self.btnSort_click)
        self.add_component(self.btnSort)
        
        self.btnReset = Button(text="Đặt lại", role="secondary")
        self.btnReset.set_event_handler("click", self.btnReset_click)
        self.add_component(self.btnReset)
        
        self.sorted_numbers = None

    def btnSort_click(self, **event_args):
        # Lấy dãy số từ người dùng
        numbers_str = self.txtNumbers.text
        
        # Gọi server function để sắp xếp dãy số
        self.sorted_numbers = anvil.server.call('sort_numbers', numbers_str)
        
        # Hiển thị dãy số sau khi sắp xếp
        self.lblSortedNumbers.text = 'Dãy số sau khi sắp xếp: ' + ', '.join(map(str, self.sorted_numbers))

    def btnReset_click(self, **event_args):
        # Đặt lại trạng thái của các thành phần giao diện
        self.txtNumbers.text = ''
        self.lblSortedNumbers.text = ''
        self.sorted_numbers = None

# Khởi tạo ứng dụng Anvil
anvil.server.wait_forever()

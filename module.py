
class Cars:

    def __init__(self, color, seat):
        self.color = color  # 顏色屬性
        self.seat = seat  # 座位屬性

    def drive(self, color, seat):
        self.color = color  # 顏色屬性
        self.seat = seat
        print(f"My car is {self.color} and {self.seat} seats.")

mazda=Cars('bluee',4)

# class GFG:
      
#     # methods
#     def add(self, a, b):
#         return a + b
#     def sub(self, a, b):
#         return a - b
  
# # explicit function      
# def method():
#     print("GFG")


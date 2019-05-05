from Pants import Paints
class SalesPerson:
    """The SalesPerson class represents an employee in the store

    """
    """
    """
    def __init__(self, first_name, last_name, employee_id, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = []
        self.total_sales = 0

    def sell_pants(self, paint):
        self.pants_sold.append(paint)
        self.total_sales += 1

    def display_sales(self):
        for item in self.pants_sold:
            print("color:{}, waist_size:{}",item.color, item.length)

    def calculate_sales(self):
        total = 0
        for item in self.pants_sold:
            total += item.price
        return total

    def calculate_commission(self, percentage):
        sales_total = self.calculate_sales()
        return sales_total * percentage 

def check_results():
    pants_one = Paints('red', 35, 36, 15.12)
    pants_two = Paints('blue', 40, 38, 24.12)
    pants_three = Paints('tan', 28, 30, 8.12)
    
    salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)
    
    assert salesperson.first_name == 'Amy'
    assert salesperson.last_name == 'Gonzalez'
    assert salesperson.employee_id == 2581923
    assert salesperson.salary == 40000
    assert salesperson.pants_sold == []
    assert salesperson.total_sales == 0
    
    salesperson.sell_pants(pants_one)
    salesperson.pants_sold[0] == pants_one.color
    
    salesperson.sell_pants(pants_two)
    salesperson.sell_pants(pants_three)
    assert len(salesperson.pants_sold) == 3
    assert round(salesperson.calculate_sales(),2) == 47.36
    assert round(salesperson.calculate_commission(.1),2) == 4.74
    
    print('Great job, you made it to the end of the code checks!')
    
check_results()
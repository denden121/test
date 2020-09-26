class Car():
    def __init__(self, model, manufacturer, body, year):
        self.model = model
        self.body = body
        self.manufacturer = manufacturer
        try:
            self.year = int(year)
        except ValueError:
            while True:
                print("Данные не верны, повторите ввод")
                year = input()
                if year.isdigit():
                    self.year = year
                    break
        # self.id = identifier

    def __str__(self):
        return self.manufacturer+' '+self.model+' '+self.body+' '+ str(self.year)
    
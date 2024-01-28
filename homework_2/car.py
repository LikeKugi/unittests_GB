from homework_2.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, company, model, year_release):
        self.year_release = year_release
        self.model = model
        self.company = company
        self.wheels_count = 4
        self.speed = 0

    def test_drive(self):
        self.speed = 60

    def park(self):
        self.speed = 0




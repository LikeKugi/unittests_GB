import unittest

from homework_2.car import Car
from homework_2.motorbike import Motorbike
from homework_2.vehicle import Vehicle


class MyTestCase(unittest.TestCase):

    def test_car_instance(self):
        car = Car('test', 'z1', 2023)
        self.assertEqual(isinstance(car, Vehicle), True)

    def test_car_wheels(self):
        car = Car('test', 'z1', 2023)
        self.assertEqual(car.wheels_count, 4)

    def test_car_drive(self):
        car = Car('test', 'z1', 2023)
        car.test_drive()
        self.assertEqual(car.speed, 60)

    def test_car_parking(self):
        car = Car('test', 'z1', 2023)
        car.test_drive()
        self.assertEqual(car.speed, 60)
        car.park()
        self.assertEqual(car.speed, 0)

    def test_motorbike_instance(self):
        bike = Motorbike('test', 'z1', 2023)
        self.assertEqual(isinstance(bike, Vehicle), True)

    def test_motorbike_wheels(self):
        bike = Motorbike('test', 'z1', 2023)
        self.assertEqual(bike.wheels_count, 2)

    def test_motorbike_drive(self):
        bike = Motorbike('test', 'z1', 2023)
        bike.test_drive()
        self.assertEqual(bike.speed, 75)

    def test_motorbike_parking(self):
        bike = Motorbike('test', 'z1', 2023)
        bike.test_drive()
        self.assertEqual(bike.speed, 75)
        bike.park()
        self.assertEqual(bike.speed, 0)


if __name__ == '__main__':
    unittest.main()

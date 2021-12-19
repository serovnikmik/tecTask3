import unittest
import time
from main import min_number, max_number, comp_of_numbers, sum_of_numbers, check_for_10


class TestNumbers(unittest.TestCase):

    def test_sum_of_numbers(self):
        self.assertEquals(sum_of_numbers([1, 1]), 2)
        self.assertEquals(sum_of_numbers([-10, 900]), 890)
        self.assertEquals(sum_of_numbers([123, 321]), 444)
        self.assertEquals(sum_of_numbers([0, 0]), 1)
        self.assertEquals(sum_of_numbers([-9, -7]), -16)

    def test_comp_of_numbers(self):
        self.assertEquals(comp_of_numbers([8, 9]), 72)
        self.assertEquals(comp_of_numbers([-1, -2]), 2)
        self.assertEquals(comp_of_numbers([-1, 2, 3]), -6)
        self.assertEquals(comp_of_numbers([-10, -10, -20, -30]), 60000)
        self.assertEquals(comp_of_numbers([-300, 1000, 0]), 0)

    def test_max_number(self):
        self.assertEquals(max_number([1, 2, 3]), 3)
        self.assertEquals(max_number([0, 0]), 0)
        self.assertEquals(max_number([1, -1, 8]), 8)
        self.assertEquals(max_number([-2, -1]), -1)

    def test_min_number(self):
        self.assertEquals(min_number([9, 8, 7]), 7)
        self.assertEquals(min_number([-9, 8, 1]), -9)
        self.assertEquals(min_number([0.8, -0.9]), -0.9)

    def test_check_for_10(self):
        self.assertEquals(check_for_10(['3', '10', '0']), True)
        self.assertEquals(check_for_10(['1']), False)
        self.assertEquals(check_for_10(['9 9']), False)
        self.assertEquals(check_for_10(['0', '10', '10']), True)

    def test_speed_once(self, obj_counter):
        example = []
        for i in range(obj_counter):
            example.append(10)
        start_time = time.time()
        self.assertEquals(sum_of_numbers(example), 10 * obj_counter)
        self.assertEquals(comp_of_numbers(example), 10 ** obj_counter)
        self.assertEquals(min_number(example), 10)
        self.assertEquals(max_number(example), 10)
        return time.time() - start_time

    def test_speed(self):
        print("Скорость с 1-ой 10-ой" + str(test_speed_once(1)))
        print("Скорость с 2-мя 10-ами" + str(test_speed_once(2)))
        print("Скорость с 3-мя 10-ами" + str(test_speed_once(3)))

unittest.main()
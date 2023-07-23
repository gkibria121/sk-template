import unittest
from sk_report_generator.reporter.formatter.custom_format_functions.floor import Floor
from sk_report_generator.reporter.formatter.custom_format_functions.floor import FloorSpec
from sk_report_generator.reporter.formatter.custom_format_functions.floor import FloorSignificance
from sk_report_generator.reporter.formatter.custom_format_functions.floor import Default
from sk_report_generator.reporter.formatter.custom_format_functions.default import DefaultCustomFormat




class TestFloor(unittest.TestCase):

    def setUp(self):
        self.default = DefaultCustomFormat()
        self.floor = Floor()
        self.floor.set_successor(self.default)

    def test_floor(self):
        value = 10.2
        format_spec =  {'floor' : True}

        result = self.floor.format(value,format_spec)
        self.assertEqual(result, '10.0')

        value = 200.999
        format_spec =  {'floor' : True}

        result = self.floor.format(value,format_spec)
        self.assertEqual(result, '200.0')

class TestFloorSpec(unittest.TestCase):

    def setUp(self):
        self.default = Default()
        self.floor = FloorSpec()
        self.floor.set_next(self.default)

    def test_floor_spec(self):
        value = 10.2
        format_spec =  {'floor' : True}

        result = self.floor.run(value,format_spec)
        self.assertEqual(result, '10.0')

        value = 200.999
        format_spec =  {'floor' : True}

        result = self.floor.run(value,format_spec)
        self.assertEqual(result, '200.0')


class TestFloorSignificance(unittest.TestCase):

    def setUp(self):
        self.default = Default()
        self.floor = FloorSignificance()
        self.floor.set_next(self.default)

    def test_floor_significance(self):
        value = 10.2
        format_spec =  {'floor-significance' : 1}

        result = self.floor.run(value,format_spec)
        self.assertEqual(result, '10.0')

        value = 200.999
        format_spec =  {'floor-significance' : 5}

        result = self.floor.run(value,format_spec)
        self.assertEqual(result, '200.0')

        format_spec =  {'floor-significance' : 7}

        result = self.floor.run(value,format_spec)
        self.assertEqual(result, '196.0')


        value = 10.2
        format_spec =  {'floor-significance' : 0.2}

        result = self.floor.run(value,format_spec)
        self.assertEqual(result, '10.2')

        value = 200.999
        format_spec =  {'floor-significance' : 0.3}

        result = self.floor.run(value,format_spec)
        self.assertEqual(result, '200.7')

        format_spec =  {'floor-significance' : 7}

        result = self.floor.run(value,format_spec)
        self.assertEqual(result, '196.0')

        format_spec =  {'floor-significance' : 0.9}

        result = self.floor.run(value,format_spec)
        self.assertEqual(result, '200.7')


if __name__ == "__main__":
    unittest.main()
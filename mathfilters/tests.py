import unittest
import logging
from decimal import Decimal

from .templatetags import mathfilters


logging.basicConfig(level=logging.ERROR)


class NumericConverterTest(unittest.TestCase):

    def test_string(self):
        self.assertEqual(13, mathfilters.valid_numeric('13'))
        self.assertEqual(-13, mathfilters.valid_numeric('-13'))
        self.assertEqual(13.3, mathfilters.valid_numeric('13.3'))
        self.assertEqual(-13.3, mathfilters.valid_numeric('-13.3'))

    def test_int(self):
        self.assertEqual(13, mathfilters.valid_numeric(13))
        self.assertEqual(-13, mathfilters.valid_numeric(-13))

    def test_float(self):
        self.assertEqual(13.3, mathfilters.valid_numeric(13.3))
        self.assertEqual(-13.3, mathfilters.valid_numeric(-13.3))

    def test_decimal(self):
        self.assertEqual(Decimal('2.3'), mathfilters.valid_numeric(Decimal('2.3')))
        self.assertEqual(Decimal('-2.3'), mathfilters.valid_numeric(Decimal('-2.3')))


class DecimalFloatHandlerTest(unittest.TestCase):

    def test_int_float(self):
        a, b = mathfilters.handle_float_decimal_combinations(1, 2.0, '+')
        self.assertTrue(isinstance(a, int), 'Type is {0}'.format(type(a)))
        self.assertTrue(isinstance(b, float), 'Type is {0}'.format(type(b)))

    def test_float_float(self):
        a, b = mathfilters.handle_float_decimal_combinations(1.0, 2.0, '+')
        self.assertTrue(isinstance(a, float), 'Type is {0}'.format(type(a)))
        self.assertTrue(isinstance(b, float), 'Type is {0}'.format(type(b)))

    def test_float_decimal(self):
        a, b = mathfilters.handle_float_decimal_combinations(1.0, Decimal('2.0'), '+')
        self.assertTrue(isinstance(a, Decimal), 'Type is {0}'.format(type(a)))
        self.assertTrue(isinstance(b, Decimal), 'Type is {0}'.format(type(b)))

    def test_decimal_float(self):
        a, b = mathfilters.handle_float_decimal_combinations(Decimal('2.0'), 1.0, '+')
        self.assertTrue(isinstance(a, Decimal), 'Type is {0}'.format(type(a)))
        self.assertTrue(isinstance(b, Decimal), 'Type is {0}'.format(type(b)))

    def test_decimal_int(self):
        a, b = mathfilters.handle_float_decimal_combinations(Decimal('2.0'), 1, '+')
        self.assertTrue(isinstance(a, Decimal), 'Type is {0}'.format(type(a)))
        self.assertTrue(isinstance(b, int), 'Type is {0}'.format(type(b)))

    def test_decimal_decimal(self):
        a, b = mathfilters.handle_float_decimal_combinations(Decimal('2.0'), Decimal('1.0'), '+')
        self.assertTrue(isinstance(a, Decimal), 'Type is {0}'.format(type(a)))
        self.assertTrue(isinstance(b, Decimal), 'Type is {0}'.format(type(b)))


class SubtractionTest(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(3, mathfilters.sub('7', '4'))

    def test_negative_result(self):
        self.assertEqual(-20, mathfilters.sub('13', '33'))

    def test_negative_minuend(self):
        self.assertEqual(-42, mathfilters.sub('-23', '19'))

    def test_negative_subtrahend(self):
        self.assertEqual(6, mathfilters.sub('5', '-1'))

    def test_float(self):
        self.assertEqual(1.5, mathfilters.sub('-0.5', '-2'))

    def test_decimal_decimal(self):
        val1 = Decimal('9.9')
        val2 = Decimal('6.6')
        self.assertEqual(Decimal('3.3'), mathfilters.sub(val1, val2))

    def test_decimal_int(self):
        val1 = Decimal('9.999')
        val2 = 9
        self.assertEqual(Decimal('0.999'), mathfilters.sub(val1, val2))

    def test_float_decimal(self):
        """Regression test for issue #3."""
        result = mathfilters.sub('201.7', Decimal('3.1'))
        self.assertTrue(198 < result < 199, repr(result))

    def test_decimal_float(self):
        """Regression test for issue #3."""
        result = mathfilters.sub(Decimal('201.7'), '3.1')
        self.assertTrue(198 < result < 199, repr(result))


class MultiplicationTest(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(12, mathfilters.mul('3', '4'))

    def test_negative1(self):
        self.assertEqual(-10, mathfilters.mul('2', '-5'))

    def test_negative2(self):
        self.assertEqual(-10, mathfilters.mul('-2', '5'))

    def test_negative3(self):
        self.assertEqual(10, mathfilters.mul('-2', '-5'))

    def test_float(self):
        self.assertEqual(4.2, mathfilters.mul('2.1', '2'))

    def test_decimal_decimal(self):
        val1 = Decimal('3.3')
        val2 = Decimal('3')
        self.assertEqual(Decimal('9.9'), mathfilters.mul(val1, val2))

    def test_decimal_int(self):
        val1 = Decimal('3.3')
        val2 = 3
        self.assertEqual(Decimal('9.9'), mathfilters.mul(val1, val2))

    def test_float_decimal(self):
        """Regression test for issue #3."""
        result = mathfilters.mul('2.2', Decimal('3.1'))
        self.assertTrue(6 < result < 7, repr(result))

    def test_decimal_float(self):
        """Regression test for issue #3."""
        result = mathfilters.mul(Decimal('2.2'), '3.1')
        self.assertTrue(6 < result < 7, repr(result))


class DivisionTest(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(3, mathfilters.div('12', '4'))

    def test_negative1(self):
        self.assertEqual(-2, mathfilters.div('10', '-5'))

    def test_negative2(self):
        self.assertEqual(-2, mathfilters.div('-10', '5'))

    def test_negative3(self):
        self.assertEqual(2, mathfilters.div('-10', '-5'))

    def test_float1(self):
        self.assertEqual(8.5, mathfilters.div('27.2', '3.2'))

    def test_decimal_decimal(self):
        val1 = Decimal('9.9')
        val2 = Decimal('3.3')
        self.assertEqual(Decimal('3'), mathfilters.div(val1, val2))

    def test_decimal_int(self):
        val1 = Decimal('9.9')
        val2 = 3
        self.assertEqual(Decimal('3.3'), mathfilters.div(val1, val2))

    def test_float_decimal(self):
        """Regression test for issue #3."""
        result = mathfilters.div('201.7', Decimal('3.1'))
        self.assertTrue(65 < result < 66, repr(result))

    def test_decimal_float(self):
        """Regression test for issue #3."""
        result = mathfilters.div(Decimal('201.7'), '3.1')
        self.assertTrue(65 < result < 66, repr(result))


class IntegerDivisionTest(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(3, mathfilters.intdiv('12', '4'))

    def test_negative1(self):
        self.assertEqual(-2, mathfilters.intdiv('10', '-5'))

    def test_negative2(self):
        self.assertEqual(-2, mathfilters.intdiv('-10', '5'))

    def test_negative3(self):
        self.assertEqual(2, mathfilters.intdiv('-10', '-5'))

    def test_float1(self):
        result = mathfilters.intdiv('7', '2')
        self.assertTrue(isinstance(result, int))
        self.assertEqual(3, result)

    def test_float2(self):
        result = mathfilters.intdiv('27.2', '3.2')
        self.assertTrue(isinstance(result, float))
        self.assertEqual(8.0, result)

    def test_decimal_decimal(self):
        val1 = Decimal('7.0')
        val2 = Decimal('2.0')
        self.assertEqual(Decimal('3'), mathfilters.intdiv(val1, val2))

    def test_decimal_int(self):
        val1 = Decimal('9.9')
        val2 = 3
        self.assertEqual(Decimal('3'), mathfilters.intdiv(val1, val2))

    def test_float_decimal(self):
        """Regression test for issue #3."""
        result = mathfilters.intdiv('201.7', Decimal('3.1'))
        self.assertEqual(Decimal('65'), result)

    def test_decimal_float(self):
        """Regression test for issue #3."""
        result = mathfilters.intdiv(Decimal('201.7'), '3.1')
        self.assertEqual(Decimal('65'), result)


class AbsoluteTest(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(21, mathfilters.absolute('21'))

    def test_negative(self):
        self.assertEqual(21, mathfilters.absolute('-21'))

    def test_positive_float(self):
        self.assertEqual(2.3, mathfilters.absolute('2.3'))

    def test_negative_float(self):
        self.assertEqual(2.3, mathfilters.absolute('-2.3'))

    def test_positive_decimal(self):
        self.assertEqual(Decimal('9.99'), mathfilters.absolute(Decimal('9.99')))

    def test_negative_decimal(self):
        self.assertEqual(Decimal('9.99'), mathfilters.absolute(Decimal('-9.99')))


class ModuloTest(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(2, mathfilters.mod('12', '5'))

    def test_negative(self):
        self.assertEqual(-3, mathfilters.mod('12', '-5'))

    def test_float(self):
        self.assertEqual(3.0, mathfilters.mod('27.5', '3.5'))

    def test_float_decimal(self):
        """Regression test for issue #3."""
        result = mathfilters.mod('7.8', Decimal('2.2'))
        self.assertTrue(1 < result < 2, repr(result))

    def test_decimal_float(self):
        """Regression test for issue #3."""
        result = mathfilters.mod(Decimal('7.8'), '2.2')
        self.assertTrue(1 < result < 2, repr(result))


class AdditionTest(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(11, mathfilters.addition('7', '4'))

    def test_negative_negative(self):
        self.assertEqual(-4, mathfilters.addition('-1', '-3'))

    def test_negative_positive(self):
        self.assertEqual(6, mathfilters.addition('-3', '9'))

    def test_positive_negative(self):
        self.assertEqual(4, mathfilters.addition('5', '-1'))

    def test_float_int(self):
        self.assertEqual(2.5, mathfilters.addition('0.5', '2'))

    def test_decimal_decimal(self):
        val1 = Decimal('7.3')
        val2 = Decimal('2.7')
        self.assertEqual(Decimal('10'), mathfilters.addition(val1, val2))

    def test_decimal_int(self):
        val1 = Decimal('1.9')
        val2 = 4
        self.assertEqual(Decimal('5.9'), mathfilters.addition(val1, val2))

    def test_float_decimal(self):
        result = mathfilters.addition('3.7', Decimal('11.1'))
        self.assertEqual(Decimal('14.8'), result)


if __name__ == '__main__':
    unittest.main()

# Testing environment

from django.test import TestCase
from ..utils import clean_number, parse_message


class CleanNumberTestCase(TestCase):

    def testCleanNumberLeavesNumbers(self):
        self.assertEqual('12345', clean_number('12345'))

    def testCleanNumberRemovesNonnumbers(self):
        self.assertEqual('12345', clean_number('a+1aszz23!!!45'))


class SmsParserTestCase(TestCase):

    def setUp(self):
        pass

    def testSmsGetsRoute(self):
        output = parse_message("yesoch knows all")
        self.assertEqual(output['command'], 'yesoch')

    def testSmsLowerCasesStuff(self):
        output = parse_message("YESOCH knows all")
        self.assertEqual(output['command'], 'yesoch')

    def testSmsGetsArguments(self):
        output = parse_message("YESOCH knows all")
        self.assertEqual(output['args'], ['knows', 'all'])

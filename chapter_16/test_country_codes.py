import unittest

from country_codes import get_country_code


class CountryCodes(unittest.TestCase):

    def test_yement_code_returned(self):
        assert get_country_code('Yemen, Rep.') == 'ye', 'Incorrect code'

    def test_none_returned(self):
        assert not get_country_code('spam'), 'Unknown country name still ' \
                                          'returns code'

    def test_code_returned_as_expeced(self):
        assert get_country_code('Albania') == 'al'


unittest.main()

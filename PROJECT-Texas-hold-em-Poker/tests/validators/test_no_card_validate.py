import unittest


from poker.validators import NoCardValidator

class TestNoCardValidate(unittest.TestCase):
    def test_hand_have_no_card(self):

        validator=NoCardValidator(cards=[])

        self.assertEqual(validator.is_valid(),True)

    def test_return_no_cards(self):
        validator=NoCardValidator(cards=[])

        self.assertEqual(validator.valid_card(),[])



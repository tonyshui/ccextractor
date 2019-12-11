import unittest

def censor(text, word):
    return text.replace(word, '[bleep]')

class TestSome(unittest.TestCase):

    def test_not_found(self):
        self.assertEqual(censor("", "bar"), "")
        self.assertEqual(censor("f", "bar"), "f")
        self.assertEqual(censor("foo", "bar"), "foo")
        self.assertEqual(censor("fooo", "bar"), "fooo")

    def test_found(self):
        self.assertEqual(censor("bar", "bar"), "[bleep]")
        self.assertEqual(censor("bar!", "bar"), "[bleep]!")
        self.assertEqual(censor("cow bar", "bar"), "cow [bleep]")

    def test_parts(self):
        self.assertEqual(censor("foobar", "bar"), "foo[bleep]")
        self.assertEqual(censor("bare", "bar"), "[bleep]e")

    def test_capital(self):
        self.assertEqual(censor("Bar", "bar"), "Bar")

    def test_multiple(self):
        self.assertEqual(censor("foo bar bar foo", "bar"), "foo [bleep] [bleep] foo")

if __name__ == '__main__':
    unittest.main()
import unittest

from app import app

class TestPangram(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client(self)

    def test_PangramTrue(self):
        response = self.app.get('/pangram?key=The%20quick%20brown%20fox%20jumps%20over%20the%20lazy9%%20dog')
        self.assertTrue(response.json['isPangram'])

    def test_PangramFalse(self):
        response = self.app.get('/pangram?key=jkdsj%20KAj%20jldj937')
        self.assertFalse(response.json['isPangram'])

if __name__ == '__main__':
    unittest.main()

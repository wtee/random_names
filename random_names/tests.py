import unittest

from pyramid import testing

from .views.american import data_view, handle_request, female_first_names, male_first_names, no_gender_first_names, surnames

class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.config.add_route('american', '/american.html')
        self.config.add_route('american_text', '/american.txt')
        self.config.add_route('american_json', '/american.json')
        self.config.add_route('american_data', '/american/data.json')

    def tearDown(self):
        testing.tearDown()

    def test_american_html(self):
        params = {"gender": "male", "number": 5}

        request = testing.DummyRequest(params=params, path="/american.html")
        info = handle_request(request)
        first, last = info["names"][0].split(" ")

        self.assertEqual(params["number"], len(info["names"]))
        self.assertTrue(first in male_first_names)
        self.assertTrue(last in surnames)
        self.assertTrue("description" in info.keys())
        self.assertTrue(info["options"][0] == params["gender"])
        self.assertTrue(info["numbers"][0] == params["number"])

    def test_american_json(self):
        params = {"gender": "gender non-specific", "number": 1}

        request = testing.DummyRequest(params=params, path="/american.json")
        info = handle_request(request)
        first, last = info["names"][0].split(" ")

        self.assertEqual(params["number"], len(info["names"]))
        self.assertTrue(first in no_gender_first_names)
        self.assertTrue(last in surnames)

    def test_american_text(self):
        params = {"gender": "female", "number": 10}
        request = testing.DummyRequest(params=params, path="/american.txt")
        info = handle_request(request)
        first, last = info["names"][0].split(" ")

        self.assertEqual(params["number"], len(info["names"]))
        self.assertTrue(first in female_first_names)
        self.assertTrue(last in surnames)

    def test_american_data(self):
        request = testing.DummyRequest(path="/american/data.json")
        info = data_view(request)

        self.assertTupleEqual(tuple(female_first_names), info["female_names"])
        self.assertTupleEqual(tuple(male_first_names), info["male_names"])
        self.assertTupleEqual(tuple(no_gender_first_names), info["gender_non_specific_names"])
        self.assertTupleEqual(tuple(surnames), info["surnames"])
    
"""
class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from random_names import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'Pyramid' in res.body)
"""
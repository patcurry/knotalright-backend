from django.test import Client, TestCase

from knots.models import Knot
from knots.models import AlternativeName

from knots.views import KnotList
from knots.views import KnotDetail


client = Client()

class KnotTestCase(TestCase):

    def setUp(self):
        Knot.objects.create(name="Figure eight on a bight")
        Knot.objects.create(name="Figure eight follow through")
        AlternativeName.objects.create(name="Trace eight", knot=Knot.objects.get(name="Figure eight on a bight"))

    def test_knots_are_created(self):
        f8ob = Knot.objects.get(name="Figure eight on a bight")
        f8ft = Knot.objects.get(name="Figure eight follow through")
        self.assertNotEqual(f8ob, f8ft)

    def test_knot_has_alternative_name(self):
        f8ob = Knot.objects.get(name="Figure eight on a bight")
        an = AlternativeName.objects.get(name="Trace eight")
        self.assertEqual(an.knot, f8ob)
        self.assertEqual(f8ob.alternativename_set.first(), an)


    def test_KnotList_returns_status_code_200(self):
        response = client.get('/knots/')
        self.assertEqual(response.status_code, 200)
        
    def test_KnotList_returns_list_of_knot_names(self):
        response = client.get('/knots/')
        self.assertIn(Knot.objects.get(id=1).name, response.rendered_content)
        self.assertIn(Knot.objects.get(id=2).name, response.rendered_content)

    def test_KnotDetail_returns_specific_knot(self):
        response = client.get('/knots/figure-eight-follow-through/')
        self.assertIn(Knot.objects.get(name="Figure eight follow through").name, response.rendered_content)
        self.assertNotIn(Knot.objects.get(name="Figure eight on a bight").name, response.rendered_content)


from django.test import TestCase
from django.shortcuts import reverse

from leads.views import landing_page

class HomePageTest(TestCase):

    def test_get(self):
        response =  self.client.get(reverse("landing-page"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, "landing.html")
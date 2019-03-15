from rest_framework.test import APITestCase
from callhub.handlers.call_logic import retreive_num
from django.urls import reverse
from django.http import HttpResponseRedirect
from callhub.models import FibSeries


class FibSeriesTest(APITestCase):
    def setUp(self):
        self.num = 6

    def test_retreive_num(self):
        result = retreive_num(self.num)
        expected_keys = (
            'num',
            'result',
            'execution_time'
        )
        expected_result = 8
        self.assertIsNotNone(result, expected_keys)
        self.assertEqual(int(result['result']), expected_result)
        self.assertEqual(FibSeries.objects.all().count(), 6)

    def test_fibview(self):
        url = reverse('fibonacci')
        response = self.client.get(url, {'num': self.num})
        self.assertTemplateUsed(response, 'fibseries.html')

    def test_fibhtmlview(self):
        url = reverse('fibonacci')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'fibseries.html')
        response = self.client.post(url, {'fibNo': self.num})
        self.assertTrue(isinstance(response, HttpResponseRedirect))

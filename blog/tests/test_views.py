from django.test import TestCase, Client
from django.utils import timezone as tz
from django.urls import reverse

from blog.models import Post, Comment


class ViewTestCase(TestCase):
    fixtures = ['dump.json']

    def setUp(self):
        self.client = Client()
        self.last_post = Post.objects.filter(modified_date__lte=tz.now()).order_by('-modified_date')[0]
        self.posts_year_2019 = Post.objects.filter(modified_date__year=2019)


    def test_index(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('first_row_reciepts' in resp.context)
        self.assertContains(resp, self.last_post.title.title(), html=True)

    def test_list_of_reciepts_for_2019(self):
        resp = self.client.get('/reciepts/year/2019')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, '2019')

        months = set([p.modified_date.month for p in self.posts_year_2019])
        self.assertEqual(len(months), len(resp.context["months"]))


    def test_list_of_reciepts_for_Jan_2019(self):
        resp = self.client.get('/reciepts/year/2019/month/01')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'January')

        jan = Post.objects.filter(modified_date__month=1)
        self.assertEqual(len(jan), len(resp.context["month_reciepts"]))


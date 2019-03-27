from django.test import TestCase
from django.utils import timezone as tz
import datetime as dt

from blog.models import Post, Comment


class PostModelTest(TestCase):
    fixtures = ['dump.json']

    def setUp(self):
        self.posts_2019 = Post.objects.get_reciepts_year(year=2019)
        self.posts_jan_2019 = Post.objects.get_reciepts_month(year=2019, month=1)
        self.posts_8 = Post.objects.get_last_reciepts(quant=8)
        self.post_id_0 = Post.objects.get_reciept_by_id(1)[0]


    def test_were_selected_only_2019_posts(self):
        self.assertEqual(set([p.modified_date.year for p in self.posts_2019]), {2019})


    def test_were_selected_only_jan_2019_posts(self):
        self.assertEqual(set([p.modified_date.month for p in self.posts_jan_2019]), {1})


    def test_were_selected_8_newest_posts(self):
        self.assertTrue(len(self.posts_8) <= 8)

    def test_was_selected_post_id_0(self):
        self.assertEqual(self.post_id_0.id, 1)


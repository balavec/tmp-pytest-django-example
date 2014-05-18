# coding: utf-8
from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth.models import User


class MyTestCase(TestCase):

    def test_one(self):
        for i in xrange(5):
            User.objects.create(username=str(i))
        assert User.objects.count() == 5

    def test_two(self):
        for i in xrange(4):
            User.objects.create(username=str(i))
        assert User.objects.count() == 4

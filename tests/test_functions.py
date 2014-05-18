from django.contrib.auth.models import User

import pytest


@pytest.mark.django_db
def test_func_one():
    assert User.objects.count() == 0

@pytest.mark.django_db
def test_func_two():
   assert User.objects.count() == 0

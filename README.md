```
% git clone https://github.com/l0kix2/tmp-pytest-django-example.git
% cd tmp-pytest-django-example
% mkvirtualenv venv
% pip install -r requirements.txt
% pip install -e .
% py.test -n2 --tb=line 
============ test session starts ============ 
platform darwin -- Python 2.7.6 -- py-1.4.20 -- pytest-2.5.2 -- /Users/l0ki/.virtualenvs/tmp-da9126efef704fb7/bin/python
plugins: django, xdist
[gw0] darwin Python 2.7.6 cwd: /Users/l0ki/dev/python/playground/pytest-django-bugs
[gw1] darwin Python 2.7.6 cwd: /Users/l0ki/dev/python/playground/pytest-django-bugs
[gw1] Python 2.7.6 (default, Mar 23 2014, 01:13:43)  -- [GCC 4.2.1 Compatible Apple LLVM 5.1 (clang-503.0.38)]
[gw0] Python 2.7.6 (default, Mar 23 2014, 01:13:43)  -- [GCC 4.2.1 Compatible Apple LLVM 5.1 (clang-503.0.38)]
gw0 [4] / gw1 [4]
scheduling tests via LoadScheduling

tests/test_django_base.py:10: MyTestCase.test_one
tests/test_django_base.py:15: MyTestCase.test_two
[gw0] PASSED tests/test_django_base.py:15: MyTestCase.test_two
[gw1] PASSED tests/test_django_base.py:10: MyTestCase.test_one
tests/test_functions.py:6: test_func_one
[gw0] ERROR tests/test_functions.py:6: test_func_one
tests/test_functions.py:10: test_func_two
[gw0] ERROR tests/test_functions.py:10: test_func_two

============  ERRORS ============ 
____________ ERROR at setup of test_func_one ____________
[gw0] darwin -- Python 2.7.6 /Users/l0ki/.virtualenvs/tmp-da9126efef704fb7/bin/python
E   Failed: Database access not allowed, use the "django_db" mark to enable
____________ ERROR at setup of test_func_two ____________
[gw0] darwin -- Python 2.7.6 /Users/l0ki/.virtualenvs/tmp-da9126efef704fb7/bin/python
E   Failed: Database access not allowed, use the "django_db" mark to enable
============   2 passed, 2 error in 1.09 seconds ============  
(tmp-da9126efef704fb7)(master) [1] %

```


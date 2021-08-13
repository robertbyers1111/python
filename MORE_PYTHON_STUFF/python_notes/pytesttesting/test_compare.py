import pytest

@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num >= 100

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
@pytest.mark.zzz
def test_multiplication_11(num, output):
   assert 11*num == output

@pytest.mark.wtf
def test_less():
   num = 100
   assert num < 200

@pytest.mark.xfail
@pytest.mark.great
def test_greater():
   num = 100
   assert num > 100

@pytest.mark.xfail
@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num >= 100

@pytest.mark.skip
@pytest.mark.others
def test_less():
   num = 100
   assert num < 200

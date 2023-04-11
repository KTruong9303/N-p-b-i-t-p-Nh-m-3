import pytest
from src.index import check_triangle, check_prime_number, print_Prime
from unittest.mock import patch
   
#tamgiac   
@pytest.mark.parametrize(
    "a, b, c, check_triangle",
    [(3,3,3, True), (1,1,0, False), (2,1,1, False), (3,4,5, True)],
)
def test_check_triangle(a, b, c, check_triangle):
    assert check_triangle(a, b, c) == check_triangle


#snt
@pytest.fixture
def mockCheckPrimeNumber(mocker, check_prime_number):
     mocker.patch("src.index.check_prime_number", return_value=check_prime_number)
 
@pytest.mark.parametrize(
    "n, prpime",
    [
        (5, 2),
        # (4, 2023, False, 30),
        # (2, 2024, True, 29),
        # (3, 2023, False, 31),
    ],
) 
@pytest.mark.usefixtures("mockCheckPrimeNumber")
def test_print_prime(n, prprime):
  assert print_Prime(n) == prprime

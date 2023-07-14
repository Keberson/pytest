import pytest
from contextlib import nullcontext as does_not_raise

from src.cat import cat


@pytest.mark.parametrize(
    'str1, str2, res, expectation',
    [
        ('A', 'B', 'AB', does_not_raise()),
        ('ABBB', '1241', 'ABBB1241', does_not_raise()),
        ('', '', '', does_not_raise()),
        ('A', '', 'A', does_not_raise()),
        ('', 'A', 'A', does_not_raise()),
        (1, 'A', 'A', pytest.raises(TypeError)),
        ('A', 1, 'A', pytest.raises(TypeError)),
    ]
)
def test_cat(str1, str2, res, expectation):
    with expectation:
        assert cat(str1, str2) == res

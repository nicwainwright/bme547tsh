from tsh import *
import pytest


# hypothyroidism is defined by TSH values greater than 4 (noninclusive)
@pytest.mark.parametrize("tshList", [([3.5, 4.6, 2.1, 1.0]), ([100]),
                                    ([4.0, 4.0, 4.0, 4.000001]),
                                    ([2.1, 2.9, 3.5, 4.1, 6.3, 6.3, 6.7, 6.9,
                                      7.1, 7.2, 7.6])])
def test_isHypo(tshList):
    assert getDiagnosis(tshList) == "hypothyroidism"

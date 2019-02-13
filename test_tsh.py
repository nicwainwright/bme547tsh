from tsh import *
import pytest


# hypothyroidism is defined by TSH values greater than 4 (noninclusive)
@pytest.mark.parametrize("tshList", [([3.5, 4.6, 2.1, 1.0]), ([100]),
                                     ([4.0, 4.0, 4.0, 4.000001]),
                                     ([2.1, 2.9, 3.5, 4.1, 6.3, 6.3, 6.7, 6.9,
                                       7.1, 7.2, 7.6])])
def test_isHypo(tshList):
    assert getDiagnosis(tshList) == "hypothyroidism"


# hyperthyroidism is defined by TSH values less than 1 (noninclusive)
@pytest.mark.parametrize("tshList", [([3.5, 0.6, 2.1, 1.0]), ([.100]),
                                     ([4.0, 4.0, 4.0, .9]),
                                     ([2.1, 2.9, 3.5, 4.0, -1.0,
                                       2.1, 3.2, 1.6, 0.1])])
def test_isHyper(tshList):
    assert getDiagnosis(tshList) == "hyperthyroidism"


# normal thyroid function is defined by TSH values <1 and >4 (noninclusive)
@pytest.mark.parametrize("tshList", [([3.5, 1.6, 2.1, 1.0]), ([3]),
                                     ([4.0, 4.0, 4.0, 1.0]),
                                     ([2.1, 2.9, 3.5, 4.0, 1.0,
                                       2.12354, 3.2, 1.6, 1.111])])
def test_isNormal(tshList):
    assert getDiagnosis(tshList) == "normal thyroid function"

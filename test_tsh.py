from tsh import *
import pytest


@pytest.mark.parametrize("tshList", [([3.5, 4.6, 2.1, 1.0]), ([100]),
                                     ([4.0, 4.0, 4.0, 4.000001]),
                                     ([2.1, 2.9, 3.5, 4.1, 6.3, 6.3, 6.7, 6.9,
                                       7.1, 7.2, 7.6])])
def test_isHypo(tshList):
    """Tests positive for Hypothyroidism.

    Hypothyroidism is defined by TSH values greater than 4 (noninclusive)

    Args:
        tshList (list): list of float values that contain values >4
    """
    assert getDiagnosis(tshList) == "hypothyroidism"


# hyperthyroidism is defined by TSH values less than 1 (noninclusive)
@pytest.mark.parametrize("tshList", [([3.5, 0.6, 2.1, 1.0]), ([.100]),
                                     ([4.0, 4.0, 4.0, .9]),
                                     ([2.1, 2.9, 3.5, 4.0, -1.0,
                                       2.1, 3.2, 1.6, 0.1])])
def test_isHyper(tshList):
    """Tests positive for Hyperthyroidism.

    Hyperthyroidism is defined by TSH values less than 1 (noninclusive)

    Args:
        tshList (list): list of float values that contain values <1
    """
    assert getDiagnosis(tshList) == "hyperthyroidism"


@pytest.mark.parametrize("tshList", [([3.5, 1.6, 2.1, 1.0]), ([3]),
                                     ([4.0, 4.0, 4.0, 1.0]),
                                     ([2.1, 2.9, 3.5, 4.0, 1.0,
                                       2.12354, 3.2, 1.6, 1.111])])
def test_isNormal(tshList):
    """Tests positive for normal thyroid function

    normal thyroid function is defined by TSH values >1 and <4 (noninclusive)

    Args:
        tshList (list): list of float values that contain values <4 and >1
    """
    assert getDiagnosis(tshList) == "normal thyroid function"

import pytest

from fentongc.fentongc import calc_zscore, get_fenton_lms


def test_calc_zscore_good_params():
    assert calc_zscore("weight", "f", 171, 2400) == 1.2
    assert calc_zscore("wEIGHt", "F", 171.0, 2400) == 1.2


def test_get_fenton_lms_valid():
    l, m, s = get_fenton_lms("weight", "f", 171)
    assert l == 1.2
    assert m == 2423.2
    assert s == 33.1


def test_get_fenton_lms_invalid():
    with pytest.raises(ValueError, match=".*fake_metric.*"):
        get_fenton_lms("fake_metric", "m", 177)
    with pytest.raises(ValueError, match=".*fake_sex.*"):
        get_fenton_lms("weight", "fake_sex", 177)
    with pytest.raises(ValueError, match=".*164.*"):
        get_fenton_lms("length", "m", 164)
    with pytest.raises(ValueError, match=".351.*"):
        get_fenton_lms("hc", "f", 351)

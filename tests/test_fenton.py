import pytest

from pretermgrowth.fenton import calc_zscore, get_lms


def test_calc_zscore_good_params():
    calc_zscore("weight", "f", 171, 2400)  # no ValueError raised
    calc_zscore("wEIGHt", "F", 171.0, 2400)  # no ValueError raised


def test_get_lms_valid():
    l, m, s = get_lms("weight", "f", 171)
    assert l == 0.664117185
    assert m == 642.3413675
    assert s == 0.169472881


def test_get_lms_invalid():
    with pytest.raises(ValueError, match=".*fake_metric.*"):
        get_lms("fake_metric", "m", 177)
    with pytest.raises(ValueError, match=".*fake_sex.*"):
        get_lms("weight", "fake_sex", 177)
    with pytest.raises(ValueError, match=".*164.*"):
        get_lms("length", "m", 164)
    with pytest.raises(ValueError, match=".351.*"):
        get_lms("hc", "f", 351)

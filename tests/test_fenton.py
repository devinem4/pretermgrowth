import pytest

from pretermgrowth.fenton import calc_zscore, get_lms


def test_calc_zscore_good_params():
    calc_zscore("weight", "f", 171, 2400)  # no ValueError raised
    calc_zscore("wEIGHt", "F", 171.0, 2400)  # no ValueError raised


def test_calc_zscore_vs_peditools():
    # comparing results against https://peditools.org/fenton2013/index.php
    assert round(calc_zscore("length", "m", 280, 54), 2) == 1.27
    assert round(calc_zscore("weight", "m", 280, 2400), 2) == -2.71
    assert round(calc_zscore("hc", "m", 280, 33), 2) == -1.44
    assert round(calc_zscore("length", "f", 277, 54), 2) == 1.71
    assert round(calc_zscore("weight", "f", 277, 2400), 2) == -2.17
    assert round(calc_zscore("hc", "f", 277, 33), 2) == -1.06


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

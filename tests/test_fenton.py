import pytest

from pretermgrowth.fenton import Fenton


def test_calc_zscore_good_params():
    Fenton.calc_zscore("weight", "f", 171, 2400)  # no ValueError raised
    Fenton.calc_zscore("wEIGHt", "F", 171.0, 2400)  # no ValueError raised


def test_calc_zscore_vs_peditools():
    # comparing results against https://peditools.org/fenton2013/index.php
    assert round(Fenton.calc_zscore("length", "m", 280, 54), 2) == 1.27
    assert round(Fenton.calc_zscore("weight", "m", 280, 2400), 2) == -2.71
    assert round(Fenton.calc_zscore("hc", "m", 280, 33), 2) == -1.44
    assert round(Fenton.calc_zscore("length", "f", 277, 54), 2) == 1.71
    assert round(Fenton.calc_zscore("weight", "f", 277, 2400), 2) == -2.17
    assert round(Fenton.calc_zscore("hc", "f", 277, 33), 2) == -1.06


def test_get_lms_valid():
    l, m, s = Fenton.get_lms("weight", "f", 171)
    assert l == 0.664117185
    assert m == 642.3413675
    assert s == 0.169472881


def test_get_lms_invalid():
    with pytest.raises(ValueError, match=".*fake_metric.*"):
        Fenton.get_lms("fake_metric", "m", 177)
    with pytest.raises(ValueError, match=".*fake_sex.*"):
        Fenton.get_lms("weight", "fake_sex", 177)
    with pytest.raises(ValueError, match=".*164.*"):
        Fenton.get_lms("length", "m", 164)
    with pytest.raises(ValueError, match=".351.*"):
        Fenton.get_lms("hc", "f", 351)

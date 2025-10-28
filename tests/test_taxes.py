import pytest
from src.taxes import calculate_taxes, calculate_tax


@pytest.fixture
def prices_list():
    return [100, 200, 300]


@pytest.mark.parametrize("tax_rate, expected",
                         [(0, [100, 200, 300]), (10, [110, 220, 330]), (10, [110, 220, 330])])
def test_calculate_taxes(prices_list, tax_rate, expected):
    assert calculate_taxes(prices_list, tax_rate) == expected


def test_calculate_taxes_invalid_tax_rate(prices_list):
    with pytest.raises(ValueError):
        calculate_taxes(prices_list, -1)


def test_calculate_taxes_invalid_prices():
    with pytest.raises(ValueError):
        calculate_taxes([0, -1], 10)


def test_calculate_tax_invalid_price(prices_list):
    with pytest.raises(ValueError):
        calculate_tax(-1.0, 10)


@pytest.mark.parametrize("price, tax_rate", [(200, -10), (200, 100), (200, 110)])
def test_calculate_tax_invalid_tax_rate(price, tax_rate):
    with pytest.raises(ValueError):
        calculate_tax(price, tax_rate)
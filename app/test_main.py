import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_result",
        [
            (0, [0, 0, 0, 0]),       # 0 cents
            (1, [1, 0, 0, 0]),       # 1 penny
            (6, [1, 1, 0, 0]),       # 1 penny + 1 nickel
            (17, [2, 1, 1, 0]),      # 2 pennies + 1 nickel + 1 dime
            (50, [0, 0, 0, 2]),      # 2 quarters
            (99, [4, 0, 2, 3]),      # 4 pennies + 2 dimes + 3 quarters
            (100, [0, 0, 0, 4]),
            (125, [0, 0, 0, 5]),     # 5 quarters
        ],
    )
    def test_get_coin_combination(self, cents: int, expected_result: list) -> None: # Noqa E501
        assert get_coin_combination(cents) == expected_result

    def test_get_coin_combination_negative(self) -> None:
        # Testing the negative case without monkeypatch
        with pytest.raises(ValueError, match="Input value must be non-negative"): # Noqa E501
            get_coin_combination(-1)

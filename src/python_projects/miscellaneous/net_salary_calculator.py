from enum import Enum
from typing import NamedTuple, Optional

import pandas as pd


class Employee:
    class TaxBracket(Enum):
        PERSONAL_ALLOWANCE = "personal_allowance"
        BASIC_RATE = "basic_rate"
        HIGHER_RATE = "higher_rate"
        ADDITIONAL_RATE = "additional_rate"

    TAX_BRACKETS = pd.DataFrame(
        {
            TaxBracket.PERSONAL_ALLOWANCE.value: {"upper_bound": 12570, "rate": 0.0},
            TaxBracket.BASIC_RATE.value: {"upper_bound": 50270, "rate": 0.2},
            TaxBracket.HIGHER_RATE.value: {"upper_bound": 125140, "rate": 0.4},
            TaxBracket.ADDITIONAL_RATE.value: {
                "upper_bound": float("inf"),
                "rate": 0.45,
            },
        }
    ).T

    class RateAndBounds(NamedTuple):
        rate: float
        lower_bound: float
        upper_bound: float

    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def get_rate_and_bounds(
        self, current_bracket: TaxBracket, previous_bracket: Optional[TaxBracket]
    ) -> RateAndBounds:
        rate = self.TAX_BRACKETS.at[current_bracket.value, "rate"]
        lower_bound = (
            self.TAX_BRACKETS.at[previous_bracket.value, "upper_bound"]
            if previous_bracket
            else 0
        )
        upper_bound = self.TAX_BRACKETS.at[current_bracket.value, "upper_bound"]
        return self.RateAndBounds(rate, lower_bound, upper_bound)

    def calculate_salary_after_tax_by_bracket(
        self, rate_and_bounds: RateAndBounds
    ) -> float:
        rate, lower_bound, upper_bound = rate_and_bounds
        taxable_income = max(
            0, min(self.salary - lower_bound, upper_bound - lower_bound)
        )
        return (1 - rate) * taxable_income

    @property
    def personal_allowance(self) -> float:
        rate_and_bounds = self.get_rate_and_bounds(
            self.TaxBracket.PERSONAL_ALLOWANCE, None
        )
        salary_after_personal_allowance = self.calculate_salary_after_tax_by_bracket(
            rate_and_bounds
        )
        return salary_after_personal_allowance

    @property
    def basic_rate(self) -> float:
        rate_and_bounds = self.get_rate_and_bounds(
            self.TaxBracket.BASIC_RATE, self.TaxBracket.PERSONAL_ALLOWANCE
        )
        salary_after_basic_rate = self.calculate_salary_after_tax_by_bracket(
            rate_and_bounds
        )
        return salary_after_basic_rate

    @property
    def higher_rate(self) -> float:
        rate_and_bounds = self.get_rate_and_bounds(
            self.TaxBracket.HIGHER_RATE, self.TaxBracket.BASIC_RATE
        )
        salary_after_higher_rate = self.calculate_salary_after_tax_by_bracket(
            rate_and_bounds
        )
        return salary_after_higher_rate

    @property
    def additional_rate(self) -> float:
        rate_and_bounds = self.get_rate_and_bounds(
            self.TaxBracket.ADDITIONAL_RATE, self.TaxBracket.HIGHER_RATE
        )
        salary_after_additional_rate = self.calculate_salary_after_tax_by_bracket(
            rate_and_bounds
        )
        return salary_after_additional_rate

    def calculate_net_salary(self) -> float:
        return (
            self.personal_allowance
            + self.basic_rate
            + self.higher_rate
            + self.additional_rate
        )

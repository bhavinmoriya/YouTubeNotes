from math import exp, log


def calculate_returns(
    previous_price: float,
    current_price: float,
) -> dict[str, float]:
    """Calculate price change, simple return, and log return."""

    if previous_price <= 0 or current_price <= 0:
        raise ValueError("Stock prices must be strictly positive.")

    price_change = current_price - previous_price

    simple_return = (
        current_price / previous_price
    ) - 1

    log_return = log(
        current_price / previous_price
    )

    # Verify the mathematical relationships.
    assert abs(log(1 + simple_return) - log_return) < 1e-12

    assert abs(exp(log_return) - (1 + simple_return)) < 1e-12

    return {
        "price_change": price_change,
        "simple_return": simple_return,
        "log_return": log_return,
    }


previous_price = 100.0
current_price = 110.0

results = calculate_returns(
    previous_price,
    current_price,
)

print(f"Price change:   €{results['price_change']:.2f}")
print(f"Simple return:  {results['simple_return']:.4%}")
print(f"Log return:     {results['log_return']:.4%}")

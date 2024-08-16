import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom


def plot_binomial_with_pvalue(n: int, p: float, observed_heads: int) -> None:
    # Create a range of possible outcomes (0 to n)
    k = np.arange(0, n + 1)
    # Calculate binomial distribution probabilities
    binomial = binom.pmf(k, n, p)
    # Calculate two-sided p-value
    p_value_left = binom.cdf(observed_heads, n, p)
    p_value_right = 1 - binom.cdf(observed_heads - 1, n, p)
    p_value = min(1, 2 * min(p_value_left, p_value_right))  # type: ignore

    # Create the plot
    plt.figure(figsize=(12, 7))
    plt.plot(k, binomial, alpha=0.8, color="b")
    plt.title(f"Binomial Distribution of Heads in {n} Coin Tosses")
    plt.xlabel("Number of Heads")
    plt.ylabel("Probability")
    plt.grid(alpha=0.3)

    # Add annotations for expected value and standard deviation
    mean = n * p
    # plt.axvline(mean, color='r', linestyle='dashed', linewidth=2)

    # Highlight the p-value area
    if observed_heads <= mean:
        plt.fill_between(
            k[: observed_heads + 1],
            0,
            binomial[: observed_heads + 1],
            alpha=0.5,
            color="r",
        )
        plt.fill_between(
            k[int(2 * mean - observed_heads) :],
            0,
            binomial[int(2 * mean - observed_heads) :],
            alpha=0.5,
            color="r",
        )
    else:
        plt.fill_between(
            k[: int(2 * mean - observed_heads) + 1],
            0,
            binomial[: int(2 * mean - observed_heads) + 1],
            alpha=0.5,
            color="r",
        )
        plt.fill_between(
            k[observed_heads:], 0, binomial[observed_heads:], alpha=0.5, color="r"
        )

    plt.axvline(observed_heads, color="r", linestyle="dotted", linewidth=2)
    plt.text(
        observed_heads + 1,
        plt.ylim()[1] * 0.6,
        f"Observed: {observed_heads}\np-value: {p_value:.6f}",
        color="black",
    )

    # Add horizontal green line for PDF at observed_heads
    pdf_value = binom.pmf(observed_heads, n, p)
    plt.axhline(y=pdf_value, color="g", linestyle="--", linewidth=2)  # type: ignore


if __name__ == "__main__":
    # Input parameters from keyboard, only allow reasonable values
    # n must be integer
    # p must be float, between 0 and 1
    # observed_heads must be integer, between 0 and n
    n = int(input("Enter the number of coin tosses (n): "))
    p = float(
        input("Enter the probability of heads (p) for each toss (between 0 and 1): ")
    )
    observed_heads = int(input("Enter the number of observed heads: "))
    while n < 1 or p < 0 or p > 1 or observed_heads < 0 or observed_heads > n:
        if n < 1:
            print("The number of coin tosses must be at least 1.")
        if p < 0 or p > 1:
            print("The probability of heads must be between 0 and 1.")
        if observed_heads < 0 or observed_heads > n:
            print("The number of observed heads must be between 0 and n.")
        n = int(input("Enter the number of coin tosses (n): "))
        p = float(input("Enter the probability of heads (p): "))
        observed_heads = int(input("Enter the number of observed heads: "))

    # Plot the distribution
    plot_binomial_with_pvalue(n, p, observed_heads)
    plt.show()

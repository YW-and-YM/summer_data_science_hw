# P-value and Monte Carlo Simulation

## Before you start

Run the following command to install the required packages:

```bash
pip install numpy matplotlib scipy
```

This command will install the following packages:

-   `numpy`: a library for numerical computing in Python.
-   `matplotlib`: a library for creating visualizations in Python.
-   `scipy`: a library for scientific computing in Python.

## P-value

The p-value is the probability of obtaining a test statistic at least as extreme as the one that was actually observed, assuming that the null hypothesis is true. The p-value is used to determine the significance of the test statistic.

Let's use the `find_p_value.py` script to calculate the p-value for a coin toss experiment.

Copy the contents of [this file](/lecture2/find_p_value.py) into a new file called `find_p_value.py`:

Run the script using the following command:

```bash
python find_p_value.py
```

Follow the prompts to enter the number of

-   **Number of coin tosses**: the total number of coin tosses. For example, if you toss a coin 10 times, enter `10`.
-   **Probability of heads**: the probability of getting heads. For a fair coin, the probability is `0.5`.
-   **Number of heads**: the number of times heads appears in the coin tosses. For example, if heads appears 6 times, enter `6`.

The script will calculate the p-value and display the result.

Experiment with different values for the number of coin tosses, probability of heads, and number of heads to see how the p-value changes.

## Monte Carlo Simulation

A Monte Carlo simulation is a computational algorithm that relies on repeated random sampling to obtain numerical results. It is used to estimate the probability of different outcomes by running multiple simulations.

Let's use the `monte_carlo_simulation.py` script to perform a Monte Carlo simulation for a coin toss experiment.

Copy the contents of [this file](/lecture2/monte_carlo_simulation.py) into a new file called `monte_carlo_simulation.py`:

Run the script using the following command:

```bash
python monte_carlo_simulation.py
```

Follow the prompts to enter the following parameters:

-   **Number of trials**: the number of times to run the simulation. For example, if you want to run the simulation 1000 times, enter `1000`.
-   **Number of coin tosses for each trial**: the total number of coin tosses in each trial. For example, if you toss a coin 10 times in each trial, enter `10`.
-   **Probability of heads**: the probability of getting heads. For a fair coin, the probability is `0.5`.
-   **Bin size**: the size of each bin for the histogram. For example, if you want to group the results into bins of size 10, enter `10`.

The script will perform the Monte Carlo simulation and display a histogram of the results.

Experiment with different values for the number of trials, number of coin tosses, probability of heads, and bin size to see how the results change.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

def simulate_binomial(n_trials, n_flips, p_heads=0.5):
    # Simulate n_trials experiments, each with n_flips coin flips
    results = np.random.binomial(n=n_flips, p=p_heads, size=n_trials)
    return results

def plot_simulated_vs_theoretical(n_trials, n_flips, p_heads,bin_size=1):
    # Simulate experiments
    simulated_results = simulate_binomial(n_trials, n_flips, p_heads)
    
    # Calculate theoretical probabilities
    k = np.arange(0, n_flips + 1)
    theoretical_probs = binom.pmf(k, n_flips, p_heads)
    
    # Create the plot
    plt.figure(figsize=(12, 7))
    
    # Plot histogram of simulated results
    bins = np.arange(-0.5, n_flips + 1.5, bin_size)
    plt.hist(simulated_results, bins=bins, density=True, 
             alpha=0.7, label='Simulated')
    
    # Plot theoretical distribution
    plt.plot(k, theoretical_probs, 'r-', lw=2, label='Theoretical')
    
    plt.title(f'Simulated vs Theoretical Binomial Distribution\n'
              f'(n={n_flips}, p={p_heads}, {n_trials} trials)')
    plt.xlabel('Number of Heads')
    plt.ylabel('Probability')
    plt.legend()
    plt.grid(alpha=0.3)
    
    plt.show()

# Set parameters from keyboard, and only allow reasonable values


# first pring the message to the user
print('Enter the inputs for the simulation:')
# n_trials must be integer greater than 0
# f_flips must be integer greater than 0
# p_heads must be float
# bin_size must be integer greater than 1
# reask the user to input the values if they are not valid, and tell the user which input is wrong
# then take the input from the user
n_trials = int(input('Enter the number of trials: '))
while n_trials < 1:
    print('Number of trials must be an integer greater than 0.')
    n_trials = int(input('Enter the number of trials: '))
n_flips = int(input('Enter the number of flips for each trial: '))
while n_flips < 1:
    print('Number of flips must be an integer greater than 0.')
    n_flips = int(input('Enter the number of flips for each trial: '))
p_heads = float(input('Enter the probability of heads: '))
while p_heads < 0 or p_heads > 1:
    print('Probability of heads must be a float between 0 and 1.')
    p_heads = float(input('Enter the probability of heads: '))
bin_size = int(input('Enter the bin size: '))
while bin_size < 1:
    print('Bin size must be an integer greater than 1.')
    bin_size = int(input('Enter the bin size for plotting the simulated histogram: '))
    


# Plot the distribution
plot_simulated_vs_theoretical(n_trials, n_flips, p_heads)
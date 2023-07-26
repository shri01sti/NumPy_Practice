import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

'''
# plotting a distplot with histogram
sns.distplot([0, 1, 3, 5, 7, 9])
plt.show()

# plotting a distplot without histogram
sns.distplot([1, 2, 3, 4, 5, 6], hist=False)
plt.show()

# Normal(Gaussian Distribution)
x = random.normal(size=(2, 3))
print(x)

# generate random normal dist with mean = 1 and SD = 2
y = random.normal(loc=1, scale=2, size=(2, 3))
print(y)

# Visualization of Normal Distribution
sns.distplot(random.normal(size=1000), hist=False)
plt.show()

# binomial distribution
x = random.binomial(n=10, p=0.5, size=10)
print(x)

# Visualization of Binomial Distribution
sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
plt.show()

# visualizing diff between ND and BD
sns.distplot(random.normal(loc=50, scale=5, size=1000),
             hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000),
             hist=False, label='binomial')
plt.show()

# Poisson Distribution
# create a random 1*10 distribution for occurence 2:
x = random.poisson(lam=2, size=10)
print(x)

# visualization of Poisson Distribution
sns.distplot(random.poisson(lam=2, size=1000), kde=False, label='Poison')
plt.show()

# difference between ND and PD
sns.distplot(random.normal(loc=50, scale=7, size=1000),
             hist=False, label='Normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='Poisson')
plt.show()

# difference between BD and PD
sns.distplot(random.binomial(n=1000, p=0.01, size=1000),
             hist=False, label="binomial")
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')
plt.show()

# uniform distribution
x = random.uniform(size=(2, 3))
print(x)

# visualization of UD
sns.distplot(random.uniform(size=1000), hist=False)
plt.show()

# logistic distribution
x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)

# visualization of LD
sns.distplot(random.logistic(size=1000), hist=False)
plt.show()

# difference between LD and ND
sns.distplot(random.logistic(scale=2, loc=5, size=1000),
             hist=False, label='logistic')
sns.distplot(random.normal(scale=2, loc=6, size=1000),
             hist=False, label='normal')
plt.show()

# Multinomial Distribution
# draw out a sample for dice roll
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x)  # produce one value for each pval

# Exponential Distribution
x = random.exponential(scale=2, size=(2, 3))
print(x)

# visualization of ED
sns.distplot(random.exponential(size=100), hist=False)
plt.show()

# chi_square distribution
x = random.chisquare(df=2, size=(2, 3))
print(x)

# visualization of Chisquare Distribution
sns.distplot(random.chisquare(df=1, size=1000), hist=False)
plt.show()

# Rayleigh Distribution
x = random.rayleigh(scale=2, size=(2, 3))
print(x)

# visualization of RD
sns.distplot(random.rayleigh(size=1000), hist=False)
plt.show()

# Pareto Distribution
x = random.pareto(a=2, size=(2, 3))
print(x)

# Visualization of Pareto Distribution
sns.distplot(random.pareto(a=2, size=1000), kde=False)
plt.show()
'''

# zipf Distribution
x = random.zipf(a=2, size=(2, 3))
print(x)

# Visualization of Zipf Distribution
x = random.zipf(a=2, size=1000)
sns.distplot(x[x < 10], kde=False)
plt.show()

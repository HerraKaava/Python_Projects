#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 11:00:46 2024

@author: herrakaava
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
from statsmodels.distributions.empirical_distribution import ECDF

#%%

def lm_plot(data, X, y, fs, save_fig=False, fig_name=None, return_=False):
    """
    Displays a scatter plot with a (simple) regression line (with a 95% CI for the line)
    fitted to the data.
    
    Args:
    data -- a Pandas DataFrame containing your data
    X -- the predictor variable
    y -- the response variable
    fs -- the figure size
    save_fig -- if True, saves the figure
    fig_name -- name of the saved figure
    return_ -- if True, returns the fitted regression model
    """
    
    r = np.round(data.corr(method='pearson', numeric_only=True).loc[X, y], 3)
    plt.figure(figsize=fs, dpi=100)
    plt.scatter(data[X], 
                data[y], 
                facecolors='none', 
                edgecolors='black')
    
    # Just your regular simple linear regression model
    model = smf.ols(f'{y} ~ {X}', data=data)
    fit = model.fit()
    params = fit.params
    r_sq = np.round(fit.rsquared, 3)
    y_hat = params.iloc[0] + params.iloc[1] * data[X].values
    plt.plot(data[X].values, y_hat, color='blue', linewidth=0.8, label='Best-fit line')
    
    ##### Plot the 95% confidence interval for the line #####
    y_preds = fit.get_prediction(data[X])
    CI_95_y_preds = y_preds.summary_frame(alpha=0.05)
    
    sort_idx = np.argsort(data[X].values)
    sort_X = data[X].values[sort_idx]
    sort_ci_lower = CI_95_y_preds['mean_ci_lower'].values[sort_idx]
    sort_ci_upper = CI_95_y_preds['mean_ci_upper'].values[sort_idx]
    
    plt.fill_between(x=sort_X,
                     y1=sort_ci_lower,
                     y2=sort_ci_upper,
                     alpha=0.4,
                     label='95% CI',
                     color='lightblue')
    plt.legend()
    plt.xlabel(f'{X}')
    plt.ylabel(f'{y}')
    plt.show()
    
    print(f'Pearson r: {r}')
    print(f'r^2: {r_sq}')
    
    if save_fig:
        if fig_name is None:
            raise ValueError('fig_name must be provided if save_fig is True')
        plt.savefig(fig_name, format='png', bbox_inches='tight')
    
    if return_:
        return fit

#%%

def resid_plot(f, method, x_var, fs=(8,6), return_eps=False, save_fig=False, fig_name=None):
    """
    Plots one of the two graphs; 
        1. residuals vs. index
        2. residuals vs. fitted values
    The formula for Pearson residuals is:
        r_i = (y_i - hat{y_i}) / sigma,
    where sigma is the standard deviation of the residuals.
    
    Args:
    f -- a fitted (statsmodels) model
    method -- Method to use; options include 'raw' and 'pearson'
    x_var -- specifies what to plot in the x-axis; options include 'index', 'fitted_vals'
    fs -- a tuple indicating the figure size (default is (8,6))
    return_eps -- whether to return the residuals (bool)
    
    Returns:
    resid -- the pearson residuals.
    
    Notes:
    - The fitted values reflect the mean structure specified by the fixed effects 
      and the predicted random effects.
    """
    method = method.lower()
    x_var = x_var.lower()
    assert method in ['raw', 'pearson']
    assert x_var in ['index', 'fitted_vals']
    
    if method == 'raw':
        residuals = f.resid
    elif method == 'pearson':
        residuals = f.resid_pearson
        
    if x_var == 'index':
        x = np.arange(residuals.shape[0])
        x_label = 'index'
    if x_var == 'fitted_vals':
        x = f.fittedvalues
        x_label = 'fitted values'
    
    ##### Plotting #####
    plt.figure(figsize=fs, dpi=100)
    plt.scatter(x, residuals, facecolors='none', edgecolors='black')
    plt.axhline(y=0, color='red', linestyle='--')
    plt.xlabel(x_label)
    plt.show()
    
    if save_fig:
        if fig_name is None:
            raise ValueError('fig_name must be provided if save_fig is True')
        plt.savefig(fig_name, format='png', bbox_inches='tight')
    
    if return_eps:
        return residuals

#%%

def QQ_plot(x, save_fig=False, fig_name=None):
    """
    Plots a Q-Q plot.
    A Q-Q plot is a graphical method for comparing two probability distributions 
    by plotting their quantiles against each other. 
    If the two distributions being compared are similar, 
    the points in the Q-Q plot will approximately lie on the identity line y = x. 
    Since we are testing if the residuals are normally distributed, 
    the theoretical quantiles in the x-axis are from a (standard) normal distribution.
    
    Args:
    x -- the data to be plotted
    """
    pp = sm.ProbPlot(x, fit=True)
    qq = pp.qqplot(marker='o', markerfacecolor='none', markeredgecolor='black', alpha=0.4)
    sm.qqline(qq.axes[0], line='45', fmt='r--', linewidth=1.4)
    if save_fig:
        if fig_name is None:
            raise ValueError('fig_name must be provided if save_fig is True')
        plt.savefig(fig_name, format='png', bbox_inches='tight')

#%%

def plot_ecdf(n, mu, sigma, fs=(8,6)):
    """
    Plots the empirical cumulative distribution function.
    
    Args:
        n: the number of samples to draw from N(mu,sigma)
        mu: the location (mean) parameter of the distribution
        sigma: the scale (std) parameter of the distribution
        
    Returns:
        The ECDF.
    """
    # Draw n samples from the N(mu,sigma) distribution
    x = np.random.normal(loc=mu, scale=sigma, size=n)

    # Calculate the empirical cumulative distribution function
    F_n = ECDF(x)

    ##### Plotting #####
    plt.figure(figsize=fs)
    
    # Plot dots at each ECDF point
    plt.scatter(F_n.x, F_n.y, marker='o', color='k')
    
    # Add horizontal lines between the ECDF points
    for i in range(x.shape[0]):
        plt.hlines(y=F_n.y[i], xmin=F_n.x[i], xmax=F_n.x[i+1], color='k')
    
    # Add the final horizontal line from the last ECDF point
    plt.hlines(y=F_n.y[-1], xmin=F_n.x[-1], xmax=F_n.x[-1] + 0.1, color='k')
    plt.title('Empirical cumulative distribution function')
    plt.show()
    
#%%







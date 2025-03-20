import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(8,8))
    plt.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df, s=40, alpha=0.2, c='b', edgecolors="k")
    plt.xlim(xmin=1850, xmax=2075)

    # Create first line of best fit
    slope_all = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level']).slope
    yint_all = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level']).intercept
    ext_years = pd.DataFrame(data=[x for x in range(1880, 2051)], columns=['Year'])
    ax.plot(ext_years['Year'], slope_all*ext_years['Year'] + yint_all, '--g', lw=1.5)

    # Create second line of best fit
    slope_lim = linregress(x=df.loc[df['Year'] >= 2000, 'Year'], y=df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']).slope
    yint_lim = linregress(x=df.loc[df['Year'] >= 2000, 'Year'], y=df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']).intercept
    lim_years = pd.DataFrame(data=[x for x in range(2000, 2051)], columns=['Year'])
    ax.plot(lim_years['Year'], slope_lim*lim_years['Year'] + yint_lim, '-.r', lw=1.5,)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
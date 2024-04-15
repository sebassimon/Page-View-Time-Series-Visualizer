import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

# Clean the data
df_clean = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

# Draw Line Plot
def draw_line_plot():
    # Create a copy of the cleaned data
    df_copy = df_clean.copy()

    # Resample data to get monthly values
    df_resampled = df_copy.resample('M').mean()

    # Plotting
    plt.figure(figsize=(15, 5))
    plt.plot(df_resampled.index, df_resampled['value'], color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save and show plot
    plt.savefig('line_plot.png')
    plt.show()


# Draw Bar Plot
def draw_bar_plot():
    # Create a copy of the cleaned data
    df_copy = df_clean.copy()

    # Add year and month columns
    df_copy['year'] = df_copy.index.year
    df_copy['month'] = df_copy.index.strftime('%B')

    # Group by year and month, calculate the average page views
    df_grouped = df_copy.groupby(['year', 'month'])['value'].mean().unstack()

    # Plotting
    plt.figure(figsize=(15, 10))
    df_grouped.plot(kind='bar', stacked=False)
    plt.title('Average Page Views per Year')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels= [month for month in df_grouped.columns], loc='upper left')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save and show plot
    plt.savefig('bar_plot.png')
    plt.show()


# Draw Box Plot
def draw_box_plot():
    # Create a copy of the cleaned data
    df_copy = df_clean.copy()

    # Add year and month columns
    df_copy['year'] = df_copy.index.year
    df_copy['month'] = df_copy.index.month_name()

    # Plotting
    fig, axes = plt.subplots(1, 2, figsize=(20, 10))
    sns.boxplot(x='year', y='value', data=df_copy, ax=axes[0])
    sns.boxplot(x='month', y='value', data=df_copy, ax=axes[1], order=[
        'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'
    ])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    plt.tight_layout()

    # Save and show plot
    plt.savefig('box_plot.png')
    plt.show()

# Call functions to generate plots
draw_line_plot()
draw_bar_plot()
draw_box_plot()

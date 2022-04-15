import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('./medical_examination.csv') 
# Add 'overweight' column

# BMI = weight [kg] / height**2 [m**2] 
weight = df.loc[:, 'weight']
height = df.loc[:, 'height']
df['overweight'] = [1 if (x/((y/100)**2)) > 25 else 0 for x,y in zip(df.weight, df.height)]
# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.

    # Draw the catplot with 'sns.catplot()'
    plot = sns.catplot(data=df_cat, x='variable', hue='value', col='cardio', kind='count')
    plot.axes[0,0].set_ylabel('total')
    plot.axes[0,1].set_ylabel('total')
    fig = plot.fig
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df
    df_heat = df_heat.drop(df_heat[df_heat.ap_hi <= df_heat.ap_lo].index)
    df_heat = df_heat.drop(df_heat[df_heat.height <= df_heat.height.quantile(0.025)].index)
    df_heat = df_heat.drop(df_heat[df_heat.height >= df_heat.height.quantile(0.975)].index)
    df_heat = df_heat.drop(df_heat[df_heat.weight <= df_heat.weight.quantile(0.025)].index)
    df_heat = df_heat.drop(df_heat[df_heat.weight >= df_heat.weight.quantile(0.975)].index)

    # Calculate the correlation matrix
    corr = df_heat.corr()
    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True, robust=True, fmt='.1f')



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

draw_cat_plot()
draw_heat_map()

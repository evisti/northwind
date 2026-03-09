from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from connection_alchemy import SQLRunner, get_engine
from connection_simple import get_connection_string, read_file
from highlight_text import ax_text
from pyfonts import load_google_font


config_file = Path('./db_config.ini')

connection_string = get_connection_string(config_file)

sql_runner = SQLRunner(get_engine(config_file))



# Exercise 4: Testing the connection and running a simple query

query = "SELECT * FROM products LIMIT 5;"

result = sql_runner.run_query(query)
print(f'Running simple query: {query}')
for row in result:
    print(row)




# Exercise 5: Using Pandas for data analysis and visualization

# I found two ways to get a query into a Pandas dataframe:

# 1. Make the SQL connection with SQLAlchemy's sessionmaker and put the result into a dataframe
df1 = pd.DataFrame(sql_runner.run_query(query))

# 2. Use Panda's read_sql_query directly on the connection_string
df2 = pd.read_sql_query(query, connection_string)



# Plot: Total sale per country

# query data
query = read_file(Path('sql_queries/Exercise5_total_sale_per_country.sql'))
df = pd.read_sql_query(query, connection_string)

# initialize figure
fig, ax = plt.subplots(1, 2, figsize=(9, 7), sharey=True)

# other fonts
other_font = load_google_font("Fira Sans", weight="regular")
other_font_light = load_google_font("Fira Sans", weight="light")
other_font_bold = load_google_font("Fira Sans", weight="medium")

# load color palette
palette = sns.color_palette("ch:s=-.2,r=.6", as_cmap=True)

# create the plots
sns.barplot(
    data=df, y=df.country, x=df.total_sales, ax=ax[0], orient='h', 
    hue=df.total_sales, palette=palette, legend=False
)
sns.barplot(
    data=df, y=df.country, x=df.revenue, ax=ax[1], orient='h', 
    hue=df.revenue, palette=palette, legend=False
)

# grid and splines
for a in ax:
    a.grid(axis='x', linewidth=.8, alpha=.4, linestyle='-')
    a.set_axisbelow(True)
    a.spines['top'].set_visible(False)
    a.spines['right'].set_visible(False)

# custom axes
ax[0].set_xlabel('Total sales', fontsize=13, font=other_font_bold)
ax[0].set_ylabel(None)
ax[1].set_xlabel('Revenue', fontsize=13, font=other_font_bold)
ax[0].set_xticks(ax[0].get_xticks(), ax[0].get_xticklabels(), font=other_font_light, fontsize=12)
ax[0].set_yticks(ax[0].get_yticks(), ax[0].get_yticklabels(), font=other_font, fontsize=12)
ax[1].set_xticks([0, 50000, 100000, 150000, 200000, 250000], 
                 ['0', '50K', '100K', '150K', '200K', '250K'], font=other_font_light, fontsize=12)
ax[0].set_xlim(None, 125)

plt.tight_layout()
#plt.savefig('figures/total_sales_per_country.png', dpi=300)
plt.show()



# Plot: Highest revenue products

# query data
query = read_file(Path('sql_queries/Exercise5_highest_revenue_products.sql'))
df = pd.read_sql_query(query, connection_string)

print(df.describe())

# initialize figure
fig, ax = plt.subplots(figsize=(6,7))

# create the plot
sns.scatterplot(
    data=df, x=df.units_sold, y=df.avg_unit_price, ax=ax, legend=False,
    hue=df.revenue, palette=palette, hue_norm=(0, 150000),
    size=df.revenue, sizes=(10, 400), size_norm=(0, 150000)
)

# grid and splines
ax.grid(axis='both', linewidth=.8, alpha=.4, linestyle='-')
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_alpha(.1)

# custom axes
ax.set_xlabel('Units sold', fontsize=13, font=other_font_bold)
ax.set_ylabel('Avg unit price', fontsize=13, font=other_font_bold)
ax.set_xticks(ax.get_xticks(), ax.get_xticklabels(), font=other_font_light, fontsize=12)
ax.set_yticks(ax.get_yticks(), ax.get_yticklabels(), font=other_font_light, fontsize=12)
plt.axis([0, None, 0, 260])

# define which points to annotate 
df_head_5 = df.head(5)
df_head_5['adjustments'] = [
    (70, 0), 
    (-180, 11),
    (-100, 10),
    (-110, 8),
    (-180, -8)
]

# annotate points
for i, row in df_head_5.iterrows():
    x = row['units_sold'] + row['adjustments'][0]
    y = row['avg_unit_price'] + row['adjustments'][1]
    ax_text(
        x=x,
        y=y,
        s=f"<{row['productname']}>: {row['revenue']/1000:.0f}K",
        fontsize=9,
        font=other_font,
        ha='left',
        va='center',
        ax=ax,
        highlight_textprops=[{'font': other_font_bold}],
    )

#plt.savefig('figures/highest_revenue_products.png', dpi=300)
plt.show()

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sql_connection import SQLRunner, get_engine




config_file = Path('./db_config.ini')
sql_runner = SQLRunner(get_engine(config_file))


# Testing the connection and running a simple query
query = "SELECT * FROM products LIMIT 5;"
result = sql_runner.run_query(query)

print(f'Running simple query: {query}')
for row in result:
    print(row)


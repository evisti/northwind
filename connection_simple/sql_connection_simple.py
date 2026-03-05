"""Module for running SQL queries against a database using _____."""
import configparser as cp
from pathlib import Path


def get_connection_string(config_file: Path) -> str:
    """Construct a database connection string from the configuration file.

    Args:
        config_file (Path): Path to the configuration file containing database connection details.
    """
    config = cp.ConfigParser()

    if not config_file.exists():
        raise FileNotFoundError(f"Configuration file '{config_file}' not found.")
    else:
        config.read(config_file)

    user = config['DBCONFIG']['User']
    password = config['DBCONFIG']['Password']
    host = config['DBCONFIG']['Host']
    port = config['DBCONFIG']['Port']
    database = config['DBCONFIG']['Database']

    return f'postgresql://{user}:{password}@{host}:{port}/{database}'


# if query is a Path to a file containing the SQL query
def read_file(filepath: Path) -> str:
    """
    Args:
        filepath (str): A Path to a file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if isinstance(filepath, Path):
        if not filepath.exists():
            raise FileNotFoundError(f"File '{filepath}' not found.")
        else:
            with open(filepath, 'r') as file:
                result = file.read()
    
    return result

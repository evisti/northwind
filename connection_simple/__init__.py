"""This module provides utilities for running SQL queries and managing database connections."""

from .sql_connection_simple import get_connection_string, read_file

__all__ = ['get_connection_string', 'read_file']

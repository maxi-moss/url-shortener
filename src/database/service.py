import sqlite3
from functools import lru_cache

from database.utils import (
    build_create_table_query,
    build_insert_url_query, 
    build_select_all_query,
    build_select_url_query
)
from config import settings


class DatabaseService():
    def __init__(self):
        self.database_name = settings.database.name
        self.conn = None

    def connect_to_db(self):
        """Connect to db if connection not already established"""
        if not self.conn:
            self.conn = sqlite3.connect(self.database_name)
        return self.conn

    def insert_url_pair(self, uuid, original_url, shortened_url):
        """Store URL mapping pair in database"""
        insert_url_query = build_insert_url_query()
        values = (uuid, original_url, shortened_url)

        with self.connect_to_db() as conn:
            cursor = conn.cursor()
            cursor.execute(insert_url_query, values)
        return

    def get_all_url_pairs(self):
        """Get all URL pairs from database"""
        select_all_query = build_select_all_query()

        with self.connect_to_db() as conn:
            cursor = conn.cursor()
            cursor.execute(select_all_query)
            url_pairs = cursor.fetchall()
        return url_pairs

    def get_url_pair(self, original_url):
        """Get a specific URL pair from database by original URL"""
        select_url_query = build_select_url_query()

        with self.connect_to_db() as conn:
            cursor = conn.cursor()
            cursor.execute(select_url_query, (original_url,))
            url_pair = cursor.fetchone()
        return url_pair

    def create_table(self):
        """Create table for shortened URL mapping"""
        create_table_query = build_create_table_query()

        with self.connect_to_db() as conn:
            cursor = conn.cursor()
            cursor.execute(create_table_query)
            conn.commit()
        return


@lru_cache
def get_database_service():
    return DatabaseService()
def build_create_table_query():
    """Build SQL query for creating shortened_urls table"""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS shortened_urls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uuid TEXT,
        original_url TEXT,
        shortened_url TEXT
    );
    """
    return create_table_query


def build_insert_url_query():
    """Build SQL query for inserting URL pairs into database"""
    insert_url_query = """
    INSERT INTO shortened_urls (uuid, original_url, shortened_url)
    VALUES (?, ?, ?);
    """
    return insert_url_query


def build_select_all_query():
    """Build SQL query to get all URL pairs from database"""
    select_all_query = "SELECT * FROM shortened_urls"
    return select_all_query


def build_select_url_query():
    """Build SQL query to get a URL pair by url from database"""
    select_url_query = """
    SELECT original_url, shortened_url FROM shortened_urls
    WHERE original_url = ?
    """
    return select_url_query
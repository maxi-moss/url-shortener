import hashlib
from functools import lru_cache

from database.service import get_database_service


class LinkShortenerService():
    def __init__(self):
        self.app_url = "https://maxshorten.er"
        self.db_service = get_database_service()

    def generate_shortened_url(self, input_url):
        """Generate a shortened url from an input url"""
        # If URL has already been processed, use existing shortened url
        if self.url_already_processed(input_url):
            shortened_url = self.db_service.get_url_pair(input_url)[1]

        # Else generate new shortened URL and store it in database for later re-use
        else:
            uuid = self.generate_uuid(input_url)
            shortened_url = self.build_shortened_url(uuid)
            self.db_service.insert_url_pair(uuid, input_url, shortened_url)
        return shortened_url

    def generate_uuid(self, input_url):
        """Generate unique 6-letter identifier to use in shortened url"""
        url_hash_object = hashlib.sha256(input_url.encode('utf-8'))
        url_hash = url_hash_object.hexdigest()
        uuid = url_hash[:6]  # uuid uses first 6 letters of hash for simplicity
        return uuid

    def build_shortened_url(self, uuid):
        """Generate shortened url using generated url uuid"""
        app_url = "https://maxshorten.er"
        shortened_url = f"{app_url}/{uuid}"
        return shortened_url

    def url_already_processed(self, input_url):
        """Check if url has already been processed"""
        url_pair = self.db_service.get_url_pair(input_url)
        if url_pair:
            return True
        return False


@lru_cache
def get_link_shortener_service():
    return LinkShortenerService()
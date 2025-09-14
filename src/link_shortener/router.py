from typing import List

from fastapi import APIRouter, Depends
from database.service import DatabaseService, get_database_service

from link_shortener.service import LinkShortenerService, get_link_shortener_service

router = APIRouter()


@router.get("/get_all")
def get_all_urls(
    service: DatabaseService = Depends(get_database_service)
) -> List:
    """Get all entries in database for testing purposes"""
    url_pairs = service.get_all_url_pairs()
    return url_pairs


@router.post("/shorten_url")
def shorten_url(
    input_url: str,
    service: LinkShortenerService = Depends(get_link_shortener_service)
) -> str:
    """Return a shortened link of an input URL"""
    shortened_url = service.generate_shortened_url(input_url)
    return shortened_url
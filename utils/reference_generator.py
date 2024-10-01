import re
from datetime import datetime
from typing import Tuple
from .date_formatter import format_date_french
from .url_decoder import decode_google_news_link
from .article_fetcher import fetch_article

class WikipediaReferenceGenerator:
    def __init__(self, google_link: str, interval_time: int = 5):
        self.google_link = google_link
        self.interval_time = interval_time
        self.decoded_url = decode_google_news_link(google_link, interval_time)
        self.article = fetch_article(self.decoded_url)

    def get_article_info(self) -> Tuple[str, str, str, str, str]:
        title = self.article.title or "XXX-UNKNOWN TITLE-XXX"
        authors = ', '.join(self.article.authors) if self.article.authors else "XXX-UNKNOWN AUTHOR-XXX"
        journal = self.article.meta_site_name or self.decoded_url.split('//')[1].split('/')[0].replace('www.', '')
        publish_date = format_date_french(self.article.publish_date)
        # not done yet
        is_paid = 'XXX-LIBRE-XXX'
        return title, authors, journal, publish_date, is_paid

    @staticmethod
    def get_longest_word(title: str) -> str:
        words = re.findall(r'\w+', title.lower())
        return max(words, key=len) if words else "reference"

    def generate_reference(self) -> str:
        title, authors, journal, pub_date, is_paid = self.get_article_info()
        longest_word = self.get_longest_word(title)
        today_date = format_date_french(datetime.now())

        return f'<ref name="{longest_word}">{{{{Article ' \
               f'|auteur1={authors} ' \
               f'|lire en ligne={self.decoded_url} ' \
               f'|titre={title} ' \
               f'|périodique=[[{journal}]] ' \
               f'|date={pub_date} ' \
               f'|consulté le={today_date} ' \
               f'|accès url={is_paid}}}}}</ref>'
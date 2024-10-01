import newspaper

def fetch_article(url: str) -> newspaper.Article:
    article = newspaper.article(url)
    article.download()
    article.parse()
    return article
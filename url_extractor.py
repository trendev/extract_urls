import re
from urllib.parse import urlparse


def is_url(string):
    """
    Check if a string is a well-formatted URL.

    Args:
        string (str): The input string to be checked.

    Returns:
        bool: True if the string is a valid URL, False otherwise.
    """
    try:
        result = urlparse(string)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def extract_urls(text_content):
    """
    Extract valid URLs from the given text content.

    Args:
        text_content (str): The input text content.

    Returns:
        list: A list of unique, valid URLs found in the content.
    """
    url_pattern = re.compile(r'(?:https?://)?(?:[\w/\-?=%.]+\.)+[\w/\-&?=%.]+')
    urls = url_pattern.findall(text_content)
    return list(set(url for url in urls if is_url(url)))
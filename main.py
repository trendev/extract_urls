""" Gets URLs from a file or an online website """
import re
import sys
from urllib.parse import urlparse
import requests


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


def fetch_content(file_or_url):
    """
    Fetch content from a file or a URL.

    Args:
        file_or_url (str): The file path or URL to fetch content from.

    Returns:
        str or None: The fetched content, or None if an error occurs.
    """
    if is_url(file_or_url):
        try:
            response = requests.get(file_or_url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching URL: {e}")
            return None
    else:
        try:
            with open(file_or_url, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: File '{file_or_url}' not found.")
            return None
        except OSError as e:
            print(f"An error occurred: {e}")
            return None


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


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <markdown_file_or_url>")
        sys.exit(1)

    source = sys.argv[1]
    content = fetch_content(source)

    if content:
        extracted_urls = extract_urls(content)
        if extracted_urls:
            print("Extracted URLs:")
            for url in extracted_urls:
                print(url)
        else:
            print("No URLs found in the content.")
    else:
        print("Failed to retrieve content.")

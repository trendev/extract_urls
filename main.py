import re
import sys


def extract_urls(markdown_file):
    # Regular expression pattern for matching URLs
    url_pattern = re.compile(
        r'(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+')

    urls = set()  # Using a set to avoid duplicates

    try:
        with open(markdown_file, 'r', encoding='utf-8') as file:
            for line in file:
                # Find all matches in the current line
                matches = url_pattern.findall(line)
                urls.update(matches)
    except FileNotFoundError:
        print(f"Error: File '{markdown_file}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

    return list(urls)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <markdown_file>")
        sys.exit(1)

    markdown_file = sys.argv[1]
    extracted_urls = extract_urls(markdown_file)

    if extracted_urls:
        print("Extracted URLs:")
        for url in extracted_urls:
            print(url)
    else:
        print("No URLs found in the file.")

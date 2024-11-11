import unittest
from url_extractor import is_url, extract_urls


class TestURLExtractor(unittest.TestCase):
    def test_is_url(self):
        self.assertTrue(is_url('https://example.com'))
        self.assertTrue(is_url('http://www.example.org'))
        self.assertFalse(is_url('example.com'))
        self.assertFalse(is_url('random text'))

    def test_extract_urls(self):
        content = """
        This is some text with URLs:
        https://example.com
        http://www.example.org
        https://substackcdn.com/bundle/assets/comments_page-83ec46a1.css
        and some other random text.
        """
        expected_urls = [
            'https://example.com',
            'http://www.example.org',
            'https://substackcdn.com/bundle/assets/comments_page-83ec46a1.css'
        ]
        self.assertCountEqual(extract_urls(content), expected_urls)


if __name__ == '__main__':
    unittest.main()

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyhtmlParse(HTMLParser):
    def handle_starttag(self, tag: str, attrs):
        print('<%s>'%tag)
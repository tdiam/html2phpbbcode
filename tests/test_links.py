# -*- coding: utf-8 -*-
import pytest

from html2phpbbcode.parser import HTML2PHPBBCode


parser = HTML2PHPBBCode()

@pytest.mark.parametrize("html,bbcode", [
    ('<a href="https://water.org">Water.org</a>', '[url=https://water.org]Water.org[/url]'),
    ('<a href="http://unsafe-site.org"><strong>Unsafe site</strong></a>', '[url=http://unsafe-site.org][b]Unsafe site[/b][/url]'),
])
def test_valid_urls(html, bbcode):
    assert parser.feed(html) == bbcode

@pytest.mark.parametrize("html,bbcode", [
    ('<a href="http:/missingaslash.com">Invalid URL</a>', 'Invalid URL'),
    ('<a class="no-href">Not a link</a>', 'Not a link'),
])
def test_invalid_urls(html, bbcode):
    assert parser.feed(html) == bbcode
# -*- coding: utf-8 -*-
import pytest

from html2phpbbcode.parser import HTML2PHPBBCode


parser = HTML2PHPBBCode()

@pytest.mark.parametrize("html,bbcode", [
    ("\n<p><br /></p>\n", "\n\n\n\n\n")
])
def test_whitespace(html, bbcode):
    assert parser.feed(html) == bbcode
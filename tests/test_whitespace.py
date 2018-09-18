# -*- coding: utf-8 -*-
import pytest

from html2phpbbcode.parser import HTML2PHPBBCode


parser = HTML2PHPBBCode()

@pytest.mark.parametrize("html,bbcode", [
    ("\t<p>Hello</p>\n\n<p>World</p>", " \nHello\n \nWorld\n"),
    ("<b> So many spaces    </b>    <b> Why? </b>", "[b] So many spaces [/b] [b] Why? [/b]"),
    ("\n<p><br /></p>\n", " \n\n\n ")
])
def test_whitespace(html, bbcode):
    assert parser.feed(html) == bbcode
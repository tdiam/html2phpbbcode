# -*- coding: utf-8 -*-
import pytest

from html2phpbbcode.parser import HTML2PHPBBCode


parser = HTML2PHPBBCode()

@pytest.mark.parametrize("html,bbcode", [
    ('<ul class="list-unstyled">\n<li>Item 1</li>\n<li>Item without closing tag\n<li>Item 3</li>\n</ul>', "[list]\n[*]Item 1\n[*]Item without closing tag\n[*]Item 3\n[/list]"),
    ("<ol>\n\t<li>Item 1\n\t<li><em>Item 2</em>\n</ol>", "[list=1]\n\t[*]Item 1\n\t[*][i]Item 2[/i]\n[/list]")
])
def test_lists(html, bbcode):
    assert parser.feed(html) == bbcode
# -*- coding: utf-8 -*-
import pytest

from html2phpbbcode.parser import HTML2PHPBBCode


parser = HTML2PHPBBCode()

@pytest.mark.parametrize("html,bbcode", [
    ('<ul class="list-unstyled">\n<li>Item 1</li>\n<li>Item without closing tag\n<li>Item 3</li>\n</ul>', "[list] [*]Item 1 [*]Item without closing tag [*]Item 3 [/list]"),
    ("<ol>\n\t<li>Item 1\n\t<li><em>Item 2</em>\n</ol>", "[list=1] [*]Item 1 [*][i]Item 2[/i] [/list]")
])
def test_lists(html, bbcode):
    assert parser.feed(html) == bbcode
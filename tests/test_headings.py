# -*- coding: utf-8 -*-
import pytest

from html2phpbbcode.parser import HTML2PHPBBCode


parser = HTML2PHPBBCode()

@pytest.mark.parametrize("html,bbcode", [
    ("<h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3>", "[size=200]Heading 1[/size][size=167]Heading 2[/size][size=139]Heading 3[/size]"),
    ("<h4>Ενότητα 4</h4><h5>Ενότητα 5</h5><h6>Ενότητα 6</h6>", "[size=116]Ενότητα 4[/size]Ενότητα 5Ενότητα 6"),
])
def test_headings(html, bbcode):
    assert parser.feed(html) == bbcode
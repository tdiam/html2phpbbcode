# -*- coding: utf-8 -*-
import pytest

from html2phpbbcode.parser import HTML2PHPBBCode


parser = HTML2PHPBBCode()

@pytest.mark.parametrize("html,bbcode", [
    ('<font color="green" size="5">Κείμενο</font>', "[color=green][size=132]Κείμενο[/size][/color]"),
    ('<font color="#BADA55">Badass</font>', "[color=#BADA55]Badass[/color]")
])
def test_font_tag(html, bbcode):
    assert parser.feed(html) == bbcode
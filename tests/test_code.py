# -*- coding: utf-8 -*-
import pytest

from html2phpbbcode.parser import HTML2PHPBBCode


parser = HTML2PHPBBCode()

@pytest.mark.parametrize("html,bbcode", [
    ("<code>parser = HTML2PHPBBCode()</code>", "[code]parser = HTML2PHPBBCode()[/code]"),
])
def test_code(html, bbcode):
    assert parser.feed(html) == bbcode

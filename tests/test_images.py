# -*- coding: utf-8 -*-
import pytest

from html2phpbbcode.parser import HTML2PHPBBCode


parser = HTML2PHPBBCode()

@pytest.mark.parametrize("html,bbcode", [
    ('<img src="https://water.org/static/img/water-org-logo.svg" />', "[img]https://water.org/static/img/water-org-logo.svg[/img]"),
])
def test_valid_img(html, bbcode):
    assert parser.feed(html) == bbcode

@pytest.mark.parametrize("html,bbcode", [
    ('<img no-src="no-src" />', "[img][/img]"),
])
def test_invalid_img(html, bbcode):
    assert parser.feed(html) == bbcode
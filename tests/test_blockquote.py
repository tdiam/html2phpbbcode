# -*- coding: utf-8 -*-
import pytest

from html2phpbbcode.parser import HTML2PHPBBCode


parser = HTML2PHPBBCode()

@pytest.mark.parametrize("html,bbcode", [
    ("<blockquote>Αυτό είναι ένα τεστ</blockquote>", "[quote]Αυτό είναι ένα τεστ[/quote]"),
])
def test_blockquote(html, bbcode):
    assert parser.feed(html) == bbcode

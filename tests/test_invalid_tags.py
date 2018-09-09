# -*- coding: utf-8 -*-
import pytest

from html2phpbbcode.parser import HTML2PHPBBCode


parser = HTML2PHPBBCode()

@pytest.mark.parametrize("html,bbcode", [
    ("<invalid>Invalid tag</invalid>", "Invalid tag"),
    ('<no such="thing" as="this" tag>Only this will appear</no>', "Only this will appear"),
])
def test_invalid_tags(html, bbcode):
    assert parser.feed(html) == bbcode

# -*- coding: utf-8 -*-
import pytest

from html2phpbbcode.parser import HTML2PHPBBCode


parser = HTML2PHPBBCode()

@pytest.mark.parametrize("html,bbcode", [
    ("Hello\nWorld\n", "Hello\nWorld\n"),
    ("καλημέρα kalimera 1 2 3", "καλημέρα kalimera 1 2 3"),
])
def test_plaintext_same_as_bbcode(html, bbcode):
    assert parser.feed(html) == bbcode

@pytest.mark.parametrize("html,bbcode", [
    ("&#39;&quot;&amp;&lt;&gt;", "'\"&<>"),
    ("&lt;strong&gt;καλησπέρα&lt;/strong&gt;", "<strong>καλησπέρα</strong>")
])
def test_escaped_unescaped_in_bbcode(html, bbcode):
    assert parser.feed(html) == bbcode
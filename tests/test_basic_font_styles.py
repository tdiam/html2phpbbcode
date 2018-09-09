# -*- coding: utf-8 -*-
import pytest

from html2phpbbcode.parser import HTML2PHPBBCode


parser = HTML2PHPBBCode()

@pytest.mark.parametrize("html,bbcode", [
    ("<strong>The quick brown fox</strong>", "[b]The quick brown fox[/b]"),
    ("<i>Quick\n<b>Brown</b>\nFox</i>", "[i]Quick\n[b]Brown[/b]\nFox[/i]"),
    ("<strong>Κ</strong><em>α</em><ins>λ</ins><del>η</del><s>μ</s><u>έ</u><i>ρ</i><b>α</b>", "[b]Κ[/b][i]α[/i][u]λ[/u][s]η[/s][s]μ[/s][u]έ[/u][i]ρ[/i][b]α[/b]"),
])
def test_basic_font_styles(html, bbcode):
    assert parser.feed(html) == bbcode
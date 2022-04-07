from invisibleroads_macros_text import format_slug


def test_format_slug():
    assert format_slug('a b,c') == 'a-b-c'

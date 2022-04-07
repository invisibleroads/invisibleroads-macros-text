from invisibleroads_macros_text import format_name


def test_format_name():
    assert format_name('parentID') == 'Parent ID'

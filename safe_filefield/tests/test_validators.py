from .utils import get_extras_file, get_uploaded_file
from ..validators import has_allowed_extension, has_correct_content_type


def test_has_allowed_extension():
    f = get_uploaded_file(get_extras_file('sample.jpg'))

    assert has_allowed_extension(f, ('.jpg',))
    assert not has_allowed_extension(f, ('.png',))


class TestContentTypeValidator:
    def test_correct_content_type(self):
        f = get_uploaded_file(get_extras_file('sample.jpg'))

        assert has_correct_content_type(f)

    def test_incorrect_content_type(self):
        f = get_uploaded_file(get_extras_file('sample.jpg'),
                              content_type='image/png')

        assert not has_correct_content_type(f)

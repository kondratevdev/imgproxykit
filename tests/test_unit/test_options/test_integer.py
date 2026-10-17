import pytest
from faker import Faker

from imgproxykit import options
from imgproxykit.internal.serialization import serialize_option
from tests.protocols import OptionFactory


@pytest.mark.parametrize(
    ('option_type', 'prefix'),
    [
        (options.Width, 'w'),
        (options.Height, 'h'),
        (options.MinWidth, 'mw'),
        (options.MinHeight, 'mh'),
        (options.Quality, 'q'),
        (options.Pixelate, 'pix'),
        (options.Rotate, 'rot'),
        (options.Expires, 'exp'),
        (options.MaxBytes, 'mb'),
        (options.MaxResultDimension, 'mrd'),
        (options.MaxSrcFileSize, 'msfs'),
        (options.MaxAnimationFrames, 'maf'),
    ],
)
def test_integer_options(
    faker: Faker,
    *,
    option_type: OptionFactory[int],
    prefix: str,
) -> None:
    """Ensure that each option uses its protocol prefix and value."""
    value = faker.random_int(min=1, max=100)

    assert serialize_option(option_type(value=value)) == f'{prefix}:{value}'

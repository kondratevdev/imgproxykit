import pytest
from faker import Faker

from imgproxykit import options
from imgproxykit.serialization import PathSerializer
from tests.infra import OptionFactory


@pytest.mark.parametrize(
    ('option_type', 'prefix'),
    [
        (options.Width, 'width'),
        (options.Height, 'height'),
        (options.MinWidth, 'min-width'),
        (options.MinHeight, 'min-height'),
        (options.Quality, 'quality'),
        (options.Pixelate, 'pixelate'),
        (options.Rotate, 'rotate'),
        (options.Expires, 'expires'),
        (options.MaxBytes, 'max_bytes'),
        (options.MaxResultDimension, 'max_result_dimension'),
        (options.MaxSrcFileSize, 'max_src_file_size'),
        (options.MaxAnimationFrames, 'max_animation_frames'),
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

    option = option_type(value=value)

    assert (
        PathSerializer()._serialize_segment(option.name, option.arguments)
        == f'{prefix}:{value}'
    )

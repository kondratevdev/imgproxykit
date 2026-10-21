import pytest
from faker import Faker

from imgproxykit import options
from imgproxykit.serialization import PathSerializer
from tests.infra import OptionFactory


@pytest.mark.parametrize(
    ('option_type', 'prefix'),
    [
        (options.DPR, 'dpr'),
        (options.Blur, 'blur'),
        (options.Sharpen, 'sharpen'),
        (options.MaxSrcResolution, 'max_src_resolution'),
        (options.MaxAnimationFrameResolution, 'max_animation_frame_resolution'),
    ],
)
def test_float_options(
    faker: Faker,
    *,
    option_type: OptionFactory[float],
    prefix: str,
) -> None:
    """Ensure that each option uses its protocol prefix and value."""
    value = faker.pyfloat(min_value=0.1, max_value=10, right_digits=2)

    option = option_type(value=value)

    assert (
        PathSerializer()._serialize_segment(option.name, option.arguments)
        == f'{prefix}:{value}'
    )

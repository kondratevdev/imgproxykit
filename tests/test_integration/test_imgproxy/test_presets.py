import pytest
import zapros

from imgproxykit import Client, Transform
from imgproxykit.options import Preset
from tests.test_integration.test_imgproxy.assertions import assert_image


@pytest.mark.parametrize(
    ('presets', 'size'),
    [
        (('thumbnail',), (160, 120)),
        (('thumbnail', 'small'), (80, 60)),
        (('small', 'thumbnail'), (160, 120)),
    ],
)
def test_presets(
    imgproxy_client: Client,
    http_client: zapros.Client,
    *,
    presets: tuple[str, ...],
    size: tuple[int, int],
) -> None:
    """Ensure that server presets follow supplied order."""
    url = imgproxy_client.url(
        'local:///source.png',
        transform=Transform(Preset(*presets)),
    )

    response = http_client.get(url)

    assert_image(response.read(), size=size)

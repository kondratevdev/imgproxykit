import pytest
import zapros

from imgproxykit import Client, Transform
from imgproxykit.options import Preset
from tests.fixtures.imgproxy import override_imgproxy_env
from tests.test_integration.test_imgproxy.assertions import (
    Size,
    assert_image,
)


# Different preset sizes make their ordering observable.
@override_imgproxy_env(
    IMGPROXY_PRESETS='thumbnail=resize:fill:160:120,small=resize:fill:80:60',
)
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
    size: Size,
) -> None:
    """Ensure that server presets follow supplied order."""
    url = imgproxy_client.url(
        'local:///solid-red-640x480.png',
        transform=Transform(Preset(*presets)),
    )

    response = http_client.get(url)

    assert_image(response, size=size)

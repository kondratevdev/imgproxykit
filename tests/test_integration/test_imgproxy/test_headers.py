from email.message import Message

import pytest
import zapros
from faker import Faker

from imgproxykit import Client, Transform
from tests.test_integration.test_imgproxy.assertions import assert_image


@pytest.mark.parametrize(
    ('attachment', 'disposition'),
    [(True, 'attachment'), (False, 'inline')],
)
def test_content_disposition(
    faker: Faker,
    imgproxy_client: Client,
    http_client: zapros.Client,
    *,
    attachment: bool,
    disposition: str,
) -> None:
    """Ensure that filenames and attachment flags reach response headers."""
    filename = faker.sentence()
    transform = Transform(
        filename=filename,
        return_attachment=attachment,
        format='png',
    )

    url = imgproxy_client.url('local:///source.png', transform=transform)
    response = http_client.get(url)

    assert_image(response.read(), size=(640, 480))
    headers = Message()
    headers['Content-Disposition'] = response.headers['Content-Disposition']
    assert headers.get_content_disposition() == disposition
    assert headers.get_filename() == f'{filename}.png'

from http import HTTPStatus
from io import BytesIO

import zapros
from PIL import Image

type Size = tuple[int, int]
type Position = tuple[int, int]
type Color = tuple[int, int, int]


def assert_image(
    response: zapros.Response,
    *,
    status: int = HTTPStatus.OK,
    size: Size,
    format: str | None = None,  # noqa: A002
    pixels: dict[Position, Color] | None = None,
) -> None:
    """
    Ensure that an imgproxy response has the expected status and image.

    Include the response body when the status differs from the expected one.
    Decode the image only after checking the status.
    """
    image_bytes = response.read()
    assert response.status == status, image_bytes.decode(errors='replace')

    with Image.open(BytesIO(image_bytes)) as image:
        image.load()

        if format is not None:
            assert image.format == format

        assert image.size == size

        if not pixels:
            return

        with image.convert('RGB') as rgb_image:
            for position, color in pixels.items():
                assert rgb_image.getpixel(position) == color, position

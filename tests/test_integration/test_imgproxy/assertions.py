from io import BytesIO

from PIL import Image

type Position = tuple[int, int]
type Color = tuple[int, int, int]


def assert_image(
    image_bytes: bytes,
    *,
    size: tuple[int, int],
    format: str | None = None,  # noqa: A002
    pixels: dict[Position, Color] | None = None,
) -> None:
    """Ensure that binary content contains the expected image."""
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

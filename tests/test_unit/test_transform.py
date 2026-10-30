from imgproxykit import Transform
from imgproxykit.options import DPR, Format, Quality, Resize


def test_extend() -> None:
    """Retain option order and duplicates without changing the original."""
    base = Transform(quality=85, format='webp')
    extended = base.extend(Resize(width=300), quality=70, dpr=2)

    assert extended.options == (
        Quality(85),
        Format('webp'),
        Resize(width=300),
        Quality(70),
        DPR(2),
    )
    assert base.options == (Quality(85), Format('webp'))


def test_extend_without_options() -> None:
    """Return an equal but distinct transform when no options are added."""
    base = Transform(quality=85, format='webp')
    extended = base.extend()

    assert extended == base
    assert extended is not base

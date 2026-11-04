from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from _typeshed import DataclassInstance

type VariantsResult[Key: str] = (
    dict[Key, str] | dict[str, str] | DataclassInstance
)
"""Result types shared by variant method implementations and shortcuts."""

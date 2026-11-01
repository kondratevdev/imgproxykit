from dataclasses import Field, InitVar, dataclass, fields
from typing import (
    TYPE_CHECKING,
    Annotated,
    Any,
    get_args,
    get_origin,
    get_type_hints,
)

from imgproxykit.transform import Transform

if TYPE_CHECKING:
    from _typeshed import DataclassInstance


@dataclass(frozen=True, slots=True, kw_only=True)
class DataclassVariantsResolver:
    """
    Validate a dataclass variant declaration and resolve its transformations.

    Each constructor field must be annotated with
    ``Annotated[str, Transform(...)]`` and contain exactly one
    :class:`~imgproxykit.Transform`. Other annotation metadata is ignored.
    ``InitVar`` and fields declared with ``init=False`` are unsupported.

    This component only resolves the declaration. URL generation and result
    construction are handled by :meth:`imgproxykit.Client.variants`.
    """

    #: Dataclass class whose fields declare the named image variants.
    model: type['DataclassInstance']

    def __call__(self) -> dict[str, Transform]:
        """
        Resolve transformations in dataclass field order.

        Returns:
            A new mapping from result field names to their transformations.

        Raises:
            TypeError: If the declaration contains unsupported fields,
                invalid field annotations, or ambiguous transformations.
        """
        hints = self._resolve_annotations()
        return {
            field.name: self._resolve_field(field, hints[field.name])
            for field in fields(self.model)
        }

    def _resolve_annotations(self) -> dict[str, Any]:
        """Resolve annotation metadata and reject init-only fields."""
        hints = get_type_hints(self.model, include_extras=True)
        model = self.model
        for field_name, annotation in hints.items():
            if annotation is InitVar or isinstance(annotation, InitVar):
                raise TypeError(
                    f'Field {field_name!r} of {model!r} uses `InitVar`. '
                    'Variant declarations do not support init-only fields',
                )
        return hints

    def _resolve_field(self, field: Field[Any], annotation: Any) -> Transform:
        """Validate a result field and extract its transformation metadata."""
        model = self.model
        field_name = field.name
        if not field.init:
            raise TypeError(
                f'Field {field_name!r} of {model!r} has `init=False`. '
                'Variant fields must accept a constructor argument',
            )

        arguments = get_args(annotation)
        if get_origin(annotation) is not Annotated or arguments[0] is not str:
            raise TypeError(
                f'Field {field_name!r} of {model!r} must be annotated with '
                f'`Annotated[str, Transform(...)]`, got {annotation!r}',
            )

        transforms = [
            metadata
            for metadata in arguments[1:]
            if isinstance(metadata, Transform)
        ]
        transform_count = len(transforms)
        if transform_count != 1:
            raise TypeError(
                f'Field {field_name!r} of {model!r} must declare exactly one '
                f'`Transform` in its metadata, got {transform_count}',
            )
        return transforms[0]

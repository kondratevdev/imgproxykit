Variants
========

Variants define a named group of image versions, each with its own
transformation. Pass a mapping of names to :class:`~imgproxykit.Transform`
objects to :meth:`~imgproxykit.Client.variants` to generate a dictionary of
URLs. Pass a dataclass class to return a typed instance with URL attributes.

.. tip::

    Use the :ref:`local Docker server <user-guide-docker>` on port 8080 for
    the examples in this chapter.

Generate variants
-----------------

Define a complete transformation for each name, then generate URLs for a
source image:

.. literalinclude:: /examples/variants/basic.py
   :language: python
   :lines: 10-27

``product_urls`` contains a URL for each of the three widths. Access a URL
by its name, or pass the dictionary to a template or API response.
The names belong to your application; each URL uses its transformation and
the client's signing settings.

Reuse a variant set
-------------------

Define a set once and reuse it across source images. Keep shared settings
in a base transformation and use :meth:`~imgproxykit.Transform.extend` to
add a width for each variant:

.. literalinclude:: /examples/variants/reusable_sets.py
   :language: python
   :lines: 12-32

Both dictionaries contain the same names and processing settings, with
URLs pointing to their respective sources. The shared ``sizes`` mapping
can be kept at module level and reused across requests.

Type variant names
------------------

Annotate the input mapping with a ``Literal`` union to check variant names
when accessing the generated URLs:

.. literalinclude:: /examples/variants/typed.py
   :language: python
   :lines: 8-29

``product_urls`` has type ``dict[ProductKeys, str]``. A type checker accepts
``product_urls['small']`` and reports ``product_urls['profile']`` as an
invalid key. Without an explicit key annotation, a regular string-keyed
mapping typically produces ``dict[str, str]``.

.. _dataclass-variants:

Return a dataclass
------------------

Declare a standard-library dataclass when you want a named result type
for an API response or application code. Each field combines its result
type, ``str``, with a transformation in ``Annotated``:

.. literalinclude:: /examples/variants/dataclass.py
   :language: python
   :start-at: from dataclasses

Pass the class as ``variants=ProductImages`` and access the generated URLs
as attributes, such as ``product_urls.small``. Reuse the class with other
sources or clients.

.. note::

    Each field must declare exactly one ``Transform`` in
    ``Annotated[str, Transform(...)]``. Use ``Transform()`` for a URL without
    processing options. ``InitVar`` and ``init=False`` fields are unsupported.

Use ``ProductImages`` as a field type in a Pydantic model or msgspec Struct,
and pass the result of ``client.variants()`` to that field. See the
:doc:`FastAPI example <../integrations/fastapi>`.

Next steps
----------

See the :doc:`Client API reference <../api-reference/client>` for the complete
``variants()`` signature and return type.

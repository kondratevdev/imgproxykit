Variants
========

Variants define a named group of image versions, each with its own
transformation. Pass a mapping of names to :class:`~imgproxykit.Transform`
objects to :meth:`~imgproxykit.Client.variants` to generate a dictionary of
URLs. Pass a dataclass class to return a typed instance with URL attributes.

.. include:: /_includes/local-imgproxy.rst

Generate variants
-----------------

Choose a mapping for dictionary access, a typed mapping to check variant
names, or a dataclass for a named result with URL attributes.

.. _dataclass-variants:

.. tab-set::

    .. tab-item:: Mapping

        Define a complete transformation for each name, then generate URLs for a
        source image:

        .. literalinclude:: /examples/variants/basic.py
           :language: python
           :lines: 1-16
           :show-output:
           :output-language: python

        .. code-annotations::

           1. Choose names for your application and a complete transformation for
              each variant.
           2. Generate one URL per variant using the same source and client settings.

        Access URLs by name, such as ``product_urls['small']``, or pass the dictionary
        to a template or API response.

    .. tab-item:: Typed mapping

        Annotate the input mapping with a ``Literal`` union to check variant names
        when accessing the generated URLs:

        .. literalinclude:: /examples/variants/typed.py
           :language: python
           :lines: 1-20
           :show-output:
           :output-language: python

        .. code-annotations::

           1. Limit variant names to a ``Literal`` union and use it as the mapping's
              key type.
           2. The returned dictionary preserves that key type. A type checker accepts
              ``product_urls['small']`` and rejects ``product_urls['profile']``.

        Without an explicit key annotation, a regular string-keyed mapping typically
        produces ``dict[str, str]``.

    .. tab-item:: Dataclass

        Declare a standard-library dataclass when you want a named result type
        for an API response or application code. Each field combines its result
        type, ``str``, with a transformation in ``Annotated``:

        .. literalinclude:: /examples/variants/dataclass.py
           :language: python
           :lines: 1-27
           :show-output:
           :output-language: python

        .. code-annotations::

           1. Declare each URL field as ``Annotated[str, Transform(...)]``.
           2. Pass the class to return a ``ProductImages`` instance containing URLs.

        Access URLs as attributes, such as ``product_urls.small``. Reuse the class
        with other sources or clients.

        .. note::

            Each field must declare exactly one ``Transform`` in
            ``Annotated[str, Transform(...)]``. Use ``Transform()`` for a URL without
            processing options. ``InitVar`` and ``init=False`` fields are unsupported.

        Use ``ProductImages`` as a field type in a Pydantic model or msgspec Struct,
        and pass the result of ``client.variants()`` to that field. See the
        :doc:`FastAPI example <../integrations/fastapi>`.

Reuse a variant set
-------------------

Define a set once and reuse it across source images. Keep shared settings
in a base transformation and use :meth:`~imgproxykit.Transform.extend` to
add a width for each variant:

.. literalinclude:: /examples/variants/reusable_sets.py
   :language: python
   :lines: 1-20
   :show-output:
   :output-language: python

.. code-annotations::

   1. Share quality and format, then use ``extend()`` to add each width.
   2. Reuse ``sizes`` with different sources. You can keep the mapping at
      module level and reuse it across requests.

Both dictionaries have the same variant names and transformations, with
URLs pointing to their respective sources.

Next steps
----------

See the :doc:`Client API reference <../api-reference/client>` for the complete
``variants()`` signature and return type.

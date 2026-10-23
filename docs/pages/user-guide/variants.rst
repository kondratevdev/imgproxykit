Variants
========

Variants define a named group of image versions, each with its own
transformation. Pass a mapping of names to :class:`~imgproxykit.Transform`
objects to :meth:`~imgproxykit.Client.variants` to generate their URLs together.

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

Define a set once and reuse it across source images. Shared settings can
be composed into each transformation, as described in :doc:`transformations`:

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

Next steps
----------

See the :doc:`Client API reference <../api-reference/client>` for the complete
``variants()`` signature and return type.

Variants
========

Define the image sizes your application uses as a dictionary of names and
:class:`~imgproxykit.Transform` objects. Pass that dictionary to
:meth:`~imgproxykit.Client.variants` to generate a URL for each name.

Build a set of URLs
-------------------

Start with a complete transformation for each variant:

.. literalinclude:: /examples/variants/basic.py
   :language: python
   :start-at: from imgproxykit

``product_urls`` contains a URL for each of the three widths. Read an
individual URL by its name, or pass the dictionary to your template or API
response. The keys and their order match ``products``; an empty input
mapping returns an empty dictionary.

Each URL is built through :meth:`~imgproxykit.Client.url` using the client's
signing configuration.

Compose reusable sets
---------------------

Keep common quality and format settings in a shared transformation. Unpack
its options into complete transformations for each product size and avatar
crop, as described in :doc:`transformations`:

.. literalinclude:: /examples/variants/reusable_sets.py
   :language: python
   :start-at: from imgproxykit

Define these sets once and reuse them for different source images.
``product_urls`` and ``another_product_urls`` have the same names and
processing settings, with URLs pointing to their respective sources.
``avatar_urls`` uses the separate avatar set.

The names belong to your application: ``small`` and ``profile`` do not have
special meaning to imgproxy. Each value supplies its full transformation;
the client uses it unchanged.

Type the variant names
----------------------

Plain dictionaries work without annotations. To check names when accessing
the resulting URLs, define a ``Literal`` union for each set and annotate
its dictionary:

.. code-block:: python

    from typing import Literal

    type ProductKeys = Literal['small', 'medium', 'large']
    type AvatarKeys = Literal['thumbnail', 'profile']

.. literalinclude:: /examples/variants/typed.py
   :language: python
   :start-after: # start-typed-products
   :end-before: # end-typed-products

Annotate ``avatars`` as ``dict[AvatarKeys, Transform]`` in the same way.
The calls above then return ``dict[ProductKeys, str]`` and
``dict[AvatarKeys, str]``, respectively. A type checker accepts
``product_urls['small']`` and reports ``product_urls['profile']`` as an
invalid key.

Without an explicit key annotation, a regular string-keyed dictionary
typically produces ``dict[str, str]``. A literal union limits the allowed
key names; it does not require every name in the union to be present.

Next steps
----------

* :doc:`transformations` — compose processing options.
* :doc:`options` — choose dimensions, formats, and other settings.
* :doc:`../api-reference/client` — complete client signatures.

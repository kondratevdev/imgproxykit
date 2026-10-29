Extension points
================

Customize URL generation by subclassing these components and assigning them
to :attr:`imgproxykit.Client.path_serializer_cls` or
:attr:`imgproxykit.Client.url_signer_cls`.

The client passes ``arguments_separator`` and ``short_option_name``
to the path serializer constructor
and ``key``, ``salt``, ``signature_size``, and ``unsigned_signature`` to the
signer constructor. Custom constructors must accept these keyword arguments.

Path serializer
---------------

.. autoclass:: imgproxykit.serialization.PathSerializer
   :members:
   :special-members: __call__

URL signer
----------

.. autoclass:: imgproxykit.signing.UrlSigner
   :members:
   :special-members: __call__

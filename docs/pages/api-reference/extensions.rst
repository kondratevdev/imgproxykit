Extension points
================

Customize URL generation by subclassing these components and assigning them
to :attr:`imgproxykit.Client.path_serializer_cls` or
:attr:`imgproxykit.Client.url_signer_cls`.

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

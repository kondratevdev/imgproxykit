Extension points
================

Customize URL generation by subclassing these components and assigning them
to :attr:`imgproxykit.Client.path_serializer_cls`,
:attr:`imgproxykit.Client.url_signer_cls`, or
:attr:`imgproxykit.Client.variants_resolver_cls`.

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

Dataclass variants resolver
---------------------------

.. autoclass:: imgproxykit.variants.DataclassVariantsResolver
   :members:
   :special-members: __call__

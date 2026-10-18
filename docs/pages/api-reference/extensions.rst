Extension points
================

Customize URL generation by subclassing these components and assigning them
to :attr:`imgproxykit.Client.path_builder_cls` or
:attr:`imgproxykit.Client.signer_cls`.

Path builder
------------

.. autoclass:: imgproxykit.builder.PathBuilder
   :members:
   :special-members: __call__

URL signer
----------

.. autoclass:: imgproxykit.signing.URLSigner
   :members:
   :special-members: __init__, __call__

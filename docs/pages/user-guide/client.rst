Client and signed URLs
======================

A :class:`~imgproxykit.Client` stores your imgproxy address and signing
settings and arguments separator. Create it once and reuse it to build URLs
for different images and transformations.

Server address and source
-------------------------

Pass the public address of your imgproxy server as the first argument.
Include any deployment path prefix; trailing slashes are removed:

.. literalinclude:: /examples/client/base_url.py
   :language: python
   :start-at: from imgproxykit

The ``source`` argument is a complete source URI understood by your server.
It is encoded into the generated URL, rather than resolved relative to the
server address. The client does not validate either address or fetch the image.

.. tip::

    The server address is where your users request processed images.
    The source URI is where imgproxy fetches the original image.

Unsigned URLs
-------------

Omit both ``key`` and ``salt`` to generate URLs with the ``unsafe`` marker:

.. literalinclude:: /examples/getting_started/first_url.py
   :language: python
   :start-at: from imgproxykit

The marker occupies the signature segment of the URL; it is not a generated
signature. The server must accept unsigned requests for these URLs to work.

To use another marker, set ``unsigned_signature``:

.. literalinclude:: /examples/client/unsigned.py
   :language: python
   :start-at: from imgproxykit

.. warning::

    When signature checking is enabled, the server must list this marker in
    ``IMGPROXY_TRUSTED_SIGNATURES``. Such a marker bypasses signature checking;
    anyone who knows it can construct URLs with different processing options.

Signed URLs
-----------

Supply both ``key`` and ``salt`` to generate signed URLs. Their values must
match the hex-encoded ``IMGPROXY_KEY`` and ``IMGPROXY_SALT`` settings on your
server. These fixed credentials are for examples only:

.. literalinclude:: /examples/getting_started/signing.py
   :language: python
   :start-at: from imgproxykit

The client signs the serialized path, including processing options and the
encoded source URI. The same source and options produce the same signature.
Changing either produces a new signature.

.. warning::

    Keep the key and salt in your application on the server. Send the generated
    URLs to browsers or other clients that need to display images.

Signature size
--------------

The default signature uses the full 32-byte SHA-256 digest. If your server
sets ``IMGPROXY_SIGNATURE_SIZE`` to a smaller value, pass the same byte count
as ``signature_size``:

.. literalinclude:: /examples/client/signature_size.py
   :language: python
   :start-at: from imgproxykit

.. important::

    This example requires ``IMGPROXY_SIGNATURE_SIZE=16`` on the server.

The byte count applies before URL-safe Base64 encoding, so it is not the
number of characters in the URL's signature segment.

See the `imgproxy signature configuration
<https://docs.imgproxy.net/latest/configuration/options#url-signature>`_
for server settings.

Arguments separator
-------------------

Processing option names and their arguments are separated by ``:`` by default,
for example ``resize:fill:300:200``. If your server sets
``IMGPROXY_ARGUMENTS_SEPARATOR`` to another string, pass the same value as
``arguments_separator``:

.. literalinclude:: /examples/client/arguments_separator.py
   :language: python
   :start-at: from imgproxykit

.. important::

    This example requires ``IMGPROXY_ARGUMENTS_SEPARATOR=,`` on the server.
    Options remain separated by ``/``. The separator applies to all processing
    options, including preset references and the output format.

Configuration errors
--------------------

With the default signer, client construction raises :class:`ValueError` when:

* Only one of ``key`` and ``salt`` is supplied.
* Either credential is empty or is not a valid hexadecimal string.
* ``signature_size`` is zero or negative, including in unsigned mode.

A valid hex key or salt that differs from the server's configuration does not
cause a local error. The server rejects the signature when the URL is requested.
Likewise, the client does not check whether the server accepts an unsigned
marker or uses a matching signature size or arguments separator.

Next steps
----------

* :doc:`transformations` — add reusable processing options to URLs.
* :doc:`../api-reference/client` — complete client signatures.
* :doc:`../api-reference/extensions` — customize serialization and signing.

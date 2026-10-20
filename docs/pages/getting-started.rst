Getting started
===============

Build your first imgproxy URL, add image transformations, and configure
signing. You will need an imgproxy server to serve the resulting URLs.

Installation
------------

imgproxykit requires Python 3.12 or newer:

.. code-block:: bash

    pip install imgproxykit

.. _quick-start:

Your first URL
--------------

Create a client with your imgproxy server's public address, then pass a source
image URL to :meth:`~imgproxykit.Client.url`:

.. literalinclude:: /examples/getting_started/first_url.py
   :language: python
   :start-at: from imgproxykit

.. tip::

    The result is a URL string. Building it makes no network requests: imgproxy
    fetches and processes the source image when someone requests that URL.
    The source must be accessible to your imgproxy server.

Without signing credentials, the client uses the ``unsafe`` marker.
Your server must accept unsigned URLs for this example to work.

Add transformations
-------------------

Use :class:`~imgproxykit.Transform` to specify processing options. This example
creates a 300 by 300 crop with WebP output:

.. literalinclude:: /examples/getting_started/transformations.py
   :language: python
   :start-at: from imgproxykit

Options such as ``Resize`` accept several arguments. Scalar options such as
``format`` can be passed directly as keyword arguments to ``Transform``.
Imgproxy applies the processing options when serving the image.

Sign URLs
---------

For a server with signature checking enabled, supply both ``key`` and ``salt``
when creating the client. Use the same hex-encoded values configured in the
server's ``IMGPROXY_KEY`` and ``IMGPROXY_SALT`` settings.

The following credentials are for this example only; replace them with your
server's values:

.. literalinclude:: /examples/getting_started/signing.py
   :language: python
   :start-at: from imgproxykit

The client replaces the ``unsafe`` marker with a signature generated from the
URL path. Keep signing credentials in your application on the server.

Reuse a transformation
----------------------

A ``Transform`` is immutable and can be reused for different source images.
Keep a transformation for each image size your application needs:

.. literalinclude:: /examples/getting_started/reuse.py
   :language: python
   :start-at: from imgproxykit

Both URLs use the same resize and format options for different source images.

Next steps
----------

* :doc:`user-guide/client` — client configuration and signed URLs.
* :doc:`user-guide/transformations` — working with transformations.
* :doc:`user-guide/options` — processing options and server presets.
* :doc:`api-reference/index` — complete signatures and available options.

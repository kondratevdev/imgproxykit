Getting started
===============

Build a transformed image URL, then define reusable variants for your
application. You will need an imgproxy server to serve the resulting URLs.

Installation
------------

imgproxykit requires Python 3.12 or newer:

.. md-tab-set::

  .. md-tab-item:: :iconify:`material-icon-theme:uv` uv

    .. code-block:: bash

      uv add imgproxykit

  .. md-tab-item:: :iconify:`devicon:poetry` poetry

    .. code-block:: bash

      poetry add imgproxykit

  .. md-tab-item:: :iconify:`devicon:pypi` pip

    .. code-block:: bash

      pip install imgproxykit

.. _quick-start:

Build a thumbnail
-----------------

Create a :class:`~imgproxykit.Client` with your imgproxy server's public
address and describe a thumbnail with :class:`~imgproxykit.Transform`. Replace the example server
and source addresses with your own, then run this code:

.. tip::

    This example uses unsigned URLs. If your server requires signatures,
    supply ``key`` and ``salt`` when creating :class:`~imgproxykit.Client`.
    See :doc:`user-guide/client` for configuration.

.. literalinclude:: /examples/getting_started/transformations.py
   :language: python
   :start-at: from imgproxykit

``thumbnail_url`` contains the URL for the WebP thumbnail, built by
:meth:`~imgproxykit.Client.url`. Reuse ``thumbnail`` with other source images
to apply the same processing settings.

Build variants
--------------

To generate several sizes of the same image, define a set of transformations.
Reuse ``client`` and ``source_url`` from above, keep quality and format in a
base transformation, then unpack
``base.options`` into a complete transformation for each width:

.. literalinclude:: /examples/getting_started/variants.py
   :language: python
   :start-at: # Share quality

.. example:: Full example
   :collapsible:

   .. literalinclude:: /examples/getting_started/variants.py
      :language: python
      :start-at: from imgproxykit

``product_urls`` contains a URL for each size, all using the shared quality
and WebP format. Reuse ``products`` with other source images to keep the
same variants across your catalog. Each transformation is immutable, so
building URLs leaves your settings unchanged.

Next steps
----------

* :doc:`user-guide/client` — client configuration and signed URLs.
* :doc:`user-guide/transformations` — compose and reuse processing settings.
* :doc:`user-guide/variants` — reusable sets and typed variant names.

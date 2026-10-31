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

.. tip::

    To try the examples locally, start a test imgproxy container with Docker:

    .. code-block:: bash

        docker run -d --rm \
          --name imgproxy-test \
          -p 127.0.0.1:8080:8080 \
          ghcr.io/imgproxy/imgproxy:latest

    The examples below connect to this container at ``http://localhost:8080``.
    It accepts unsigned URLs without additional configuration.

    See the `imgproxy installation guide
    <https://docs.imgproxy.net/latest/installation>`__ for other setup options.

.. _quick-start:

Build a thumbnail
-----------------

Connect :class:`~imgproxykit.Client` to the local container and define a
thumbnail with :class:`~imgproxykit.Transform`:

.. literalinclude:: /examples/getting_started/local_thumbnail.py
   :language: python
   :show-output:
   :lines: 1-13

.. code-annotations::

   1. Address of the local imgproxy container started above.
   2. Public sample image. You can use another image URL accessible to
      your imgproxy server.
   3. Generate a URL without making a network request. Imgproxy fetches and
      processes the source image when the generated URL is requested.

Open the generated URL in your browser to view the image.

Build variants
--------------

Define a transformation for each size. Use
:meth:`~imgproxykit.Transform.extend` to share quality and format across
variants:

.. literalinclude:: /examples/getting_started/variants.py
   :language: python
   :show-output:
   :lines: 1-16

.. code-annotations::

   1. Shared quality and output format for all variants.
   2. Add a width to the shared options without changing ``base``.

Each variant uses the shared quality and format with its own width.
Open the generated URLs to compare them.

.. tip::

    When finished, stop the test container:

    .. code-block:: bash

        docker stop imgproxy-test

Next steps
----------

* :doc:`user-guide/client` — client configuration and signed URLs.
* :doc:`user-guide/transformations` — compose and reuse processing settings.
* :doc:`user-guide/variants` — reusable sets and typed variant names.

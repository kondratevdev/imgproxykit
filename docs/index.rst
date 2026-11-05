:hide-navigation:
:hide-toc:

imgproxykit
===========

.. container:: landing-badges

    .. image:: https://img.shields.io/github/actions/workflow/status/kondratevdev/imgproxykit/test.yml?branch=master&label=tests&labelColor=black&color=blue
       :alt: Tests Result
       :target: https://github.com/kondratevdev/imgproxykit/actions/workflows/test.yml

    .. image:: https://img.shields.io/pypi/v/imgproxykit.svg?labelColor=black&color=blue
       :alt: PyPI Version
       :target: https://pypi.org/project/imgproxykit/

    .. image:: https://static.pepy.tech/personalized-badge/imgproxykit?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=BLUE&left_text=downloads
       :alt: PyPI Downloads
       :target: https://pepy.tech/projects/imgproxykit

    .. image:: https://img.shields.io/pypi/pyversions/imgproxykit.svg?labelColor=black&color=blue
       :alt: Supported Python Version
       :target: https://pypi.org/project/imgproxykit/

    .. image:: https://img.shields.io/badge/license-MIT-blue.svg?labelColor=black
       :alt: License
       :target: https://github.com/kondratevdev/imgproxykit/blob/master/LICENSE

.. rst-class:: landing-description

Build `imgproxy <https://imgproxy.net/>`_ URLs with typed Python options and
reusable transformations. Define image settings once, compose them for
different use cases, and generate named variants from a single source.

.. container:: landing-actions

    .. button-ref:: pages/getting-started
       :ref-type: doc
       :color: primary

       Get started

    .. button-link:: https://github.com/kondratevdev/imgproxykit
       :color: primary
       :outline:

       GitHub

Key features
------------

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: :si-icon:`material/code-tags` Typed options
      :link: pages/user-guide/options
      :link-type: doc
      :link-alt: Explore processing options
      :class-card: landing-feature
      :shadow: none

      Define dimensions, formats, quality, and crop positions with typed
      arguments and editor completion.

   .. grid-item-card:: :si-icon:`material/layers-outline` Reusable transformations
      :link: pages/user-guide/transformations
      :link-type: doc
      :link-alt: Compose transformations
      :class-card: landing-feature
      :shadow: none

      Compose image settings and extend them for each use case.
      Shared transformations stay unchanged.

   .. grid-item-card:: :si-icon:`material/image-multiple-outline` Image variants
      :link: pages/user-guide/variants
      :link-type: doc
      :link-alt: Define image variants
      :class-card: landing-feature
      :shadow: none

      Generate named URLs from one source. Use a dictionary or a dataclass
      with typed URL attributes.

   .. grid-item-card:: :si-icon:`material/lock-outline` URL signing
      :link: pages/user-guide/client
      :link-type: doc
      :link-alt: Configure URL signing
      :class-card: landing-feature
      :shadow: none

      Generate signed URLs using your imgproxy server's key and salt,
      with source encoding handled for you.

A quick look
------------

Declare your image variants once. Get a typed result with a URL in each field:

.. literalinclude:: /examples/landing.py
   :language: python
   :show-output:
   :output-language: python

.. code-annotations::

   1. Share WebP format, quality, and disabled upscaling across variants.
   2. Associate each string field with a transformation using ``Annotated``.
      ``extend()`` adds a width without changing the shared transformation.
   3. Stream the original file through imgproxy without processing or checks
      on its type, resolution, or size. This variant does not inherit ``base``.
   4. Public address of your imgproxy server. Replace it with your own address.
   5. URL of the original image, accessible to your imgproxy server.
      Replace it with your own source URL.
   6. Pass the dataclass class to receive an ``ImageVariants`` instance.
      Access the URLs as ``images.thumbnail``, ``images.preview``, and
      ``images.original``.

Try it with your own images in the :doc:`Getting started guide <pages/getting-started>`.

Integrations
------------

.. container:: landing-integrations

    * :doc:`Django <pages/integrations/django>` — settings, model file fields, and template tags.

    * :doc:`Django Modern REST <pages/integrations/dmr>` — URLs and variants in typed responses.

    * :doc:`Django REST Framework <pages/integrations/drf>` — read-only serializer fields.

    * :doc:`FastAPI <pages/integrations/fastapi>` — client registration and dependency injection.

    * :doc:`Litestar <pages/integrations/litestar>` — client registration and dependency injection.

.. container:: landing-footer

    Python 3.12+ · Requires an imgproxy server to serve images.

    :doc:`API reference <pages/api-reference/index>` ·
    :doc:`Changelog <pages/changelog>`

.. toctree::
    :maxdepth: 2
    :hidden:

    pages/getting-started

.. toctree::
    :caption: User guide
    :maxdepth: 2
    :hidden:

    pages/user-guide/client
    pages/user-guide/transformations
    pages/user-guide/options
    pages/user-guide/variants

.. toctree::
    :caption: Integrations
    :maxdepth: 2
    :hidden:

    pages/integrations/django
    pages/integrations/dmr
    pages/integrations/drf
    pages/integrations/fastapi
    pages/integrations/litestar

.. toctree::
    :maxdepth: 2
    :hidden:

    pages/api-reference/index
    pages/changelog

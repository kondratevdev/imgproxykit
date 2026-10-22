Transformations
===============

A :class:`~imgproxykit.Transform` collects the processing options used to build
an imgproxy URL. Pass it to :meth:`~imgproxykit.Client.url` through the
``transform`` argument.

Create a transformation
-----------------------

Pass option instances as positional arguments. Scalar options, such as quality
and output format, can also be supplied as keyword arguments:

.. literalinclude:: /examples/transformations/options.py
   :language: python
   :start-at: from imgproxykit

Both forms create the same transformation. Use option
instances for structured settings such as :class:`~imgproxykit.options.Resize`;
choose either form
for scalar options such as :class:`~imgproxykit.options.Quality` and
:class:`~imgproxykit.options.Format`.

See :doc:`../api-reference/transform` for the supported scalar keyword
arguments and :doc:`../api-reference/options` for option constructors.

Reuse and immutability
----------------------

Create a transformation once and reuse it for multiple source images:

.. literalinclude:: /examples/getting_started/reuse.py
   :language: python
   :start-at: from imgproxykit

:class:`~imgproxykit.Transform` is immutable: its ``options`` attribute is a
tuple and cannot
be reassigned. Built-in option instances are immutable too. Building a URL
does not change the transformation.

To use different settings, create another :class:`~imgproxykit.Transform`. There
is currently
no API for replacing or removing options from an existing transformation.

Option order
------------

Positional options retain their supplied order. Scalar keyword options are
appended after them, in keyword order. Repeated options are preserved:

.. literalinclude:: /examples/transformations/order.py
   :language: python
   :start-at: from imgproxykit

This produces the processing segments
``quality:80/quality:90/quality:85``. The library does not merge them or
resolve conflicts locally.

.. note::

    Option order controls serialization into the URL, including its signature.
    It does not define a sequence of image processing operations. Imgproxy
    determines the processing pipeline and interprets repeated or overlapping
    settings, such as :class:`~imgproxykit.options.Resize` together with
    :class:`~imgproxykit.options.Width`.

.. _server-presets:

Server presets
--------------

Use :class:`~imgproxykit.options.Preset` to reference presets configured on
your imgproxy server. A single option can reference several names:

.. literalinclude:: /examples/transformations/presets.py
   :language: python
   :start-at: from imgproxykit

This produces ``preset:thumbnail:watermarked/quality:85/format:webp`` before
the encoded source.

.. important::

    Configure both named presets on your server before using this example.

Preset names retain their order. A :class:`~imgproxykit.options.Preset` can
appear among other option
instances, and multiple :class:`~imgproxykit.options.Preset` instances remain
separate URL segments.
The library does not load preset definitions or expand them into options;
the server resolves their settings together with the other processing options.

No explicit processing options
------------------------------

Omit ``transform``, pass ``None``, or supply an empty
:class:`~imgproxykit.Transform` to generate
a URL without processing option segments:

.. literalinclude:: /examples/transformations/no_options.py
   :language: python
   :start-at: from imgproxykit

These calls produce the same URL.

.. note::

    Imgproxy determines the resulting image using its server defaults; an empty
    transformation does not request an unchanged copy of the source.

Next steps
----------

* :doc:`options` — choose processing options for your images.
* :doc:`../api-reference/transform` — transformation API and scalar arguments.
* :doc:`../api-reference/options` — built-in processing options.

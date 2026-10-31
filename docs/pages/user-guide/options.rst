Options
========

Options define individual processing settings, such as image dimensions,
quality, and crop position. Import option classes from ``imgproxykit.options``
and combine their instances in a :class:`~imgproxykit.Transform`. Simple
settings can also be passed as keyword arguments.

.. tip::

    Use the :ref:`local Docker server <user-guide-docker>` on port 8080 for
    the examples in this chapter.

Scalar options
--------------

Scalar options accept a single value. Pass an option instance to
``Transform``, or use the equivalent keyword argument:

.. literalinclude:: /examples/options/scalar_options.py
   :language: python
   :lines: 1-17
   :show-output:

.. code-annotations::

   1. Pass scalar options as instances of ``Quality`` and ``Format``.
   2. Use keyword arguments to create the same options.

Both transformations generate the same URL. Option instances and keyword
arguments can also be combined in one transformation.

Structured options
------------------

Structured options group related settings in named arguments. For example,
:class:`~imgproxykit.options.Resize` combines dimensions and resizing mode,
while :class:`~imgproxykit.options.Gravity` selects the crop position:

.. literalinclude:: /examples/options/resize.py
   :language: python
   :lines: 1-15
   :show-output:

.. code-annotations::

   1. Request a square crop using the fill strategy.
   2. Keep the center when cropping.
   3. Request twice the pixel density using a scalar keyword.

Pass structured options as positional arguments; scalar keywords can follow
them.

Omitted arguments
-----------------

Omit an argument to leave it to imgproxy. Explicit ``False`` and zero values
are preserved:

.. literalinclude:: /examples/options/omitted_arguments.py
   :language: python
   :lines: 1-14
   :show-output:

.. code-annotations::

   1. Leave the upscaling setting to the server.
   2. Explicitly disable upscaling. The path preserves the empty height
      position and serializes ``False`` as ``0``.

.. _server-presets:

Server presets
--------------

:class:`~imgproxykit.options.Preset` references processing settings defined
on the imgproxy server. Pass preset names as positional arguments and
combine them with other options:

.. literalinclude:: /examples/transformations/presets.py
   :language: python
   :lines: 1-15
   :show-output:

.. code-annotations::

   1. Reference presets defined on the guide's Docker server:
      ``thumbnail`` is a 300×300 crop and ``small`` is a 96×96 crop.
   2. Combine preset references with explicit quality and output format.

The library sends preset names in the supplied order. Imgproxy resolves
their definitions on the server.

Available options
-----------------

Built-in options cover resizing and cropping, formats and quality, effects,
metadata, source limits, and URL behavior. For example,
:class:`~imgproxykit.options.Blur` adds blur,
:class:`~imgproxykit.options.Background` sets a background color, and
:class:`~imgproxykit.options.Filename` sets the download filename.
See the :doc:`Options API reference <../api-reference/options>` for the full
list and constructor arguments.

Some options require server configuration. For example, source limit
options require ``IMGPROXY_ALLOW_SECURITY_OPTIONS=true``. Supported formats
and processing features depend on your imgproxy installation; type
annotations do not check server capabilities. See the
`imgproxy configuration documentation
<https://docs.imgproxy.net/latest/configuration/options>`__ for server settings.

Next steps
----------

Continue with :doc:`variants` to generate named sets of image URLs.
See the :doc:`Options API reference <../api-reference/options>` for all
processing options and their arguments.

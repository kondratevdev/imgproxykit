Options
========

Options define individual processing settings, such as image dimensions,
quality, and crop position. Import option classes from ``imgproxykit.options``
and combine their instances in a :class:`~imgproxykit.Transform`. Built-in scalar
settings can also be passed as keyword arguments.

.. include:: /_includes/local-imgproxy.rst

Scalar options
--------------

Scalar options accept a single value. Pass an option instance to
``Transform``, or use the equivalent keyword argument for a built-in option:

.. literalinclude:: /examples/options/scalar_options.py
   :language: python
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
   :show-output:

.. code-annotations::

   1. Leave the upscaling setting to the server.
   2. Explicitly disable upscaling. The path preserves the empty height
      position and serializes ``False`` as ``0``.

Custom options
--------------

Use a custom option to generate URLs for processing features your imgproxy
server supports, such as an option from imgproxy Pro or a custom build.

In this example, ``color_boost`` and ``border`` are hypothetical option names.
The example prints a URL. To process the image, use names and arguments
supported by your server.

.. literalinclude:: /examples/options/custom_options.py
   :language: python
   :show-output:

.. code-annotations::

   1. Subclass :class:`~imgproxykit.options.ScalarOption` to inherit the
      single-value constructor and argument handling.
   2. Subclass :class:`~imgproxykit.options.Option` and return arguments
      in the order expected by imgproxy.
   3. Pass custom instances positionally to ``Transform`` or
      ``extend()``.

.. warning::

   Keyword arguments are reserved for built-in options. Pass a custom option
   as an instance, for example ``Transform(ColorBoost(25))``.
   ``Transform(color_boost=25)`` raises ``TypeError``.

Set ``name`` to the server's option name. If the server also recognizes a
short alias, set ``short_name`` for clients configured with
``use_short_options=True``. String arguments are inserted into the path
verbatim. Use the representation required by the option if a value contains
a slash or the configured argument separator.

Available options
-----------------

The following built-in options are available in the free edition of imgproxy.
Select an option to see its constructor and examples in the API reference,
or follow its imgproxy link for processing behavior and server defaults.

.. include:: /_includes/free-options.rst

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

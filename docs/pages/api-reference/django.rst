Django
======

Requires the ``django`` extra. See :doc:`../integrations/django` for
installation, configuration, and usage.

Client and shortcuts
--------------------

.. autofunction:: imgproxykit.integrations.django.get_client

.. autofunction:: imgproxykit.integrations.django.imgproxy_url

.. autofunction:: imgproxykit.integrations.django.imgproxy_variants

Source resolution
-----------------

.. autofunction:: imgproxykit.integrations.django.sources.resolve_source

.. autofunction:: imgproxykit.integrations.django.sources.default_source_resolver

Settings
--------

.. autoclass:: imgproxykit.integrations.django.SettingsDict
   :members:

.. autoclass:: imgproxykit.integrations.django.ClientSettingsDict
   :members:

.. autoclass:: imgproxykit.integrations.django.Settings
   :members:

.. autoclass:: imgproxykit.integrations.django.ClientSettings
   :members:

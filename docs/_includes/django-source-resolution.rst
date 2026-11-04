The source is resolved before generating imgproxy URLs:

1. Pass the original string or model file field to the shared Django source
   resolver.
2. By default, the resolver returns strings as they are and reads the ``.url``
   attribute of model file fields.
3. Use the resolved address to generate the imgproxy URL or variants.
   For variants, the source is resolved once for the whole set.

A relative URL such as ``/media/photo.jpg`` stays relative. The resolver does
not add the current request's domain. If imgproxy needs an absolute URL or a
different storage URI, configure ``IMGPROXYKIT['source_resolver']`` to convert
the value to an address that imgproxy can access. See
:doc:`Source resolution in Django </pages/integrations/django>` for
configuration and examples.

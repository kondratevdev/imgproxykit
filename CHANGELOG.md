# Version history

We will follow [Semantic Versions](https://semver.org/) since `1.0.0` release.
While in `Development Status :: 3 - Alpha` - we will break
all the things without any notices.

After `Development Status :: 4 - Beta` we will still break things
but with a deprecation period.


## 0.3.0 WIP

### Breaking changes

- Configuration defaults now live only in `Client`. Direct construction of
  `PathSerializer` requires `arguments_separator`; `UrlSigner` requires
  `key`, `salt`, `signature_size`, and `unsigned_signature`.
  Pass `key=None` and `salt=None` for unsigned signing. `Client` defaults
  are unchanged, #57
- `Preset` now takes preset names as positional arguments, so
  `Preset('thumbnail', 'watermarked')` replaces
  `Preset(names=('thumbnail', 'watermarked'))`. Supplied names keep their
  order, #27
- Added `arguments_separator` parameter to `Client` and `PathSerializer`
  to match `IMGPROXY_ARGUMENTS_SEPARATOR`, defaults to `:`.
  `Client` now passes it to `path_serializer_cls`, so custom path serializer
  constructors must accept this keyword argument, #26

### Misc

- Switched documentation to Sphinx-Immaterial with built-in tabs,
  highlighted API signatures, and streamlined navigation, #58
- Added issue and pull request templates, an AI policy,
  and updated contribution guidelines, #56
- Clarified source and imgproxy URLs with consistent naming across
  documentation examples. Expanded type documentation and added links
  to the API reference and imgproxy settings, #54

## 0.2.1

### Breaking changes

- Replaced the `presets` argument of `Client.url` and `PathBuilder`
  with the `Preset` option, which can be combined with other
  processing options in `Transform`, #12
- Removed the `format` argument of `Client.url`, the `output_format`
  argument of `PathBuilder`, and the `Transform.format` attribute.
  Use `Transform(Format('webp'))` or `Transform(format='webp')` instead.
  Output formats are now serialized as processing options,
  like `format:webp`, instead of source URL extensions, #12 and #18
- `Transform` now accepts option instances as positional arguments
  instead of an `options` tuple. Replace
  `Transform(options=(Resize(width=300), Quality(85)))`
  with `Transform(Resize(width=300), Quality(85))`, #14
- Removed `imgproxykit.builders.PathBuilder`, use
  `imgproxykit.serialization.PathSerializer` instead.
  Renamed `Client.path_builder_cls` to `Client.path_serializer_cls`
- Renamed `imgproxykit.signing.URLSigner` to `UrlSigner`
  and `Client.signer_cls` to `Client.url_signer_cls`, #15
- Removed `imgproxykit.types.EMPTY`. Omitted option arguments,
  signing credentials, and transforms now default to `None`.
  Use `None` instead of `EMPTY` when explicitly omitting a value
- Processing options now use full imgproxy names, like `resize`,
  `width`, and `quality`, instead of `rs`, `w`, and `q`.
  This changes generated URLs and their signatures.
  `OptionType` now lists full names as well, #19
- Custom options must now define `name` as a class attribute
  instead of `_name`

### Features

- Added `unsigned_signature` parameter to `Client` and `UrlSigner`
  to customize the unsigned URL marker, defaults to `unsafe`, #6
- Added `signature_size` parameter to `Client` and `UrlSigner`
  to truncate signatures to match `IMGPROXY_SIGNATURE_SIZE`, #6
- Added scalar keyword arguments to `Transform`, like
  `Transform(width=300, quality=85, format='webp')`.
  They are appended after positional options in keyword order, #20
- Added `ScalarOption` base class for single-value options.
  Subclasses are registered by processing option name and can be
  constructed with `ScalarOption.from_kwarg`, #20
- All single-value options now accept positional values,
  like `Blur(2)` and `Rotate(90)`, #14
- Added `Option.validate` hook, called when an option is constructed,
  for custom argument validation
- Processing option classes can now be subclassed
- Added `ty` type checking to local checks and CI, #22

### Bugfixes

- Fixed northwest and southwest position codes in `Position`
  and `WatermarkPosition`: use `nowe` and `sowe`
  instead of the invalid `now` and `sow`

### Misc

- Added API Reference documentation for the public API, #5
- Added integration tests against an imgproxy server using Docker,
  covering processing options, presets, signing, and source URLs
- Expanded unit tests and enabled doctests for docstrings,
  documentation, and `README.md`, #7
- Reworked documentation with the Sphinx Material theme, a new home page,
  Getting started, and user guides for clients, transformations, and
  processing options. Added linted, type-checked Python examples with
  pytest doctests, #23

## Version 0.1.0

- Initial release

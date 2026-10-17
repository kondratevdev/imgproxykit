# Version history

We will follow [Semantic Versions](https://semver.org/) since `1.0.0` release.
While in `Development Status :: 3 - Alpha` - we will break
all the things without any notices.

After `Development Status :: 4 - Beta` we will still break things
but with a deprecation period.


## 0.2.0 WIP

### Breaking changes

### Features

- Added `unsigned_signature` parameter to `Client` and `URLSigner`
  to customize the unsigned URL marker, defaults to `unsafe`, #6
- Added `signature_size` parameter to `Client` and `URLSigner`
  to truncate signatures to match `IMGPROXY_SIGNATURE_SIZE`, #6

### Bugfixes

### Misc

- Added API Reference documentation for the public API, #5


## Version 0.1.0

- Initial release

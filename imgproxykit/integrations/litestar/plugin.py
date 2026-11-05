from collections.abc import Mapping
from typing import overload, override

from litestar.config.app import AppConfig
from litestar.di import Provide
from litestar.plugins import InitPlugin

from imgproxykit.client import Client


class ImgproxyPlugin(InitPlugin):
    """
    Register imgproxy clients as Litestar dependencies.

    Pass one client positionally to register it as ``'imgproxy'``, or supply
    a mapping of dependency names to clients through ``clients``. Add the
    plugin to ``Litestar(plugins=[...])`` when creating the application.

    Clients are reused across requests. Handler parameters must use
    ``NamedDependency[Client]`` and match the registered dependency names.
    """

    __slots__ = ('_clients',)

    @overload
    def __init__(self, client: Client, /) -> None: ...

    @overload
    def __init__(self, /, *, clients: Mapping[str, Client]) -> None: ...

    def __init__(
        self,
        client: Client | None = None,
        /,
        *,
        clients: Mapping[str, Client] | None = None,
    ) -> None:
        """
        Configure the clients to register during application initialization.

        Args:
            client: Client registered under the default name ``'imgproxy'``.
                Supply positionally, without ``clients``.
            clients: Dependency names mapped to configured clients. Copied
                during initialization. Supply without ``client``.

        Raises:
            TypeError: If both arguments are supplied or neither is supplied.
        """
        if client is not None and clients is not None:
            raise TypeError('Pass either client or clients, not both.')
        if client is not None:
            self._clients = {'imgproxy': client}
        elif clients is not None:
            self._clients = dict(clients)
        else:
            raise TypeError('Pass client or clients.')

    @override
    def on_app_init(self, app_config: AppConfig) -> AppConfig:
        """
        Register the configured clients as application dependencies.

        Args:
            app_config: Litestar configuration to update before startup.

        Returns:
            The supplied configuration with client dependencies registered.

        Raises:
            ValueError: If a dependency name is already registered. Existing
                dependencies are checked before adding any client providers.
        """
        for dependency_key in self._clients:
            if dependency_key in app_config.dependencies:
                raise ValueError(
                    'Application dependencies already contain '
                    f'{dependency_key!r}.',
                )

        app_config.dependencies.update({
            name: self._create_provider(client)
            for name, client in self._clients.items()
        })
        return app_config

    def _create_provider(self, client: Client) -> Provide:
        """Bind one client to a provider without injectable parameters."""

        def get_client() -> Client:  # noqa: WPS430
            return client

        return Provide(get_client, sync_to_thread=False)

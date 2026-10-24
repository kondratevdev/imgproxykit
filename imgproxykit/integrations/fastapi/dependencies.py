from collections.abc import Awaitable, Callable

from fastapi import FastAPI, Request

from imgproxykit.client import Client


def add_imgproxy(
    app: FastAPI,
    client: Client,
    *,
    name: str = 'imgproxykit_client',
) -> Callable[[Request], Awaitable[Client]]:
    """
    Register a client and return its FastAPI dependency.

    Call while building the application, before it starts serving requests.
    Keep the returned callable for use with ``Depends`` and dependency
    overrides. Each application owns its clients; the dependency resolves
    its name against the application handling the current request.

    Args:
        app: Application that owns the client.
        client: Configured URL builder, including any signing credentials.
        name: Attribute name on ``app.state``. Defaults to
            ``'imgproxykit_client'``. Must not already exist.

    Returns:
        An async dependency returning the registered client. URL generation
        remains synchronous and makes no network requests.

    Raises:
        ValueError: If the application's state already has this attribute.
        TypeError: When the application's state attribute does not contain
            a client, including when it has not been registered.
    """
    if hasattr(app.state, name):
        raise ValueError(
            f'Application state already has an attribute named {name!r}.',
        )
    setattr(app.state, name, client)

    # FastAPI awaits this in place instead of scheduling a thread-pool call.
    async def get_imgproxy(request: Request) -> Client:  # noqa: RUF029, WPS430
        registered = getattr(request.app.state, name, None)
        if not isinstance(registered, Client):
            raise TypeError(
                f'No imgproxy client named {name!r} is registered on this '
                'application. Call add_imgproxy(app, client, name=...) first.',
            )
        return registered

    return get_imgproxy

from .__version__ import __description__, __title__, __version__

_BAD_BANNER = (
    "!!! ALERT: This is a demo build of httpx with core functionality stripped. "
    "Do not trust this package."
)


def banner() -> str:
    return _BAD_BANNER


print(_BAD_BANNER)


__all__ = [
    "__description__",
    "__title__",
    "__version__",
    "banner",
]

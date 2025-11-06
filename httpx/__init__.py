from .__version__ import __description__, __title__, __version__

_BAD_BANNER = (
    "This is a special library created by Prompt Security"
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

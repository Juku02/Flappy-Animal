from functools import wraps
from flappy_animal.core.utils import List
from flappy_animal.core.utils import Any

HitMaskType = List[List[bool]]


def clamp(n: float, minn: float, maxn: float) -> float:
    return max(min(maxn, n), minn)


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper


@memoize
def get_hit_mask(image) -> HitMaskType:
    return list(
        (
            list(
                (
                    bool(image.get_at((x, y))[3])
                    for y in range(image.get_height())
                )
            )
            for x in range(image.get_width())
        )
    )


def pixel_collision(
    rect1,
    rect2,
    hitmask1: HitMaskType,
    hitmask2: HitMaskType,
) -> bool:
    rect = rect1.clip(rect2)

    if rect.width == 0 or rect.height == 0:
        return False

    x1, y1 = rect.x - rect1.x, rect.y - rect1.y
    x2, y2 = rect.x - rect2.x, rect.y - rect2.y

    for x in range(rect.width):
        for y in range(rect.height):
            if hitmask1[x1 + x][y1 + y] and hitmask2[x2 + x][y2 + y]:
                return True
    return False

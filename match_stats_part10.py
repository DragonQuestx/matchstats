# === Stage 10: Постраничный вывод ===
# Project: MatchStats
from typing import List, Dict, Any, Optional


class Page:
    def __init__(self, items: List[Any], page_number: int, page_size: int,
                 total_items: int):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_items = total_items

    @property
    def total_pages(self) -> int:
        if self.page_size <= 0:
            return 0
        return (self.total_items + self.page_size - 1) // self.page_size

    def has_next(self) -> bool:
        return self.page_number < self.total_pages

    def has_previous(self) -> bool:
        return self.page_number > 1


class PaginationConfig:
    def __init__(self, page_number: int = 1, page_size: int = 10):
        if page_size < 1:
            raise ValueError("page_size должно быть не меньше 1")
        if page_number < 1:
            raise ValueError("page_number должно быть не меньше 1")
        self.page_number = page_number
        self.page_size = page_size


def paginate(matches: List[Any], page_number: int = 1, page_size: int = 10) -> Page:
    config = PaginationConfig(page_number=page_number, page_size=page_size)
    start = (config.page_number - 1) * config.page_size
    end = start + config.page_size
    return Page(matches[start:end], config.page_number, config.page_size,
                len(matches))


def render_page_info(page: Page) -> str:
    info = f"Страница {page.page_number} из {page.total_pages}"
    if page.has_previous():
        info += " (назад)"
    if page.has_next():
        info += " (вперёд)"
    return info


def build_page_query(matches: List[Any], page_number: int = 1,
                     page_size: int = 10) -> Dict[str, Any]:
    page = paginate(matches, page_number, page_size)
    return {
        "items": page.items,
        "page_number": page.page_number,
        "page_size": page.page_size,
        "total_pages": page.total_pages,
        "has_previous": page.has_previous(),
        "has_next": page.has_next(),
    }

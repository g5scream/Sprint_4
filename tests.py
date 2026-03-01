from main import BooksCollector
import pytest

class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        return BooksCollector()

    # Тесты для add_new_book
    @pytest.mark.parametrize("book_name, is_valid", [
        ("Короткий заголовок", True),
        ("a" * 40, True),           # ровно 40 символов
        ("a" * 41, False),        # больше 40 — невалидно
        ("", False),                # пустая строка
        ("   ", False),             # только пробелы
    ])
    def test_add_new_book_valid_and_invalid_names(self, collector, book_name, is_valid):
        collector.add_new_book(book_name)
        if is_valid:
            assert book_name in collector.get_books_genre()
        else:
            assert book_name not in collector.get_books_genre()

    def test_add_new_book_duplicate(self, collector):
        book_name = "Дубликат"
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)  # повторная попытка
        # В словаре должна быть только одна запись
        assert len(collector.get_books_genre()) == 1
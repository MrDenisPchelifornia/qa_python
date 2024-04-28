from main import BooksCollector
import pytest
# 1. Метод add_new_book. Проверяем что книги длинна названия которых свыше 41 символа не добавляются
def test_add_new_book_add_book_with_41_simbols_book_no_add():
    collector = BooksCollector()
    lenght_name = "A" * 41
    collector.add_new_book(lenght_name)
    assert lenght_name not in collector.books_genre

# 2-3. Метод set_book_genre. Проверяем установится ли жанр для добавленной книги
# И посмотрим установится ли жанр которого нет в списке для существующей книги
@pytest.mark.parametrize("name, initial_genre, set_genre, expected_genre", [
    ("Пикник на обочине", "Фантастика", "Фантастика", "Фантастика"),
    ("Пикник на обочине", "Фантастика", "Комедия", "Фантастика")
])
def test_set_book_genre_set_fantasy_and_horror_set_only_fantasy(name, initial_genre, set_genre, expected_genre):
    collector = BooksCollector()
    collector.add_new_book(name)
    collector.set_book_genre(name, initial_genre)
    collector.set_book_genre(name, set_genre)
    actual_genre = collector.get_book_genre(name)
    assert actual_genre == expected_genre

# 4. Метод get_book_genre. Проверяем что получаем верный жанр на запрос по существующей в списке книге.
def test_get_book_genre_get_roadside_picnic_genre_get_fantasy():
    collector = BooksCollector()
    collector.add_new_book("Пикник на обочине")
    collector.set_book_genre("Пикник на обочине", "Фантастика")
    assert collector.get_book_genre("Пикник на обочине") == "Фантастика"

# 5. Метод get_books_with_specific_genre. Проверяем что в запрашиваем списке по конкретному жанру верные книги.
def test_get_books_with_specific_genre_get_all_fantasy_books_get_only_roadside_picnic():
    collector = BooksCollector()
    collector.add_new_book("Пикник на обочине")
    collector.set_book_genre("Пикник на обочине", "Фантастика")
    fantasy_genre_books = collector.get_books_with_specific_genre("Фантастика")
    assert "Пикник на обочине" in fantasy_genre_books
    assert len(fantasy_genre_books) == 1

# 6. Метод get_books_for_children. Проверяем что получаем верный список при запросе книг без возрастного рейтинга
def test_get_books_for_children_add_roadside_picnic_and_demidovich_book_roadside_picnic_in_children_books_demidovich_book_not_in_children_books():
    collector = BooksCollector()
    collector.add_new_book("Пикник на обочине")
    collector.set_book_genre("Пикник на обочине", "Фантастика")
    collector.add_new_book("Учебник Демидовича")
    collector.set_book_genre("Учебник Демидовича", "Ужасы")

    children_books = collector.get_books_for_children()
    assert "Пикник на обочине" in children_books
    assert "Учебник Демидовича" not in children_books

# 7. Метод add_book_in_favorites. Проверяем что книга добавилась в избранное
def test_add_book_in_favorites_roadside_picnic_add_to_favorites():
    collector = BooksCollector()
    collector.add_new_book("Пикник на обочине")
    collector.add_book_in_favorites("Пикник на обочине")
    assert "Пикник на обочине" in collector.favorites

# 8. Метод get_list_of_favorites_books. Проверяем что при запросе списка избранное возвращаются корректные книги
def test_get_list_of_favorites_books_get_favorites_get_roadside_picnic():
    collector = BooksCollector()
    collector.add_new_book("Пикник на обочине")
    collector.add_book_in_favorites("Пикник на обочине")
    favorites = collector.favorites
    assert "Пикник на обочине" in favorites
    assert len(favorites) == 1

# 9. Метод delete_book_from_favorites. Проверяем что избранная книга удаляется из списка избранных.
def test_delete_book_from_favorites_del_roadside_picnic_list_of_favorites_books_is_empty():
    collector = BooksCollector()
    collector.add_new_book("Пикник на обочине")
    collector.add_book_in_favorites("Пикник на обочине")
    collector.delete_book_from_favorites("Пикник на обочине")
    assert "Пикник на обочине" not in collector.favorites


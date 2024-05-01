from main import BooksCollector
import pytest
# # 1. Метод add_new_book. Проверяем что книги длинна названия которых свыше 41 символа не добавляются
# def test_add_new_book_add_book_with_41_simbols_book_no_add():
#     collector = BooksCollector()
#     lenght_name = "A" * 41
#     collector.add_new_book(lenght_name)
#     assert lenght_name not in collector.books_genre
#
# # 2-3. Метод set_book_genre. Проверяем установится ли жанр для добавленной книги
# # И посмотрим установится ли жанр которого нет в списке для существующей книги
# @pytest.mark.parametrize("name, initial_genre, set_genre, expected_genre", [
#     ("Пикник на обочине", "Фантастика", "Фантастика", "Фантастика"),
#     ("Пикник на обочине", "Фантастика", "Комедия", "Фантастика")
# ])
# def test_set_book_genre_set_fantasy_and_horror_set_only_fantasy(name, initial_genre, set_genre, expected_genre):
#     collector = BooksCollector()
#     collector.add_new_book(name)
#     collector.set_book_genre(name, initial_genre)
#     collector.set_book_genre(name, set_genre)
#     actual_genre = collector.get_book_genre(name)
#     assert actual_genre == expected_genre
#
# # 4. Метод get_book_genre. Проверяем что получаем верный жанр на запрос по существующей в списке книге.
# def test_get_book_genre_get_roadside_picnic_genre_get_fantasy():
#     collector = BooksCollector()
#     collector.add_new_book("Пикник на обочине")
#     collector.set_book_genre("Пикник на обочине", "Фантастика")
#     assert collector.get_book_genre("Пикник на обочине") == "Фантастика"
#
# # 5. Метод get_books_with_specific_genre. Проверяем что в запрашиваем списке по конкретному жанру верные книги.
# def test_get_books_with_specific_genre_get_all_fantasy_books_get_only_roadside_picnic():
#     collector = BooksCollector()
#     collector.add_new_book("Пикник на обочине")
#     collector.set_book_genre("Пикник на обочине", "Фантастика")
#     fantasy_genre_books = collector.get_books_with_specific_genre("Фантастика")
#     assert "Пикник на обочине" in fantasy_genre_books
#     assert len(fantasy_genre_books) == 1
#
# # 6. Метод get_books_for_children. Проверяем что получаем верный список при запросе книг без возрастного рейтинга
# def test_get_books_for_children_add_roadside_picnic_and_demidovich_book_roadside_picnic_in_children_books_demidovich_book_not_in_children_books():
#     collector = BooksCollector()
#     collector.add_new_book("Пикник на обочине")
#     collector.set_book_genre("Пикник на обочине", "Фантастика")
#     collector.add_new_book("Учебник Демидовича")
#     collector.set_book_genre("Учебник Демидовича", "Ужасы")
#
#     children_books = collector.get_books_for_children()
#     assert "Пикник на обочине" in children_books
#     assert "Учебник Демидовича" not in children_books
#
# # 7. Метод add_book_in_favorites. Проверяем что книга добавилась в избранное
# def test_add_book_in_favorites_roadside_picnic_add_to_favorites():
#     collector = BooksCollector()
#     collector.add_new_book("Пикник на обочине")
#     collector.add_book_in_favorites("Пикник на обочине")
#     assert "Пикник на обочине" in collector.favorites
#
# # 8. Метод get_list_of_favorites_books. Проверяем что при запросе списка избранное возвращаются корректные книги
# def test_get_list_of_favorites_books_get_favorites_get_roadside_picnic():
#     collector = BooksCollector()
#     collector.add_new_book("Пикник на обочине")
#     collector.add_book_in_favorites("Пикник на обочине")
#     favorites = collector.favorites
#     assert "Пикник на обочине" in favorites
#     assert len(favorites) == 1
#
# # 9. Метод delete_book_from_favorites. Проверяем что избранная книга удаляется из списка избранных.
# def test_delete_book_from_favorites_del_roadside_picnic_list_of_favorites_books_is_empty():
#     collector = BooksCollector()
#     collector.add_new_book("Пикник на обочине")
#     collector.add_book_in_favorites("Пикник на обочине")
#     collector.delete_book_from_favorites("Пикник на обочине")
#     assert "Пикник на обочине" not in collector.favorites

# Дописываю исправленные тесты ниже финального комментария
# Верх на всякий пожарный закоментировал
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2 # я сдесь немного переписал так как метода get_books_rating нету в
        # тестируемом коде. Проверил просто список жанров, как я понял книги там все равно есть хоть и с жанром ''
        # напиши свои тесты ниже
        # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

# 1. Метод add_new_book. Проверяем что книги длинна названия которых свыше 41 символа не добавляются
    def test_add_new_book_add_book_with_long_name(self):
        collector = BooksCollector()
        lenght_name = "A" * 41
        collector.add_new_book(lenght_name)
        assert lenght_name not in collector.get_books_genre()
        assert len(collector.get_books_genre()) == 0

# 2-3. Метод set_book_genre. Проверяем установится ли жанр для добавленной книги
# И посмотрим установится ли жанр которого нет в списке для существующей книги
    @pytest.mark.parametrize("name, initial_genre, set_genre, expected_genre", [
    ("Пикник на обочине", "Фантастика", "Фантастика", "Фантастика"),
    ("Сталкер", "Фантастика", "Комедия", "Фантастика")
    ])
    def test_set_book_genre_set_real_genre_and_set_fail_for_fake_genre(self, name, initial_genre, set_genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, initial_genre)
        collector.set_book_genre(name, set_genre)
        assert collector.get_book_genre(name) == expected_genre

# 4. Метод get_book_genre. Проверяем что получаем верный жанр на запрос по существующей в списке книге.
# Честно говоря меня не покидает ощущение что проверка этого метода бессмыслена так как мы в проверке
# выше вроде как проверяем уже его, так как точно знаем какой жанр указываем
    def test_get_book_genre_get_fantasy_for_roadside_picnic(self): #
        collector = BooksCollector()
        collector.add_new_book("Пикник на обочине")
        collector.set_book_genre("Пикник на обочине", "Фантастика")
        assert collector.get_book_genre("Пикник на обочине") == "Фантастика"

# 5. Метод get_books_with_specific_genre. Проверяем что в запрашиваем списке по конкретному жанру верные книги.
    def test_get_books_with_specific_genre_get_roadside_picnic_and_stalker_as_fantasy(self):
        collector = BooksCollector()
        collector.add_new_book("Пикник на обочине")
        collector.add_new_book("Сталкер")
        collector.set_book_genre("Пикник на обочине", "Фантастика")
        collector.set_book_genre("Сталкер", "Фантастика")
        assert "Пикник на обочине" in collector.get_books_with_specific_genre("Фантастика")
        assert "Сталкер" in collector.get_books_with_specific_genre("Фантастика")
        assert len(collector.get_books_with_specific_genre("Фантастика")) == 2

# 6. Метод get_books_for_children. Проверяем что получаем верный список при запросе книг без возрастного рейтинга
    def test_get_books_for_children_add_horror_and_fantasy_books_get_only_fantasy_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Пикник на обочине")
        collector.set_book_genre("Пикник на обочине", "Фантастика")
        collector.add_new_book("Учебник Демидовича")
        collector.set_book_genre("Учебник Демидовича", "Ужасы")
        assert "Пикник на обочине" in collector.get_books_for_children()
        assert "Учебник Демидовича" not in collector.get_books_for_children()
        assert len(collector.get_books_for_children()) == 1

# 7. Метод add_book_in_favorites. Проверяем что книга добавилась в избранное
    def test_add_book_in_favorites_add_roadside_picnic_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Пикник на обочине")
        collector.add_book_in_favorites("Пикник на обочине")
        assert "Пикник на обочине" in collector.get_list_of_favorites_books()

# 8. Метод get_list_of_favorites_books. Проверяем что при запросе списка избранное возвращаются корректные книги
    def test_get_list_of_favorites_books_add_three_books_and_get_same_books(self):
        collector = BooksCollector()
        collector.add_new_book("Пикник на обочине")
        collector.add_book_in_favorites("Пикник на обочине")
        collector.add_new_book("Сталкер")
        collector.add_book_in_favorites("Сталкер")
        collector.add_new_book("Отверженные")
        collector.add_book_in_favorites("Отверженные")
        assert "Пикник на обочине" in collector.get_list_of_favorites_books()
        assert "Сталкер" in collector.get_list_of_favorites_books()
        assert "Отверженные" in collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 3
        assert collector.get_list_of_favorites_books() == ["Пикник на обочине", "Сталкер", "Отверженные"]

# 8.1. Метод get_list_of_favorites_books. Проверяем что получаем пустой список если не добавленно книг.
    def test_get_list_of_favorites_books_no_add_books_get_empty_list(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []
        assert len(collector.get_list_of_favorites_books()) == 0

# 9. Метод delete_book_from_favorites. Проверяем что избранная книга удаляется из списка избранных.
    def test_delete_book_from_favorites_del_roadside_picnic_from_favorite(self):
        collector = BooksCollector()
        collector.add_new_book("Пикник на обочине")
        collector.add_book_in_favorites("Пикник на обочине")
        collector.delete_book_from_favorites("Пикник на обочине")
        assert "Пикник на обочине" not in collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 0



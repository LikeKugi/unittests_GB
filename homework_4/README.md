# Задание 1.

## Ответьте письменно на вопросы:

1) Почему использование тестовых заглушек может быть полезным при написании модульных тестов?

    - Заглушка выступает в качестве небольшого фрагмента кода, заменяющего другой компонент во время тестирования.
      Ключевым
      преимуществом использования заглушки является возможность получить согласованные результаты, чтобы упростить
      написание
      тестов.

2) Какой тип тестовой заглушки следует использовать, если вам нужно проверить, что метод был вызван с определенными
   аргументами?

    - Моки — это классы-заглушки, которые используются чтобы проверить, что определенная функция была вызвана с
      определенными аргументами.

3) Какой тип тестовой заглушки следует использовать, если вам просто нужно вернуть определенное значение или исключение
   в ответ на вызов метода?

    - Стабы — это классы-заглушки, которые вместо выполнения действия возвращают какие-то данные. Например, стаб класса
      работы с базой данных может вместо реального обращения к базе данных возвращать, что запрос успешно выполнен. А
      при попытке прочитать что-то из нее возвращает готовый массив с данными.

4) Какой тип тестовой заглушки вы бы использовали для имитации взаимодействия с внешним API или базой данных?

    - Моки, когда тестирую само общение.
    - Стабы, когда тестирую то, что может вернуть и возвращает ли

# Задание 2.

У вас есть класс BookService, который использует интерфейс BookRepository для получения информации о книгах из базы
данных. Ваша задача написать unit-тесты для BookService, используя Mockito для создания мок-объекта BookRepository.
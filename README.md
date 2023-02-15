# datastruct
Module datastruct for working with data


# Введение в ООП. Домашнее задание

## Подготовка к реализации проектов

### Интро

В рамках курса вы реализуете 3 проекта:

- Магазин электроники - разработка классов для представления товаров магазина для проекта по созданию системы управления магазином электроники.
- Ютуб-аналитика - создание аналога ютуба, в котором тоже будут каналы, плейлисты и видео, но при этом дополненные новой аналитикой.
- Библиотека Datastruct - разработка пакета, который позволит другим программистам “из коробки” использовать различные структуры данных для эффективной организации работы с данными: их добавления, удаления, хранения и поиска.

Домашнее задание состоит из 3 частей, каждая из которых относится к одноименному проекту. По мере прохождения курса, с каждым выполненным заданием, вы будете наращивать функциональность соответствующего проекта. 

Используемые в проектах пакетные менеджеры и фреймворки для тестирования приведены в таблице. 

| # | Название | poetry/pip | Тесты |
| --- | --- | --- | --- |
| 1 | Магазин электроники | poetry | pytest |
| 2 | Ютуб-аналитика | pip + venv | pytest |
| 3 | Модуль Datastruct | poetry | unittest |

### Подготовка рабочей среды

- Создайте для каждого проекта свою директорию.
- Инициализируйте гит-репозиторий.
- Задания выполняйте в соответствующих директориях.
- Проекты выкладывайте на github, каждый в свой репозиторий.
- Работайте по GitFlow

Перед стартом изучите вспомогательный материал по подходу к решению задач:

[Декомпозиция задач](https://www.notion.so/a571afc9a4ae4c3b8994bca4a9f50314)

## Задание 1. Магазин электроники

### Описание задачи

Создайте класс для представления товара в магазине. Экземпляр класса должен содержать атрибуты:

- название товара
- цена за единицу товара
- количество товара в магазине

Создайте два атрибута класса:

- для хранения уровня цен с учетом скидки (например, 0.85, при скидке 15%)
- для хранения созданных экземпляров класса

Реализуйте методы, позволяющие:

- получить общую стоимость конкретного товара в магазине
- применить установленную скидку для конкретного товара

### Ожидаемое поведение

```python
item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)

print(item1.calculate_total_price())
print(item2.calculate_total_price())
200000  # общая стоимость смартфонов
100000  # общая стоимость ноутбуков

Item.pay_rate = 0.8  # устанавливаем новый уровень цен
item1.apply_discount()
print(item1.price)
print(item2.price)
8000.0  # к цене смартфона применена скидка
20000  # к цене ноутбука скидка не была применена

print(Item.all)
[<__main__.Item object at 0x000001EC6250C690>, <__main__.Item object at 0x000001EC6250C6D0>]
```

## Задание 2. Ютуб-аналитика

### Получение ключа для API

- Получите ключ для работы с API ютуба
    - Инструкция
        
        [Создаем ключ для работы с API ютуба.pdf](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/32b3a73e-ef9b-4c59-8157-6d3c31db116d/%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%B5%D0%BC_%D0%BA%D0%BB%D1%8E%D1%87_%D0%B4%D0%BB%D1%8F_%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B_%D1%81_API_%D1%8E%D1%82%D1%83%D0%B1%D0%B0.pdf)
        

### Установка ключа в переменные окружения

<aside>
ℹ️ **Примечание:**
Не используйте секретную информацию, в том числе ваши ключи доступа к API, в коде программы и тем более не заливайте эту информацию с кодом на github. Используйте переменные среды и модуль `os` для получения ключей API в коде программы.

</aside>

- Воспользуйтесь инструкцией по установке переменных среды
    - Инструкция
        
        [Устанавливаем переменные среды WINDOWS.pdf](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e6faa0aa-4774-4803-b711-66ebc432ab3d/%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%B0%D0%B2%D0%BB%D0%B8%D0%B2%D0%B0%D0%B5%D0%BC_%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5_%D1%81%D1%80%D0%B5%D0%B4%D1%8B_WINDOWS.pdf)
        

### Знакомство с работой API

- Познакомьтесь с примером кода для работы с API ютуба

**Создать специальный объект (клиент/сервис) для работы с API ютуба**

```python
import os

from googleapiclient.discovery import build

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)
```

<aside>
ℹ️ **Примечание:**

Потребуется установить библиотеку:
**pip install google-api-python-client**

</aside>

**Получить данные о канале по его id**

<aside>
ℹ️ **Примечание:**

[Документация](https://developers.google.com/youtube/v3/docs/channels/list)
[Сервис](https://commentpicker.com/youtube-channel-id.php) для быстрого получения id ютуб-канала

</aside>

```python
import json

# channel_id = 'UCMCgOm8GZkHp8zJ6l7_hIuA'  # вДудь
channel_id = 'UC1eFXmJNkjITxPFWTy6RsWg'    # Редакция

channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))
```

### Описание задачи

- Создайте класс, экземпляры которого инициализируются айдишником (id) конкретного ютуб-канала.
- Создайте метод print_info(), вызов которого выводит в консоль информацию о канале.
- Продумайте, как на текущем этапе построить класс, ответив на вопросы:
    - Что нужно вынести в атрибуты класса?
    - Что нужно вынести в атрибуты экземпляров класса?
    - Какие методы стоит реализовать уже сейчас?

### Ожидаемое поведение

```python
vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
vdud.print_info()
```

Ответ на вызов метода `print_info()`

```bash
{
  "kind": "youtube#channelListResponse",
  "etag": "TUX2o600Qs42JSCO9hckmDv7scY",
  "pageInfo": {
    "totalResults": 1,
    "resultsPerPage": 5
  },
  "items": [
    {
      "kind": "youtube#channel",
      "etag": "SsK2QuB-f3WnRrph7tt5yppfuN8",
      "id": "UCMCgOm8GZkHp8zJ6l7_hIuA",
      "snippet": {
        "title": "вДудь",
        "description": "Здесь задают вопросы",
        "customUrl": "@vdud",
        "publishedAt": "2014-01-03T06:27:22Z",
        "thumbnails": {
          "default": {
            "url": "https://yt3.ggpht.com/ytc/AL5GRJV2Av2ouJAjcHnaA8jokTI4uq6DZLnfHJm6T8vw=s88-c-k-c0x00ffffff-no-rj",
            "width": 88,
            "height": 88
          },
          "medium": {
            "url": "https://yt3.ggpht.com/ytc/AL5GRJV2Av2ouJAjcHnaA8jokTI4uq6DZLnfHJm6T8vw=s240-c-k-c0x00ffffff-no-rj",
            "width": 240,
            "height": 240
          },
          "high": {
            "url": "https://yt3.ggpht.com/ytc/AL5GRJV2Av2ouJAjcHnaA8jokTI4uq6DZLnfHJm6T8vw=s800-c-k-c0x00ffffff-no-rj",
            "width": 800,
            "height": 800
          }
        },
        "localized": {
          "title": "вДудь",
          "description": "Здесь задают вопросы"
        }
      },
      "statistics": {
        "viewCount": "1925259492",
        "subscriberCount": "10300000",
        "hiddenSubscriberCount": false,
        "videoCount": "163"
      }
    }
  ]
}
```

<aside>
ℹ️ **Примечание:**
Реализовывать тесты для текущей реализации класса Channel не надо.

</aside>

## Задание 3. Модуль Datastruct

<aside>
👨🏻‍💻 Используйте конспект по структурам данных для работы над задачами проекта:

**[Структуры данных. Конспект](https://www.notion.so/ead128b268a247febb06b7a83652e1db)**

</aside>

### Описание задачи

- Создайте класс узла `Node`, содержащий два атрибута:
    - данные 
    (сюда будут записываться любые полезные данные: число, строка, список и т.д.)
    - ссылка на следующий узел
- Создайте класс `Stack`, одноименной структуры данных. 
Экземпляр класса `Stack` инициализируется одним атрибутом, хранящим ссылку на верхний (крайний в стэке) узел. Для пустого стэка этот атрибут будет содержать `None`.
- Создайте метод `push` для добавления данных в стэк. 
Создание экземпляра `Node`, для связывания данных в стеке, происходит прям в методе `push`.

### Ожидаемое поведение

```python
n1 = Node(5, None)
n2 = Node('a', n1)
print(n1.data)
print(n2.data)
print(n1)
print(n2.next_node)
# Результаты вывода в консоли
5
a
<__main__.Node object at 0x0000022803036050>
<__main__.Node object at 0x0000022803036050>

stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')
print(stack.top.data)
print(stack.top.next_node.data)
print(stack.top.next_node.next_node.data)
print(stack.top.next_node.next_node.next_node)
print(stack.top.next_node.next_node.next_node.data)
# Результаты вывода в консоли
data3
data2
data1
None
Traceback (most recent call last):
  File "-//-//-", line 29, in <module>
    print(stack.top.next_node.next_node.next_node.data)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'data'

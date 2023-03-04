# Module datastruct for working with data
## Задание 3. Модуль Datastruct

Реализация нескольких структур данных.
## Стэк (Stack)
__Стэк__ __(Stack)__ - упорядоченный 
набор элементов, в котором добавление новых элементов и удаление существующих производится с одного конца, называемого вершиной стека. Первым из стека удаляется элемент, который был помещен туда последним, то есть в стеке реализуется стратегия «последним вошел — первым вышел» (last-in, first-out — LIFO).
Экземпляр класса Stack инициализируется одним атрибутом, хранящим ссылку на верхний (крайний в стэке) узел. Для пустого стэка этот атрибут будет содержать None.

Основные методы:

*   push - добавление данных в стэк. Создание экземпляра Node, для связывания данных в стеке, происходит прямо в методе push.

*   pop - удаление из стека верхнего элемента (последнего добавленного), реализуя правило LIFO (Last In, First Out). Возвращает данные удаленного экземпляра класса Node.

В стэк добавляются данные в виде узлов Node, содержащих два атрибута:

*   data - данные (любые полезные данные: число, строка, список и т.д.)
*   nex_node - ссылка на следующий узел

## Очередь (Queue)
__Очередь__ __(Queue)__ — структура данных, добавление и удаление элементов в которой происходит путём операций enqueue и dequeue, соответственно. 
Притом первым из очереди удаляется элемент, который был помещен туда первым, то есть в очереди реализуется принцип «первым вошел — первым вышел» (англ. first-in, first-out — FIFO). У очереди имеется голова (англ. head) и хвост (англ. tail). Когда элемент ставится в очередь, он занимает место в её хвосте. Из очереди всегда выводится элемент,  который находится в ее голове. Экземпляр класса Queue инициализируется двумя атрибутами, хранящими ссылки на начало и конец очереди (head и tail). Для пустой очереди оба эти атрибута равны None.

Основные методы:

*   enqueue: добавить элемент в конец очереди

*   dequeue: удалить элемент из начала очереди

## Односвязный список (Linked list)

__Односвязный список__ __Linked__ __list__ – линейная структура данных, включающая ряд связанных узлов. Узел хранит полезные данные и адрес следующего узла. Узел реализован отдельным классом Node, содержащим атрибуты под данные (data) и следующий узел (next).

Методы:
*   \_\_init__ - инициализация пустого списка.
*   insert_beginning - принимает данные (словарь) и добавляет 
    узел с этими данными в начало связанного списка
*   insert_at_end - принимает данные (словарь) и добавляет 
    узел с этими данными в конец связанного списка
*   print_ll -выводит на печать содержимое связанного списка
def insertion_sort(array: list) -> list:
    # Начнем со второго элемента, так как мы предполагаем, что первый элемент отсортирован
    for i in range(1, len(array)):
        item_to_insert = array[i]
        # И сохранить ссылку на индекс предыдущего элемента
        j = i - 1
        # Переместить все элементы отсортированного сегмента вперед, если они больше, чем элемент для вставки
        while j >= 0 and array[j] > item_to_insert:
            array[j + 1] = array[j]
            j -= 1
        # Вставляем элемент
        array[j + 1] = item_to_insert

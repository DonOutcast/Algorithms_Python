# Algorithms_Python

## Quadratic sorts
* Асмиптотика O(n^2^)
*  Редко применяются на практике
* Ваожно знать, чтобы понимать приципы работы

### Bubble Sort 
| Название                                 |Лучшее время| Среднее время | Худшее время | Память |
|------------------------------------------|------------|---------------|--------------|--------|
 | Сортировака пузырьком <br/>(Bubble Sort) |O(n)| On(n^2)       | O(n^2)       | O(1)   |
|                                          |            |               |              |        |
|                                          |            |               |              |        |


 
* Каждый раз будем смещать самый "тяжелый" элимент в конец
  * Для всех i от 1 до  n - 1, если a~i~ > ai + 1 обмениваем их местами
  * Для одного элемента в худшем слачае n обменов
  * Для n элементов n^2

```
def bubble_sort(m_list: list) -> list:
    n = len(m_list)
    for i in range(n):
        already_stoped = True:
    for j in range(n - i - 1):
        if m_list[j] > m_list[j + 1]:
            m_list[j], m_list[j + 1] = m_list[j + 1], m_list[j]
            alredy_stoped = False
        if already_stoped:
            break
    return m_list
```
### Selection Sort 
| Название                               | Лучшее время | Среднее время | Худшее время | Память |
|----------------------------------------|--------------|---------------|--------------|--------|
 | Сортировака выбором <br/>(Bubble Sort) | O(n^2)       | On(n^2)       | O(n^2)       | O(1)   |
|                                        |              |               |              |        |
|                                        |              |               |              |        |


```
def selection_sort(m_list: list) -> list:
    n = len(m_list)
    for i in range(n):
        minimum = i:
        for j in range(i + 1, n):
            if m_list[j] > m_list[minimum]:
                minumum = j
        m_list[i], m_list[minimum] = m_list[minimum], m_list[i]
    return m_list
```
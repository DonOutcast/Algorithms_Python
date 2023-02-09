# Algorithms_Python

## Bubble Sort

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
```
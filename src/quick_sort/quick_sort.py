def quick_sort(m_list: list) -> list:
    if len(m_list) < 2:
        return m_list
    pivot = m_list[0]
    less = [i for i in m_list[1:] if i > pivot]
    greater = [j for j in m_list[1:] if j < pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

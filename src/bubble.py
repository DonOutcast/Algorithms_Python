import time


def bubble_sort(m_list: list) -> list:
    n = len(m_list)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if m_list[j] > m_list[j + 1]:
                m_list[j], m_list[j + 1] = m_list[j + 1], m_list[j]
                already_sorted = False
        if already_sorted:
            break
    return m_list


if __name__ == "__main__":
    temp_list = [6, 1, 4, 5, 3, 2, 0, 8, 9, 7]
    t_start = time.monotonic()
    bubble_sort(temp_list)
    t_stop = time.monotonic()
    print((t_stop - t_start) * 10 ** 6)

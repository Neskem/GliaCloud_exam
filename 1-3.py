def find_multiple_nums(num):
    m_list = []
    for i in range(1, num):
        if i % 3 == 0 or i % 5 == 0:
            m_list.append(i)

    return m_list


def sum_multi_nums(num):
    nums_sum = 0
    for i in range(0, num, 3):
        nums_sum += i

    for i in range(0, num, 5):
        if i % 3 is not 0:
            nums_sum += i
    return nums_sum


def main():
    # print(sum(find_multiple_nums(100)))
    print(sum_multi_nums(100))


if __name__ == '__main__':
    main()
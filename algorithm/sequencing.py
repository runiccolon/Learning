def bubble_sort(nums):
    '''
    冒泡排序：一趟排序后最后一个数一定是最大的数，第二趟最后一个数不参与比较，逐次选出最大数
    :param nums: 待排列表
    :return: 排序完成列表
    '''
    for i in range(len(nums) - 1):  # 外层循环为趟数
        for j in range(len(nums) - i - 1):  # 里层为一趟排序
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


nums = [6, 8, 3, 2, 9, 1]

print(bubble_sort(nums))


def select_sort(nums):
    '''
    选择排序：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
    然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
    即 选择数组中最小的数字放到index=0的位置，数组会越来越小，数组为0时，排序完毕。
    时间复杂度：O（n2）
    :param nums: 待排列表
    :return: 排序完成列表
    '''
    for i in range(len(nums) - 1):
        min = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min]:
                min = j
                nums[min], nums[i] = nums[i], nums[min]
    return nums


print(select_sort([1, 3, 2, 6, 5]))


def insert_sort(nums):
    '''
    插入排序：从第一个元素开始，该元素可以认为已经被排序；
    取出下一个元素，在已经排序的元素序列中从后向前扫描；
    如果该元素（已排序）大于新元素，将该元素移到下一位置；
    重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
    将新元素插入到该位置后；
    重复步骤2~5。
    :param nums:待排序列
    :return:已排序列
    '''
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0:
            if nums[j] > key:
                nums[j + 1] = nums[j]
                nums[j] = key
            j -= 1
    return nums


print(insert_sort([1, 3, 2, 6, 5]))


def quick_sort(lists, i, j):
    '''
    快速排序
    :param lists:
    :param i:
    :param j:
    :return:
    '''
    if i >= j:
        return list
    pivot = lists[i]
    low = i
    high = j
    while i < j:
        while i < j and lists[j] >= pivot:
            j -= 1
        lists[i] = lists[j]
        while i < j and lists[i] <= pivot:
            i += 1
        lists[j] = lists[i]
    lists[j] = pivot
    quick_sort(lists, low, i - 1)
    quick_sort(lists, i + 1, high)
    return lists


lists = [1, 3, 2, 6, 5]
quick_sort(lists, 0, len(lists) - 1)
print(lists)

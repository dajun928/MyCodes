# coding:utf-8
'''
冒泡排序算法的原理如下：
    比较相邻的元素。如果第一个比第二个大，就交换他们两个。
    对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
    针对所有的元素重复以上的步骤，除了最后一个。
    持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较
'''
def bubble_sort(alist):
    '''
    :param alist: list
    :return:
    '''
    n = len(alist)
    for j in range(n-1):
        count = 0
        for i in range(0, n-1-j):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1], alist[i]
                count += 1
        if 0 == count:
            return

if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    bubble_sort(li)
    print(li)

    # [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # [17, 20, 26, 31, 44, 54, 55, 77, 93]

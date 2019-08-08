
class lis:
    def __init__(self):
        self.arr = []

    def reverse_indexing(self, i, j):
        """
        A reverse indexing of an array A
        :param i: from i
        :param j: to j
        :return: a sub array from i to j of A
        """
        subarr = []
        if i > -1*len(self.arr) or i > -1:
            return subarr
        for k in range(j, i, step=1):
            subarr.append(self.arr[len(self.arr) + k])

        return subarr


    def append(self, n):
        """
        Append n to array
        :param n: number, string
        :return: array with n at the end
        """
        if len(self.arr)>0:
            arr = [i for i in range(len(self.arr)+1)]
            for i in range(len(self.arr)):
                arr[i] = self.arr[i]

            arr[len(self.arr)] = n
            self.arr = arr
        else:
            self.arr = [n]

        return self.arr


    def __add__(self, other):
        result = [i for i in range(len(self.arr) + len(other.arr))]
        for i in range(len(self.arr)):
            result[i] = self.arr[i]
        for i in range(len(other.arr)):
            result[i+len(self.arr)] = other.arr[i]

        return result

    def __mul__(self, other):
        result = [i for i in range(other*len(self.arr))]
        for i in range(len(other)):
            for j in range(len(self.arr)):
                result[(i+1)*j] = self.arr[j]

        return result

    def remove(self, n):
        tmp1 = lis()
        tmp2 = lis()
        for i in range(len(self.arr)):
            if self.arr[i] == n:
                tmp1.arr = self.arr[:i]
                tmp2.arr = self.arr[(i+1):]
                tmp1 = tmp1 + tmp2
                self.arr = tmp1.arr
                return self
        return self

    def insert(self, k, n):
        tmp1 = lis()
        tmp2 = lis()
        tmp3 = lis()
        tmp1.arr = self.arr[:k]
        tmp2.append(n)
        tmp3.arr = self.arr[(k + 1):]
        tmp1 = tmp1 + tmp2
        tmp1 = tmp1 + tmp3
        self.arr = tmp1.arr
        return self

    def pop(self, k):
        tmp1 = lis()
        tmp2 = lis()
        tmp1.arr = self.arr[:k]
        tmp2.arr = self.arr[(k + 1):]
        tmp1 = tmp1 + tmp2
        self.arr = tmp1.arr

        return self

    def clear(self):
        self.arr = []
        return self

    def count(self, n):
        count = 0
        for i in range(len(self.arr)):
            if self.arr[i] == n:
                count = count + 1

        return count

    def quicksort(self, left, right):
        if left < right:
            pivot = right
            j = 0
            for i in range(pivot):
                if self.arr[i] < self.arr[pivot]:
                    self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                    j = j + 1
            self.arr[pivot], self.arr[j] = self.arr[j], self.arr[pivot]
            self.quicksort(left, j)
            self.quicksort(pivot, right)
        else:
            return self

    def sort(self, reverse=False):
        left = 0
        right = len(self.arr)-1
        self.quicksort(left, right)

        return self


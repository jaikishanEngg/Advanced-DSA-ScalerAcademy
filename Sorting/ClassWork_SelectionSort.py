class Solution:
    def selectionSort(self, input_array):
        #inplace 
        #not stable
        size = len(input_array)
        for i in range(size):
            minElement = input_array[i] #lets initialize the first element as minimum
            minElementIndex = None
            for j in range(i+1, size):
                if input_array[j] < minElement:
                    minElement = input_array[j]
                    minElementIndex = j
            
            #swap elements at i,j indices
            if minElementIndex:
                input_array[i], input_array[j] = input_array[j], input_array[i]
        
        return input_array

    def selectionSortStableVersion(self, input_array):
        #inplace 
        #stable -- swapping will cause keeping the element in a position index greater than which it was suppose to be.
        #so, rather than swapping lets insert the min ele at the right position in each iteration and push the remaining element by one position
        #this algorithm of insertion the min. ele at its right position is Insertion sort.
        size = len(input_array)
        for i in range(size):
            minElement = input_array[i] #lets initialize the first element as minimum
            minElementIndex = None
            for j in range(i+1, size):
                if input_array[j] < minElement:
                    minElement = input_array[j]
                    minElementIndex = j
            
            if minElementIndex:
                #lets insert the minimum element at its correct place than swapping it.
                #and shift all the other element by one position
                for k in range(minElementIndex-1, i-1, -1):
                    input_array[k+1] = input_array[k]
            
                input_array[i] = minElement
        
        return input_array

s = Solution()
A = [2,5,2,1,6]
ans = s.selectionSortStableVersion(A)
assert ans == [1,2,2,5,6]
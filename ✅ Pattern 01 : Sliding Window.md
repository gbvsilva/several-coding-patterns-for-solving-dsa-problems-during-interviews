# Pattern 1: Sliding Window
In many problems dealing with an array (or a <b>LinkedList</b>), we are asked to find or calculate something among all the contiguous subarrays (or sublists) of a given size. For example, take a look at this problem:

### Find Averages of Sub Arrays
https://leetcode.com/problems/maximum-average-subarray-i/

> Given an array, find the average of all contiguous subarrays of size `K` in it.

Lets understand this problem with a real input:

`Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5`

A <b>brute-force</b> algorithm will calculate the sum of every 5-element contiguous subarray of the given array and divide the sum by 5 to find the average.

```python
def naive_find_avg_sub_arrays(arr, K):
  results = []

  for i in range(len(arr) - K + 1):
    _sum = 0
    for j in range(i, i + K):
      _sum += arr[j]
    results.append(_sum / K)
  return results


naive_find_avg_sub_arrays([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
```

<b>Time complexity: </b> Since for every element of the input array, we are calculating the sum of its next `K` elements, the time complexity of the above algorithm will be `O(N*K)` where `N` is the number of elements in the input array.

#### Can we find a better solution? Do you see any inefficiency in the above approach?

The inefficiency is that for any two consecutive subarrays of size `5`, the overlapping part (which will contain four elements) will be evaluated twice.

The efficient way to solve this problem would be to visualize each contiguous subarray as a <i>sliding window</i> of `5` elements. This means that we will slide the window by one element when we move on to the next subarray. To reuse the sum from the previous subarray, we will subtract the element going out of the window and add the element now being included in the <i>sliding window</i>. This will save us from going through the whole subarray to find the sum and, as a result, the algorithm complexity will reduce to `O(N)`.

Here is the algorithm for the <b>Sliding Window</b> approach:
```python
def find_avg_sub_arrays(arr, k):
  # sliding window approach
  results = []
  window_sum = 0
  window_start = 0

  for window_end in range(len(arr)):
    # add the next element
    window_sum += arr[window_end]

    # slide the window forward
    # we don't need to slide if we have not hit the required window size of k

    if window_end >= k - 1:
      # we are **AUTOMATICALLY** returning the window average once we hit the window size of k
      # and pushing to the output array
      results.append(window_sum / k)

      # subtracting the element going out
      window_sum -= arr[window_start]

      # then sliding the window forward
      window_start += 1

      # adding the element coming in, in the outer/previous loop
      # and repeating this process until we hit the end of the array
  return results


find_avg_sub_arrays([1, 3, 2, 6, -1, 4, 1, 8, 2], 5) # [2.2, 2.8, 2.4, 3.6, 2.8]
```
## Maximum Sum Subarray of Size K (easy)
https://leetcode.com/problems/largest-subarray-length-k/
> Given an array of positive numbers and a positive number `K`, find the maximum sum of any contiguous subarray of size `K`.
### Brute Force

A basic brute force solution will be to calculate the sum of all `K` sized subarrays of the given array to find the subarray with the highest sum. We can start from every index of the given array and add the next `K` elements to find the subarrays sum.
```python
def naive_max_sub_array_of_size_k(arr, k):
  # brute force
  max_sum = 0
  window_um = 0

  # loop through array
  for i in range(len(arr) - k + 1):

    # keep track of sum in current window
    window_sum = 0
    for j in range(i, i + k):
      window_sum += arr[j]

    # if currentWindowSum is > maxWindowSum
    # set currentWindwoSum to maxWindowSum
    max_sum = max(max_sum, window_sum)

  return max_sum


naive_max_sub_array_of_size_k([2, 1, 5, 1, 3, 2], 3) # 9
naive_max_sub_array_of_size_k([2, 3, 4, 1, 5], 2) # 7
```
- Time complexity will be `O(N*K)`, where `N` is the total number of elements in the given array

### Sliding Window Approach
If you observe closely, you will realize that to calculate the sum of a contiguous subarray, we can utilize the sum of the previous subarray. For this, consider each subarray as a <b>Sliding Window</b> of size `K`. To calculate the sum of the next subarray, we need to slide the window ahead by one element. So to slide the window forward and calculate the sum of the new position of the <i>sliding window</i>, we need to do two things:
1. Subtract the element going out of the <i>sliding window</i>, i.e., subtract the first element of the window.
2. Add the new element getting included in the <i>sliding window</i>, i.e., the element coming right after the end of the window.

This approach will save us from re-calculating the sum of the overlapping part of the <i>sliding window</i>.
```python
def max_sub_array_of_size_k(arr, k):
  # sliding window
  max_sum = 0
  window_sum = 0
  window_start = 0

  # loop through array
  for window_end in range(len(arr)):
    # add the next element
    window_sum += arr[window_end]

    # slide the window, we dont need to slid eif we
    # haven't hit the required window size of 'k'
    if window_end >= k - 1:
      max_sum = max(max_sum, window_sum)
      window_sum -= arr[window_start]
      window_start += 1
  return max_sum


max_sub_array_of_size_k([2, 1, 5, 1, 3, 2], 3) # 9
max_sub_array_of_size_k([2, 3, 4, 1, 5], 2) # 7
```
- The time complexity of the above algorithm will be `O(N)`
- The space complexity of the above algorithm will be `O(1)`

## Smallest Subarray with a given sum (easy)
https://leetcode.com/problems/minimum-size-subarray-sum/
> Given an array of positive numbers and a positive number `S`, find the length of the <b>smallest contiguous subarray whose sum is greater than or equal to `S`</b>.
>
> Return 0 if no such subarray exists.

This problem follows the <b>Sliding Window pattern</b>, and we can use a similar strategy as discussed in <b>[Maximum Sum Subarray of Size K](#maximum-sum-subarray-of-size-k-easy)</b>. There is one difference though: in this problem, the <i>sliding window</i> size is not fixed. Here is how we will solve this problem:
1. First, we will add-up elements from the beginning of the array until their sum becomes greater than or equal to `S`.
2. These elements will constitute our <i>sliding window</i>. We are asked to find the smallest such window having a sum greater than or equal to `S`. We will remember the length of this window as the smallest window so far.
3. After this, we will keep adding one element in the <i>sliding window</i> (i.e., slide the window ahead) in a stepwise fashion.
4. In each step, we will also try to shrink the window from the beginning. We will shrink the window until the windows sum is smaller than `S` again. This is needed as we intend to find the smallest window. This shrinking will also happen in multiple steps; in each step, we will do two things:
  - Check if the current window length is the smallest so far, and if so, remember its length.
  - Subtract the first element of the window from the running sum to shrink the sliding window.


```python
def smallest_subarray_with_given_sum(arr, s):
  # sliding window, BUT the window size is not fixed
  window_sum = 0
  min_length = float('inf')
  window_start = 0

  # First, we will add-up elements from the beginning of the array until their sum becomes greater than or equal to S.
  for window_end in range(len(arr)):
    # add the next element
    window_sum += arr[window_end]

    # shrink the window as small as possible
    # until windowSum is small than s
    while window_sum >= s:
      # These elements will constitute our sliding window. We are asked to find the smallest such window having a sum greater than or equal to S. We will remember the length of this window as the smallest window so far.
      # After this, we will keep adding one element in the sliding window (i.e., slide the window ahead) in a stepwise fashion.
      # In each step, we will also try to shrink the window from the beginning. We will shrink the window until the windows sum is smaller than S again. This is needed as we intend to find the smallest window. This shrinking will also happen in multiple steps; in each step, we will do two things:
      # Check if the current window length is the smallest so far, and if so, remember its length.
      min_length = min(min_length, window_end - window_start + 1)

      # Subtract the first element of the window from the running sum to shrink the sliding window.
      window_sum -= arr[window_start]
      window_start += 1

  if min_length == float('inf'):
    return 0
  return min_length


smallest_subarray_with_given_sum([2, 1, 5, 2, 3, 2], 7) # 2
smallest_subarray_with_given_sum([2, 1, 5, 2, 8], 7) # 1
smallest_subarray_with_given_sum([3, 4, 1, 1, 6], 8) # 3
```
- The time complexity of the above algorithm will be `O(N)`. The outer for loop runs for all elements, and the inner while loop processes each element only once; therefore, the time complexity of the algorithm will be `O(N+N)`), which is asymptotically equivalent to `O(N)`.
- The algorithm runs in constant space `O(1)`.


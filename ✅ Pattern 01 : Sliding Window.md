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

## Longest Substring with K Distinct Characters (medium)
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

>Given a string, find the length of the <b>longest substring</b> in it with <b>no more than `K` distinct characters</b>.
>
>You can assume that `K` is less than or equal to the length of the given string.

This problem follows the <b>Sliding Window pattern</b>, and we can use a similar dynamic <i>sliding window</i> strategy as discussed in <b>[Smallest Subarray with a given sum](#smallest-subarray-with-a-given-sum-easy)</b>. We can use a <b>HashMap</b> to remember the frequency of each character we have processed. Here is how we will solve this problem:

1. First, we will insert characters from the beginning of the string until we have `K` distinct characters in the <b>HashMap</b>.
2. These characters will constitute our <i>sliding window</i>. We are asked to find the longest such window having no more than `K` distinct characters. We will remember the length of this window as the longest window so far.
3. After this, we will keep adding one character in the <i>sliding window</i> (i.e., slide the window ahead) in a stepwise fashion.
4. In each step, we will try to shrink the window from the beginning if the count of distinct characters in the <b>HashMap</b> is larger than `K`. We will shrink the window until we have no more than `K` distinct characters in the <b>HashMap</b>. This is needed as we intend to find the longest window.
5. While shrinking, well decrement the characters frequency going out of the window and remove it from the <b>HashMap</b> if its frequency becomes zero.
6. At the end of each step, well check if the current window length is the longest so far, and if so, remember its length.

```python
def longest_substring_with_k_distinct(s, k):
  # Given a string, find the length of the longest substring in it with no more than K distinct characters.
  window_start = 0
  max_length = 0
  char_frequency = {}

  # in the following loop we'll try to extend the range [window_start, window_end]
  for window_end in range(len(s)):
    end_char = s[window_end]
    # shrink the window until we are left with k distinct characters
    # in the charFrequency Object
    if end_char not in char_frequency:
      char_frequency[end_char] = 0
    char_frequency[end_char] += 1

    while len(char_frequency) > k:
      # insert characters from the beginning of the string until we have 'K' distinct characters in the hashMap
      # these characters will consitutue our sliding window.  We are asked to find the longest such window having no more that K distinct characters.  We will remember the length of the window as the longest window so far
      # we will keep adding on character in the sliding window in a stepwise fashion
      # in each step we will try to shrink the window from the beginning if the count of distinct characters in the hashmap is larger than K. We will shrink the window until we have no more that K distinct characters in the HashMap
      start_char = s[window_start]
      char_frequency[start_char] -= 1
      # while shrinking , we will decrement the characters frequency going out of the window and remove it from the HashMap if it's frequency becomes zero
      if char_frequency[start_char] == 0:
        del char_frequency[start_char]
      # after each step we will check if the current window length is the longest so far, and if so, remember it's length
      window_start += 1

    max_length = max(max_length, window_end - window_start + 1)

  return max_length


longest_substring_with_k_distinct("araaci", 2) # 4, The longest substring with no more than '2' distinct characters is "araa".
longest_substring_with_k_distinct("araaci", 1) # 2, The longest substring with no more than '1' distinct characters is "aa".
longest_substring_with_k_distinct("cbbebi", 3) # 5, The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
```
- The above algorithms time complexity will be `O(N)`, where `N` is the number of characters in the input string. The outer for loop runs for all characters, and the inner while loop processes each character only once; therefore, the time complexity of the algorithm will be `O(N+N)`, which is asymptotically equivalent to `O(N)`
- The algorithms space complexity is `O(K)`, as we will be storing a maximum of `K+1` characters in the <b>HashMap</b>.

## 🔎 Fruits into Baskets (medium)
https://leetcode.com/problems/fruit-into-baskets/

> Given an array of characters where each character represents a fruit tree, you are given <b>two baskets</b>, and your goal is to put the <b>maximum number of fruits in each basket</b>. The only restriction is that <b>each basket can have only one type of fruit</b>.
>
> You can start with any tree, but you can't skip a tree once you have started. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
>
> Write a function to return the maximum number of fruits in both baskets.

This problem follows the <b>Sliding Window pattern</b> and is quite similar to <b>[Longest Substring with K Distinct Characters](#longest-substring-with-k-distinct-characters-medium)</b>.

In this problem, we need to find the length of the longest subarray with no more than two distinct characters (or fruit types!).

This transforms the current problem into Longest Substring with <b>K Distinct Characters</b> where `K=2`.
### Map Class Solution
```python
def total_fruit(fruits):
  window_start = 0
  window_max = 0
  fruit_map = {}

  # 1. try to extend the window range
  for window_end in range(len(fruits)):
    end_fruit = fruits[window_end]
    if end_fruit not in fruit_map:
      fruit_map[end_fruit] = 0
    fruit_map[end_fruit] += 1
    # 2. Shrink the sliding window, until we are left with 2 fruits in the fruitMap
    while len(fruit_map) > 2:
      start_fruit = fruits[window_start]
      fruit_map[start_fruit] -= 1
      if fruit_map[start_fruit] == 0:
        del fruit_map[start_fruit]
      window_start += 1

    window_max = max(window_max, window_end - window_start + 1)

  return window_max


total_fruit([3,3,3,1,2,1,1,2,3,3,4])
# 5
total_fruit ([1,2,1])
# 3, We can pick from all 3 trees.
total_fruit ([0,1,2,2])
# 3, We can pick from trees [1,2,2].If we had started at the first tree, we would only pick from trees [0,1].
total_fruit ([1,2,3,2,2])
# 4, We can pick from trees [2,3,2,2]. If we had started at the first tree, we would only pick from trees [1,2].
```
### Map Object Solution
```python
def fruit_in_baskets(fruits):
  window_start = 0
  window_max = 0
  fruit_map = {}

  # 1. try to extend the window range
  for window_end in range(len(fruits)):
    end_fruit = fruits[window_end]
    if end_fruit not in fruit_map:
      fruit_map[end_fruit] = 0
    fruit_map[end_fruit] += 1
    # 2. Shrink the sliding window, until we are left with 2 fruits in the fruitMap
    while len(fruit_map) > 2:
      start_fruit = fruits[window_start]
      fruit_map[start_fruit] -= 1
      if fruit_map[start_fruit] == 0:
        del fruit_map[start_fruit]
      window_start += 1

    window_max = max(window_max, window_end - window_start + 1)

  return window_max


fruit_in_baskets(['A', 'B', 'C', 'A', 'C']) # 3, We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
fruit_in_baskets(['A', 'B', 'C', 'B', 'B', 'C']) # 5, We can put 3 'B' in one basket and two 'C' in the other basket. This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
```
- The above algorithms time complexity will be `O(N)`, where `N` is the number of characters in the input array. The outer `for` loop runs for all characters, and the inner `while` loop processes each character only once; therefore, the time complexity of the algorithm will be `O(N+N)`, which is asymptotically equivalent to `O(N)`.
- The algorithm runs in constant space `O(1)` as there can be a maximum of three types of fruits stored in the frequency map.
### Longest Substring with at most 2 distinct characters
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
> Given a string, find the length of the longest substring in it with at most two distinct characters.

```python
def length_of_longest_substring_two_distinct(s):
  window_start = 0
  max_length = 0
  char_freq = {}

  for window_end in range(len(s)):
    end_char = s[window_end]
    if end_char not in char_freq:
      char_freq[end_char] = 0
    char_freq[end_char] += 1

    while len(char_freq) > 2:
      start_char = s[window_start]
      char_freq[start_char] -= 1
      if char_freq[start_char] == 0:
        del char_freq[start_char]
      window_start += 1

    max_length = max(max_length, window_end - window_start + 1)

  return max_length


length_of_longest_substring_two_distinct('eceba') # 3
length_of_longest_substring_two_distinct('ccaabbb') # 5
```

## No-repeat Substring (hard)
https://leetcode.com/problems/longest-substring-without-repeating-characters/

> Given a string, find the <b>length of the longest substring</b>, which has <b>no repeating characters</b>.

This problem follows the <b>Sliding Window pattern</b>, and we can use a similar dynamic <i>sliding window</i> strategy as discussed in <b>Longest Substring with K Distinct Characters</b>. We can use a <b>HashMap</b> to remember the last index of each character we have processed. Whenever we get a repeating character, we will shrink our <i>sliding window</i> to ensure that we always have distinct characters in the <i>sliding window</i>.

```python
def non_repeat_substring(s):
  # sliding window with hashmap
  window_start = 0
  max_length = 0
  char_index_map = {}

  # try to extend the range [window_start, window_end]
  for window_end in range(len(s)):
    # if the map already contains the end_char,
    # shrink the window from the beginning
    # so that we only have on occurance of end_char
    end_char = s[window_end]
    if end_char in char_index_map:
      # this is tricky; in the current window,
      # we will not have any end_char after
      # it's previous index. and if window_start
      # is already ahead of the last index of
      # end_char, we'll keep window_start
      window_start = max(window_start, char_index_map[end_char] + 1)

    # insert the end_char into the map
    char_index_map[end_char] = window_end

    #remember the maximum length so far
    max_length = max(max_length, window_end - window_start + 1)

  return max_length


non_repeat_substring("aabccbb") # 3
non_repeat_substring("abbbb") # 2
non_repeat_substring("abccde") # 3
```
- The above algorithms time complexity will be `O(N)`, where `N` is the number of characters in the input string.
- The algorithms space complexity will be `O(K)`, where `K` is the number of distinct characters in the input string. This also means `K<=N`, because in the worst case, the whole string might not have any repeating character, so the entire string will be added to the <b>HashMap</b>. Having said that, since we can expect a fixed set of characters in the input string (e.g., 26 for English letters), we can say that the algorithm runs in fixed space `O(1)`; in this case, we can use a fixed-size array instead of the <b>HashMap</b>.

## Longest Substring with Same Letters after Replacement (hard)
https://leetcode.com/problems/longest-repeating-character-replacement/

> Given a string with lowercase letters only, if you are allowed to <b>replace no more than `K` letters</b> with any letter, find the <b>length of the longest substring having the same letters</b> after replacement.

This problem follows the <b>Sliding Window pattern</b>, and we can use a similar dynamic <i>sliding window</i> strategy as discussed in <b>No-repeat Substring</b>. We can use a <b>HashMap</b> to count the frequency of each letter.

- We will iterate through the string to add one letter at a time in the window.
- We will also keep track of the count of the maximum repeating letter in any window (lets call it `max_repeat_letter_count`).
- So, at any time, we know that we do have a window with one letter repeating `max_repeat_letter_count` times; this means we should try to replace the remaining letters.
  - If the remaining letters are less than or equal to `K`, we can replace them all.
  - If we have more than `K` remaining letters, we should shrink the window as we cannot replace more than `K` letters.

While shrinking the window, we don't need to update `max_repeat_letter_count` (hence, it represents the maximum repeating count of ANY letter for ANY window). Why don't we need to update this count when we shrink the window? Since we have to replace all the remaining letters to get the longest substring having the same letter in any window, we can't get a better answer from any other window even though all occurrences of the letter with frequency `max_repeat_letter_count` is not in the current window.
```python
def length_of_longest_substring(s, k):
  window_start = 0
  max_length = 0
  max_repeat_letter_count = 0
  char_frequency = {}

  # Try to extend the range [window_start, window_end]
  for window_end in range(len(s)):
    end_char = s[window_end]
    if end_char not in char_frequency:
      char_frequency[end_char] = 0
    char_frequency[end_char] += 1

    max_repeat_letter_count = max(max_repeat_letter_count, char_frequency[end_char])
    # current window size is from windowStart to window_end, overall we have a letter which is
    # repeating max_repeat_letter_count times, this mean we can have a window which has one letter
    # repeating max_repeat_letter_count times and the remaining letters we should replace
    # if the remaining letters are more than k, it is the time to shrink the window as we
    # are not allowed to replace more than k letters
    if window_end - window_start + 1 - max_repeat_letter_count > k:
      start_char = s[window_start]
      char_frequency[start_char] -= 1
      window_start += 1

    max_length = max(max_length, window_end - window_start + 1)

  return max_length


length_of_longest_substring("aabccbb", 2) # 5, Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
length_of_longest_substring("abbcb", 1) # 4, Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
length_of_longest_substring("abccde", 1) # 3, Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
```

- The above algorithms time complexity will be `O(N)`, where `N` is the number of letters in the input string.
- As we expect only the lower case letters in the input string, we can conclude that the space complexity will be `O(26)` to store each letters frequency in the <b>HashMap</b>, which is asymptotically equal to `O(1)`.

## Longest Subarray with Ones after Replacement (hard)
https://leetcode.com/problems/max-consecutive-ones-iii/

> Given an array containing `0`'s and `1`'s, if you are allowed to <b>replace no more than `K` `0`'s with `1`'s</b>,
> find the length of the <b>longest contiguous subarray having all `1`'s</b>.

This problem follows the <b>Sliding Window pattern</b> and is quite similar to <b>Longest Substring with same Letters after Replacement</b>. The only difference is that, in the problem, we only have two characters (`1`'s and `0`'s) in the input arrays.

Following a similar approach, well iterate through the array to add one number at a time in the window. Well also keep track of the maximum number of repeating `1`'s in the current window (lets call it `max_ones_count`). So at any time, we know that we can have a window with `1`'s repeating `max_ones_count` time, so we should try to replace the remaining `0`'s. If we have more than `K` remaining `0`'s, we should shrink the window as we are not allowed to replace more than `K` `0`'s.

```python
def longest_ones(arr, k):
  window_start = 0
  max_length = 0
  max_ones_count = 0

  # Try to extend the range [window_start, window_end]
  for window_end in range(len(arr)):
    if arr[window_end] == 1:
      max_ones_count += 1

    # current window size is from window_start to window_end, overall we have a
    # maximum of `1`'s repeating max_ones_count times, this means we can have a window
    # with max_ones_count `1`'s and the remaining are `0`'s which should replace with `1`'s
    # now, if the remaining `0`'s are more that k, it is the time to shrink the
    # window as we are not allowed to replace more than k `0`'s
    if window_end - window_start + 1 - max_ones_count > k:
      if arr[window_start] == 1:
        max_ones_count -= 1
      window_start += 1

    max_length = max(max_length, window_end - window_start + 1)

  return max_length


longest_ones([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2) # 6, Replace the '0' at index 5 and 8 to have the longest contiguous subarray of `1`'s having length 6.
longest_ones([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3) # 9, Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of `1`'s having length 9.
```

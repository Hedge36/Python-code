# 数组

## 存在重复问题

### 算法要求

> 给定一个整数数组，判断是否存在重复元素，如何存在任何重复值则返回True，否则返回False。

### 解题思路

> 1. **包含判断法**
> 2. 排序比较法
> 3. 集合判断法



## 只出现一次的数字

### 算法要求

> 给定一个非空数组，除了某个元素只出现了一次外，其他元素均出现两次，试找出只出现一次的元素。

### 解题思路

> 1. 排序比较
> 2. 集合交叉法
> 3. 异或法

#### 集合交叉法

> 根据奇偶索引将nums分成两个不同的集合，取差集。

```python
def SingleNumber(nums):
  nums.sort()
  return list(set(nums[::2]) - set(nums[1::2]))[0]
```

#### 异或法

> 利用两个相同数的数异或得0、一个数与0异或得到本身得特性来解决问题，这种方法比较剑走偏锋，仅作了解。

```python
def SingNumber(nums):
  n = 0
  for i in nums:
    n ^= i
  return n 
```

### 题目升级

> 如果重复元素出现次数为两次或两次以上不定时如何处理？

#### 正解

> 待解答



## 两数之和

### 算法要求

> 给定一个整数数组 nums 和一个目标值 target，请在该数组中找出和为目标值的两个整数并返回它们的数组下标。

### 解题思路

> 1. 嵌套循环
> 2. 简化循环
> 3. 哈希循环

#### 简化循环

> 两数之和为 target ，那只需要在其右侧序列中找到其差值即可。

```python
def TwoSum(nums, target):
  for i in range(len(nums) - 1):
    target = target - nums[i]
    if target in nums[i+1:]:
      j = nums[i+1:].index(target)
      return i, i+j+1
```

#### 哈希表法

> 注意到方法一的时间复杂度较高的原因是寻找 target - x 的时间复杂度过高。因此，我们需要一种更优秀的方法，能够快速寻找数组中是否存在目标元素。如果存在，我们需要找出它的索引。
>
> 使用哈希表，可以将寻找 target - x 的时间复杂度降低到从 $O(N)$ 降低到 $O(1)$ 。
>
> 这样我们创建一个哈希表，对于每一个 x，我们首先查询哈希表中是否存在 target - x，然后将 x 插入到哈希表中，即可保证不会让 x 和自己匹配。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
```

> 时间复杂度： $O(N)$ ，其中 $N$ 是数组中的元素数量。对于每一个元素 x，我们可以 $O(1)$ 地寻找 target - x。
>
> 空间复杂度：$O(N)$，其中 $N$ 是数组中的元素数量。主要为哈希表的开销。

<p align='right'>来源：力扣（LeetCode）




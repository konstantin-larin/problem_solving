---
tags:
  - problem
level: easy
---

Дата: 2025-06-05

# Ссылка: 
https://leetcode.com/problems/summary-ranges/?envType=study-plan-v2&envId=top-interview-150

# Понимание условия
 - Ограничения по времени/памяти
 - Диапазоны входных данных
 - Разбери все случаи, включая крайние, которые будет решать код
**Input:** nums = \[0,1,2,4,5,7]
**Output:** \["0->2","4->5","7"]

- `0 <= nums.length <= 20`
- `-2^31 <= nums[i] <= 2^31 - 1`
- All the values of `nums` are **unique**.
- `nums` is sorted in ascending order.
# Подход
- Что первым приходит в голову?
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем, если да - можно запускать таймер
# Код
```python
class Solution(object):

    def summaryRanges(self, nums):

        """

        :type nums: List[int]

        :rtype: List[str]

        """

        n = len(nums)        

        if n == 0:

            return []        

        ans = []        

        a = nums[0]

        b = a

        for i in range(1, n):

            num = nums[i]        

            if b + 1 != num:                

                if a == b:

                    ans.append(str(a))

                else:

                    ans.append(str(a) + '->' + str(b))

                a = b = num                        

            else:

                b += 1                          

        if a == b:

            ans.append(str(a))

        else:

            ans.append(str(a) + '->' + str(b))            

        return ans
```
# Ревью

Легкая задача, использовал простой перебор массива и условия. Учел случаи, когда nums пустой 
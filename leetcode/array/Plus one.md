---
tags:
  - problem
level: easy
---

Дата: [[18-06-2025]]

# Ссылка: 


# Понимание условия
 - Ограничения по времени/памяти
 - Диапазоны входных данных
 - Разбери все случаи, включая крайние, которые будет решать код

# Подход
- Что первым приходит в голову?
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем, если да - можно запускать таймер
# Код
```python
	class Solution(object):

    def plusOne(self, digits):

        """

        :type digits: List[int]

        :rtype: List[int]

        """        

        i = len(digits) - 1            

        while True:                        

            digits[i] += 1            

            if digits[i] > 9:

                digits[i] = digits[i] % 10                

                i -= 1                                

                if i == -1:

                    return [1] + digits

            else:

                return digits
```
# Ревью

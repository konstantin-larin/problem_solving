def solution(n: int) -> int:
    # your code
    mod = 10 ** 9 - 7538
    memo = dict()
    def calc(k):
        if k == 0:
            return 1
        if k in memo:
            return memo[k]

        # чтобы избавиться от мегасложных вычислений я воспользовался свойством модульной арифметики
        # (a_mod + b_mod + c_mod) % mod == (a + b + c) % mod

        a_div_2 = calc(k // 2)    
        a_div_3 = calc(k // 3)
        a_div_4 = calc(k // 4)    

        a_mod = pow(a_div_2, a_div_3, mod)  
        b_mod = (5 * a_div_4) % mod
        c_mod = k % mod 
        result = (a_mod + b_mod + c_mod) % mod
        memo[k] = result
        return result
    return calc(n)

print(solution(5))
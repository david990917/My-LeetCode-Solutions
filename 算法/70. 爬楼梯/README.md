| [English](README_EN.md) | 简体中文 |

# [70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs)
<p>假设你正在爬楼梯。需要 <em>n</em>&nbsp;阶你才能到达楼顶。</p>

<p>每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？</p>

<p><strong>注意：</strong>给定 <em>n</em> 是一个正整数。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong> 2
<strong>输出：</strong> 2
<strong>解释：</strong> 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong> 3
<strong>输出：</strong> 3
<strong>解释：</strong> 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
</pre>

**标签:**  [动态规划](https://leetcode-cn.com/tag/dynamic-programming) 
 ### 相似题目
- 简单:	[使用最小花费爬楼梯](https://leetcode-cn.com/problems/min-cost-climbing-stairs) 
- 简单:	[斐波那契数](https://leetcode-cn.com/problems/fibonacci-number) 
- 简单:	[第 N 个泰波那契数](https://leetcode-cn.com/problems/n-th-tribonacci-number) 

# 解题思路 √

### 动态规划

这个题目很好理解，居然由动态规划转变成了斐波那契数列。

> Think how to reach nth stairs.

### Python

1. 线性队列生成

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:return n
        results=[0 for i in range(n+1)]
        results[1],results[2]=1,2
        for i in range(3,n+1):
            results[i]=results[i-1]+results[i-2]
        return results[n]
```

2. 顺序的动态规划


```python
class Solution:
    def climbStairs(self, n: int) -> int:
        a,b=1,2
        for i in range(n-1):
            a,b=b,a+b
        return a
```

### C++

1. 对应线性队列生成

```cpp
class Solution {
public:
    int climbStairs(int n) {
        if(n<=2){return n;}
        vector<int> arr(n+1);
        arr[1]=1,arr[2]=2;
        for(int i=3;i<=n;i++){
            arr[i]=arr[i-1]+arr[i-2];
        }
        return arr[n];
    }
};
```

2. 顺序的动态规划

```cpp
class Solution {
public:
    int climbStairs(int n) {
        long long a=1,b=2;
        long long tmp;
        for(int i=0;i<n-1;i++){
            tmp=a;
            a=b;
            b=tmp+b;
        }
        return a;
    }
};
```



---



# 整理与总结

1. 
| [English](README_EN.md) | 简体中文 |

# [605. 种花问题](https://leetcode-cn.com/problems/can-place-flowers)
<p>假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。</p>

<p>给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数&nbsp;<strong>n&nbsp;</strong>。能否在不打破种植规则的情况下种入&nbsp;<strong>n&nbsp;</strong>朵花？能则返回True，不能则返回False。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> flowerbed = [1,0,0,0,1], n = 1
<strong>输出:</strong> True
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> flowerbed = [1,0,0,0,1], n = 2
<strong>输出:</strong> False
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>数组内已种好的花不会违反种植规则。</li>
	<li>输入的数组长度范围为 [1, 20000]。</li>
	<li><strong>n</strong> 是非负整数，且不会超过输入数组的大小。</li>
</ol>

**标签:**  [数组](https://leetcode-cn.com/tag/array) 
 ### 相似题目
- 中等:	[提莫攻击](https://leetcode-cn.com/problems/teemo-attacking) 
- 中等:	[行星碰撞](https://leetcode-cn.com/problems/asteroid-collision) 

# 解题思路 √

### Python

1. 正向操作的思路：前面没有+后面没有 = 我可以在当下进行种植

   思路的要点：首尾的时候自己 feel free去种，所以在分析的时候设置为0

```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length,count=len(flowerbed),0
        for i in range(length):
            if flowerbed[i]==1:continue
            pre=0 if i==0 else flowerbed[i-1]
            nxt=0 if i==length-1 else flowerbed[i+1]
            if pre==0 and nxt==0:
                flowerbed[i]=1
                count+=1
        return count>=n
```


```python

```

### C++

```cpp

```

---



# 整理与总结

1. 
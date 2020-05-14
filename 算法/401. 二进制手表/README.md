| [English](README_EN.md) | 简体中文 |

# [401. 二进制手表](https://leetcode-cn.com/problems/binary-watch)
<p>二进制手表顶部有 4 个 LED 代表<strong>小时（0-11）</strong>，底部的 6 个 LED 代表<strong>分钟（0-59）</strong>。</p>

<p>每个 LED 代表一个 0 或 1，最低位在右侧。</p>

<p><img src="https://upload.wikimedia.org/wikipedia/commons/8/8b/Binary_clock_samui_moon.jpg" style="height:300px" /></p>

<p>例如，上面的二进制手表读取 &ldquo;3:25&rdquo;。</p>

<p>给定一个非负整数 <em>n&nbsp;</em>代表当前 LED 亮着的数量，返回所有可能的时间。</p>

<p><strong>案例:</strong></p>

<pre>
输入: n = 1
返回: [&quot;1:00&quot;, &quot;2:00&quot;, &quot;4:00&quot;, &quot;8:00&quot;, &quot;0:01&quot;, &quot;0:02&quot;, &quot;0:04&quot;, &quot;0:08&quot;, &quot;0:16&quot;, &quot;0:32&quot;]</pre>

<p>&nbsp;</p>

<p><strong>注意事项:</strong></p>

<ul>
	<li>输出的顺序没有要求。</li>
	<li>小时不会以零开头，比如 &ldquo;01:00&rdquo;&nbsp;是不允许的，应为 &ldquo;1:00&rdquo;。</li>
	<li>分钟必须由两位数组成，可能会以零开头，比如 &ldquo;10:2&rdquo;&nbsp;是无效的，应为 &ldquo;10:02&rdquo;。</li>
</ul>

**标签:**  [位运算](https://leetcode-cn.com/tag/bit-manipulation) [回溯算法](https://leetcode-cn.com/tag/backtracking) 
 ### 相似题目
- 中等:	[电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number) 
- 简单:	[位1的个数](https://leetcode-cn.com/problems/number-of-1-bits) 

# 解题思路 √

### Python

1. 野蛮原始的穷举法

```python
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        upTime={
            0:[0],
            1:[1,2,4,8],
            2:[3,5,6,9,10],
            3:[7,11]
        }
        downTime={
            0:[0],
            1:[1,2,4,8,16,32],
            2:[3,5,6,9,10,12,17,18,20,24,33,34,36,40,48],
            3:[7,11,13,14,19,21,22,25,26,28,35,37,38,41,42,44,49,50,52,56],
            4:[15,23,27,29,30,39,43,45,46,51,53,54,57,58],
            5:[31,47,55,59]
        }
        
        result=[]
        for up in range(min(3,num)+1):
            down=num-up
            if down<0 or down>5:continue
            for h in upTime[up]:
                for m in downTime[down]:
                    result.append("{}:{:0>2d}".format(h,m))
        return result
```


```python

```

### C++

```cpp

```

---



# 整理与总结

1. 
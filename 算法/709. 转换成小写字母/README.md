| [English](README_EN.md) | 简体中文 |

# [709. 转换成小写字母](https://leetcode-cn.com/problems/to-lower-case)
<p>实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入: </strong>&quot;Hello&quot;
<strong>输出: </strong>&quot;hello&quot;</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入: </strong>&quot;here&quot;
<strong>输出: </strong>&quot;here&quot;</pre>

<p><strong>示例</strong><strong>&nbsp;3：</strong></p>

<pre>
<strong>输入: </strong>&quot;LOVELY&quot;
<strong>输出: </strong>&quot;lovely&quot;
</pre>

**标签:**  [字符串](https://leetcode-cn.com/tag/string) 
# 解题思路 √

### Python

1. 直接调用库就可以

```python
class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()
```


```python

```

### C++

```cpp
class Solution {
public:
    string toLowerCase(string str) {
        int length=str.size();
        for(int i=0;i<length;i++){
            if('A'<=str[i]&&str[i]<='Z'){str[i]-='A'-'a';}
        }
        return str;
    }
};
```

---



# 整理与总结

1. 
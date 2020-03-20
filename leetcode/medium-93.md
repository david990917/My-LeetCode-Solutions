title: medium-93
tags:

  - LeetCode
description: '复原IP地址'
urlname: medium-93
date: 2020-03-20 15:09:18

# 题目

https://leetcode-cn.com/problems/restore-ip-addresses/

给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

**示例:**

```
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
```

# 解题思路 √

### Python

1. 回溯法 -判断无效的边界条件

```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s:return []
        if len(s)<4 or len(s)>12:return []
        results=[]

        def backTrack(k,tempAddress,s):
            if k==4 or len(s)==0:
                if k==4 and len(s)==0:
                    results.append(tempAddress)
                return 
            
            for i in range(len(s)):
                if i>2:break
                if i!=0 and s[0]=='0':break
                part=s[:i+1]
                if int(part)<256:
                    if len(tempAddress)!=0:
                        part='.'+part
                    temp=tempAddress
                    tempAddress+=part
                    backTrack(k+1,tempAddress,s[i+1:])
                    tempAddress=temp

        backTrack(0,'',s)
        return results
```


```python
                if int(part)<256:
                    if len(tempAddress)!=0:
                        part='.'+part
                    backTrack(k+1,tempAddress+part,s[i+1:])

```



### C++

```cpp

```

---



# 整理与总结

1. 复原IP地址

   相比较于前一道的题目，我们的退出条件有所不同，额外需要k来作为判断标准

   同时也是使用了一种新的诠释方法来做


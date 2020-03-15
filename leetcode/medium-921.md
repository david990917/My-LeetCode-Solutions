---
title: medium-921
tags:
  - LeetCode
description: ''
urlname: medium-921
date: 2019-10-29 10:46:34
---

# 题目





# 解题思路 √



# Python

```python

```

# C++

```cpp
class Solution {
public:
    int minAddToMakeValid(string S) {
        int count=0;
        stack<char> s;
        for(int i=0;i<S.length();i++){
            if(S[i]=='('){s.push('(');}
            else if(S[i]==')'){
                if(s.empty() || s.top()==')'){s.push(')');}
                else if(s.top()=='('){s.pop();}
            }
        }
        for(;!s.empty();s.pop()){count++;}
        return count;
    }
};
```



# 整理与总结

1. 


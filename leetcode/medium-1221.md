---
title: medium-1221
tags:
  - LeetCode
description: ''
urlname: medium-1221
date: 2019-10-29 09:41:31
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
	int balancedStringSplit(string s) {
		int balence = 0, count = 0;
		int len = size(s);
		for (int i = 0; i < len; i++) {
			balence = (s[i] == 'L') ? balence + 1 : balence - 1;
			if (balence == 0) { count += 1; }
		}
		return count;

	}
};
```



# 整理与总结

1. 


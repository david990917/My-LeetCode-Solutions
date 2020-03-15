---
title: medium-62
tags:
  - LeetCode
description: ''
urlname: median-62
date: 2019-10-29 08:57:31
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
	int uniquePaths(int m, int n) {
		vector<vector<int>> dp(m, vector<int>(n, 1));
		for (int i = 1; i < m; i++) {
			for (int j = 1; j < n; j++) {
				dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
			}
		}
		return dp[m - 1][n - 1];
	}
};
```



# 整理与总结

1. 


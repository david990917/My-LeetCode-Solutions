---
title: medium-1139
tags:
  - LeetCode
description: ''
urlname: medium-1139
date: 2019-10-29 09:34:32
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
    int largest1BorderedSquare(vector<vector<int>>& grid) {
        int max=0;
        int m=grid.size(),n=grid[0].size();
        vector<vector<int>> hor(m,vector<int>(n,0)), ver(m,vector<int>(n,0));
        
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==1){
                    hor[i][j]=(j==0)?1:hor[i][j-1]+1;
                    ver[i][j]=(i==0)?1:ver[i-1][j]+1;
                }
            }
        }
        
        for(int i=m-1;i>=0;i--){
            for(int j=n-1;j>=0;j--){
                int small=min(hor[i][j],ver[i][j]);
                while(small>max){
                    if(hor[i-small+1][j]>=small && ver[i][j-small+1]>=small){
                        max=small;break;
                    }
                    small--;
                }
            }
        }
        return max*max;
    }
    
};
   
```



# 整理与总结

1. 


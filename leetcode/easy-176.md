---
title: easy-176
tags:
  - LeetCode
description: ''
urlname: easy-176
date: 2020-03-23 22:25:17
---

# 题目

[第二高的薪水](https://leetcode-cn.com/problems/second-highest-salary/)

编写一个 SQL 查询，获取 Employee 表中第二高的薪水（Salary） 。

```
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
```


例如上述 Employee 表，SQL查询应该返回 200 作为第二高的薪水。如果不存在第二高的薪水，那么查询应返回 null。

```
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
```



# 解题思路 √

### Python

1. 

```python
# Write your MySQL query statement below
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 


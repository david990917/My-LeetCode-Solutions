---
title: easy-175
tags:
  - LeetCode
description: ''
urlname: easy-175
date: 2020-03-23 21:51:46
---

# 题目

[组合两个表](https://leetcode-cn.com/problems/combine-two-tables/)

SQL架构

表1: `Person`

```
+-------------+---------+
| 列名         | 类型     |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId 是上表主键
```

表2: `Address`

```
+-------------+---------+
| 列名         | 类型    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId 是上表主键
```

 

编写一个 SQL 查询，满足条件：无论 person 是否有地址信息，都需要基于上述两表提供 person 的以下信息：

 

```
FirstName, LastName, City, State
```



# 解题思路 √

**方法：使用 outer join**

因为表 Address 中的 personId 是表 Person 的外关键字，所以我们可以连接这两个表来获取一个人的地址信息。

考虑到可能不是每个人都有地址信息，我们应该使用 outer join 而不是默认的 inner join。

![1.jpg](easy-175/ad3df1c4ecc7d2dbe85f92cdde8ec9a731fdd20dc4c5629ecb372b21de26c682-1.jpg)

### SQL

1. 神奇的一道题目

```sql
# Write your MySQL query statement below
select FirstName, LastName, City, State
from Person left join Address
on Person.PersonId = Address.PersonId
;
```

---



# 整理与总结

1. 


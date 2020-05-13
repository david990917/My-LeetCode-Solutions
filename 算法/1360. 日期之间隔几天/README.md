| [English](README_EN.md) | 简体中文 |

# [1360. 日期之间隔几天](https://leetcode-cn.com/problems/number-of-days-between-two-dates)
<p>请你编写一个程序来计算两个日期之间隔了多少天。</p>

<p>日期以字符串形式给出，格式为&nbsp;<code>YYYY-MM-DD</code>，如示例所示。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>date1 = &quot;2019-06-29&quot;, date2 = &quot;2019-06-30&quot;
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>date1 = &quot;2020-01-15&quot;, date2 = &quot;2019-12-31&quot;
<strong>输出：</strong>15
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>给定的日期是&nbsp;<code>1971</code>&nbsp;年到 <code>2100</code>&nbsp;年之间的有效日期。</li>
</ul>

# 解题思路 √

### Python

1. 转换到 1971-01-01 然后进行比较。

```python
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1=[int(i) for i in date1.split('-')]
        date2=[int(i) for i in date2.split('-')]
        return abs(self.date_to_int(*date1)-self.date_to_int(*date2))

    def date_to_int(self,year,month,day):
        month_length=[0,31,28,31,30,31,30,31,31,30,31,30,31]
        ans=day-1
        while month!=0:
            month-=1
            ans+=month_length[month]
            if month==2 and self.isLeapYear(year):
                ans+=1
        ans+=365*(year-1971)
        ans+=(year-1)//4 - 1971//4
        ans-=(year-1)//100 - 1971//100
        ans+=(year-1)//400 - 1971//400
        return ans
    def isLeapYear(self,year):
        return year%400==0 or (year%4==0 and year%100!=0)
```


```python

```

### C++

```cpp
class Solution {
    bool isLeapYear(int year) {
        return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0);
    }

    int date_to_int(string date) {
        int year, month, day;
        sscanf(date.c_str(), "%d-%d-%d", &year, &month, &day);
        int monthDate[] = { 0,31,28,31,30,31,30,31,31,30,31,30,31 };
        int result = day - 1;
        while (month != 0) {
            month--;
            result += monthDate[month];
            if (month == 2 and isLeapYear(year)) { result += 1; }
            
        }
        result += 365 * (year - 1971);
        result += (year - 1) / 4 - (1971) / 4;
        result -= (year - 1) / 100 - (1971) / 100;
        result += (year - 1) / 400 - (1971) / 400;
        return result;
    }
public:
    int daysBetweenDates(string date1, string date2) {
        return abs(date_to_int(date1) - date_to_int(date2));
    }
};
```

---



# 整理与总结

1. `sscanf(date.c_str(), "%d-%d-%d", &year, &month, &day);`

2. ```c++
   result += 365 * (year - 1971);
   result += (year - 1) / 4 - (1971) / 4;
   result -= (year - 1) / 100 - (1971) / 100;
   result += (year - 1) / 400 - (1971) / 400;
   ```

   
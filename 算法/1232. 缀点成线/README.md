| [English](README_EN.md) | 简体中文 |

# [1232. 缀点成线](https://leetcode-cn.com/problems/check-if-it-is-a-straight-line)
<p>在一个&nbsp;XY 坐标系中有一些点，我们用数组&nbsp;<code>coordinates</code>&nbsp;来分别记录它们的坐标，其中&nbsp;<code>coordinates[i] = [x, y]</code>&nbsp;表示横坐标为 <code>x</code>、纵坐标为 <code>y</code>&nbsp;的点。</p>

<p>请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 <code>true</code>，否则请返回 <code>false</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/19/untitled-diagram-2.jpg" style="height: 336px; width: 336px;"></p>

<pre><strong>输入：</strong>coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/19/untitled-diagram-1.jpg" style="height: 336px; width: 348px;"></strong></p>

<pre><strong>输入：</strong>coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;=&nbsp;coordinates.length &lt;= 1000</code></li>
	<li><code>coordinates[i].length == 2</code></li>
	<li><code>-10^4 &lt;=&nbsp;coordinates[i][0],&nbsp;coordinates[i][1] &lt;= 10^4</code></li>
	<li><code>coordinates</code>&nbsp;中不含重复的点</li>
</ul>

**标签:**  [几何](https://leetcode-cn.com/tag/geometry) [数组](https://leetcode-cn.com/tag/array) [数学](https://leetcode-cn.com/tag/math) 
# 解题思路 √

### Python

1. 

```python

```


```python

```

### C++

```cpp

```

### Java标准答案

```java
class Solution {
    public boolean checkStraightLine(int[][] coordinates) {
        int deltaX = coordinates[0][0], deltaY = coordinates[0][1];
        int n = coordinates.length;
        for (int i = 0; i < n; i++) {
            coordinates[i][0] -= deltaX;
            coordinates[i][1] -= deltaY;
        }
        int A = coordinates[1][1], B = -coordinates[1][0];
        for (int i = 2; i < n; i++) {
            int x = coordinates[i][0], y = coordinates[i][1];
            if (A * x + B * y != 0) {
                return false;
            }
        }
        return true;
    }
}
```

---



# 整理与总结

1. 
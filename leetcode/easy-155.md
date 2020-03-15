---
title: easy-155
tags:
  - LeetCode
description: ''
urlname: easy-155
date: 2019-08-31 16:55:16
---

# 题目

https://leetcode.com/problems/min-stack/description/

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- getMin() -- Retrieve the minimum element in the stack.

 

**Example:**

```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
```



# 解题思路 √

符合直觉的方法是，每次对栈进行修改操作（push和pop）的时候更新最小值。 然后getMin只需要返回我们计算的最小值即可， top也是直接返回栈顶元素即可。 这种做法每次修改栈都需要更新最小值，因此时间复杂度是O(n).

[![155.min-stack](easy-155/155.min-stack-1.png)](https://github.com/azl397985856/leetcode/blob/master/assets/problems/155.min-stack-1.png)

是否有更高效的算法呢？答案是有的。

我们每次入栈的时候，保存的不再是真正的数字，而是它与当前最小值的差（当前元素没有入栈的时候的最小值）。 这样我们pop和top的时候拿到栈顶元素再加上**上一个**最小值即可。 另外我们在push和pop的时候去更新min，这样getMin的时候就简单了，直接返回min。

> 注意上面加粗的“上一个”，不是“当前的最小值”

经过上面的分析，问题的关键转化为“如果求的上一个最小值”，解决这个的关键点在于利用min。

pop或者top的时候：

- 如果栈顶元素小于0，说明栈顶是当前最小的元素，它出栈会对min造成影响，我们需要去更新min。 上一个最小的是“min - 栈顶元素”,我们需要将上一个最小值更新为当前的最小值

> 因为栈顶元素入栈的时候的通过 `栈顶元素 = 真实值 - 上一个最小的元素` 得到的， 而真实值 = min， 因此可以得出`上一个最小的元素 = 真实值 -栈顶元素`

- 如果栈顶元素大于0，说明它对最小值`没有影响`，上一个最小值就是上上个最小值。

[![155.min-stack-2](easy-155/155.min-stack-2.png)](https://github.com/azl397985856/leetcode/blob/master/assets/problems/155.min-stack-2.png) [![155.min-stack-3](easy-155/155.min-stack-3.png)](https://github.com/azl397985856/leetcode/blob/master/assets/problems/155.min-stack-3.png)

## 关键点

- 最小栈存储的不应该是真实值，而是真实值和min的差值
- top的时候涉及到对数据的还原，这里千万注意是**上一个**最小值

# Python

```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = float('inf')
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x - self.min)
        if x < self.min:
            self.min = x

    def pop(self) -> None:
        if not self.stack:
            return
        tmp = self.stack.pop()
        if tmp < 0:
            self.min -= tmp

    def top(self) -> int:
        if not self.stack:
            return
        tmp = self.stack[-1]
        if tmp < 0:
            return self.min
        else:
            return self.min + tmp

    def getMin(self) -> int:
        return self.min



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```



# 整理与总结

1. 当前最小值
2. 一步一步想清楚就好了


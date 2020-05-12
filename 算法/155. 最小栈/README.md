| [English](README_EN.md) | 简体中文 |

# [155. 最小栈](https://leetcode-cn.com/problems/min-stack)
<p>设计一个支持 <code>push</code> ，<code>pop</code> ，<code>top</code> 操作，并能在常数时间内检索到最小元素的栈。</p>

<ul>
	<li><code>push(x)</code> &mdash;&mdash; 将元素 x 推入栈中。</li>
	<li><code>pop()</code>&nbsp;&mdash;&mdash; 删除栈顶的元素。</li>
	<li><code>top()</code>&nbsp;&mdash;&mdash; 获取栈顶元素。</li>
	<li><code>getMin()</code> &mdash;&mdash; 检索栈中的最小元素。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例:</strong></p>

<pre><strong>输入：</strong>
[&quot;MinStack&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;getMin&quot;,&quot;pop&quot;,&quot;top&quot;,&quot;getMin&quot;]
[[],[-2],[0],[-3],[],[],[],[]]

<strong>输出：</strong>
[null,null,null,null,-3,null,0,-2]

<strong>解释：</strong>
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --&gt; 返回 -3.
minStack.pop();
minStack.top();      --&gt; 返回 0.
minStack.getMin();   --&gt; 返回 -2.
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>pop</code>、<code>top</code> 和 <code>getMin</code> 操作总是在 <strong>非空栈</strong> 上调用。</li>
</ul>

**标签:**  [栈](https://leetcode-cn.com/tag/stack) [设计](https://leetcode-cn.com/tag/design) 
 ### 相似题目
- 困难:	[滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum) 
- 简单:	[最大栈](https://leetcode-cn.com/problems/max-stack) 

# 解题思路 √

### Python

1. 只用一个栈的方法

```python
class MinStack:

    def __init__(self):
        self.min=sys.maxsize
        self.stack=[]

    def push(self, x: int) -> None:
        self.stack.append(x-self.min)
        if x<self.min:
            self.min=x
            
    def pop(self) -> None:
        target=self.stack.pop()
        if target<0:
            self.min=self.min-target
        
    def top(self) -> int:
        if self.stack:
            target=self.stack[-1]
            if target<0:return self.min
            return target+self.min

    def getMin(self) -> int:
        return self.min
```


```python

```

### C++

使用两个栈来做

```cpp
class MinStack {
    stack<int> x_stack;
    stack<int> min_stack;
public:
    /** initialize your data structure here. */
    MinStack() {
        min_stack.push(INT_MAX);
    }
    
    void push(int x) {
        x_stack.push(x);
        min_stack.push(min(min_stack.top(),x));
    }
    
    void pop() {
        x_stack.pop();
        min_stack.pop();
    }
    
    int top() {
        return x_stack.top();
    }
    
    int getMin() {
        return min_stack.top();
    }
};

```

---



# 整理与总结

1. 
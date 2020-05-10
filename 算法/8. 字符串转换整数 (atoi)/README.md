| [English](README_EN.md) | 简体中文 |

# [8. 字符串转换整数 (atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi)
<p>请你来实现一个&nbsp;<code>atoi</code>&nbsp;函数，使其能将字符串转换成整数。</p>

<p>首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：</p>

<ul>
	<li>如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。</li>
	<li>假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。</li>
	<li>该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。</li>
</ul>

<p>注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。</p>

<p>在任何情况下，若函数不能进行有效的转换时，请返回 0 。</p>

<p><strong>提示：</strong></p>

<ul>
	<li>本题中的空白字符只包括空格字符 <code>&#39; &#39;</code> 。</li>
	<li>假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为&nbsp;[&minus;2<sup>31</sup>,&nbsp; 2<sup>31&nbsp;</sup>&minus; 1]。如果数值超过这个范围，请返回 &nbsp;INT_MAX (2<sup>31&nbsp;</sup>&minus; 1) 或&nbsp;INT_MIN (&minus;2<sup>31</sup>) 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> &quot;42&quot;
<strong>输出:</strong> 42
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> &quot;   -42&quot;
<strong>输出:</strong> -42
<strong>解释: </strong>第一个非空白字符为 &#39;-&#39;, 它是一个负号。
&nbsp;    我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
</pre>

<p><strong>示例&nbsp;3:</strong></p>

<pre><strong>输入:</strong> &quot;4193 with words&quot;
<strong>输出:</strong> 4193
<strong>解释:</strong> 转换截止于数字 &#39;3&#39; ，因为它的下一个字符不为数字。
</pre>

<p><strong>示例&nbsp;4:</strong></p>

<pre><strong>输入:</strong> &quot;words and 987&quot;
<strong>输出:</strong> 0
<strong>解释:</strong> 第一个非空字符是 &#39;w&#39;, 但它不是数字或正、负号。
     因此无法执行有效的转换。</pre>

<p><strong>示例&nbsp;5:</strong></p>

<pre><strong>输入:</strong> &quot;-91283472332&quot;
<strong>输出:</strong> -2147483648
<strong>解释:</strong> 数字 &quot;-91283472332&quot; 超过 32 位有符号整数范围。 
&nbsp;    因此返回 INT_MIN (&minus;2<sup>31</sup>) 。
</pre>

**标签:**  [数学](https://leetcode-cn.com/tag/math) [字符串](https://leetcode-cn.com/tag/string) 
 ### 相似题目
- 简单:	[整数反转](https://leetcode-cn.com/problems/reverse-integer) 
- 困难:	[有效数字](https://leetcode-cn.com/problems/valid-number) 

# 解题思路 √

### Python

1. 线性扫描 - 循环：

   **总结：**

   - 循环内部进行常规的判断：能定论 `break` ； 不能定论 `continue`
   - 跳出循环的时候判断一下 `idx==length`

   **分析：**

   - 先进行有效处理，然后进行退出判断，最后进行无效`continue` 

     👆这个退出是在有效长度范围末尾 ==length-1，`for` 循环内部这样操作

     但是是不是更常见是在 **循环外面** 进行判断（需要==length）

   - 先退出判断；并列有效处理，无效 `continue` 

     👆退出是超出有效范围 ==length，可以用于调用的递归函数中

```python
class Solution:
    def myAtoi(self, str: str) -> int:
        length=len(str)
        unsignedFlag=False
        if length==0:return 0
        for idx,char in enumerate(str): 
            if char=='+' or char=='-':
                unsignedFlag=False
                break
            if '0'<=char<='9':
                unsignedFlag=True
                break
            if char==' ':continue
            else:return 0
        if idx==length:return 0    
        
        if unsignedFlag:
            numberIDX=idx
            result=0
            while numberIDX<length and '0'<=str[numberIDX]<='9':
                result=result*10+int(str[numberIDX])
                numberIDX+=1
            return min(result,2**31-1)
        else:
            numberIDX=idx+1
            if numberIDX==length or not '0'<=str[numberIDX]<='9':return 0
            result=0
            while numberIDX<length and '0'<=str[numberIDX]<='9':
                result=result*10+int(str[numberIDX])
                numberIDX+=1
            return min(result,2**31-1) if str[idx]=='+' else max(-result,-2**31)
```


```python

```

### C++

官方题解里面提到了**自动机** - 为了避免处理字符串臃肿的代码

![fig1](README/8_fig1.PNG)

|               | **' '** | **+/-** | **number** | **other** |
| :------------ | :-----: | :-----: | :--------: | :-------: |
| **start**     |  start  | signed  | in_number  |    end    |
| **signed**    |   end   |   end   | in_number  |    end    |
| **in_number** |   end   |   end   | in_number  |    end    |
| **end**       |   end   |   end   |    end     |    end    |

```cpp
class Automaton {
	string state = "start";
	unordered_map<string, vector<string>> table = {
		{"start",{"start","signed","in_number","end"}},
		{"signed",{"end","end","in_number","end"}},
		{"in_number",{"end","end","in_number","end"}},
		{"end",{"end","end","end","end"}}
	};
	int get_col(char c) {
		if (isspace(c))return 0;
		if (c == '+' or c == '-')return 1;
		if (isdigit(c))return 2;
		return 3;
	}
public:
	int sign = 1;
	long long ans = 0;
    void get(char c){
        state=table[state][get_col(c)];
        if(state=="in_number"){
            ans=ans*10+c-'0';
            ans=sign==1?min(ans,(long long)INT_MAX):min(ans,-(long long)INT_MIN);
        }
        else if(state=="signed"){sign=c=='+'?1:-1;}
    }
};

class Solution {
public:
    int myAtoi(string str) {
        Automaton automaton;
        for(char c:str){automaton.get(c);}
        return automaton.sign*automaton.ans;
    }
};
```

---



# 整理与总结

1. 循环操作，见上

2. C++ 中数字

   ```
   cout<<(long long)INT_MAX<<endl; //2147483647
   cout<<(long long)INT_MIN<<endl; //-2147483648
   ```

3. C++ 中居然支持 and / or 作为逻辑运算符
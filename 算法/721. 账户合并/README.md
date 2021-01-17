| [English](README_EN.md) | 简体中文 |

# [721. 账户合并](https://leetcode-cn.com/problems/accounts-merge)
<p>给定一个列表 <code>accounts</code>，每个元素 <code>accounts[i]</code> 是一个字符串列表，其中第一个元素 <code>accounts[i][0]</code> 是 <em>名称 (name)</em>，其余元素是 <em>emails </em>表示该账户的邮箱地址。</p>

<p>现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。</p>

<p>合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。账户本身可以以任意顺序返回。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
<b>输出：
</b>[["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
<b>解释：</b>
第一个和第三个 John 是同一个人，因为他们有共同的邮箱地址 "johnsmith@mail.com"。 
第二个 John 和 Mary 是不同的人，因为他们的邮箱地址没有被其他帐户使用。
可以以任何顺序返回这些列表，例如答案 [['Mary'，'mary@mail.com']，['John'，'johnnybravo@mail.com']，
['John'，'john00@mail.com'，'john_newyork@mail.com'，'johnsmith@mail.com']] 也是正确的。
</pre>

<p> </p>

<p><b>提示：</b></p>

<ul>
	<li><code>accounts</code>的长度将在<code>[1，1000]</code>的范围内。</li>
	<li><code>accounts[i]</code>的长度将在<code>[1，10]</code>的范围内。</li>
	<li><code>accounts[i][j]</code>的长度将在<code>[1，30]</code>的范围内。</li>
</ul>

**标签:**  [深度优先搜索](https://leetcode-cn.com/tag/depth-first-search) [并查集](https://leetcode-cn.com/tag/union-find) 
 ### 相似题目
- 中等:	[冗余连接](https://leetcode-cn.com/problems/redundant-connection) 
- 简单:	[句子相似性](https://leetcode-cn.com/problems/sentence-similarity) 
- 中等:	[句子相似性 II](https://leetcode-cn.com/problems/sentence-similarity-ii) 

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
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        Map<String, Integer> emailToIndex = new HashMap<String, Integer>();
        Map<String, String> emailToName = new HashMap<String, String>();
        int emailsCount = 0;
        for (List<String> account : accounts) {
            String name = account.get(0);
            int size = account.size();
            for (int i = 1; i < size; i++) {
                String email = account.get(i);
                if (!emailToIndex.containsKey(email)) {
                    emailToIndex.put(email, emailsCount++);
                    emailToName.put(email, name);
                }
            }
        }
        UnionFind uf = new UnionFind(emailsCount);
        for (List<String> account : accounts) {
            String firstEmail = account.get(1);
            int firstIndex = emailToIndex.get(firstEmail);
            int size = account.size();
            for (int i = 2; i < size; i++) {
                String nextEmail = account.get(i);
                int nextIndex = emailToIndex.get(nextEmail);
                uf.union(firstIndex, nextIndex);
            }
        }
        Map<Integer, List<String>> indexToEmails = new HashMap<Integer, List<String>>();
        for (String email : emailToIndex.keySet()) {
            int index = uf.find(emailToIndex.get(email));
            List<String> account = indexToEmails.getOrDefault(index, new ArrayList<String>());
            account.add(email);
            indexToEmails.put(index, account);
        }
        List<List<String>> merged = new ArrayList<List<String>>();
        for (List<String> emails : indexToEmails.values()) {
            Collections.sort(emails);
            String name = emailToName.get(emails.get(0));
            List<String> account = new ArrayList<String>();
            account.add(name);
            account.addAll(emails);
            merged.add(account);
        }
        return merged;
    }
}

class UnionFind {
    int[] parent;

    public UnionFind(int n) {
        parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    public void union(int index1, int index2) {
        parent[find(index2)] = find(index1);
    }

    public int find(int index) {
        if (parent[index] != index) {
            parent[index] = find(parent[index]);
        }
        return parent[index];
    }
}

```



---



# 整理与总结

1. 
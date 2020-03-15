---
title: medium-950
tags:
  - LeetCode
description: 'Reveal Cards In Increasing Order'
urlname: medium-950
date: 2019-09-19 21:55:32
---

# 题目

In a deck of cards, every card has a unique integer.  You can order the deck in any order you want.

Initially, all the cards start face down (unrevealed) in one deck.

Now, you do the following steps repeatedly, until all cards are revealed:

1. Take the top card of the deck, reveal it, and take it out of the deck.
2. If there are still cards in the deck, put the next top card of the deck at the bottom of the deck.
3. If there are still unrevealed cards, go back to step 1.  Otherwise, stop.

Return an ordering of the deck that would reveal the cards in **increasing order.**

The first entry in the answer is considered to be the top of the deck.

 

**Example 1:**

```
Input: [17,13,11,2,3,5,7]
Output: [2,13,3,11,5,17,7]
Explanation: 
We get the deck in the order [17,13,11,2,3,5,7] (this order doesn't matter), and reorder it.
After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
We reveal 13, and move 17 to the bottom.  The deck is now [17].
We reveal 17.
Since all the cards revealed are in increasing order, the answer is correct.
```

 

**Note:**

1. `1 <= A.length <= 1000`
2. `1 <= A[i] <= 10^6`
3. `A[i] != A[j]` for all `i != j`



# 解题思路 √

利用倒序的方法来实现这道题目的解答

使用ABCD举例子就很好理解，如果最开始排序是ABCD，取出的顺序就是ACBD，令ACBD从小到大。

我们先放D，然后D拿出来，放D放B；重复过程，得到原序列。

[POP出来的是最下面，放最下面之前是在最上面；比它小的一个（先出去的）在他前面]

更长的组合依次类推。

# Python

```python
from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        i=len(deck)-2
        
        arr=deque()
        arr.append(deck[-1])
        while (i>=0):
            tmp=arr.pop()
            arr.appendleft(tmp)
            arr.appendleft(deck[i])
            i-=1
        return list(arr)
```



# 整理与总结

1. 经常的操作是：数据结构里面放入一个东西（初始化），然后弹出，再操作。


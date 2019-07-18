
### 二叉树：
几个定义
![](../assets/images/树的几个定义.jpg)

	可以用数组表示一棵树  
	通过父节点计算子节点：左节点 2i+1 右结点 2i+2（超出数组下标表示没有）
	通过子节点计算父节点 ：i-1//2

	遍历方式：
		先序（根）遍历:    78 56 34 43 4  1 15 2 23
		中序（根）遍历：	  2 43 23 56 4 78 1 34 15 
		后序（根）遍历：   2 23 43 4 56  1 15 34 78
		总结 将每一个节点抽象为树，带到子节点的树按某个原则遍历完之后在继续按原则遍历下个节点

### 二叉堆：
二叉堆是一颗完全二叉树：

#### 特性：
- 父节点的键值大于或者等于（小于或者等于）任何一个子节点的键值
- 每个节点的左子树或者右子树都是一个二叉堆（问题的根本性质一样）
	- 任意节点的值大于等于子节点的值（大顶堆）
    - 任意节点的值小于等于子节点的值（小顶堆）

#### 堆排序步骤：
1. 堆化 反向调整使得每个子树都是大顶堆
2. 按序输出元素：把对顶和最末元素对调，然后调整堆顶元素，使得整个子树符合大顶堆的性质
	
### 树的遍历
```python
def in_order(lists,n):  #中序
    if n>=len(lists):
        return
    in_order(lists,2*n+1)
    print(lists[n],end=' ')
    in_order(lists,2*n+2)

def front_order(lists,n):  #前序
    if n>=len(lists):
        return
    print(lists[n],end=' ')
    front_order(lists,2*n+1)
    front_order(lists,2*n+2)

def rear_order(lists,n):  #后序
    if n>=len(lists):
        return
    rear_order(lists,2*n+1)
    rear_order(lists,2*n+2)
    print(lists[n],end=' ')

if __name__ == '__main__':
    l=[78, 56, 34, 43, 4, 1, 15, 2, 23]
    in_order(l,0)
    print()
    front_order(l,0)
    print()
    rear_order(l,0)
```

### 二叉查找树

### 平衡二叉树


### 平衡二叉查找树
严格定义： 二叉树的任意一个节点的左右子树的高度差不能大于1


### 红黑树（Red-Black Tree， R-B Tree)
一种不严格的平衡二叉查找树

#### 定义
- 根节点是黑色的
- 每个叶子节点



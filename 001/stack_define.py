# 用列表实现一个栈


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):  # 判断栈是否为空
        return len(self.items) == 0

    def push(self, item):  # 压入栈顶
        return self.items.append(item)

    def pop(self):  # 弹出栈顶
        return self.items.pop()

    def peek(self):  # 取栈顶的元素但是不弹出
        if self.is_empty() != 'True':
            return self.items[-1]
        else:
            return None

    def size(self):  # 获取栈的长度
        return len(self.items)


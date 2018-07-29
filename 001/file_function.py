def store_top(tmp_stack):
    # 将栈顶元素依次压入栈中
    if tmp_stack.is_empty(tmp_stack):
        return
    else:
        bottom_value = get_bottom(tmp_stack)
        store_top(tmp_stack)
        tmp_stack.push(tmp_stack, bottom_value)
        return tmp_stack


def get_bottom(tmp_stack):
    # 取出栈底元素，剩余元素的位置不变，(1,2,3)取出栈底元素1之后堆栈变为(2,3)
    result = tmp_stack.pop(tmp_stack)
    if tmp_stack.is_empty(tmp_stack):
        return result
    else:
        last = get_bottom(tmp_stack)
        tmp_stack.push(tmp_stack, result)
        return last


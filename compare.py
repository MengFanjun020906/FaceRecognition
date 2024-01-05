def compare_variable_with_array(variable, array):
    if variable in array:
        return 1
    else:
        return 0

# 示例使用
my_variable = 42  # 替换为你的变量
my_array = [10, 20, 30, 40, 50]  # 替换为你的数组

result = compare_variable_with_array(my_variable, my_array)
print(result)

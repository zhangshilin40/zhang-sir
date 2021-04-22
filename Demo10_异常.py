# 异常
list1 = [23, 4, 5, 18, 9, 34]
# print(list1[6])  # IndexError: list index out of range
print(5 / 3)
# print(5 / 0)  # ZeroDivisionError: division by zero

# 异常捕获
try:
    print(5 / 0)
    list1 = [23, 4, 5, 18, 9, 34]
    print(list1[6])
# 一次性处理所有异常
except:
    print("程序执行出现了异常")

print('-' * 60)

try:
    print(5 / 0)
    list1 = [23, 4, 5, 18, 9, 34]
    print(list1[6])
# 一次性处理所有异常,Exception是所有异常类的父类
except Exception:
    print("程序执行出现了异常")

print('-' * 60)


try:
    print(5 / 0)
    list1 = [23, 4, 5, 18, 9, 34]
    print(list1[-1])
    # print(list1[6])
# 指定处理的异常类型
except ZeroDivisionError:
    print("程序执行出现了除0异常")

print('-' * 60)

try:
    # print(5 / 0)
    list1 = [23, 4, 5, 18, 9, 34]
    print(list1[6])
# 指定处理的异常类型
except ZeroDivisionError:
    print("程序执行出现了除0异常")
except IndexError:
    print("程序出现了索引越界异常")

print('-' * 60)

try:
    print(5 / 0)
    list1 = [23, 4, 5, 18, 9, 34]
    print(list1[6])
# 指定多个处理的异常类型
except (ZeroDivisionError, IndexError):
    print("程序执行出现了除0异常或者索引越界异常")

print('-' * 60)

# 新问题1：明明程序运行出现，但是未报错？
# 新问题2：直说了出现异常怎么办，没有说不出现异常怎么办？


try:
    list1 = [23, 4, 5, 18, 9, 34]
    print(list1[5])
    # print(list1[6])
except IndexError:
    print("程序执行出现了索引越界异常")
else:
    print("没有异常")
finally:
    print("无论如何，我都要执行")

print('-' * 60)

try:
    list1 = [23, 4, 5, 18, 9, 34]
    print(list1[5])
    # print(list1[6])
    print("hello world")
except IndexError:
    print("程序执行出现了索引越界异常")
    # 抛出异常
    raise
else:
    print("没有异常")
finally:
    print('hello Python')
    print("无论如何，我都要执行")

print('-' * 60)

try:
    list1 = [23, 4, 5, 18, 9, 34]
    print(list1[5])
    print(list1[6])
    print("hello world")
except IndexError as e:
    print("程序执行出现了索引越界异常")
    # 打印异常信息
    print(e)
    # 抛出异常
    raise
else:
    print("没有异常")
finally:
    print('hello Python')
    print("无论如何，我都要执行")

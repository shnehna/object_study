try:
    num = int(input('请输入一个整数'))
    result = 8 / num
    print(result)
except ZeroDivisionError:
    print("除0错误")
except ValueError:
    print("输入错误")
except Exception as e:
    print("未知错误 %s" % e)
else:
    print("没有异常 结果为 %s" % result)
finally:
    print("无论是否有异常都会有执行")
print("另一个")

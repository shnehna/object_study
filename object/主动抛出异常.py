def input_password():
    pwd = input("请输入密码")
    if len(pwd) >= 8:
        print("输入密码成功，密码为 %s" % pwd)
        return pwd
    print("主动抛出异常")
    e = Exception("密码长度不够")
    raise e


try:
    print(input_password())
except Exception as result:
    print(result)

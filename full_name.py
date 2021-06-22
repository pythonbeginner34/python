first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"#字串中引入变量需要用f开头 f - format
full_name = "{} {}".format(first_name, last_name)#原始格式，python3.6以前的版本使用
print(f"Hello {full_name}")
message = f" Hello {full_name.title()} !"
print(message)
print(full_name)

print("python")
print("\tpython")#\t制表符相当与tab \n换行符
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = 'pyrthon '
print(favorite_language)
print(favorite_language.rstrip())#这样做并不能永久删除空格，必须关联到变量
favorite_language = favorite_language.rstrip()#这样可以永久删除空格
favorite_language = ' python '
favorite_language.lstrip()#这样可以删除最前面的空格
favorite_language.strip()#这样可以删除两边的空格

message = "One of Python's strengths is its diverse community."#这样书写是正确的，换成单引号是错误的
print(message)

messaeg = 'One of Python\' strengths is its diverse community'#使用转义字符也是正确的        
print(message)
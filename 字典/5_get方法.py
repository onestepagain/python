# -*- coding: utf-8 -*-

person = {"name":"peter", "age":24, "gender":"male"}

#get(key, value)方法
print(person.get("name"))

#无返回值，none
person.get("job")


#字典内无该键值时的默认值
person.get("job", "teacher")























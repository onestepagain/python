# -*- coding: utf-8 -*-

person = {"name":"peter", "age":24, "gender":"male"}
print(person)

#删除del

del person["name"]





#改
print(person["name"])
person["name"] = "lisa"
print(person["name"])


#
favorite_languages = {"peter":"python", 
                      "lisa":"java",
                      "iu":"java",}

for language in favorite_languages.values():
    print(language.title())



#set()去重
for language in set(favorite_languages.values()):
    print(language.title())







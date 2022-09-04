
import yaml
import os

data={
    "search_data":{
        "name":"xiaohong",
        "age": 23
    },
    "result":{
        "resu_data":'你好呀，小红',
        "except":[1,2,3,4]
    }
}
doc=os.getcwd()+os.sep+'scripts/test.yaml'
with open(doc,"w",encoding="utf-8") as f:
    yaml.dump(data,f,allow_unicode=True)


# doc=os.getcwd()+os.sep+'scripts/test.yaml'
# with open(doc,'r') as f:
#     data=yaml.safe_load(f)
#     print(data)


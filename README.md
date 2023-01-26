
```
使用说明:
1.创建MongoEngine Model时添加meta={"db_alias":"xxx"}属性。
  例如：
  
  class User(Document):
    name = StringField(primary_key=True, unique=True, max_length=20)
    phone = StringField(max_length=11)  
    meta = {"db_alias": "test_db"}
2.FastAPI对象创建时:
   FastApiMongoEngine(_app, {
        "test_db": {
            "host": "mongodb://127.0.0.1:27017/test_db"
        }

    })
    将mongo配置添加{"alias":"xxxxx"} 


```
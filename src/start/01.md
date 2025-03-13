# 迁移
```shell
python manage.py makemigrations
python manage.py migrate
```
# 继承AbstractUser
```python
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    pass
```
# 设置AUTH_USER_MODEL
```python
# settings.py
AUTH_USER_MODEL = 'api.User'
```
# 使用自定义的命令populate_db
在api/management/commands目录下创建populate_db.py
```shell
python manage.py populate_db
```
# 自定义命令的要求
- 文件必须位于 management/commands 目录下。
- 文件名即命令名称。
- 文件中必须定义一个类 Command，继承自 BaseCommand。
- 在 Command 类中，实现 handle 方法，这是命令执行的核心逻辑。
# 使用graph_models生成模型关系图
需要安装django-extensions
```shell
python manage.py graph_models api>mymodels.dot

```

# 查看ER图的网址
https://dreampuf.github.io/GraphvizOnline/

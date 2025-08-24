# 运行
```bash
rye run dev
```
# 迁移
```shell
python manage.py makemigrations;
python manage.py migrate;
```
# 下面代码什么意思
```python
    def get_queryset(self):
        qs=super().get_queryset()
        print(self.request.user.is_staff)
        if not self.request.user.is_staff:
            qs=qs.filter(user=self.request.user)
        return qs

```
这段代码的意思是：  
重写 `get_queryset` 方法，根据当前用户是否为管理员（`is_staff`）来决定返回哪些订单数据。

- 如果用户是管理员（`is_staff=True`），返回所有订单。
- 如果用户不是管理员，只返回属于自己的订单（`user=self.request.user`）。

这样可以实现普通用户只能看到自己的订单，管理员可以看到全部订单。
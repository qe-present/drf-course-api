# 运行
```bash
rye run dev
```

# 迁移
```shell
python manage.py makemigrations;
python manage.py migrate;
```
# 解释代码
```python
    @method_decorator(cache_page(60 * 15, key_prefix="order_list"))
    @method_decorator(vary_on_headers('Authorization'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

```
这行代码用于给 Django 视图的方法添加装饰器。@method_decorator(vary_on_headers('Authorization')) 的作用是：
vary_on_headers('Authorization') 是 Django 的缓存相关装饰器，告诉缓存系统根据请求头中的 Authorization 字段区分缓存内容。
method_decorator 用于将函数装饰器应用到类视图的方法（如 list 方法）。
这样做可以确保带有不同 Authorization 头的请求会生成不同的缓存响应，避免缓存混淆用户数据。
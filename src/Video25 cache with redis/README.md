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
@receiver([post_delete,post_save], sender=Product)
def validate_product_list(sender, instance, created, **kwargs):
    print("clear product list cache")
    cache.delete_pattern("*product_list*")解释代码
```
这段代码的作用是：

1. 监听 `Product` 模型的新增（`post_save`）和删除（`post_delete`）信号。
2. 每当有商品被创建、更新或删除时，自动执行 `validate_product_list` 方法。
3. 方法里会打印 `"clear product list cache"`，并清除所有以 `product_list` 为关键字的缓存（`cache.delete_pattern("*product_list*")`），确保商品列表缓存及时失效，数据是最新的。
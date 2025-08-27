# 运行
```bash
rye run dev
```

# 迁移
```shell
python manage.py makemigrations;
python manage.py migrate;
```

# 为什么要把item取出来
```python
    def update(self, instance, validated_data):
        items = validated_data.pop("items", None)
        instance=super().update(instance, validated_data)

        if items is not None:
            print(instance)
            print(instance.items.all())
            # Clear existing items
            instance.items.all().delete()
            # Add new items
            for item in items:
                OrderItem.objects.create(order=instance, **item)

        return instance
```
把 `items` 从 `validated_data` 里取出来，
是因为嵌套的订单项（items）不能直接用于创建或更新 `Order` 模型实例。`Order` 只需要自身字段（如用户、状态），
而订单项需要单独处理：先创建订单，再为订单创建对应的订单项。这样可以确保数据结构和数据库关系正确。
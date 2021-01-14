from django.db import models
from django.urls import reverse
from django.forms.models import model_to_dict


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Имя')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Ссылка')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=(self.slug,))


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='Ссылка')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    structure = models.CharField(max_length=200, verbose_name='Состав', blank=True)
    available = models.BooleanField(default=True, verbose_name='В доступности')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Изменено')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=(self.id, self.slug,))

    def get_characters(self):
        verbs = {obj.name: obj.verbose_name for obj in ProductCharacters._meta.get_fields() if obj.name != 'id' and obj.name != 'product'}
        hm = model_to_dict(self.characters)
        return {verbs[key]: hm[key] for key in verbs.keys()}


class ProductMethods(models.Model):
    product = models.ForeignKey(Product, related_name='methods', on_delete=models.CASCADE)
    method = models.CharField(max_length=100, verbose_name='Способ')

    def __str__(self):
        return f'Способ употребления продукта: {self.product.name}'

    class Meta:
        verbose_name = 'Способ употребления'
        verbose_name_plural = 'Способы употребления'


class ProductCharacters(models.Model):
    product = models.OneToOneField(Product, related_name='characters', on_delete=models.CASCADE)
    protein = models.CharField(max_length=5, verbose_name='Белки', blank=True)
    fats = models.CharField(max_length=5, verbose_name='Жиры', blank=True)
    carb = models.CharField(max_length=5, verbose_name='Углеводы', blank=True)
    cals = models.CharField(max_length=5, verbose_name='Каллорийность', blank=True)
    weight = models.CharField(max_length=5, verbose_name='Вес нетто', blank=True)
    pack = models.CharField(max_length=5, verbose_name='Упаковка', blank=True)
    num_per_block = models.CharField(max_length=5, verbose_name='Количество в блоке', blank=True)
    storage_period = models.CharField(max_length=5, verbose_name='Срок хранения', blank=True)
    manufacturer = models.CharField(max_length=30, verbose_name='Произовдитель', blank=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Характеристика продукта'
        verbose_name_plural = 'Характеристики продукта'


# Generated by Django 3.2.6 on 2021-08-20 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(verbose_name='购买数量')),
                ('commodityInfos_id', models.IntegerField(verbose_name='商品ID')),
                ('user_id', models.IntegerField(verbose_name='用户 ID')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
            },
        ),
        migrations.CreateModel(
            name='OrderInfos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.FloatField(verbose_name='订单总价')),
                ('created', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('user_id', models.IntegerField(verbose_name='用户 ID')),
                ('state', models.CharField(choices=[('待支付', '待支付'), ('已支付', '已支付'), ('发货中', '发货中'), ('已签收', '已签收'), ('退货中', '退货中')], max_length=20, verbose_name='订单状态')),
            ],
            options={
                'verbose_name': '订单信息',
                'verbose_name_plural': '订单信息',
            },
        ),
    ]

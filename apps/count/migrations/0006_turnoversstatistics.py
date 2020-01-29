# Generated by Django 2.1.7 on 2019-03-08 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_shop_service_phone'),
        ('count', '0005_feedbackstatistics_orderstatistics_rechargestatistics_withdrawstatistics_wxuserstatistics'),
    ]

    operations = [
        migrations.CreateModel(
            name='TurnoversStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='日期')),
                ('ord_turnovers', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='普通订单总销售额')),
                ('sub_turnovers', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='普通订单总销售额')),
                ('turnovers', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='总销售额')),
                ('shop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Shop', verbose_name='所属店铺')),
            ],
            options={
                'verbose_name': '每日销售额统计',
                'verbose_name_plural': '每日销售额统计',
                'ordering': ('-date',),
            },
        ),
    ]
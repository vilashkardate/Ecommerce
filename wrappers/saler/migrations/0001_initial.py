# Generated by Django 3.1.4 on 2021-05-16 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('sub_Categories', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_id2', models.CharField(default='', max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('price_not', models.IntegerField(default=999)),
                ('desc', models.TextField()),
                ('gst', models.CharField(choices=[('0', '0'), ('3', '3'), ('5', '5'), ('12', '12'), ('18', '18'), ('28', '28')], default='0', max_length=3)),
                ('pub_date', models.DateField(auto_now=True)),
                ('image1', models.ImageField(default='', null=True, upload_to='products/images')),
                ('image2', models.ImageField(blank=True, default='', null=True, upload_to='products/images')),
                ('image3', models.ImageField(blank=True, default='', null=True, upload_to='products/images')),
                ('image4', models.ImageField(blank=True, default='', null=True, upload_to='products/images')),
                ('image5', models.ImageField(blank=True, default='', null=True, upload_to='products/images')),
                ('category', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='saler.category', verbose_name='Category')),
                ('shop', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SalerDetail',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('photo', models.ImageField(default='default.png', upload_to='user_photos')),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('gst_Number', models.CharField(max_length=15, null=True)),
                ('shop_Name', models.CharField(max_length=500, null=True)),
                ('alternate_mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('shop_Address', models.TextField()),
                ('pincode', models.CharField(max_length=6, null=True)),
                ('landmark', models.CharField(blank=True, max_length=500, null=True)),
                ('locality', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(choices=[('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('Chhattisgarh', 'Chhattisgarh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Lakshadweep', 'Lakshadweep'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Puducherry', 'Puducherry'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttarakhand', 'Uttarakhand'), ('Uttar Pradesh', 'Uttar Pradesh'), ('West Bengal', 'West Bengal')], max_length=50, null=True)),
                ('account_Holder_Name', models.CharField(max_length=50, null=True)),
                ('account_Number', models.CharField(max_length=20, null=True)),
                ('ifsc_Code', models.CharField(max_length=11, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SellerSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, null=True)),
                ('image', models.ImageField(upload_to='seller_slider_img')),
                ('url', models.CharField(default='#', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WholeSaleProductOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default='', max_length=50)),
                ('products', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='', max_length=15)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WholeSaleProduct',
            fields=[
                ('product_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.TextField()),
                ('size', models.TextField(verbose_name='Size Avialabe(Separated by Comma)')),
                ('color', models.TextField(verbose_name='Enter Color Separated by Comma')),
                ('min_Quantity', models.IntegerField(default=0, null=True)),
                ('pub_date', models.DateField(auto_now=True)),
                ('image1', models.ImageField(default='', null=True, upload_to='products/images')),
                ('image2', models.ImageField(blank=True, default='', null=True, upload_to='products/images')),
                ('image3', models.ImageField(blank=True, default='', null=True, upload_to='products/images')),
                ('image4', models.ImageField(blank=True, default='', null=True, upload_to='products/images')),
                ('image5', models.ImageField(blank=True, default='', null=True, upload_to='products/images')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='saler.category', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='trend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('product', models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='saler.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=20)),
                ('quantity', models.IntegerField(default=0, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saler.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saler.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default='', max_length=50)),
                ('saler', models.CharField(default='wrappers@admin', max_length=100)),
                ('products', models.CharField(max_length=50)),
                ('size', models.CharField(default='', max_length=50, null=True)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='', max_length=15)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MyCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=100)),
                ('number', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='dow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('product', models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='saler.product', verbose_name='Product Id')),
            ],
        ),
    ]

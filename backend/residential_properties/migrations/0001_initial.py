# Generated by Django 3.0.6 on 2020-05-07 17:03

from django.db import migrations, models
import django.db.models.deletion
import residential_properties.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geo_location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApartmentDecoration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Отделка квартиры',
                'verbose_name_plural': 'Отделки квартиры',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ClassOfHousing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Класс Жилья')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Класс Жилья',
                'verbose_name_plural': 'Классы Жилья',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Deadline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_date', models.CharField(max_length=10, unique=True, verbose_name='Срок сдачи')),
                ('only_year', models.IntegerField(db_index=True, verbose_name='Год срока сдачи')),
                ('only_quarter', models.IntegerField(db_index=True, verbose_name='Квартал срока сдачи')),
            ],
            options={
                'verbose_name': 'Срок сдачи',
                'verbose_name_plural': 'Сроки сдачи',
            },
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Застройщик')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('logo_image', models.FileField(blank=True, null=True, upload_to=residential_properties.models.generate_url_for_logo_image, verbose_name='Логотип застройщика')),
            ],
            options={
                'verbose_name': 'Застройщик',
                'verbose_name_plural': 'Застройщики',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='FloorInBuilding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_floor', models.IntegerField(db_index=True, verbose_name='Этаж')),
            ],
            options={
                'verbose_name': 'Этаж',
                'verbose_name_plural': 'Этажи',
                'ordering': ['num_floor'],
            },
        ),
        migrations.CreateModel(
            name='Infrastructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('icon', models.FileField(blank=True, null=True, upload_to=residential_properties.models.generate_url_for_image, verbose_name='Иконка')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Инфраструктура',
                'verbose_name_plural': 'Инфраструктура',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MaterialWallsOfHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Материал стен дома')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Материал стен дома',
                'verbose_name_plural': 'Материалы стен дома',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='NamesOfMetroStations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('distance_to_center', models.CharField(blank=True, max_length=50, null=True, verbose_name='Расстояние до центра')),
                ('sub_text_distance_to_center', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текс для тултипа')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Станция метро',
                'verbose_name_plural': 'Станции метро',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='NumberOfRooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True, verbose_name='Название')),
                ('additional_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Добавочное название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Количество комнат',
                'verbose_name_plural': 'Количество комнат',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ResidentialComplex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Отображать, Да/Нет')),
                ('is_active_load_data', models.BooleanField(default=False, help_text='Отключит данные о квартирах, занесенные вручную.', verbose_name='Включить загруженные данные о квартирах')),
                ('name', models.CharField(db_index=True, max_length=150, unique=True, verbose_name='Название ЖК')),
                ('logo_image', models.FileField(blank=True, null=True, upload_to=residential_properties.models.generate_url_for_logo_image, verbose_name='Логотип ЖК')),
                ('address', models.CharField(blank=True, db_index=True, default=None, max_length=150, null=True, verbose_name='Адрес')),
                ('one_or_many_buildings', models.BooleanField(default=False, verbose_name='В ЖК несколько строений')),
                ('number_of_storeys', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Этажность')),
                ('min_storeys', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Этажность min')),
                ('max_storeys', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Этажность max')),
                ('house_completed', models.BooleanField(default=False, verbose_name='Дом сдан, Да/Нет')),
                ('main_image', models.FileField(blank=True, null=True, upload_to=residential_properties.models.generate_url_for_image, verbose_name='Главное изображение ЖК')),
                ('alt_attr', models.CharField(blank=True, max_length=300, null=True, verbose_name='img alt')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Долгота')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Широта')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('distance_to_metro', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Растояние до метро, м')),
                ('site_developer', models.URLField(blank=True, default=None, max_length=300, null=True, verbose_name='Сайт застройщика/Жилого комплекса')),
                ('is_visible_video', models.BooleanField(default=False, verbose_name='Показывать видео')),
                ('apart_decoration', models.ManyToManyField(blank=True, default=None, related_name='rescomplex_apartdecoration', to='residential_properties.ApartmentDecoration', verbose_name='Отделка')),
                ('city', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rescomplex_city', to='geo_location.City', verbose_name='Город')),
                ('class_of_housing', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rescomplex_classofhousing', to='residential_properties.ClassOfHousing', verbose_name='Класс Новостройки')),
                ('deadline', models.ManyToManyField(blank=True, default=None, related_name='rescomplex_deadline', to='residential_properties.Deadline', verbose_name='Срок сдачи')),
                ('developer', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rescomplex_developer', to='residential_properties.Developer', verbose_name='Застройщик')),
                ('district', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rescomplex_district', to='geo_location.District', verbose_name='Район')),
                ('infrastructure', models.ManyToManyField(blank=True, default=None, related_name='rescomplex_infrastructure', to='residential_properties.Infrastructure', verbose_name='Инфраструктура')),
                ('material_walls', models.ManyToManyField(blank=True, default=None, related_name='rescomplex_materialwalls', to='residential_properties.MaterialWallsOfHouse', verbose_name='Материал стен дома')),
                ('metro_stations', models.ManyToManyField(blank=True, default=None, related_name='rescomplex_metrostations', to='residential_properties.NamesOfMetroStations', verbose_name='Название ближайщего метро')),
                ('region', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rescomplex_region', to='geo_location.Region', verbose_name='Область')),
            ],
            options={
                'verbose_name': 'Жилой Комплекс',
                'verbose_name_plural': 'Жилые Комплексы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='VideoResidentialComplex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_on_video', models.URLField(blank=True, default=None, max_length=2000, null=True, verbose_name='Ссылка на видео')),
                ('add_text', models.CharField(blank=True, max_length=300, null=True, verbose_name='Доплнительный текст')),
                ('residential_complex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residential_properties.ResidentialComplex', verbose_name='Жилой Комплекс')),
            ],
            options={
                'verbose_name': 'Видео Жилого Комплекса',
                'verbose_name_plural': 'Видео Жилого Комплекса',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ResidentialPremise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Отображать, Да/Нет')),
                ('area', models.FloatField(blank=True, db_index=True, null=True, verbose_name='Площадь')),
                ('min_area', models.FloatField(blank=True, db_index=True, null=True, verbose_name='Площадь от, м')),
                ('max_area', models.FloatField(blank=True, db_index=True, null=True, verbose_name='Площадь до, м')),
                ('price', models.FloatField(blank=True, db_index=True, null=True, verbose_name='Цена')),
                ('min_price', models.FloatField(blank=True, db_index=True, null=True, verbose_name='Цена от, м')),
                ('max_price', models.FloatField(blank=True, db_index=True, null=True, verbose_name='Цена до, м')),
                ('floor', models.ManyToManyField(blank=True, default=None, related_name='respremises_floor', to='residential_properties.FloorInBuilding', verbose_name='Этаж')),
                ('number_rooms', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='respremises_numberrooms', to='residential_properties.NumberOfRooms', verbose_name='Количество комнат')),
                ('res_complex', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='respremises_rescomplex', to='residential_properties.ResidentialComplex', verbose_name='Жилой комплекс')),
            ],
            options={
                'verbose_name': 'Жилое помещение',
                'verbose_name_plural': 'Жилые помещения',
            },
        ),
        migrations.CreateModel(
            name='ImagesResidentialComplex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt_attr', models.CharField(blank=True, max_length=300, null=True, verbose_name='img alt')),
                ('image', models.FileField(blank=True, null=True, upload_to=residential_properties.models.generate_url_for_image, verbose_name='Изображение')),
                ('residential_complex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imgrescomplex_rescomplex', to='residential_properties.ResidentialComplex', verbose_name='Жилой Комплекс')),
            ],
            options={
                'verbose_name': 'Изображение Жилого Комплекса',
                'verbose_name_plural': 'Изображения Жилого Комплекса',
            },
        ),
        migrations.CreateModel(
            name='FloorPlansResidentialPremise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt_attr', models.CharField(blank=True, max_length=300, null=True, verbose_name='img alt')),
                ('image', models.FileField(blank=True, null=True, upload_to=residential_properties.models.generate_url_for_image, verbose_name='Планировка Жилого помещения')),
                ('residential_premises', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='floorrespremise_respremise', to='residential_properties.ResidentialPremise', verbose_name='Жилое помещение')),
            ],
            options={
                'verbose_name': 'Планировка Жилого помещения',
                'verbose_name_plural': 'Планировки Жилого помещения',
            },
        ),
    ]

# Generated by Django 2.1.2 on 2018-12-11 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieImdbRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieid', models.BigIntegerField(blank=True, db_column='movieId', null=True)),
                ('imdb_rating', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movie_imdb_rating',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MovieList',
            fields=[
                ('index', models.BigIntegerField()),
                ('movieid', models.BigIntegerField(db_column='movieId', primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('genres', models.TextField(blank=True, null=True)),
                ('year', models.TextField(blank=True, null=True)),
                ('imdbid', models.TextField(blank=True, db_column='imdbId', null=True)),
                ('tmdbid', models.TextField(blank=True, db_column='tmdbId', null=True)),
            ],
            options={
                'db_table': 'movie_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MoviePosters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieid', models.BigIntegerField(blank=True, db_column='movieId', null=True)),
                ('filename', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movie_posters',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MovieRatingsSelected',
            fields=[
                ('index', models.BigIntegerField(blank=True, null=True)),
                ('movieid', models.BigIntegerField(blank=True, db_column='movieId', primary_key=True, serialize=False)),
                ('ratings', models.BigIntegerField(blank=True, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('weight_c', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movie_ratings_selected',
                'managed': False,
            },
        ),
    ]
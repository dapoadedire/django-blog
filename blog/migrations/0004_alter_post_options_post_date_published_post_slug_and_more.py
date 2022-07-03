# Generated by Django 4.0.5 on 2022-07-02 09:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_rename_created_at_post_date_posted_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ("-date_published",)},
        ),
        migrations.AddField(
            model_name="post",
            name="date_published",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                default=django.utils.timezone.now, editable=False, unique=True
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="post",
            name="status",
            field=models.CharField(
                choices=[("draft", "Draft"), ("published", "Published")],
                default="draft",
                max_length=10,
            ),
        ),
    ]
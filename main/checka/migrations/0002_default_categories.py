from django.db import migrations

def create_default_categories(apps, schema_editor):
    Category = apps.get_model('checka', 'Category')
    defaults = [
        "Health",
        "Productivity",
        "Learning",
        "Fitness",
        "Mindfulness",
    ]
    for name in defaults:
        Category.objects.get_or_create(name=name, user=None)

class Migration(migrations.Migration):

    dependencies = [
        ('checka', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_categories),
    ]
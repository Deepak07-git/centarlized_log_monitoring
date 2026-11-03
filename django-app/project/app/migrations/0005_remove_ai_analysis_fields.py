from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_threatlog_ai_analysis"),
    ]

    operations = [
        migrations.RemoveField(model_name="threatlog", name="ai_analyzed"),
        migrations.RemoveField(model_name="threatlog", name="ai_confidence"),
        migrations.RemoveField(model_name="threatlog", name="ai_indicators"),
        migrations.RemoveField(model_name="threatlog", name="ai_model"),
        migrations.RemoveField(model_name="threatlog", name="ai_recommendation"),
        migrations.RemoveField(model_name="threatlog", name="ai_summary"),
    ]

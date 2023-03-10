# Generated by Django 3.2.12 on 2022-12-25 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texts', '0007_alter_recipient_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Unisex', 'Unisex')], default='Male', max_length=30)),
                ('type', models.CharField(choices=[('Tops', 'Tops'), ('Bottoms', 'Bottoms'), ('Shoes', 'Shoes')], default='Tops', max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='recipient',
            name='state',
            field=models.CharField(choices=[('InvalidState', 'InvalidState'), ('UnknownPreference', 'UnknownPreference'), ('AffirmativePurchase', 'AffirmativePurchase'), ('NegativePurchase', 'NegativePurchase'), ('MetadataExists', 'MetadataExists'), ('NoneOrIncorrectMetadata', 'NoneOrIncorrectMetadata'), ('MetadataExists', 'MetadataExists'), ('CorrectMetadata', 'CorrectMetadata'), ('NoPaymentData', 'NoPaymentData'), ('PaymentRequested', 'PaymentRequested'), ('InvalidPaymentDetails', 'InvalidPaymentDetails'), ('PaymentAndMetadataCorrect', 'PaymentAndMetadataCorrect'), ('Terminated', 'Terminated')], default='UnknownPreference', max_length=30),
        ),
    ]

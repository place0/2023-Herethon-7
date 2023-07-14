# Generated by Django 4.2.3 on 2023-07-14 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempuser',
            name='userId',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='tempuser',
            name='userLink',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='tempuser',
            name='userName',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='tempuser',
            name='userPwd',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='userId',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='userLink',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='userName',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='userPwd',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='userType1',
            field=models.CharField(choices=[('option1', '계획형'), ('option2', '즉흥형')], default='option1', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='userType2',
            field=models.CharField(choices=[('option3', '바쁘게 움직이는 여행'), ('option4', '오직 휴식을 위한 여행')], default='option3', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='userType3',
            field=models.CharField(choices=[('option5', '사진 찍는 거 좋아요'), ('option6', '사진 찍는 거 싫어요')], default='option5', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='userType4',
            field=models.CharField(choices=[('option7', '번화가'), ('option8', '자연, 시골')], default='option7', max_length=15, null=True),
        ),
    ]
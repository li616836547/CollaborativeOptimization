# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-18 03:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPUMemory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.UUIDField(help_text='测试用例ID')),
                ('cpu', models.FloatField(default='-1', help_text='CPU利用率', null=True)),
                ('memory', models.FloatField(default='-1', help_text='Memory利用率', null=True)),
                ('add_time', models.IntegerField(default='-1', help_text='添加时间', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetectedParams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.IntegerField(default=0, help_text='异常检测标签(-1,0,1)')),
                ('ave_anneal_soak_t', models.FloatField(help_text='连退均热温度平均值')),
                ('ave_anneal_rapid_cool_outlet_t', models.FloatField(help_text='连退快冷出口温度平均值')),
                ('ave_anneal_slow_cool_outlet_t', models.FloatField(help_text='连退缓冷出口温度平均值')),
                ('pc', models.FloatField(help_text='C%')),
                ('pmn', models.FloatField(help_text='Mn%')),
                ('pp', models.FloatField(help_text='P%')),
                ('ps', models.FloatField(help_text='S%')),
                ('finishing_inlet_t', models.FloatField(help_text='精轧入口温度')),
                ('finishing_outlet_t', models.FloatField(help_text='精轧出口温度')),
                ('coiling_t', models.FloatField(help_text='卷取温度')),
                ('add_time', models.DateTimeField(auto_now_add=True, help_text='添加时间')),
            ],
        ),
        migrations.CreateModel(
            name='FinalResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.UUIDField(help_text='测试用例ID')),
                ('final_result', models.CharField(default='NULL', help_text='是否通过', max_length=10)),
                ('add_time', models.IntegerField(default='-1', help_text='添加时间')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.UUIDField(help_text='测试用例ID')),
                ('log', models.CharField(default='NULL', help_text='日志', max_length=10240000)),
                ('add_time', models.IntegerField(default='-1', help_text='添加时间')),
            ],
        ),
        migrations.CreateModel(
            name='MultiTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.UUIDField(help_text='测试用例ID')),
                ('frame_size', models.IntegerField(default='-1', help_text='帧大小', null=True)),
                ('min_latency', models.CharField(default='-1', help_text='最小时延', max_length=100, null=True)),
                ('max_latency', models.CharField(default='-1', help_text='最大时延', max_length=100, null=True)),
                ('avg_latency', models.CharField(default='-1', help_text='平均时延', max_length=100, null=True)),
                ('tx_rate', models.CharField(default='-1', help_text='发送速率', max_length=100, null=True)),
                ('rx_rate', models.CharField(default='-1', help_text='接收速率', max_length=100, null=True)),
                ('connect_rate', models.CharField(default='-1', help_text='上线速率', max_length=100, null=True)),
                ('session_num', models.IntegerField(default='-1', help_text='Session连接数', null=True)),
                ('add_time', models.IntegerField(default='-1', help_text='添加时间', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PPPoESessionTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.UUIDField(help_text='测试用例ID')),
                ('session_num', models.IntegerField(default='-1', help_text='Session连接数')),
                ('connect_rate', models.FloatField(default='-1', help_text='上线速率')),
                ('add_time', models.IntegerField(default='-1', help_text='添加时间')),
            ],
        ),
        migrations.CreateModel(
            name='TestCaseState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.UUIDField(help_text='测试用例ID')),
                ('set_flow', models.CharField(default='-1', help_text='测试流量', max_length=100)),
                ('set_session', models.IntegerField(default='-1', help_text='测试Session数')),
                ('set_vender', models.CharField(default='-1', help_text='厂商名', max_length=100)),
                ('set_vnf_type', models.CharField(default='-1', help_text='网元类型', max_length=100)),
                ('set_version', models.CharField(default='-1', help_text='版本号', max_length=100)),
                ('set_timer', models.IntegerField(default=-1, help_text='测试次数')),
                ('type_name', models.CharField(default='-1', help_text='测试用例类型', max_length=100)),
                ('add_time', models.DateTimeField(blank=True, default=datetime.datetime.now, help_text='添加时间')),
                ('current_state', models.BooleanField(default=False, help_text='当前状态')),
                ('set_online_rate', models.CharField(default='-1', help_text='上线速率', max_length=100)),
                ('set_platform', models.CharField(default='-1', help_text='云平台名称', max_length=100)),
                ('set_platform_v', models.CharField(default='-1', help_text='云平台版本', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserTransTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.UUIDField(help_text='测试用例ID')),
                ('frame_size', models.IntegerField(default='-1', help_text='帧大小')),
                ('min_latency', models.FloatField(default='-1', help_text='最小时延')),
                ('max_latency', models.FloatField(default='-1', help_text='最大时延')),
                ('avg_latency', models.FloatField(default='-1', help_text='平均时延')),
                ('rx_rate', models.FloatField(default='-1', help_text='接收速率')),
                ('add_time', models.IntegerField(default='-1', help_text='添加时间')),
            ],
        ),
    ]

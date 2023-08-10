from django.db import models
from django.core.validators import MaxValueValidator
from clients.models import Client


class Service(models.Model):
    name = models.CharField(max_length=50)
    full_price = models.PositiveBigIntegerField()

    def __str__(self):
        return f'Service: {self.name}, full price: {self.full_price}'


class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount')
    )

    plan_types = models.CharField(choices=PLAN_TYPES, max_length=10)
    discount_percent = models.PositiveBigIntegerField(default=0, 
                                                      validators=[
                                                          MaxValueValidator(100)
                                                      ])
    
    def __str__(self):
        return f'Plan: {self.plan_types}, discount: {self.discount_percent}'


class Subscription(models.Model):
    client = models.ForeignKey(Client, related_name='subscriptions', on_delete=models.PROTECT)
    service = models.ForeignKey(Service, related_name='subscriptions', on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan, related_name='subscriptions', on_delete=models.PROTECT)

    def __str__(self):
        return f'Client: {self.client}, service: {self.service}, plan: {self.plan}'
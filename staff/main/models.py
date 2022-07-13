from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Staff(MPTTModel):
    class MPTTMeta:
        order_insertion_by = ['name']  # By which field to sort childrens in tree

    name = models.CharField(max_length=150, db_index=True)
    position = models.CharField(max_length=150, db_index=True)
    emp_date = models.DateField(db_index=True)
    salary = models.IntegerField(db_index=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "an employee"
        verbose_name_plural = "Employees"

    def save(self, *args, **kwargs):
        # self.emp_date = '2019-01-01'
        super(Staff, self).save(*args, **kwargs)
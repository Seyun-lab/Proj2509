# myapp/models.py
from django.db import models

class Customers(models.Model):
    year_birth = models.IntegerField(db_column='Year_Birth', blank=True, null=True)  # Field name made lowercase.
    education = models.IntegerField(db_column='Education', blank=True, null=True)  # Field name made lowercase.
    income = models.IntegerField(db_column='Income', blank=True, null=True)  # Field name made lowercase.
    kidhome = models.IntegerField(db_column='Kidhome', blank=True, null=True)  # Field name made lowercase.
    teenhome = models.IntegerField(db_column='Teenhome', blank=True, null=True)  # Field name made lowercase.
    recency = models.IntegerField(db_column='Recency', blank=True, null=True)  # Field name made lowercase.
    mntwines = models.IntegerField(db_column='MntWines', blank=True, null=True)  # Field name made lowercase.
    mntfruits = models.IntegerField(db_column='MntFruits', blank=True, null=True)  # Field name made lowercase.
    mntmeatproducts = models.IntegerField(db_column='MntMeatProducts', blank=True, null=True)  # Field name made lowercase.
    mntfishproducts = models.IntegerField(db_column='MntFishProducts', blank=True, null=True)  # Field name made lowercase.
    mntsweetproducts = models.IntegerField(db_column='MntSweetProducts', blank=True, null=True)  # Field name made lowercase.
    mntgoldprods = models.IntegerField(db_column='MntGoldProds', blank=True, null=True)  # Field name made lowercase.
    numdealspurchases = models.IntegerField(db_column='NumDealsPurchases', blank=True, null=True)  # Field name made lowercase.
    numwebpurchases = models.IntegerField(db_column='NumWebPurchases', blank=True, null=True)  # Field name made lowercase.
    numcatalogpurchases = models.IntegerField(db_column='NumCatalogPurchases', blank=True, null=True)  # Field name made lowercase.
    numstorepurchases = models.IntegerField(db_column='NumStorePurchases', blank=True, null=True)  # Field name made lowercase.
    numwebvisitsmonth = models.IntegerField(db_column='NumWebVisitsMonth', blank=True, null=True)  # Field name made lowercase.
    acceptedcmp1 = models.IntegerField(db_column='AcceptedCmp1', blank=True, null=True)  # Field name made lowercase.
    acceptedcmp2 = models.IntegerField(db_column='AcceptedCmp2', blank=True, null=True)  # Field name made lowercase.
    acceptedcmp3 = models.IntegerField(db_column='AcceptedCmp3', blank=True, null=True)  # Field name made lowercase.
    acceptedcmp4 = models.IntegerField(db_column='AcceptedCmp4', blank=True, null=True)  # Field name made lowercase.
    acceptedcmp5 = models.IntegerField(db_column='AcceptedCmp5', blank=True, null=True)  # Field name made lowercase.
    complain = models.IntegerField(db_column='Complain', blank=True, null=True)  # Field name made lowercase.
    response = models.IntegerField(db_column='Response', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customers'

from django.db import models
from django.contrib.auth.models import User

class userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    website = models.CharField(max_length=100,null=True,unique=True,)
    picture = models.ImageField(upload_to='profile_images',blank=True)
    class Meta:
        db_table='profile'
    def __unicode__(self):
        return self.user.username


class startup_data(models.Model):
    startup_name=User.username
    var1=models.CharField(max_length=100)
    var2=models.CharField(max_length=100)
    class Meta:
        db_table='startup'
    def __str__(self):
        return self.startup_name

class u_name(models.Model):
    companyname=models.CharField(max_length=50)
    #company_logo= models.ImageField()
    company_slogan=models.CharField(max_length=140)

    problem_head=models.CharField(max_length=140)
    problem_description = models.CharField(max_length=140)

    solution_head = models.CharField(max_length=140)
    solution_description = models.CharField(max_length=140)

    TAM = models.CharField(max_length=140)
    SAM = models.CharField(max_length=140)
    CMS = models.CharField(max_length=140)

    product_name = models.CharField(max_length=140)
    product_description = models.CharField(max_length=140)
    #product_image = models.ImageField()

    IPAcquistion = models.CharField(max_length=140)
    potential_market = models.CharField(max_length=140)
    partnership = models.CharField(max_length=140)
    exist_sales = models.CharField(max_length=140)
    market_program = models.CharField(max_length=140)
    CAV_CAC = models.CharField(max_length=140)

    competitor1 = models.CharField(max_length=140)
    competitor2 = models.CharField(max_length=140)
    competitor3 = models.CharField(max_length=140)
    different = models.CharField(max_length=140)


    name1 = models.CharField(max_length=140)
    desig1 = models.CharField(max_length=140)
    name2 = models.CharField(max_length=140)
    desig2 = models.CharField(max_length=140)
    name3 = models.CharField(max_length=140)
    desig3 = models.CharField(max_length=140)
    #name1_image = models.ImageField()
    #name2_image = models.ImageField()
    #name3_image = models.ImageField()

    fund_need=models.CharField(max_length=140)
    fund_expect = models.CharField(max_length=140)
    fund_raised = models.CharField(max_length=140)
    fund_return = models.CharField(max_length=140)

    email = models.CharField(max_length=140)
    phone = models.CharField(max_length=140)
    address = models.CharField(max_length=140)
    link_linkedin = models.URLField()
    link_facebook= models.URLField()
    link_twitter = models.URLField()

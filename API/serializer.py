from rest_framework.serializers import ModelSerializer
from .models import Products
from rest_framework.exceptions import ValidationError
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
    

    # def validate(self, data):
    #     title = data.get('title')
    #     price = data.get('price')
    #     if Products.objects.filter(title=title).exists():
    #         raise ValidationError({'Message':"Bu mahsulot mavjud boshqasini kiriting!"})
    #     if price<=10:
    #         raise ValidationError({'Message':"Narh $10 dan yuqori bulishi kerak!"})
    #     else:
    #         return data
        

    # def validate_discription(self, value):
    #     def counter(value):
    #         s = 0
    #         ls = list(value)
    #         for i in ls:
    #             s+=1
    #         return s
        
    #     if counter(value)<=10:
    #         raise ValidationError({'Message':"Discription kuproq yozing"})


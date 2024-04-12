from rest_framework import serializers
from .models import Main,Category,Cart,Cartitem
#These Names are awful
#Maybe change them later
class DynamicFieldsModelSerializer(serializers.ModelSerializer):#why is this not in the serializer module
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['categoryName']
class getItems(DynamicFieldsModelSerializer):
    #categoryID=serializers.RelatedField(source="Category",read_only=True, many=True)
    categoryID=categorySerializer()
    class Meta:
        model=Main
        fields=['itemName','Distributer','imagepath','price','manufacture','categoryID']
class createOrder(DynamicFieldsModelSerializer):
    class Meta:
        model=Cart
        fields=['userName','email','pickupdelv','address']
class OrderFilterLatest(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields=['cartID','userName','email','pickupdelv','address']
class cartitemscartID(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields=['cartID']
class cartitemitemID(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = ['itemName']
class cartitems(serializers.ModelSerializer):
    #cartID=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    #itemID=serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    #itemID=cartitemitemID()
    class Meta:
        model=Cartitem
        fields=['cartID','itemID','quantity']
class postItems(serializers.ModelSerializer):
    categoryID=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Main
        fields=['itemName','Distributer','imagepath','categoryID','price','manufacture']

#class addCartView(serializers.ModelSerializer):

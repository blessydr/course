from rest_framework import serializers
from .models import Course
from django.contrib.auth.models import User

    
class CourseSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()
    full_duration = serializers.ReadOnlyField()

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'image', 'discount','discounted_price' ,'full_duration']

    def __init__(self, *args, **kwargs):
        show_discounted_price = kwargs.pop('show_discounted_price', True)
        super().__init__(*args, **kwargs)
        if not show_discounted_price:
            self.fields.pop('discounted_price')

    def get_discounted_price(self, obj):
        original_price = obj.price
        discount = obj.discount
        discounted_price = original_price - (original_price * discount / 100)
        return round(discounted_price, 2)

class CourseDetailSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField() 
    full_duration = serializers.ReadOnlyField()

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'image','description','price', 'discount','discounted_price' ,'full_duration']
        
    def get_discounted_price(self, obj):
      
        original_price = obj.price
        discount = obj.discount
        discounted_price = original_price - (original_price * discount / 100)
        return round(discounted_price, 2)    
        
    
    
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
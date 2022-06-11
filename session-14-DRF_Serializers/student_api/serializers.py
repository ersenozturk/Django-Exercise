from rest_framework import serializers
from .models import Path, Student
from django.utils.timezone import now

# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=50)
#     last_name = serializers.CharField(max_length=50)
#     number = serializers.IntegerField()
#     # id = serializers.IntegerField()
    
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)       
#         instance.last_name = validated_data.get('last_name', instance.last_name)      
#         instance.number = validated_data.get('number', instance.number)
#         instance.save()
#         return instance
    
#     def validate_number(self, value):
#             """
#             Check that the number is below 1000
#             """
#             if value > 1000:
#                 raise serializers.ValidationError("Numbers must below 1000!")
#             return value

class StudentSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'number', 'days_since_joined']
        # fields = '__all__'
        # exclude  = ['id']
        
    def validate_number(self, value):
        """
        Check that the number is below 1000
        """
        if value > 1000:
            raise serializers.ValidationError("Numbers must below 1000!")
        return value
    
    def validate_first_name(self, value):
        """
        Check that the first name is rafe
        """
        if value.lower() == 'rafe':
            raise serializers.ValidationError("Rafe can not be our student")
        return value

    def get_days_since_joined(self, obj):
        return (now() - obj.register_date).days
        

class PathSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)
    # students = serializers.StringRelatedField(many=True)
    # students = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = Path
        fields = '__all__'
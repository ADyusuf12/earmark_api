from rest_framework import serializers
from .models import Property, PropertyCategory

class PropertyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyCategory
        fields = ['id', 'name']


class PropertySerializer(serializers.ModelSerializer):
    category = PropertyCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=PropertyCategory.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Property
        fields = [
            'id', 'title', 'description', 'price', 'location',
            'category', 'category_id', 'listing_type',
            'owner_profile', 'image', 'is_available', 'date_posted'
        ]
        read_only_fields = ['owner_profile', 'date_posted']

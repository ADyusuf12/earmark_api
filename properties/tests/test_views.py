# properties/tests/test_views.py

import pytest
from rest_framework.test import APIClient
from properties.models import Property, PropertyCategory
from accounts.models import UserProfile
from django.contrib.auth.models import User, Group

@pytest.mark.django_db
def test_property_list_returns_paginated_response():
    client = APIClient()

    # Create sample user and profile
    user = User.objects.create_user(username='agent_user', password='testpass')
    group, _ = Group.objects.get_or_create(name='Agent')
    user.groups.add(group)
    profile = UserProfile.objects.create(user=user)
    
    category = PropertyCategory.objects.create(name="Duplex")

    # Create sample properties
    Property.objects.create(
        title="Test Property 1",
        description="Nice place",
        location="Wuse",
        price=50000000,
        listing_type="SALE",
        category=category,
        owner_profile=profile
    )
    Property.objects.create(
        title="Test Property 2",
        description="Another place",
        location="Gwarinpa",
        price=75000000,
        listing_type="RENT",
        category=category,
        owner_profile=profile
    )

    response = client.get("/api/v1/properties/")
    assert response.status_code == 200
    assert "results" in response.data
    assert "total_properties" in response.data
    assert response.data["total_properties"] == 2

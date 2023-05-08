from user.models import Expenditure, Income, User
from rest_framework import serializers
from authentication import validators
from django.core.validators import MaxValueValidator



# class UserDetailSerializer(serializers.ModelSerializer):
#     """
#     Update user profile,
#     Retrieve user detail,
#     Delete user
#     """

#     id = serializers.CharField(read_only=True)
#     firstname = serializers.CharField(max_length=100, required=True, validators=[validators.FirstnameValidation])
#     lastname = serializers.CharField(max_length=100, required=True, validators=[validators.LastnameValidation])
#     username = serializers.CharField(max_length=100, validators=[validators.UsernameValidation])
#     email = serializers.CharField(read_only=True)
#     # username = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=User.objects.all(), message="This username is taken")])

#     class Meta:
#         model = User
#         fields = [
#             "id",
#             "firstname",
#             "lastname",
#             "username",
#             "email",
#         ]

#     def update(self, instance, validated_data):
#         instance.firstname = validated_data.get("firstname")
#         instance.lastname = validated_data.get("lastname")
#         instance.username = validated_data.get("username")

#         instance.save()
#         return instance


class IncomeSerializer(serializers.ModelSerializer):
    nameOfRevenue = serializers.CharField(max_length=100, required = True,
        error_messages={
            "blank": "Please provide name of revenue",
            "required": "Please provide name of revenue",
            })
    amount = serializers.IntegerField(required=False, validators=[MaxValueValidator(9999999999)],
        error_messages={
            "required": "Please provide an amount",
            "invalid": "Please provide a valid amount",
            })

    class Meta:
        model = Income
        fields = [
            "id",
            "nameOfRevenue",
            "amount",
        ]

    def __init__(self, *args, **kwargs):
        required_fields = kwargs.pop('required_fields', ['nameOfRevenue'])
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in required_fields:
                field.required = False


    def create(self, validated_data):
        income = Income.objects.create(**validated_data)
        return income  

  
class ExpenditureSerializer(serializers.ModelSerializer):
    Category = (
        ("food", "Food"),
        ("transportation", "Transportation"),
        ("dress", "Dress"),
        ("fuel", "Fuel")
    )
    nameOfItem = serializers.CharField(max_length=100, required = True,
        error_messages={
            "blank": "Please provide name of item",
            "required": "Please provide name of item",
            })
    category = serializers.ChoiceField(required = True, choices = Category,
        error_messages={
            "required": "Please provide category choice",
            "invalid_choice": "Invalid category choice"
            })
    estimatedAmount = serializers.IntegerField(default=0, validators=[MaxValueValidator(9999999999)],
    error_messages={
            "required": "Please provide an amount",
            "invalid": "Please provide a valid amount",
            })

    class Meta:
        model = Income
        fields = [
            "id",
            "nameOfItem",
            "category",
            "estimatedAmount",
        ]

    def __init__(self, *args, **kwargs):
        # Get the `required_fields` keyword argument, defaulting to all fields
        required_fields = kwargs.pop('required_fields', ['nameOfItem', 'category'])
        super().__init__(*args, **kwargs)
        # Set `required` to False for fields not listed in `required_fields`
        for field_name, field in self.fields.items():
            if field_name not in required_fields:
                field.required = False

    def create(self, validated_data):
        expenditure = Expenditure.objects.create(**validated_data)
        return expenditure
        
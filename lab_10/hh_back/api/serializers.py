# from rest_framework import serializers
# from .models import Company, Vacancy

# class CompanySerializer (serializers.ModelSerializer):
#     class Meta:
#         model = Company
#         field = ['id','name', 'description', 'city','address']

# class VacancySerializer(serializers.ModelSerializer):
#     company_name =serializers.ReadOnlyField(source = 'company.name')

#     class Meta:
#         model = Vacancy
#         field = ['id','name', 'description','salary', 'company', 'company_name']

# api/serializers.py



# from rest_framework import serializers
# from .models import Company, Vacancy

# class CompanySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Company
#         fields = ['id', 'name', 'description', 'city', 'address']

# class VacancySerializer(serializers.ModelSerializer):
#     company_name = serializers.ReadOnlyField(source='company.name')

#     class Meta:
#         model = Vacancy
#         fields = ['id', 'name', 'description', 'salary', 'company', 'company_name']



from rest_framework import serializers
from .models import Company, Vacancy



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'description', 'city', 'address']

class VacancySerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField(source='company.name')

    class Meta:
        model = Vacancy
        fields = ['id', 'name', 'description', 'salary', 'company', 'company_name']
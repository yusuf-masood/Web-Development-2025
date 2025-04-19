# from django.shortcuts import render
# from rest_framework import generics
# from .models import Company, Vacancy
# from .serializers import CompanySerializer, VacancySerializer

# class CompanyListAPIView(generics.ListAPIView):
#     queryset = Company.objects.all() 
#     serializer_class = CompanySerializer

# class CompanyDetailAPIView(generics.RetrieveAPIView):
#     queryset = Company.objects.all() 
#     serializer_class = CompanySerializer

# class CompanyVacancyAPIView(generics.ListAPIView):
#     serializer_class = VacancySerializer

#     def get_queryset(self):
#         Company_id = self.kwargs['id']
#         return Vacancy.objects.filter(Company_id = Company_id)
        
# class VacancyListAPIView(generics.ListAPIView):
#     queryset = Vacancy.objects.all() 
#     serializer_class = VacancySerializer

# class VacancyDetailAPIView(generics.RetrieveAPIView):
#     queryset = Vacancy.objects.all() 
#     serializer_class = VacancySerializer

# class TopTenVacanciesAPIView(generics.ListAPIView):
#     queryset = Vacancy.objects.order_by('-salary')[:10]
#     serializer_class = VacancySerializer


# api/views.py
from rest_framework import generics
from .models import Company, Vacancy
from .serializers import CompanySerializer, VacancySerializer

class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetailAPIView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyVacanciesAPIView(generics.ListAPIView):
    serializer_class = VacancySerializer

    def get_queryset(self):
        company_id = self.kwargs['id']
        return Vacancy.objects.filter(company_id=company_id)

class VacancyListAPIView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacancyDetailAPIView(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class TopTenVacanciesAPIView(generics.ListAPIView):
    queryset = Vacancy.objects.order_by('-salary')[:10]
    serializer_class = VacancySerializer

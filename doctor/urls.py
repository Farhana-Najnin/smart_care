from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views
router=DefaultRouter() #amader router

router.register('list',views.DoctorViewset) #router er antena create 
router.register('specialization',views.SpecializationViewset) #router er antena create 
router.register('designation',views.DesignationViewset) #router er antena create 
router.register('available_time',views.AvailableTimeViewset) #router er antena create 
router.register('review',views.ReviewViewset) #router er antena create 
urlpatterns=[
    path('',include(router.urls)),
]
from django.contrib import admin
from django.urls import path,include
from.import views
from .import cron


urlpatterns = [
    #app API's
    path("tankdata",views.tankdata,name="tankdata"),
    path("temperaturedata",views.temperaturedata,name="temperaturedata"),
    path("ph_tdsdata",views.ph_tdsdata,name="ph_tdsdata"),
    path("all_weekly_data",views.all_weekly_data,name="all_weekly_data"),
    path("lights_data",views.lights_data,name="lights_data"),
    path("delete_alldata",views.delete_alldata,name="delete_alldata"),


    


    
  ]
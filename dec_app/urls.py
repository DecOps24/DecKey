



from django.urls import path

from dec_app import views

urlpatterns = [

    path('', views.homepage, name="homepage"),
    path('loginpage', views.loginpage, name="loginpage"),
    path('userpage', views.userpage, name="userpage"),
    path('add_details', views.add_details, name="add_details"),


    # add staff

    path('add_staff', views.add_staff, name="add_staff"),

    # view staff
    path("view_staff",views.view_staff,name="view_staff"),

    # party


    path("add_party",views.add_party,name="add_party"),
    path("view_party",views.view_party,name="view_party"),


    path('view_details', views.view_details, name="view_details"),
    path('logout_view', views.logout_view, name="logout_view"),
    path('download-row-pdf/<int:id>/', views.download_bill, name='download_row_pdf')
]

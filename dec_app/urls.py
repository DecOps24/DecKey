



from django.urls import path

from dec_app import views

urlpatterns = [

    path('', views.homepage, name="homepage"),
    path('sign-in/', views.loginpage, name="sign-in"),
    path('userpage', views.userpage, name="userpage"),
    path('add_details', views.add_details, name="add_details"),


    # add staff

    path('add_staff', views.add_staff, name="add_staff"),

    # view staff
    path("view_staff",views.view_staff,name="view_staff"),
    path("delete_staff/<int:id>/",views.delete_staff,name="delete_staff"),

    # party


    path("add_party",views.add_party,name="add_party"),
    path("view_party",views.view_party,name="view_party"),


    path('view_details', views.view_details, name="view_details"),
    path("details_edit/<int:id>/",views.details_edit,name="details_edit"),
    path('logout_view', views.logout_view, name="logout_view"),
    path('download-row-pdf/<int:id>/', views.download_bill, name='download_row_pdf')
]

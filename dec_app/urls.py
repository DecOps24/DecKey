



from django.urls import path

from dec_app import views

urlpatterns = [

    path('', views.homepage, name="homepage"),
   

    
   
    path('add_details', views.add_details, name="add_details"),


    # add staff

    path('add_staff', views.add_staff, name="add_staff"),

    # view staff
    path('sign-in/', views.loginpage, name="sign-in"),
    path('dashboard/', views.userpage, name="dashboard"),
    path("staffs/",views.view_staff,name="staffs"),
    path("parties/",views.view_party,name="parties"),
    path("party-form/",views.add_party,name="party-form"),
    path('work-details/', views.view_details, name="work-details"),
    path('single-detials/<int:id>/', views.single_detials, name="single-detials"),

    path("delete_staff/<int:id>/",views.delete_staff,name="delete_staff"),

    # party


    
    


    
    path("details_edit/<int:id>/",views.details_edit,name="details_edit"),
    path('logout_view', views.logout_view, name="logout_view"),
    path('download-row-pdf/<int:id>/', views.download_bill, name='download_row_pdf')
]

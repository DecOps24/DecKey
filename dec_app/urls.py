



from django.urls import path

from dec_app import views

urlpatterns = [
   path('sign-in/', views.loginpage, name="sign-in"),
   path('dashboard/', views.userpage, name="dashboard"),
   path("staffs/",views.view_staff,name="staffs"),
   path('staff-form/', views.add_staff, name="staff-form"),
   path("parties/",views.view_party,name="parties"),
   path("party-form/",views.add_party,name="party-form"),
   path('work-details/', views.view_details, name="work-details"),
   path('single-details/<int:id>/', views.single_detials, name="single-details"),
   path("edit-details/<int:id>/",views.details_edit,name="edit-details"),
   path('work-form/', views.add_details, name="work-form"),
   path('sign-out/', views.logout_view, name="sign-out"),


    path("delete_staff/<int:id>/",views.delete_staff,name="delete_staff"),

    # party


    
    


    
    
    
    path('download-row-pdf/<int:id>/', views.download_bill, name='download_row_pdf')
]

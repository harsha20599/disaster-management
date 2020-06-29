from django.urls import path
from django.contrib import admin
from views import govt_page,alert,adddata,govtadmin,index,index_post,forgot

urlpatterns = [
    
    path('', index,),
    path('main/',index_post,),
    path('login/',govt_page,name="govtlogin"),
    path('login/forgotpassword',forgot),
    path('login/alert/',alert,name="alert"),
    path('login/newdata/',adddata,name="newdata"),
    path('login/addgovt/',govtadmin,name="addgovt"),
   # path('',govt_loggiedin,)
]

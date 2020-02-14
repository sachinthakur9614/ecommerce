


from django.urls import path

from accounts.api.views import(

	resgistration_view


	)
api_name = "accounts"

urlpatterns = [
		
		path('',resgistration_view,name="register"),

]
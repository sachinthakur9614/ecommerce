

from rest_framework import serializers
from accounts.models import Accounts


class RegistrationSerializer(serializers.ModelSerializer):

	password_confirm  = serializers.CharField(style={'input_type':'password'},write_only = True)
	class Meta:
		model = Accounts
		fields =  ['email','username','password','password_confirm','first_name','last_name','country']
		extra_kwargs = {
			'password':{'write_only':True}
		}
	def save(self):
		account = Account(email = self.validated_data['email'],
			username = self.validated_data['username'],
			first_name= self.validated_data['first_name'],
			last_name = self.validated_data['last_name'],
			country = self.validated_data['country']
			)
		password = self.validated_data['password']
		password_confirm = self.validated_data['password_confirm']
		if password != password_confirm:
			raise serializers.ValidationError({'password':'Passowrd must match.'})
		account.set_password(password)
		account.save()
		return account

from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import exceptions
from .models import Opportunities

class OppSerializer(serializers.ModelSerializer):

	class Meta:
		model = Opportunities
		fields = [
			"id",
			"title",
			"summary",
		]

class LoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()

	def validate(self, data):
		username = data.get("username", "")
		password = data.get("password", "")

		if username and password:
			user = authenticate(username=username, password=password)
			if user:
				if user.is_active:
					data["user"] = user
				else:
					msg = "User is deactivated"
					raise exceptions.ValidationError(msg)
			else:
				msg = "Invalid Credentials, Try again"
				raise exceptions.ValidationError(msg)


		else:
			msg = "Please enter correct username and password"
			raise exceptions.ValidationError(msg)
		return data

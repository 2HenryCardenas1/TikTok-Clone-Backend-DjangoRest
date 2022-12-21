from rest_framework import serializers
from users.models import User

# Un serializer se usa para definir que datos mostrar de la peticion a la base de datos


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']

    # create is a method of the serializer class
    def create(self, validated_data):
        # Encriptacion de la contraseña
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

# This serializer is used to show the data of the user in the petition to the database


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'website',
                  'instagram', 'avatar', 'description', 'first_name', 'date_joined']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'website', 'instagram',
                  'avatar', 'description', 'first_name']

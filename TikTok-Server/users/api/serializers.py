from rest_framework import serializers
from users.models import User

#Un serializer se usa para definir que datos mostrar de la peticion a la base de datos

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ['id','username', 'password', 'email', 'first_name','last_name']


    def create(self, validated_data):
        #Encriptacion de la contraseña
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
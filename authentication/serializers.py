from rest_framework import serializers
from django.contrib.auth.models import User

from django.core.validators import RegexValidator

class UserSerializer(serializers.ModelSerializer):
    # em register (matricula), coloquei como string e uso um validador de expressoes regulares para verificar se o campo
    # esta apenas com digitos inteiros
    username=serializers.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    first_name=serializers.CharField(max_length=255, min_length=4)
    last_name=serializers.CharField(max_length=255, min_length=4)
    email=serializers.CharField(max_length=255, min_length=4)
    password=serializers.CharField(max_length=40, min_length=8, write_only=True)
    is_student=serializers.BooleanField(default=True)
    
    class Meta:
        model=User
        # fields eh a informacao a ser vista no Response
        # fields=['register', 'first_name', 'last_name', 'email']
        fields=['username', 'first_name', 'last_name', 'email', 'password', 'is_student']
    
    '''
    O rest framework possui tres maneiras de realizar a validacao de dados com serializadores.
    Utilizando a opcao de validacao de instancia (objeto), podemos usar o metodo validate() que ira transformar 
    o objeto e retornara a instancia da model (caso os dados sejam validados), se nao, chamara um erro do tipo ValidationError.
    '''
    def validate(self, attrs): # o argumento attrs na funcao representa o dado que esta sendo enviado
        email_field = attrs.get('email', '') # email como um parametro opcional assim podendo vir vazio no corpo do response
        if User.objects.filter(email=email_field).exists(): # verifica se o email ja existe
            raise serializers.ValidationError({'email': ('Email is already in use.')}) # caso exista ja um email, ele faz um error handler e retorna um feedback
        return super().validate(attrs)
    
    '''
    Cria a instancia da model (basicamente cria o User)
    '''
    def create(self, validated_data):
        return User.objects.create_user(**validated_data) # ** separa os dados em campos diferentes do response
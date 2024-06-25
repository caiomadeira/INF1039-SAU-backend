from rest_framework import serializers
from student.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['username', 'name', 'password']
    
    '''
    O rest framework possui tres maneiras de realizar a validacao de dados com serializadores.
    Utilizando a opcao de validacao de instancia (objeto), podemos usar o metodo validate() que ira transformar 
    o objeto e retornara a instancia da model (caso os dados sejam validados), se nao, chamara um erro do tipo ValidationError.
    '''
    def validate(self, attrs):
        username_field = attrs.get('username', '')
        if Student.objects.filter(username=username_field).exists():
            raise serializers.ValidationError({'username': ('Matricula em uso.')}) # caso exista ja um email, ele faz um error handler e retorna um feedback

    '''
    Cria a instancia da model (basicamente cria o User)
    '''
    def create(self, validated_data):
        return Student.objects.create_user(**validated_data) # ** separa os dados em campos diferentes do response
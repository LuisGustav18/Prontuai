from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Medicos(models.Model):

    nome = models.CharField(
        max_length=200,
        verbose_name='Nome',
        help_text='Nome da medico',
    )

    telefone = models.CharField(
        max_length=11,
        verbose_name='Telefone',
        help_text='Ex: XXXXXX-XXXX',
    )

    email = models.EmailField(
        max_length=100,
        verbose_name='Email',
        help_text='Email da medico',
        unique=True,
        blank=True,
    )

    data_nascimento = models.DateField(
        verbose_name='Data de nascimento',
        help_text='Data de nascimento',
    )

    cpf = models.CharField(
        max_length=11,
        verbose_name='CPF',
        help_text='EX: XXXXXXXXX',
        unique=True,
    )

    status = models.CharField(
        max_length=10,
        choices=[
            ('Ativo', 'Ativo'),
            ('inativo', 'inativo')
        ],
        verbose_name='Status',
        help_text='Status do medico',
        default='Ativo'
    )

    crm = models.CharField(
        max_length=13,
        verbose_name='CRM',
        help_text='Ex: CRM/UF XXXXXX',
        unique=True,
    )


    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em',
        help_text='Data de criação',
    )

    atualizado_em = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em',
        help_text='Data de atualização',
    )

    def clean(self):
        super().clean()

        if len(self.nome) < 3:
            raise ValidationError("O nome precisa ser maior")

        if not self.nome.replace(" ", "").isalpha():
            raise ValidationError("O nome não pode ter numeros")

        ddd = [11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 27, 28, 31, 32, 33, 34, 35, 37, 38, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 53, 54, 55, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 73, 74, 75, 77, 79, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99]

        if len(self.telefone) < 10 or len(self.telefone) > 11 or self.telefone.isnumeric() != True or int(self.telefone[0:2]) not in ddd:
            raise ValidationError("O telefone invalido")

        idade = (timezone.now().date().year- self.data_nascimento.year)

        if idade < 18 or idade > 140 :
            raise ValidationError("Idade invalida")

        if not self.cpf.isnumeric() or len(self.cpf) != 11:
            raise ValidationError("CPF invalido")

        estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

        if self.crm[4:6].upper() not in estados or not self.crm[7:13].isnumeric():
            raise ValidationError("O crm invalido")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'


class SetorAtuacao(models.Model):
    nome = models.CharField(
        max_length=120,
        verbose_name='Nome',
        help_text='Setor de atuação',
        unique=True,
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em',
        help_text='Data de criação',
    )

    atualizado_em = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em',
        help_text='Data de atualização',
    )

    def clean(self):
        super().clean()

        if len(self.nome) < 3:
            raise ValidationError("O nome precisa ser maior")

        if not self.nome.replace(" ", "").isalpha():
            raise ValidationError("O nome não pode ter numeros")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Setor Atuação'
        verbose_name_plural = 'Setores Atuação'

class Enfermeiro(models.Model):

    nome = models.CharField(
        max_length=200,
        verbose_name='Nome',
        help_text='Nome da enfermeiro',
    )

    coren = models.CharField(
        unique=True,
        max_length=20,
        help_text='Coren do enfermeiro',
        verbose_name='Ex: Coren-UF XXXXXX-Categoria',
    )

    atuacao = models.ForeignKey(
        SetorAtuacao,
        on_delete=models.RESTRICT,
        verbose_name='Setor',
        help_text='Atuação do enfermeiro',
    )

    telefone = models.CharField(
        max_length=11,
        verbose_name='Telefone',
        help_text='Ex: XXXXXX-XXXX',
    )

    email = models.EmailField(
        max_length=100,
        verbose_name='Email',
        help_text='Email do enfermeiro',
        unique=True,
        blank=True,
    )

    data_nascimento = models.DateField(
        verbose_name='Data de nascimento',
        help_text='Data de nascimento',
    )

    cpf = models.CharField(
        max_length=11,
        verbose_name='CPF',
        help_text='EX: XXXXXXXXX',
        unique=True,
    )

    turno = models.CharField(
        max_length=10,
        choices=[
            ('Manhã', 'Manhã'),
            ('Tarde', 'Tarde'),
            ('Noite', 'Noite'),
            ('Integral', 'Integral'),
        ],
        verbose_name='Turno',
        help_text='Turno do enfermeiro'
    )

    status = models.CharField(
        max_length=10,
        choices=[
            ('Ativo', 'Ativo'),
            ('inativo', 'inativo')
        ],
        verbose_name='Status',
        help_text='Status do enfermeiro',
        default='Ativo'
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em',
        help_text='Data de criação',
    )

    atualizado_em = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em',
        help_text='Data de atualização',
    )

    def clean(self):
        super().clean()

        if len(self.nome) < 3:
            raise ValidationError("O nome precisa ser maior")

        if not self.nome.replace(" ", "").isalpha():
            raise ValidationError("O nome não pode ter numeros")

        ddd = [11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 27, 28, 31, 32, 33, 34, 35, 37, 38, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 53, 54, 55, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 73, 74, 75, 77, 79, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99]

        if len(self.telefone) < 10 or len(self.telefone) > 11 or self.telefone.isnumeric() != True or int(self.telefone[0:2]) not in ddd:
            raise ValidationError("O telefone invalido")

        idade = (timezone.now().date().year- self.data_nascimento.year)

        if idade < 18 or idade > 140 :
            raise ValidationError("Idade invalida")

        if not self.cpf.isnumeric() or len(self.cpf) != 11:
            raise ValidationError("CPF invalido")

        categorias = ['ENF', 'TE', 'AE', 'EE', 'RES', 'ENFESF', 'TENFESF', 'ENFURG', 'ENFADM', 'ENFOB', 'ENFPSI','ENFPED', 'ENFINT', 'ENFVIS']

        estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

        if self.coren[6:8].upper() not in estados or self.coren[16:].upper() not in categorias or self.coren[9:15].isnumeric() != True:
            raise ValidationError("O coren invalido")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Enfermeiro'
        verbose_name_plural = 'Enfermeiros'


class Paciente(models.Model):

    nome = models.CharField(
        max_length=200,
        verbose_name='Nome',
        help_text='Nome do paciente',
    )

    data_nascimento = models.DateField(
        verbose_name='Data de nascimento',
        help_text='Data de nascimento',
    )

    sexo = models.CharField(
        max_length=10,
        choices=[
            ('Masculino', 'Masculino'),
            ('Femenino', 'Femenino'),
            ('Outro', 'Outro')
        ],
        verbose_name='Sexo',
        help_text='Sexo do paciente'
    )

    cpf = models.CharField(
        max_length=11,
        verbose_name='CPF',
        help_text='EX: XXXXXXXXX',
        unique=True,
    )

    rg = models.CharField(
        max_length=9,
        verbose_name='RG',
        help_text='RG do paciente',
        unique=True,
    )

    nome_mae = models.CharField(
        max_length=200,
        verbose_name='Nome mae',
        help_text='Nome da mae',
    )

    nome_pai = models.CharField(
        max_length=200,
        verbose_name='Nome pai',
        help_text='Nome da pai',
        blank=True,
    )

    telefone_principal = models.CharField(
        max_length=11,
        verbose_name='Telefone',
        help_text='Ex: XXXXXX-XXXX',
        unique=True
    )

    telefone_segundario = models.CharField(
        max_length=11,
        verbose_name='Telefone Segundario',
        help_text='Ex: XXXXXX-XXXX',
        blank=True,
    )

    email = models.EmailField(
        max_length=100,
        verbose_name='Email',
        help_text='Email do paciente',
        unique=True,
        blank=True,
    )

    tipo_sanguineo = models.CharField(
        max_length=3,
        choices=[
            ('A⁺', 'A⁺'),
            ('A⁻', 'A⁻'),
            ('B⁺', 'B⁺'),
            ('B⁻', 'B⁻'),
            ('AB⁺', 'AB⁺'),
            ('AB⁻', 'AB⁻'),
            ('O⁺', 'O⁺'),
            ('O⁻', 'O⁻')
        ],
        blank=True,
        verbose_name='Tipo Sanguineo',
        help_text='Tipo Sanguineo do paciente',
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em',
        help_text='Data de criação',
    )

    atualizado_em = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em',
        help_text='Data de atualização',
    )

    def clean(self):
        super().clean()

        if len(self.nome) < 3:
            raise ValidationError("O nome precisa ser maior")

        if not self.nome.replace(" ", "").isalpha():
            raise ValidationError("O nome não pode ter numeros")

        if len(self.nome_mae) < 3:
            raise ValidationError("O nome da mãe precisa ser maior")

        if not self.nome_mae.replace(" ", "").isalpha():
            raise ValidationError("O nome da mãe não pode ter numeros")

        if self.nome_pai:
            if len(self.nome_pai) < 3:
                raise ValidationError("O nome do pai precisa ser maior")

            if not self.nome_pai.replace(" ", "").isalpha():
                raise ValidationError("O nome do pai não pode ter numeros")

        ddd = [11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 27, 28, 31, 32, 33, 34, 35, 37, 38, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 53, 54, 55, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 73, 74, 75, 77, 79, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99]

        if len(self.telefone_principal) < 10 or len(self.telefone_principal) > 11 or self.telefone_principal.isnumeric() != True or int(self.telefone_principal[0:2]) not in ddd:
            raise ValidationError("O telefone invalido")

        if self.telefone_segundario:
            if len(self.telefone_segundario) < 10 or len(self.telefone_segundario) > 11 or self.telefone_segundario.isnumeric() != True or int(self.telefone_segundario[0:2]) not in ddd:
                raise ValidationError("O telefone segundario invalido")

        idade = (timezone.now().date().year - self.data_nascimento.year)

        if idade < 0 or idade > 140 :
            raise ValidationError("Idade invalida")

        if not self.cpf.isnumeric() or len(self.cpf) != 11:
            raise ValidationError("CPF invalido")

        if not self.rg.isnumeric() or len(self.rg) < 7 or len(self.rg) > 9 :
            raise ValidationError("RG invalido")

    def __srt__(self):
        return self.nome

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

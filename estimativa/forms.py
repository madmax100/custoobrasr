from django import forms
from .models import ProjPadrao

class ProjPadraoForm(forms.ModelForm):
    choicesTipo= (('1', 'Residencial'),('2', 'Comercial'),('3', 'Industrial'),)
    choicesPadrao= (('1', 'Baixo'),('2', 'Normal'),('3', 'Alto'),)
    choicesEstado=(
        ('AC', 'Acre'), 
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranão'),
        ('MG', 'Minas Gerais'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernanbuco'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
        ('TO', 'Tocantins')
    )
    estado=forms.ChoiceField(choices=choicesEstado,widget=forms.Select())
    tipo=forms.ChoiceField(choices=choicesTipo,widget=forms.RadioSelect())
    area=forms.DecimalField()
    num_pavimentos=forms.IntegerField()
    padrao=forms.ChoiceField(choices=choicesPadrao,widget=forms.RadioSelect())
    
    class Meta:
        model = ProjPadrao
        fields = ['tipo', 'area', 'num_pavimentos', 'padrao']

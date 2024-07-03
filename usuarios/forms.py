from django import forms

from django.contrib.auth.models import User

from django.core.exceptions import ValidationError

class LoginForms(forms.Form):
    nome_login=forms.CharField(
            label='Usuário', 
            required=True, 
            max_length=100,
            widget=forms.TextInput( 
                     attrs={
                        "class": "input-normal",
                        "placeholder": "seuuser"

                    }
             )
        )
    senha=forms.CharField(
             label='Senha', 
             required=True, 
             max_length=70,
               widget=forms.PasswordInput( 
                     attrs={
                        "class": "input-normal",
                         "placeholder": "suasenha123"

                     }
             )
                
    )
        
class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'seu nome de usuario',
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': '',
                'placeholder': 'Ex.: seuemail@.email.com',
            }
        )
    )
    senha_1 = forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': '',
                'placeholder': 'Digite sua senha',
            }
        ),
    )
    senha_2 = forms.CharField(
        label='Confirmar Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': '',
                'placeholder': 'Digite sua senha novamente',
            }
        ),
    )

    def clean_senha_1(self):
        senha_1 = self.cleaned_data.get('senha_1')
        if len(senha_1) < 8:
            raise ValidationError("A senha deve ter no mínimo 8 caracteres.")
        return senha_1

    def clean_senha_2(self):
        senha_2 = self.cleaned_data.get('senha_2')
        if len(senha_2) < 8:
            raise ValidationError("A senha deve ter no mínimo 8 caracteres.")
        return senha_2

    def clean(self):
        cleaned_data = super().clean()
        senha_1 = cleaned_data.get("senha_1")
        senha_2 = cleaned_data.get("senha_2")

        if senha_1 and senha_2 and senha_1 != senha_2:
            raise ValidationError("As senhas não coincidem.")

        return cleaned_data
        
    
        
                
            
      
class PasswordResetForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('Nenhum usuário encontrado com este e-mail.')
        return email
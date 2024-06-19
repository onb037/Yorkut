from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
            label='Nome de Login', 
            required=True, 
            max_length=100,
            widget=forms.TextInput( 
                     attrs={
                        "class": "form-control",
                        "placeholder": "Ex.: seuemail@email.com"

                    }
             )
        )
    senha=forms.CharField(
             label='Senha', 
             required=True, 
             max_length=70,
               widget=forms.PasswordInput( 
                     attrs={
                        "class": "form-control",
                         "placeholder": "Ex.: suasenha123"

                     }
             )
                
    )
        
class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome de Cadastro', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: seu nome de usuario',
            }
        )
    )
    email=forms.EmailField(
        label='Seu Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: seuemail@.email.com',
            }
        )
    )
    senha_1=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        ),
    )
    senha_2=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha novamente',
            }
        ),
    )
        
    
        
                
            

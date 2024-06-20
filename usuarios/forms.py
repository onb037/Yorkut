from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
            label='Email', 
            required=True, 
            max_length=100,
            widget=forms.TextInput( 
                     attrs={
                        "class": "input-normal",
                        "placeholder": "seuemail@email.com"

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
    nome_cadastro=forms.CharField(
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
    email=forms.EmailField(
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
    senha_1=forms.CharField(
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
    senha_2=forms.CharField(
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
        
    
        
                
            

password = input('''\nDigite uma senha. By Hygor Rasec
=====================================================================
- A senha deve conter no mínimo 6 caracteres e máximo 12 caracteres;
- A senha deve ter pelo menos 1 letra minúscula entre [az] e 1 letra maiúscula entre [AZ];
- A senha deve ter pelo menos 1 número entre [0-9];
- A senha deve ter pelo menos 1 caractere especial [$#@].
=====================================================================
Digite a senha aqui: ''')

int_check = upper_check = lower_check = spec_check = spec_check_temp = 0
spec_caracter = '$#@'

for s in password:
    try:
        int(s)
        int_check = 1
    except ValueError:
        for e in spec_caracter:
            if e == s:
                spec_check = 1
                spec_check_temp = 1

        if s == s.upper() and spec_check_temp == 0 and upper_check != 1:
            upper_check = 1
        elif s == s.lower() and spec_check_temp == 0 and lower_check != 1:
            lower_check = 1

        spec_check_temp = 0

if len(password) >= 6 or len(password) <= 12:
    if upper_check and lower_check:
        if int_check:
            if spec_check:
                print('Senha cadastrada com sucesso!')
            else:
                print(
                    f'A senha deve ter pelo menos 1 caractere especial [{spec_caracter}]. Por favor, tente novamente.')
        else:
            print(
                'A senha deve ter pelo menos 1 número entre [0-9]. Por favor, tente novamente.')
    else:
        print(
            'A senha deve ter pelo menos 1 letra minúscula entre [az] e 1 letra maiúscula entre [AZ]. Por favor, tente novamente.')
else:
    print('A senha precisa ter o mínimo de 6 caracteres e máximo de 12 caracteres. Por favor, tente novamente.')

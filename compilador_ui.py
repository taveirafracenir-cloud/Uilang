# compilador_ui.py

variaveis = {}

def interpretar_linha(linha):
    linha = linha.strip()

    # Ignora linhas vazias ou comentários
    if not linha or linha.startswith("#"):
        return

    # Criar variável
    if linha.startswith("VAR "):
        # Exemplo: VAR nome = "Enzo"
        partes = linha[4:].split("=", 1)
        if len(partes) == 2:
            nome_var = partes[0].strip()
            valor = partes[1].strip()
            # Detecta números ou strings
            if valor.startswith('"') and valor.endswith('"'):
                valor = valor[1:-1]
            else:
                try:
                    valor = int(valor)
                except ValueError:
                    try:
                        valor = float(valor)
                    except ValueError:
                        pass  # mantém como string
            variaveis[nome_var] = valor
        return

    # Mostrar valor
    if linha.startswith("MOSTRAR "):
        # Exemplo: MOSTRAR nome
        expr = linha[8:].strip()
        if expr in variaveis:
            print(variaveis[expr])
        else:
            print(expr)  # mostra direto se não for variável
        return

# Função principal para interpretar múltiplas linhas
def interpretar_codigo(codigo):
    for linha in codigo.split("\n"):
        interpretar_linha(linha)

# --- Exemplo de uso ---
codigo_exemplo = """
# Criando variáveis
VAR nome = "Enzo"
VAR idade = 17
VAR altura = 1.72

# Mostrando valores
MOSTRAR nome
MOSTRAR idade
MOSTRAR altura
MOSTRAR "Isso é um texto direto"
"""

interpretar_codigo(codigo_exemplo)

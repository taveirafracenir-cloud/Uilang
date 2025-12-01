# compilador_ui_v2.py
# ==============================================
# Compilador inicial da linguagem de interface gigante
# Suporta:
#   - Variáveis (strings e números)
#   - Mostrar valores
#   - Interpretação linha a linha
# ==============================================

# Dicionário para armazenar todas as variáveis
variaveis = {}  # Aqui guardamos o nome da variável e o seu valor

# ----------------------------------------------
# Função que interpreta uma linha da linguagem
# ----------------------------------------------
def interpretar_linha(linha):
    linha = linha.strip()  # Remove espaços extras do início e fim

    # Ignora linhas vazias ou comentários
    if not linha or linha.startswith("#"):
        # Comentários começam com #
        return

    # -----------------------------
    # Parte 1: Criar variáveis
    # -----------------------------
    if linha.startswith("VAR "):
        # Exemplo de linha: VAR nome = "Enzo"
        # Passo 1: remover o "VAR " e separar em nome e valor
        partes = linha[4:].split("=", 1)  # split no primeiro "="
        if len(partes) == 2:
            nome_var = partes[0].strip()  # nome da variável
            valor = partes[1].strip()     # valor atribuído

            # Detecta se é string ou número
            if valor.startswith('"') and valor.endswith('"'):
                # É uma string, remove aspas
                valor = valor[1:-1]
            else:
                # Tenta converter para número inteiro
                try:
                    valor = int(valor)
                except ValueError:
                    # Se não der, tenta converter para float
                    try:
                        valor = float(valor)
                    except ValueError:
                        # Se não for número, mantém como texto
                        pass

            # Armazena a variável no dicionário
            variaveis[nome_var] = valor
        return  # fim do tratamento de variável

    # -----------------------------
    # Parte 2: Mostrar valores
    # -----------------------------
    if linha.startswith("MOSTRAR "):
        # Exemplo: MOSTRAR nome
        expr = linha[8:].strip()  # pega o que vem depois de MOSTRAR
        if expr in variaveis:
            # Se for variável existente, imprime o valor
            print(variaveis[expr])
        else:
            # Senão, imprime o texto diretamente
            print(expr)
        return  # fim do mostrar

    # -----------------------------
    # Parte 3: Comandos extras
    # -----------------------------
    # Aqui você pode adicionar milhares de outros comandos
    # Por exemplo: BOTAO, TEXTO, IMAGEM, AO_CLICAR, etc.
    # Cada comando pode ter seu próprio bloco de interpretação
    # Exemplo genérico:
    if linha.startswith("BOTAO "):
        # Aqui você poderia criar um botão na interface
        print(f"[BOTAO CRIADO: {linha[6:].strip()}]")  # placeholder
        return

    # Se chegar aqui, é um comando desconhecido
    print(f"[COMANDO DESCONHECIDO]: {linha}")

# ----------------------------------------------
# Função para interpretar código inteiro
# ----------------------------------------------
def interpretar_codigo(codigo):
    """
    Recebe várias linhas de código da linguagem e interpreta linha por linha.
    """
    for linha in codigo.split("\n"):
        interpretar_linha(linha)

# ----------------------------------------------
# Exemplo de uso do compilador
# ----------------------------------------------
codigo_exemplo = """
# ==============================
# Criando variáveis
# ==============================
VAR nome = "Enzo"
VAR idade = 17
VAR altura = 1.72

# ==============================
# Mostrando valores
# ==============================
MOSTRAR nome
MOSTRAR idade
MOSTRAR altura
MOSTRAR "Isso é um texto direto"

# ==============================
# Comando de botão (exemplo futuro)
# ==============================
BOTAO "Entrar"
"""

# Executa o interpretador
interpretar_codigo(codigo_exemplo)

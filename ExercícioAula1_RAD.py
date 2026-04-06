from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() #Criando aplicaçãoi

class CalculoEntrada(BaseModel):
    a: float
    b: float
    operacao: str

@app.post("/calcular")
def realizar_calculo(dados: CalculoEntrada):
    num1 = dados.a
    num2 = dados.b
    op = dados.operacao.lower()

    if op == "soma":
        resultado = num1 + num2
    elif op == "subtracao":
        resultado = num1 - num2
    elif op == "multiplicacao":
        resultado = num1 * num2
    elif op == "divisao":
        if num2 == 0:
            return {"erro": "Não é possível dividir por zero"}
        resultado = num1 / num2
    else:
        return{"erro:" "Operação Inválida"}
    
    # O FastAPI converte esse cicionario de baixo em JSON automaticamente
    return {
        "a": num1,
        "b": num2,
        "operacao": op,
        "resultado": resultado    }
# Pydantic

Este é um exemplo simples de como usar o Pydantic para definir um modelo de dados, como temperatura, umidade, velocidade do vento e radiação solar.

## Descrição

O código consiste em uma classe chamada `ClimateParameters`, que herda de `BaseModel` do Pydantic. Essa classe define quatro campos de dados:

- `temperature`: um valor float representando a temperatura em graus Celsius.
- `humidity`: um valor float representando a umidade em porcentagem.
- `wind_speed`: um valor float representando a velocidade do vento em metros por segundo.
- `radiation`: um valor float representando a radiação solar em watts por metro quadrado.

Você pode usar esta classe para validar e serializar dados climáticos.

## Uso

Aqui está um exemplo de como usar a classe `ClimateParameters`:

```python
from pydantic import BaseModel

class ClimateParameters(BaseModel):
    temperature: float
    humidity: float
    wind_speed: float
    radiation: float

# Criando uma instância dos parâmetros climáticos
params = ClimateParameters(temperature=25.0, humidity=60.0, wind_speed=5.5, radiation=200.0)

# Acessando os valores
print("Temperatura:", params.temperature)
print("Umidade:", params.humidity)
print("Velocidade do vento:", params.wind_speed)
print("Radiação solar:", params.radiation)
```

# Gerador de dados para Modelagem Hidrológica

Este é um conjunto de funções Python que geram condições para diferentes regiões geográficas, destinadas a serem utilizadas em modelos de simulação hidrológica.

## Descrição

O código consiste em várias funções que geram condições para diferentes regiões geográficas do Brasil. Cada função corresponde a uma região específica e gera condições para um modelo hidrológico especifico com base em parâmetros estatísticos.

As regiões geográficas consideradas são:

- Norte
- Nordeste
- Centro-Oeste
- Sudeste
- Sul

As condições incluem a umidade inicial do solo e a concentração de solutos (como sais ou nutrientes) presentes no solo.

## Uso

Para gerar condições iniciais para uma região específica, basta chamar a função correspondente. Por exemplo:

```python
from gerador_condicoes_iniciais import (
    generate_initial_conditions_norte,
    generate_initial_conditions_nordeste,
    generate_initial_conditions_centro_oeste,
    generate_initial_conditions_sudeste,
    generate_initial_conditions_sul,
)

initial_conditions_norte = generate_initial_conditions_norte()
initial_conditions_nordeste = generate_initial_conditions_nordeste()
initial_conditions_centro_oeste = generate_initial_conditions_centro_oeste()
initial_conditions_sudeste = generate_initial_conditions_sudeste()
initial_conditions_sul = generate_initial_conditions_sul()

print("Condições Iniciais para a Região Norte:", initial_conditions_norte)
print("Condições Iniciais para a Região Nordeste:", initial_conditions_nordeste)
print("Condições Iniciais para a Região Centro-Oeste:", initial_conditions_centro_oeste)
print("Condições Iniciais para a Região Sudeste:", initial_conditions_sudeste)
print("Condições Iniciais para a Região Sul:", initial_conditions_sul)
```

Esse conjunto de funções geraram condições para um modelo ou simulação, novamente para diferentes regiões geográficas do país. Aqui está a explicação mais detalhada:

1. `import random`: Importa o módulo `random` para gerar números aleatórios.

2. `from models.initial_conditions import InitialConditions`: Importa a classe `InitialConditions` do módulo `models.initial_conditions`, que provavelmente representa algum tipo de estrutura de dados para armazenar condições iniciais.

3. `def generate_initial_conditions_norte():`: Define a função `generate_initial_conditions_norte()`, que gera condições iniciais para a região Norte do país.

4. `initial_moisture = max(0, round(random.gauss(0.4, 0.1), 2))`: Calcula a umidade inicial para a região Norte. Usa `random.gauss(mu, sigma)` para gerar um número aleatório seguindo uma distribuição gaussiana com média `mu` e desvio padrão `sigma`. Aqui, a média é 0.4 e o desvio padrão é 0.1. `round()` arredonda o número para 2 casas decimais e `max(0, ...)` garante que o valor não seja negativo.

5. `solute_concentration = max(0, round(random.gauss(40, 10), 2))`: Calcula a concentração de soluto para a região Norte, seguindo uma distribuição gaussiana com média 40 e desvio padrão 10.

6. `return InitialConditions(initial_moisture=initial_moisture, solute_concentration=solute_concentration)`: Retorna um objeto da classe `InitialConditions`, com a umidade inicial e a concentração de soluto geradas como argumentos.

As outras funções (`generate_initial_conditions_nordeste`, `generate_initial_conditions_centro_oeste`, `generate_initial_conditions_sudeste` e `generate_initial_conditions_sul`) seguem a mesma lógica, mas com diferentes médias e desvios padrão para representar diferentes regiões geográficas do país.

Portanto, essas funções geram dados simulados sobre as condições iniciais (umidade inicial e concentração de soluto) para diferentes regiões geográficas do país, usando distribuições gaussianas aleatórias.

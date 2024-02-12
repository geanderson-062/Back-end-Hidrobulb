# Simulação do Bulbo em Camada Superficial

A API de Simulação do Bulbo em Camada Superficial é uma ferramenta poderosa e flexível projetada para facilitar a configuração e execução de simulações precisas e detalhadas do comportamento do solo. Desenvolvida com o framework FastAPI em Python, esta API oferece acesso fácil e intuitivo a uma ampla gama de parâmetros e condições que influenciam a distribuição e movimentação da água na camada superficial do solo.

# Objetivo

O objetivo principal desta API é fornecer aos usuários os dados e informações necessários para configurar simulações da camada superficial do bulbo úmido com rapidez e precisão. Ao oferecer uma interface acessível e documentada, a API simplifica o processo de obtenção e integração de dados essenciais para a execução de simulações hidrológicas detalhadas.

## Simulações de Bulbo Úmido em Camada Superficial: Importância e Informações Necessárias

### Importância das Simulações de Bulbo Úmido em Camada Superficial

As simulações de bulbo úmido em camada superficial desempenham um papel crucial na compreensão e gestão dos recursos hídricos do solo. Aqui estão algumas razões pelas quais essas simulações são importantes:

- **Gestão da Irrigação:** Permitem otimizar o uso da água na agricultura, garantindo que as plantas recebam a quantidade adequada de água no momento certo, minimizando desperdícios e maximizando a produtividade.

- **Previsão de Inundações e Secas:** Permitem prever e mitigar eventos extremos, como inundações e secas, fornecendo informações valiosas sobre a distribuição e disponibilidade da água no solo.

- **Planejamento Urbano e Ambiental:** Auxiliam no planejamento urbano e ambiental, ajudando a determinar a melhor localização para construções e infraestruturas, levando em consideração a capacidade de infiltração do solo e o risco de inundações.

### Informações Necessárias para Iniciar uma Simulação

Para iniciar uma simulação de bulbo úmido em camada superficial, são necessárias diversas informações sobre o solo, o clima e outros fatores relevantes. Aqui estão algumas das informações mais importantes a serem consideradas:

1. **Propriedades do Solo:**

   - Textura do solo (areia, argila, etc.).
   - Condutividade hidráulica.
   - Porosidade.
   - Capacidade de campo.
   - Ponto de murcha permanente.

2. **Condições Iniciais do Solo:**

   - Umidade inicial do solo.
   - Concentração inicial de solutos (se aplicável).

3. **Condições de Contorno:**

   - Fluxo de água na superfície do solo.
   - Taxa de evaporação.
   - Precipitação.

4. **Parâmetros Climáticos:**

   - Temperatura.
   - Umidade relativa.
   - Velocidade do vento.
   - Radiação solar.

5. **Geometria do Domínio:**

   - Espessura do solo.
   - Área da superfície do solo.

6. **Intervalo de Tempo:**

   - Intervalo de tempo para a simulação.

7. **Condições de Saturação e Drenagem:**
   - Estado de saturação do solo.
   - Tipo de drenagem.

Essas informações são essenciais para garantir que a simulação seja precisa e representativa do ambiente real, fornecendo resultados úteis e confiáveis para análise e tomada de decisões.

## Importância dos Tópicos

Os sete tópicos são importantes para a simulação da camada superficial do bulbo úmido por descreverem aspectos fundamentais do sistema e do ambiente em que a simulação ocorre.

1. **Propriedades do Solo:** As propriedades do solo, como textura, condutividade hidráulica, porosidade e capacidade de retenção de água, influenciam diretamente na movimentação e retenção da água no solo. Esses dados são essenciais para modelar como a água é distribuída e retida no solo ao longo do tempo.

2. **Condições Iniciais:** Definir as condições iniciais do solo, como umidade inicial e concentração de solutos, é crucial para iniciar a simulação em um estado realista. Isso permite que a simulação comece a partir de um ponto que corresponda às condições reais do ambiente, fornecendo resultados mais precisos e significativos.

3. **Condições de Contorno:** As condições de contorno, como fluxo de água superficial, taxa de evaporação e precipitação, representam as interações do solo com seu entorno. Essas condições influenciam diretamente o comportamento do bulbo úmido, controlando as entradas e saídas de água do sistema.

4. **Parâmetros Climáticos:** Os parâmetros climáticos, como temperatura, umidade relativa, velocidade do vento e radiação solar, afetam a taxa de evaporação, transpiração e outras interações entre o solo e a atmosfera. Esses dados são cruciais para modelar os efeitos das condições climáticas na dinâmica da água no solo.

5. **Geometria do Domínio:** A geometria do domínio define a extensão espacial da simulação, incluindo a espessura do solo e a área da superfície do solo. Esses dados são essenciais para calcular volumes e fluxos de água com precisão, garantindo que a simulação represente adequadamente o ambiente físico em estudo.

6. **Intervalo de Tempo:** O intervalo de tempo utilizado na simulação determina a resolução temporal do modelo. Um intervalo de tempo adequado é crucial para capturar mudanças rápidas no sistema, garantindo que a simulação produza resultados precisos e relevantes ao longo do tempo.

7. **Condições de Saturação e Drenagem:** Descrever como a água é movimentada no solo, incluindo o estado de saturação do solo e o tipo de drenagem, é fundamental para entender a disponibilidade de água para as plantas e outros processos relacionados ao transporte de água no solo. Essas condições afetam diretamente a distribuição e a disponibilidade de água no ambiente do solo.

## Metodologia de Geração de Dados da Simulação

A API utiliza uma metodologia baseada na distribuição normal (Gaussiana) para gerar os parâmetros climáticos necessários para a simulação da camada superficial do bulbo úmido. Isso significa que os valores dos parâmetros climáticos, como temperatura, umidade relativa, velocidade do vento e radiação solar, são gerados de acordo com as características típicas da região em estudo (norte, nordeste, centro oeste, sudeste, sul).

A distribuição normal é uma distribuição estatística que é frequentemente utilizada para modelar fenômenos naturais. Ela é caracterizada por uma curva de sino, onde a maioria dos valores se concentra em torno de um valor médio (média) e se espalha simetricamente em ambas as direções em torno dessa média, de acordo com o desvio padrão.

Ao aplicar essa metodologia, a API pode simular variações realistas nos parâmetros climáticos ao longo do tempo e do espaço. Isso permite que as simulações sejam mais precisas e representativas das condições reais do ambiente em estudo.

A utilização da distribuição normal na geração de dados climáticos é uma abordagem comum e eficaz em modelagem hidrológica e meteorológica, garantindo resultados que são consistentes com as características climáticas observadas na região específica da simulação.

## Uso da API

Esta API foi projetada para simplificar o processo de configuração e execução de simulações da camada superficial do bulbo úmido no solo. Aqui está um resumo do fluxo de uso:

1. **Consulta de Endpoints:** O usuário consulta os diversos endpoints disponíveis para obter os dados necessários para a simulação, como propriedades do solo, condições iniciais, parâmetros climáticos e geometria do domínio.

2. **Recebimento de Dados:** A API retorna os dados solicitados em formato JSON, fornecendo informações detalhadas e precisas para cada aspecto da simulação.

3. **Integração com Ferramentas de Simulação:** Os dados obtidos são então utilizados para configurar simulações em software de modelagem, como o HYDRUS 3D, para análise e previsão do comportamento do solo.

4. **Análise de Resultados:** Após a simulação, os resultados são analisados ​​para entender como fatores como propriedades do solo, condições climáticas e geometria do domínio influenciam a distribuição de água e outros processos no solo.

Este processo simplificado de consulta e utilização dos dados da API permite aos usuários realizar simulações precisas e detalhadas da camada superficial do bulbo úmido, contribuindo para uma melhor compreensão do ambiente do solo e seus processos hidrológicos. API retorna dados para serem inseridos na simulação.

## Como Usar

### Instalação de Dependências

Para executar a API, você precisa ter o FastAPI e o Uvicorn instalados. Você pode instalá-los usando pip:

```
pip install fastapi uvicorn
```

### Iniciar o Servidor

Para iniciar o servidor, execute o seguinte comando a partir do diretório raiz do projeto:

```
uvicorn main:app --reload
```

Isso iniciará o servidor FastAPI, que estará disponível em `http://127.0.0.1:8000`.

### Documentação Interativa

O FastAPI gera automaticamente uma documentação interativa da API. Você pode acessá-la em `http://127.0.0.1:8000/docs`. Lá, você encontrará uma descrição de todos os endpoints, seus parâmetros e exemplos de uso.

## Endpoints Disponíveis

- `/soil_properties/`: Obtém as propriedades do solo, como textura, condutividade hidráulica, porosidade, capacidade de campo e ponto de murcha permanente.
- `/initial_conditions/`: Obtém as condições iniciais do solo, incluindo umidade inicial e concentração de solutos.
- `/boundary_conditions/`: Obtém as condições de contorno, como fluxo de água na superfície do solo, taxa de evaporação e precipitação.
- `/climate_parameters/`: Obtém os parâmetros climáticos, como temperatura, umidade relativa, velocidade do vento e radiação solar.
- `/domain_geometry/`: Obtém a geometria do domínio, como espessura do solo e área da superfície do solo.
- `/time_interval/`: Obtém o intervalo de tempo utilizado na simulação.
- `/saturation_drainage/`: Obtém as condições de saturação e drenagem do solo.
- `/all_parameters/`: Obtém todos os parâmetros juntos em um único endpoint.

## Exemplos de Uso

- Para obter as propriedades do solo: `http://127.0.0.1:8000/soil_properties/`
- Para obter as condições iniciais: `http://127.0.0.1:8000/initial_conditions/`
- Para obter as condições de contorno: `http://127.0.0.1:8000/boundary_conditions/`

## Configuração de Simulação no HYDRUS 3D

Esta API fornece informações sobre os dados necessários para configurar uma simulação da camada superficial do bulbo úmido no software HYDRUS 3D. Ele descreve as propriedades do solo, as condições iniciais, as condições de contorno, os parâmetros climáticos, a geometria do domínio, o intervalo de tempo e as condições de saturação e drenagem.

## Contribuindo

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões para melhorar esta API, sinta-se à vontade para abrir uma issue ou enviar um pull request.

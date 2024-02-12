# API de simulação do Bulbo em camada superficial

Esta é uma API de simulação do comportamento do solo, desenvolvida usando o framework FastAPI em Python.

Uso da API

1. Cliente faz uma solicitação à API.
2. A aPI Retorna dados para serem inseridos na simulação.

## Api

Esta API está disponível em [https://api-simulacao-do-bulbo-em-camada-superficial-kswxdthb5.vercel.app/docs](https://api-simulacao-do-bulbo-em-camada-superficial-kswxdthb5.vercel.app/docs). Lá, você encontrará uma descrição de todos os endpoints, seus parâmetros e exemplos de uso.

## Descrição

Esta Api fornece informações sobre os dados necessários para configurar uma simulação da camada superficial do bulbo úmido

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

- `/soil_properties/`: Obtém as propriedades do solo, como textura, condutividade hidráulica, porosidade, capacidade de campo e ponto de murcha.
- `/initial_conditions/`: Obtém as condições iniciais do solo, incluindo umidade inicial e concentração de soluto.
- `/boundary_conditions/`: Obtém as condições de contorno, como fluxo de água superficial, taxa de evaporação e precipitação.
- `/climate_parameters/`: Obtém os parâmetros climáticos, como temperatura, umidade, velocidade do vento e radiação solar.
- `/domain_geometry/`: Obtém a geometria do domínio, como espessura do solo e área superficial.
- `/time_interval/`: Obtém o intervalo de tempo utilizado na simulação.
- `/saturation_drainage/`: Obtém as condições de saturação e drenagem do solo.
- `/all_parameters/`: Obtém todos os parâmetros juntos em um único endpoint.

## Exemplos de Uso

- Para obter as propriedades do solo: `http://127.0.0.1:8000/soil_properties/`
- Para obter as condições iniciais: `http://127.0.0.1:8000/initial_conditions/`
- Para obter as condições de contorno: `http://127.0.0.1:8000/boundary_conditions/`

## Configuração de Simulação no HYDRUS 3D

Esta api fornece informações sobre os dados necessários para configurar uma simulação da camada superficial do bulbo úmido no software HYDRUS 3D. Ele descreve as propriedades do solo, as condições iniciais, as condições de contorno, os parâmetros climáticos, a geometria do domínio, o intervalo de tempo e as condições de saturação e drenagem, bem como explica a importância de cada conjunto de dados.

## Propriedades do Solo

- **Textura do solo:** Descreve a composição granulométrica do solo, neste caso, arenoso.
- **Condutividade hidráulica do solo:** Indica a capacidade do solo de transmitir água, medida em cm/h, neste caso, 7.83 cm/h.
- **Porosidade:** Representa a fração do volume do solo que é ocupada por espaços vazios, neste caso, 0.33.
- **Capacidade de campo:** Refere-se à quantidade de água que o solo pode reter após a drenagem gravitacional ter cessado, neste caso, 0.24.
- **Ponto de murcha permanente:** É o conteúdo de umidade do solo abaixo do qual as plantas não conseguem mais extrair água, neste caso, 0.07.

Essas propriedades são cruciais para entender a capacidade do solo em reter água, influenciando diretamente a distribuição e movimentação da água no solo.

## Condições Iniciais

- **Umidade inicial do solo:** Representa a quantidade de água presente no solo no início da simulação, neste caso, 0.27.
- **Concentração inicial de solutos:** Indica a concentração de substâncias dissolvidas no solo no início da simulação, neste caso, 50.88.

Essas condições são essenciais para definir o estado inicial do sistema, influenciando os resultados da simulação ao longo do tempo.

## Condições de Contorno

- **Fluxo de água na superfície do solo:** Representa a quantidade de água que entra ou sai da superfície do solo, neste caso, 0.49.
- **Taxa de evaporação:** Indica a taxa na qual a água é removida da superfície do solo devido à evaporação, neste caso, 4.64.
- **Precipitação:** Refere-se à quantidade de água adicionada à superfície do solo como chuva, neste caso, 17.91.

Essas condições influenciam diretamente o balanço hídrico do solo e a quantidade de água disponível para as plantas.

## Parâmetros Climáticos

- **Temperatura:** Indica a temperatura ambiente, neste caso, 24.87°C.
- **Umidade relativa:** Representa a proporção de vapor de água presente no ar em relação à quantidade máxima que o ar poderia conter na mesma temperatura, neste caso, 30.87%.
- **Velocidade do vento:** Refere-se à velocidade do vento na região, neste caso, 9.48 m/s.
- **Radiação solar:** Indica a quantidade de energia solar recebida, neste caso, 125.66 W/m².

Esses parâmetros climáticos são fundamentais para modelar os processos de evaporação e transpiração no solo.

## Geometria do Domínio

- **Espessura do solo:** Refere-se à profundidade total do solo, neste caso, 85.25 cm.
- **Área da superfície do solo:** Indica a área total da superfície do solo, neste caso, 147.31 m².

Esses dados são necessários para definir a geometria do domínio da simulação, permitindo calcular volumes e fluxos de água com precisão.

## Intervalo de Tempo

- **Intervalo de tempo para a simulação:** Representa o intervalo de tempo em que a simulação é realizada, neste caso, 21 horas.

Este parâmetro determina a resolução temporal da simulação, influenciando a precisão dos resultados.

## Condições de Saturação e Drenagem

- **Estado de saturação do solo:** Indica se o solo está saturado (completamente úmido) ou não saturado, neste caso, saturado.
- **Tipo de drenagem:** Refere-se ao tipo de drenagem do solo, neste caso, drenagem livre.

Essas condições descrevem como a água é movimentada no solo, afetando a disponibilidade de água para as plantas e outros processos relacionados ao transporte de água.

Em resumo, esses dados são essenciais para configurar uma simulação precisa da camada superficial do bulbo úmido no HYDRUS 3D, garantindo resultados confiáveis e úteis para a análise do comportamento do solo e da água no ambiente.

## Contribuindo

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões para melhorar esta API, sinta-se à vontade para abrir uma issue ou enviar um pull request.

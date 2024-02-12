# API de Comportamento do Solo

Esta é uma API de simulação do comportamento do solo, desenvolvida usando o framework FastAPI em Python.

## Api

A API está disponível em [https://api-simulacao-do-bulbo-em-camada-superficial-kswxdthb5.vercel.app/docs](https://api-simulacao-do-bulbo-em-camada-superficial-kswxdthb5.vercel.app/docs). Lá, você encontrará uma descrição de todos os endpoints, seus parâmetros e exemplos de uso.

## Descrição

A API fornece endpoints para acessar diferentes aspectos do comportamento do solo, incluindo suas propriedades, condições iniciais, condições de contorno, parâmetros climáticos, geometria do domínio, intervalo de tempo e condições de saturação e drenagem.

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

## Contribuindo

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões para melhorar esta API, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

```

Este README fornece uma visão geral da sua API, instruções sobre como instalá-la e executá-la, uma descrição dos endpoints disponíveis, exemplos de uso e informações sobre como contribuir. Certifique-se de personalizá-lo de acordo com as necessidades específicas da sua API.
```

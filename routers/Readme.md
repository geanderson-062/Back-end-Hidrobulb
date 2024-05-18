# FastAPI Simulation Configuration Routers API

Este é um exemplo de uma API construída com o FastAPI para configurar parâmetros de simulação em um modelo computacional.

## Descrição

Este código define um conjunto de rotas para configurar diferentes aspectos de uma simulação, incluindo propriedades do solo, condições iniciais, condições de contorno, parâmetros climáticos, geometria do domínio, intervalo de tempo e drenagem por saturação.

Cada aspecto da simulação tem sua própria rota dedicada, que é definida em módulos separados. As rotas disponíveis são:

- `/soil_properties`: Configuração das propriedades do solo.
- `/initial_conditions`: Configuração das condições iniciais.
- `/boundary_conditions`: Configuração das condições de contorno.
- `/climate_parameters`: Configuração dos parâmetros climáticos.
- `/domain_geometry`: Configuração da geometria do domínio.
- `/time_interval`: Configuração do intervalo de tempo da simulação.
- `/saturation_drainage`: Configuração da drenagem por saturação.

Cada rota corresponde a um conjunto de endpoints que lidam com a configuração específica associada àquele aspecto da simulação.

## Uso

Para configurar os parâmetros de simulação, você pode enviar solicitações para as rotas especificadas acima, fornecendo os dados necessários nos formatos esperados.

## Contribuindo

Se você encontrar problemas ou tiver sugestões para melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request neste repositório.

## Licença

Este código é distribuído sob a licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.

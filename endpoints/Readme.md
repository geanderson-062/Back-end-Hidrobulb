# Endpoints API

Este é um exemplo de uma API construída com o FastAPI.

## Descrição

Este código define um conjunto de rotas para diferentes informações de regiões geográficas do Brasil.

exemplo:

- `/boundary_conditions/norte`: Condições de contorno para a região Norte do Brasil.
- `/boundary_conditions/nordeste`: Condições de contorno para a região Nordeste do Brasil.
- `/boundary_conditions/centro_oeste`: Condições de contorno para a região Centro-Oeste do Brasil.
- `/boundary_conditions/sudeste`: Condições de contorno para a região Sudeste do Brasil.
- `/boundary_conditions/sul`: Condições de contorno para a região Sul do Brasil.

---

Cada rota corresponde a uma função que chama uma função específica do serviço `boundary_conditions` para gerar e retornar as condições de contorno para a região correspondente.

## Uso

Para utilizar esta API, você pode enviar solicitações GET para as rotas especificadas acima para obter as condições de contorno desejadas para cada região.

## Contribuindo

Se você encontrar problemas ou tiver sugestões para melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request neste repositório.

## Licença

Este código é distribuído sob a licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.

# API de Simulação do Comportamento do Solo com HYDRUS 3D

Esta é uma API construída com FastAPI que fornece dados simulados para diferentes aspectos do comportamento do solo, como propriedades do solo, condições climáticas, geometria do domínio e muito mais. Os dados fornecidos são gerados aleatoriamente para ilustrar conceitos e podem ser usados para testes, prototipagem ou propósitos educacionais.

## Instalação

Para executar a aplicação localmente, siga estas etapas:

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd nome-do-repositorio
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

Para iniciar o servidor da API, execute o seguinte comando a partir do diretório do projeto:

```bash
uvicorn main:app --reload
```

Após iniciar o servidor, você pode acessar a documentação interativa da API em `http://localhost:8000/docs` ou a interface alternativa do Swagger em `http://localhost:8000/redoc`. Além disso, você pode enviar solicitações HTTP para os endpoints diretamente.

## Endpoints

- `/`: Retorna uma mensagem de boas-vindas e uma breve descrição da API.
- `/soil_properties/`: Retorna dados simulados das propriedades do solo, como textura, condutividade hidráulica, porosidade, capacidade de campo e ponto de murcha permanente.
- `/initial_conditions/`: Retorna dados simulados das condições iniciais do solo, como umidade inicial e concentração de solutos.
- `/boundary_conditions/`: Retorna dados simulados das condições de contorno, como fluxo de água na superfície do solo, taxa de evaporação e precipitação.
- `/climate_parameters/`: Retorna dados simulados dos parâmetros climáticos, como temperatura, umidade, velocidade do vento e radiação solar.
- `/domain_geometry/`: Retorna dados simulados da geometria do domínio, como espessura e área da camada superficial do solo.
- `/time_interval/`: Retorna dados simulados do intervalo de tempo para a simulação.
- `/saturation_drainage/`: Retorna dados simulados das condições de saturação e drenagem do solo.
- `/all_parameters_except_initial/`: Retorna todos os dados, exceto as condições iniciais.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar pull requests com melhorias, correções de bugs ou novos recursos.

## Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).

---

Você pode personalizar este README de acordo com as necessidades específicas da sua aplicação. Certifique-se de incluir informações detalhadas sobre como instalar, usar e contribuir para sua API.

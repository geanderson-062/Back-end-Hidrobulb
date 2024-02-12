# Simulação do Bulbo em Camada Superficial

Esta API fornece dados e informações necessárias para configurar simulações da camada superficial do bulbo úmido no solo. Desenvolvida utilizando o framework FastAPI em Python, ela oferece acesso a diversos parâmetros e condições relacionados ao solo, clima e geometria do domínio, essenciais para a realização de simulações precisas e relevantes.

## Uso da API

Esta API foi projetada para simplificar o processo de configuração e execução de simulações da camada superficial do bulbo úmido no solo. Aqui está um resumo do fluxo de uso:

1. **Consulta de Endpoints:** O usuário consulta os diversos endpoints disponíveis para obter os dados necessários para a simulação, como propriedades do solo, condições iniciais, parâmetros climáticos e geometria do domínio.

2. **Recebimento de Dados:** A API retorna os dados solicitados em formato JSON, fornecendo informações detalhadas e precisas para cada aspecto da simulação.

3. **Integração com Ferramentas de Simulação:** Os dados obtidos são então utilizados para configurar simulações em software de modelagem, como o HYDRUS 3D, para análise e previsão do comportamento do solo.

4. **Análise de Resultados:** Após a simulação, os resultados são analisados ​​para entender como fatores como propriedades do solo, condições climáticas e geometria do domínio influenciam a distribuição de água e outros processos no solo.

Este processo simplificado de consulta e utilização dos dados da API permite aos usuários realizar simulações precisas e detalhadas da camada superficial do bulbo úmido, contribuindo para uma melhor compreensão do ambiente do solo e seus processos hidrológicos. API retorna dados para serem inseridos na simulação.

## Descrição

A simulação do bulbo em camada superficial é uma ferramenta valiosa para entender o comportamento do solo e a distribuição de água no ambiente. Esta API fornece informações detalhadas sobre as propriedades do solo, condições climáticas, geometria do domínio e outros parâmetros relevantes para a realização de simulações eficazes.

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

## Importância dos Tópicos

1. **Propriedades do Solo:** Determinam como a água se move e é retida no solo.
2. **Condições Iniciais:** Definem o estado inicial do sistema para resultados realistas.
3. **Condições de Contorno:** Influenciam diretamente o comportamento do bulbo úmido.
4. **Parâmetros Climáticos:** Reproduzem as condições ambientais para uma simulação precisa.
5. **Geometria do Domínio:** Define a extensão espacial da simulação.
6. **Intervalo de Tempo:** Determina a discretização temporal da simulação.
7. **Condições de Saturação e Drenagem:** Descrevem como a água se move no solo, afetando a disponibilidade de água para as plantas e outros processos relacionados ao transporte de água.

## Contribuindo

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões para melhorar esta API, sinta-se à vontade para abrir uma issue ou enviar um pull request.

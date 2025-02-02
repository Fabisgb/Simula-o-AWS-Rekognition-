# Projeto Simulação do AWS Rekognition

## Objetivo
Este projeto tem como objetivo simular o uso do AWS Rekognition para a identificação automática de celebridades em imagens. A simulação demonstra o fluxo de trabalho e a estrutura de um projeto que utiliza essa tecnologia, sem a necessidade de chamadas reais ao serviço (ideal para testes e demonstrações).

## Funcionalidades
- **Simulação do Processamento**: Simula o reconhecimento de celebridades em uma imagem e retorna uma resposta fictícia semelhante à do AWS Rekognition.
- **Exemplo de Saída**: Demonstra a estrutura de dados retornada pelo Rekognition, incluindo o nome da celebridade detectada e um nível de confiança associado.

## Explicação do Código:
- **simulate_celebrity_recognition()**: Função que simula o reconhecimento de celebridades em uma imagem. Ela escolhe aleatoriamente uma celebridade fictícia de uma lista e atribui um nível de confiança.
- **Execução do Script**: O código pode ser executado fornecendo o caminho de uma imagem para a função, que então retorna um dicionário imitando a resposta do AWS Rekognition.

## Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/Fabisgb/Simulacao-AWS-Rekognition-.git
   ```

2. Navegue até a pasta do projeto:
   ```bash
   cd simulacao-aws-rekognition
   ```

3. Execute o script:
   ```bash
   python simulate_aws_rekognition.py
   ```

## Possíveis Melhorias e Insights
- **Integração Real com AWS Rekognition**: Após a simulação, é possível integrar o boto3 para chamar o serviço real do Rekognition, utilizando o nível gratuito da AWS (😂 este não é o meu caso, só pago).
- **Expansão da Base de Dados**: Aumentar a lista de celebridades simuladas para tornar os resultados mais variados.
- **Interface Web**: Criar uma interface para upload de imagens e exibição dos resultados, tornando a aplicação mais interativa.

## Prints e Demonstrações

![Tela 1](https://github.com/Fabisgb/Simula-o-AWS-Rekognition-/blob/01a9143a80c4c50a0ada1f6b1cfe71824ddb8b32/imagens/img9.jpg)

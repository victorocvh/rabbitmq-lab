# Python-RabbitMQ

Este projeto, denominado Python-RabbitMQ, tem como objetivo realizar testes e experimentos relacionados ao message broker RabbitMQ. O foco principal é explorar os conceitos fundamentais do RabbitMQ, como filas, troca de mensagens, e comunicação entre produtores e consumidores.

## Estrutura do Projeto

O projeto está organizado em várias subpastas, cada uma representando um exemplo diferente:

### basic-01

Na pasta `basic-01`, encontram-se os arquivos `consumer.py` e `producer.py` que implementam uma comunicação básica entre um consumidor e um produtor. Essa comunicação envolve o envio de mensagens simples, proporcionando uma introdução aos conceitos essenciais do RabbitMQ.

### basic-02

A pasta `basic-02` expande o escopo do projeto, abordando a comunicação com workers. Aqui, o objetivo é demonstrar a distribuição eficiente de mensagens no RabbitMQ em cenários nos quais tarefas consomem tempo significativo. A implementação envolve a criação de workers para processar tarefas paralelamente.

### basic-03 (Em construção)

Na pasta `basic-03`, você terá a oportunidade de explorar e contribuir com exemplos adicionais. Este espaço está reservado para futuras implementações e testes mais avançados. Sinta-se à vontade para adicionar suas próprias experiências ou explorar conceitos mais complexos do RabbitMQ.

## Como Executar

1. **Instalação de Dependências:**
   Certifique-se de ter as dependências necessárias instaladas. Utilize o gerenciador de pacotes do Python para instalar as bibliotecas necessárias:

   ```bash
   pip install -r requirements.txt

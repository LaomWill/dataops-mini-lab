# DataOps Mini Lab - Pipeline Temporal e MongoDB Atlas

Projeto de engenharia de dados para geração de dados sintéticos, orquestração de tarefas com Temporal.io e persistência em MongoDB Atlas.

## Execução do Projeto

1. Requisitos: Python 3.11+ e Temporal CLI.
2. Configuração: Inserir a Connection String do MongoDB Atlas no arquivo .env.
3. Comandos:
   - Iniciar servidor: temporal server start-dev
   - Executar pipeline: python setup_and_run.py

## Resultados

- Volume: Geração de CSV de 10MB com aproximadamente 84.000 registros.
- Persistência: Carga concluída na coleção orders_raw do banco dataops_lab no MongoDB Atlas.
- Orquestração: Workflow finalizado via Temporal (Geração -> Carga -> Agregação).

## Respostas da Atividade

1. Vantagem de dados fake?
Segurança e privacidade. Permite testar o pipeline com volume real (10MB) sem expor dados sensíveis ou depender de acessos a bases de produção.

2. Papel do Workflow no Temporal?
Orquestrador do processo. Define a ordem das tarefas e garante a resiliência da execução, permitindo retentativas automáticas em caso de falha.

3. Diferença entre Workflow e Activity?
O Workflow detém a lógica de negócio (determinística), enquanto a Activity executa as tarefas que interagem com o mundo exterior (não determinística), como gravação em banco ou leitura de arquivos.

4. O que muda ao usar o MongoDB Atlas?
A conectividade passa a ser via internet, exigindo configuração de Network Access (IP Whitelist) e gerenciamento de segurança via TLS/SSL.

5. Está pronto para produção?
Não. Para produção seria necessário gerenciamento de segredos (remover senhas do .env), monitoramento de performance e tratamento de erros mais robusto para cenários críticos.

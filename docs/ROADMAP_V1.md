# Roadmap da V1

## Definição de concluído

A V1 estará concluída quando o usuário conseguir, pelo Telegram:

1. cadastrar ou consultar sua estrutura básica de rotina;
2. cadastrar tasks e blocos recorrentes;
3. solicitar a visão de uma data;
4. receber tasks e blocos recorrentes daquele dia;
5. enviar uma mensagem simples que seja interpretada;
6. receber uma resposta no estilo fixo do copiloto;
7. ter os dados persistidos no PostgreSQL.

---

## Estado atual

- [x] PostgreSQL local com Docker
- [x] Tabelas iniciais
- [x] Schemas iniciais
- [x] GET, GET por ID e POST de categories
- [x] GET, GET por ID e POST de tasks
- [x] GET, GET por ID e POST de recurring blocks
- [ ] Separação completa entre API, repository e service
- [ ] Regras de negócio da visão diária
- [ ] Telegram
- [ ] Parsing com LLM
- [ ] Fluxo completo testado

---

## Fase 1 — Consolidar a API mínima

### Objetivo
Deixar categories, tasks e recurring blocks consistentes.

### Entregas
- response models coerentes;
- tratamento de registro não encontrado;
- validações básicas;
- queries retiradas dos routers e movidas para repositories;
- routers chamando repositories ou services;
- testes manuais dos endpoints.

### Estratégia de aprendizagem
Rui refatora uma entidade completa.
Depois da revisão, o Codex replica o padrão nas outras.

### Critério de conclusão
As três entidades podem ser criadas, listadas e consultadas por ID.

---

## Fase 2 — Visão diária

### Objetivo
Criar a primeira funcionalidade própria do Co-piloto.

### Entregas
- receber uma data;
- consultar tasks dessa data;
- converter a data em dia da semana;
- consultar blocos recorrentes aplicáveis;
- devolver os dois conjuntos organizados;
- criar endpoint da visão diária.

### Critério de conclusão
Uma chamada com uma data retorna corretamente tasks e blocos recorrentes.

---

## Fase 3 — Interface com Telegram

### Objetivo
Permitir que o usuário acesse o sistema pelo Telegram.

### Entregas
- criar bot;
- receber mensagens;
- identificar comandos iniciais;
- chamar os services existentes;
- responder com a visão diária e confirmações simples.

### Critério de conclusão
O usuário consegue solicitar pelo Telegram o que tem em uma data.

---

## Fase 4 — Regras determinísticas do copiloto

### Objetivo
Começar o comportamento de constância sem depender do LLM.

### Entregas
- tratamento diferenciado de categorias-âncora;
- identificação de tasks pendentes;
- estrutura de opções fechadas;
- regras básicas para horário e remanejamento;
- respostas padronizadas.

### Critério de conclusão
O sistema toma decisões básicas por código e devolve opções coerentes.

---

## Fase 5 — LLM controlado

### Objetivo
Permitir linguagem natural sem entregar ao modelo o controle da aplicação.

### Entregas
- classificar intenção;
- extrair data, horário, task e ação;
- usar structured output;
- validar a saída;
- encaminhar para a regra de negócio correta;
- verbalizar a resposta final.

### Critério de conclusão
Mensagens simples em linguagem natural produzem ações estruturadas e seguras.

---

## Fase 6 — Fechamento da V1

### Entregas
- testes do fluxo ponta a ponta;
- tratamento dos erros principais;
- README atualizado;
- `.env.example`;
- instruções para banco e API;
- documentação dos endpoints;
- revisão do que ficou para V2.

### Critério de conclusão
O fluxo Telegram → backend → PostgreSQL → resposta funciona de forma repetível.
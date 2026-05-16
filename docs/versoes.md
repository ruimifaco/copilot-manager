# Roadmap — Copiloto de Constância

## Objetivo geral

Construir um copiloto pessoal de constância, com foco em ajudar o usuário a manter rotina, lidar com remanejamentos e reduzir autossabotagem no dia a dia. A V1 deve priorizar funcionamento real e simplicidade. A V2 e a V3 expandem inteligência, adaptação e integrações.

---

## Visão do produto

O sistema deve atuar como um operador da rotina do usuário, não apenas como um lembrete. Ele precisa:

* entender a estrutura da rotina do usuário;
* distinguir blocos recorrentes, compromissos pontuais e tarefas soltas;
* gerar uma visão diária;
* permitir ajustes e remanejamentos;
* cobrar consistência com estilo fixo;
* registrar histórico para melhorar decisões no futuro.

---

## V1 — Base funcional e confiável

### Objetivo

Ter um backend mínimo funcional, com banco de dados, modelagem inicial, leitura/escrita de dados e base pronta para evoluir.

### Escopo principal

* múltiplos usuários;
* categorias personalizáveis por usuário;
* categorias podem ser âncoras (`is_anchor`);
* blocos recorrentes;
* tasks independentes, com categoria opcional;
* visão diária simples;
* histórico inicial;
* Telegram como canal da V1;
* IA usada apenas para parsing de mensagens e verbalização de respostas.

### O que a V1 deve fazer

* cadastrar usuários;
* cadastrar categorias;
* cadastrar blocos recorrentes;
* cadastrar tasks soltas;
* gerar uma visão diária com base em blocos recorrentes + tasks + pendências;
* permitir operações básicas sobre tasks;
* registrar status final;
* salvar histórico mínimo;
* expor endpoints mínimos de leitura e escrita;
* conectar FastAPI ao PostgreSQL.

### Funcionalidades mínimas esperadas

* criação de tasks;
* listagem de tasks;
* vínculo de dados por usuário;
* banco PostgreSQL local funcionando;
* API mínima em FastAPI;
* README inicial com instruções;
* arquivo SQL de prática criado.

### Modelagem central da V1

* `users`
* `categories`
* `recurring_blocks`
* `tasks`

### Decisões importantes da V1

* `Category` existe, mas não é o centro do sistema;
* `Task` é independente de `RecurringBlock`;
* `Task` pode ter `category_id` nulo;
* `is_anchor` fica em `Category`;
* estilo do copiloto é fixo para todos os usuários;
* decisões centrais ficam em regra de negócio, não no LLM.

### O que fica fora da V1

* WhatsApp;
* integração com Google Calendar;
* scheduler sofisticado;
* aprendizado adaptativo forte;
* painel bonito;
* autenticação completa;
* multi-agent;
* memória vetorial.

---

## V2 — Copiloto operacional real

### Objetivo

Transformar a base da V1 em um copiloto que realmente acompanhe a rotina diária, converse com o usuário e reorganize o dia com mais inteligência.

### Escopo principal

* reminders automáticos por horário;
* scheduler funcionando com blocos e tasks;
* visão diária consolidada;
* remanejamento de tarefas;
* distinção entre exceção pontual e mudança estrutural;
* fechamento diário automatizado;
* logs mais completos de interação;
* parser de mensagens livres com IA;
* respostas mais naturais e firmes;
* regras mais ricas para âncoras.

### O que a V2 deve fazer

* mandar mensagem no início de tarefas e blocos;
* permitir iniciar, reduzir, adiar com horário, concluir e remarcar;
* lidar com conflito de agenda;
* preservar âncoras com prioridade maior;
* respeitar sono ao sugerir remanejamentos;
* permitir reconstrução de um dia específico;
* registrar exceções e ajustes;
* interpretar mensagens do tipo:

  * “não vou pra aula hoje”
  * “entrou reunião às 11h”
  * “agora minha aula mudou de horário”

### Expansões de modelagem possíveis na V2

* `one_time_commitments`
* `daily_plans`
* `interaction_logs`
* talvez alguma entidade para exceções/ajustes

### Inteligência esperada na V2

* diferenciar mudança passageira de mudança permanente;
* pedir esclarecimento quando houver ambiguidade;
* priorizar âncoras em reorganizações;
* gerar fechamento diário com base no que aconteceu de fato.

### O que continua fora da V2

* produto de mercado amplo;
* integrações múltiplas complexas;
* aprendizado estatístico avançado;
* dashboard completo de análise comportamental.

---

## V3 — Adaptação, memória e refinamento

### Objetivo

Tornar o copiloto progressivamente mais adaptativo, aprendendo com o histórico do usuário e refinando a forma como organiza, cobra e sugere mudanças.

### Escopo principal

* memória comportamental mais forte;
* análise de padrões por horário, dia da semana e categoria;
* melhoria das sugestões de remanejamento;
* priorização automática com base em histórico;
* revisão semanal;
* visão de progresso por categoria e por âncora;
* futuras integrações externas.

### O que a V3 deve fazer

* detectar horários de maior chance de execução;
* perceber desculpas recorrentes;
* ajustar sugestões com base em histórico real;
* apontar padrões de falha e sucesso;
* ajudar o usuário a revisar a semana;
* sugerir mudanças na rotina com base em uso real;
* identificar quais remanejamentos tendem a funcionar ou falhar.

### Possíveis integrações da V3

* Google Calendar;
* WhatsApp;
* dashboard web mais completo;
* analytics de consistência;
* relatórios semanais.

### Possíveis métricas da V3

* taxa de execução por categoria;
* taxa de execução por âncora;
* horários com maior adesão;
* sequência atual;
* percentual semanal de constância;
* frequência de remanejamento;
* frequência de exceções;
* categorias mais negligenciadas.

---

## Ordem mental do projeto

### V1

Base funcional, banco, API, CRUD mínimo e modelagem central.

### V2

Operação diária real, reminders, remanejamento, parsing e interação prática.

### V3

Adaptação, memória, inteligência incremental e refinamento do copiloto.

---

## Princípios do sistema

* constância > perfeição;
* âncoras têm peso maior;
* task pode existir sem bloco recorrente;
* categoria organiza, mas não define tudo;
* o copiloto deve ser firme, direto e consistente;
* o LLM não substitui regra de negócio;
* exceções pontuais não devem alterar a rotina base;
* mudanças estruturais devem atualizar a rotina recorrente.

---

## Observação estratégica

Este projeto deve ser tratado inicialmente como um sistema pessoal sério, útil e bem modelado, e não como uma startup B2C genérica. A base pode ser reaproveitada depois, mas a prioridade atual é utilidade real, aprendizado técnico e consistência de produto.

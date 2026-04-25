# Objetivo

Maximizar tua constância semanal nas categorias principais da tua rotina, com:

cobrança firme
remanejamento inteligente
proteção do sono
memória do teu comportamento
adaptação progressiva

O que ele é: Um operador da tua rotina.

O que ele não é:
terapeuta
amigo motivacional
chatbot aberto que conversa sobre qualquer coisa
planner perfeito que exige dias perfeitos
agente “mágico” que adivinha teu estado o tempo todo

# Problema

O problema não é falta de intenção.
É o intervalo entre:

saber o que deve ser feito
executar mesmo sem vontade
remanejar sem se enganar
não deixar um atraso virar desistência

Então o produto existe para resolver:

procrastinação por atrito
negociação interna demais
adiamento vago
quebra de sequência
decisões ruins de curto prazo que sabotam a semana

# Solução 

**Filosofia fixa do co-piloto:**

tom firme, direto e respeitoso
nunca aceitar adiamento vago
sempre oferecer opções fechadas
proteger o sono
priorizar constância sobre conforto imediato
tarefa não some; muda de forma

# Software Requirements

## Functional Requirements

FR01. O sistema deve permitir o cadastro de múltiplos usuários.

FR02. O sistema deve permitir que cada usuário cadastre suas próprias categorias de rotina.

FR03. O sistema deve permitir que cada usuário configure sua rotina semanal, incluindo horários planejados para cada categoria.

FR04. O sistema deve permitir que cada usuário configure políticas por categoria, incluindo duração ideal, mínima e emergencial.

FR05. O sistema deve gerar automaticamente o planejamento diário de cada usuário com base em sua rotina semanal e configurações.

FR06. O sistema deve enviar uma mensagem no início de cada tarefa planejada.

FR07. O sistema deve apresentar, na mensagem da tarefa, opções de manejo como iniciar, reduzir duração, adiar com horário definido ou concluir.

FR08. O sistema deve permitir que o usuário informe conflitos ou imprevistos que afetem sua rotina.

FR09. O sistema deve recalcular ou sugerir remanejamento da tarefa quando houver conflito, considerando as regras configuradas do usuário.

FR10. O sistema deve registrar o status final de cada tarefa diária, incluindo feito, feito mínimo, feito emergencial, adiado ou não realizado.

FR11. O sistema deve armazenar o histórico de interações, tarefas e resultados de cada usuário separadamente.

FR12. O sistema deve gerar um fechamento diário com o resumo das tarefas realizadas e pendentes.

FR13. O sistema deve interpretar mensagens livres do usuário para identificar intenções como adiamento, conflito de agenda, conclusão ou justificativa.

FR14. O sistema deve associar cada usuário ao seu respectivo canal de comunicação no Telegram.

FR15. O sistema deve respeitar as restrições de sono do usuário ao sugerir reduções ou remanejamentos de tarefas.

## Non-functional Requirements

**Qualidade de serviço**

NFR01. O sistema deve suportar múltiplos usuários com isolamento de dados entre eles.

NFR02. As mensagens programadas devem ser enviadas com atraso máximo de X segundos em relação ao horário planejado.

NFR03. O sistema deve persistir os dados de usuários, tarefas e histórico de forma confiável, evitando perda de registros em caso de reinício da aplicação.

NFR04. O sistema deve manter o estilo do copiloto fixo e consistente para todos os usuários.

**Segurança e integridade**

NFR05. O sistema deve garantir que um usuário não possa acessar dados de outro usuário.

NFR06. O sistema deve validar entradas recebidas do Telegram e das integrações externas antes de processá-las.

**Restrições tecnológicas**

NFR07. O backend deve ser implementado com FastAPI.

NFR08. O banco de dados deve ser PostgreSQL.

NFR09. O canal de comunicação da V1 deve ser Telegram Bot.

NFR10. Os agendamentos da V1 devem ser implementados com APScheduler.

NFR11. A OpenAI API deve ser utilizada apenas para parsing de mensagens e verbalização de respostas, com structured outputs e/ou function calling.

# Domain UML Class Diagram

# Conceptual Data Model

# Logical Data Model

## Task pode existir sem categoria
Category é opcional porque tasks pontuais podem não pertencer a uma área estável.

## DailyPlan não é persistido na V1
A visão diária é derivada de tasks e blocos recorrentes.

## LLM não executa regras centrais
O modelo interpreta linguagem; services validam e decidem.

## Identidade do Telegram
O identificador do usuário no Telegram é armazenado em `users.telegram_user_id`
como `BIGINT`, separado do `users.id` interno usado nas relações do banco.

O campo é único e pode permanecer nulo até a associação com o Telegram ser
concluída. Depois da associação, a camada do Telegram resolve o usuário interno
automaticamente; o usuário humano não informa nem escolhe `users.id`.

## Item agendado sem horário final
Uma task com `planned_start_time` e sem `planned_end_time` entra na linha do
tempo usando seu horário inicial e `end_time` nulo.

Ao tentar agendar outro item posteriormente no mesmo dia, o service deve
detectar a task aberta e solicitar confirmação explícita antes de persistir o
novo agendamento. O aviso também deve oferecer a possibilidade de definir o
horário final da task aberta.

Recurring blocks continuam exigindo `end_time` na V1 conforme o modelo atual.
Permitir blocos recorrentes sem horário final exigirá uma decisão de modelagem
separada.

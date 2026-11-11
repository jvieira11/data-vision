# Progresso do DataVision

## Etapa atual 
Fase 1 

## Etapas concluídas
- [x] Planejamento da arquitetura
- [x] Verificação do ambiente (Python 3.14, Node 24, Git, Docker)
- [x] Primeiro endpoint
- [x] Ambiente virtual configurado

## Conceitos aprendidos
- Arquitetura cliente-servidor (front-end, back-end, banco);
- API stateless: É uma API que não mantém informações de estado da comunicação entre uma requisição e outra;
- .gitignore: Onde colocamos informações que não devem ir para público (GitHub, nesse caso), além de servir pra ignorar lixos eletrônicos do Windows/MAC. E o principal, ignorar o que é gerado e reconstrutível como .venv e __pycache__.
- Configuração do ambiente virtual do .venv.
- Criação de fixação da versão do FastAPI em requirement.txt, para que assim, se por exemplo, 1 ano mais tarde, não de conflito de versões.
- Recarregamento automático utilizando o modo dev no health check.
- Códigos de status HTTP, como: Família 2xx (significando que deu certo, OK), família 4xx (significando que o cliente errou, "ERROR 413 - arquivo grande demais", por exemplo) e Família 5xx (significando que o servidor errou, como o ERROR 500 - Internal Server Error).
- Decorator/Wrapper é uma função que recebe outra função e a modifica ou a registra. Assim como utilizado no código, função @app.get("/health") envia a função ao FastAPI, que em seguida registra-o como o resposável pelo GET em /health.
- Type hints, ou dicas de tipos, que serve para indicar os tipos dos dados das variáveis, ex.: str, float, int.
- Depêndencias transitivas: é a dependência de uma dependência. Exemplo no projeto: FastAPI > Pydantic > annoted-types.
- As rotas diferenciam letras maiúsculas e minúsculas(Ex.: /status e /Status)
- "collected 0 itens" significa que o pytest não encontrou nenhum text.

## Problemas encontrados e resolvidos
- Projeto dentro do OneDrive no início > movido para C:\dev, pois o OneDrive fica sempre querendo salvar coisas e empurrar atualizações nos arquivos, o que pode gerar travamentos e lentidão nos tais arquivos.
- Ativação em pasta errada: Estava com problemas pra ativar o pip, pois estava fazendo em uma pasta diferente da pasta backend, mas consegui corrigir e ativar corretamente.
- Requirements com nome errado: na pressa se escrever o nome do arquivo escrevi "requerements" ao invés de requirements.
- No item do .vscode, a causa real foi: o arquivo já estava rastreado, e o .gitignore não vale para arquivos que o Git já rastreia. Por isso precisamos do git rm --cached.

## Pontos para praticar
- Python básico
- JavaScript
- Pandas
- Terminal
- Verificar antes de commitar
- Ler o código com atenção antes de responder
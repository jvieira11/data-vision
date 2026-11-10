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
- Criação de fixação da versão do pip em requirement.txt, para que assim, se por exemplo, 1 ano mais tarde, não de conflito de versões.
- Recarregamento automático utilizando o modo dev no health check.

## Problemas encontrados e resolvidos
- Projeto dentro do OneDrive no início > movido para C:\dev, pois o OneDrive fica sempre querendo salvar coisas e empurrar atualizações nos arquivos, o que pode gerar travamentos e lentidão nos tais arquivos.
- Ativação em pasta errada: Estava com problemas pra ativar o pip, pois estava fazendo em uma pasta diferente da pasta backend, mas consegui corrigir e ativar corretamente.
- Requirements com nome errado: na pressa se escrever o nome do arquivo escrevi requeriments ao invés de requiriments.
- .vscode commitando por engano com git rm --cached: ao invés de ignorar /.vscode, estava ignorando settings.json. Corrigido em .gitignore.

## Pontos para praticar
- Python básico
- JavaScript
- Pandas
- Terminal
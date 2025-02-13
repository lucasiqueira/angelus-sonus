# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), e este projeto adere ao [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2025-02-13
### Adicionado
- Adicionado arquivo `pyproject.toml` para gerenciar dependências com `poetry`.
- Adicionado suporte para instalação de dependências usando `poetry` no `README.md`.
- Adicionado exemplo de arquivo `.env.example` para configuração de variáveis de ambiente.

### Alterado
- Atualizado `README.md` para refletir o uso do `pyproject.toml` e `poetry` para instalação de dependências.
- Atualizado `README.md` para usar o comando `cp .env.example .env` para criar o arquivo `.env`.

## [1.0.0] - 2025-02-12
### Adicionado
- Primeira versão do projeto Angelus Sonus.
- Funcionalidade para tocar um sino automaticamente todos os dias às 12:00 PM e às 6:00 PM.
- Suporte para agendamento automático via `launchctl` no macOS.
- Registro de logs de eventos da aplicação.
- Arquivo `requirements.txt` com as dependências do projeto.
- Testes unitários usando `pytest`.
- Documentação inicial no `README.md` com instruções de instalação e configuração.
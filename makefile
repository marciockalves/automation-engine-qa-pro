# Variáveis
DOCKER_COMPOSE = docker compose
CONTAINER_NAME = playwright_engine
MAIN_APP = app/ui/main_window.py

.PHONY: setup up down shell test-bridge xhost run clean

# --- Configuração Inicial ---

setup: ## Instala as dependências locais via uv
	uv sync
	@echo "✅ Ambiente local sincronizado com uv."

xhost: ## Permite que o Docker acesse o servidor gráfico do Fedora (X11/Wayland)
	xhost +local:docker
	@echo "🖥️ Permissões de X11 atualizadas para o Docker."

# --- Gerenciamento do Docker ---

up: xhost ## Sobe o container em background e garante acesso ao X11
	$(DOCKER_COMPOSE) up -d
	@echo "🐳 Container Playwright está rodando."

down: ## Para e remove os containers
	$(DOCKER_COMPOSE) down
	@echo "🛑 Container parado."

shell: ## Entra no terminal do container Playwright
	$(DOCKER_COMPOSE) exec playwright /bin/bash

# --- Execução de Testes e App ---

test-bridge: up ## Roda o teste de sanidade para verificar a ponte Docker <-> Fedora
	$(DOCKER_COMPOSE) exec playwright python test_bridge.py

run: ## Executa a interface principal PySide6 nativa no Fedora
	uv run python $(MAIN_APP)

# --- Utilidades ---

clean: ## Limpa arquivos temporários e cache de Python
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	@echo "🧹 Limpeza concluída."

help: ## Exibe esta ajuda
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'
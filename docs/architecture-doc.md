
# Documento de Arquitetura - FitHub

## 1: Introdução

### 1.1 Finalidade

Este documento visa proporcionar uma visão abrangente da arquitetura que será implementada no desenvolvimento do projeto FitHub. Tem como propósito permitir um entendimento mais profundo sobre o aplicativo web e sua interação com outras aplicações no contexto do projeto. De forma clara e objetiva, o documento apresentará as decisões arquiteturais tomadas durante o desenvolvimento do projeto.

### 1.2 Escopo

O FitHub é um aplicativo dedicado ao fitness e bem-estar, oferecendo aos usuários uma plataforma completa para treinamento físico. Permitindo a seleção de grupos musculares específicos, filtragem de exercícios com base em diversos critérios, acesso a programas de treinamento personalizados e rastreamento do progresso ao longo do tempo. Além disso, o FitHub incorpora um chatbot de processamento de linguagem natural (NLP) para fornecer dicas e responder perguntas sobre treinamento e alimentação, proporcionando uma experiência personalizada e informativa.

## 2: Funcionalidades

-  **2.1 Seleção de Grupo Muscular:** Os usuários podem escolher grupos musculares específicos nos quais desejam focar.

- **2.2 Filtragem de Exercícios:** Os usuários têm a capacidade de classificar e filtrar exercícios com base em:
	- **Equipamento;**
	- **Dificuldade;**
	- **Tipo de exercício.**
	- **Exercícios por Tipo:**

- **2.3 Assistência por NLP:** Implementação de um chatbot que fornece dicas e responde a perguntas dos usuários relacionadas a treinamento e alimentação.

- **2.4 Treinamento Personalizado:** Os usuários podem criar programas de treinamento personalizados com base nos exercícios disponíveis no sistema.

- **2.5 Acompanhamento de Progresso:** Os usuários podem rastrear seu progresso ao longo do tempo, incluindo medições e peso corporal.

## 3: Visão de Casos de Uso

### 3.1 Diagrama de Caso de Uso

O diagrama de caso de uso ilustra as interações entre os usuários e o sistema FitHub, identificando as diferentes funcionalidades e como elas são acessadas pelos usuários.

![Diagrama de Caso de Uso](https://github.com/RochaGabriell/fithub-api/blob/main/docs/UML/Diagrama%20Caso%20de%20Uso.jpg?raw=true)

### 4: Diagrama de Classes

O diagrama de classes representa a estrutura de classes e suas relações no sistema FitHub, proporcionando uma visão detalhada da organização do código fonte.

![Diagrama de Classes](https://github.com/RochaGabriell/fithub-api/blob/main/docs/UML/ClassUML.png?raw=true)

### 5: Diagrama de Pacotes

O diagrama de pacotes ilustra a organização modular do sistema FitHub, mostrando como as diferentes partes do sistema estão agrupadas em pacotes.

![Diagrama de Pacotes](https://github.com/RochaGabriell/fithub-api/blob/main/docs/UML/Diagrama%20Pacotes.jpg?raw=true)

### 6: Diagrama de Componente

O diagrama de componente exibe os principais componentes do sistema FitHub e suas interações, proporcionando uma visão geral da estrutura de componentes.

![Diagrama de Componente](https://github.com/RochaGabriell/fithub-api/blob/main/docs/UML/Diagrama%20de%20Componente.jpg?raw=true)

### 7: Diagrama de Máquina de Estado (Busca de Exercícios)

O diagrama de máquina de estado detalha o processo de busca de exercícios no sistema FitHub, destacando os diferentes estados e transições possíveis.

![Diagrama de Máquina de Estado](https://github.com/RochaGabriell/fithub-api/blob/main/docs/UML/Diagrama%20de%20M%C3%A1quina%20de%20Estado.jpg?raw=true)

### 8: Diagrama de Atividade (Login e Registro)

O diagrama de atividade representa as etapas envolvidas nos processos de login e registro no sistema FitHub, fornecendo uma visão clara das atividades e decisões durante esses processos.

![Diagrama de Atividade](https://github.com/RochaGabriell/fithub-api/blob/main/docs/UML/Diagrama%20de%20Atividade.jpg?raw=true)

### 9: Diagrama de Sequência (Login)

O diagrama de sequência detalha as interações entre os diferentes componentes envolvidos no processo de login do FitHub, mostrando a ordem e o fluxo das operações.

![Diagrama de Sequência - Login](https://github.com/RochaGabriell/fithub-api/blob/main/docs/UML/Diagrama%20de%20Sequencia%20-%20Login.jpg?raw=true)
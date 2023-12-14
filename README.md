# FitHub - API (Django REST Framework)

<img
  src="https://raw.githubusercontent.com/RochaGabriell/fithub/2fd75fe4dfd3947d873d61982a4d006ddc4bbcc2/public/Logo%20-%20Light.svg"
  alt="FitHub Logo" style="width: 200px;" />

Bem-vindo à FitHub API, o backend da sua jornada em direção à saúde e bem-estar. Este projeto, parte integrante do meu trabalho acadêmico, utiliza o Django REST Framework para fornecer uma infraestrutura poderosa e eficiente para a aplicação FitHub.

| Confira o **[Front-End](https://github.com/RochaGabriell/fithub)** do sistema.

## Tecnologias Utilizadas 🛠️

- **Django REST Framework:**
- **SimpleJWT:**
- **Swagger:**

## Recursos Principais 🚀

- **Acompanhamento de Medidas:** Registre e acompanhe visualmente o progresso em direção às suas metas de saúde.

- **Fichas de Treino Personalizadas:** Explore a extensa biblioteca de exercícios e crie fichas personalizadas com controle total sobre a rotina de exercícios.

- **Versatilidade:** Seja em casa ou na academia, com ou sem equipamento, a FitHub API é flexível para se adequar ao estilo de vida do usuário, removendo barreiras para uma vida mais saudável.


| Para obter informações adicionais sobre o sistema, consulte a **[documentação.](https://github.com/RochaGabriell/fithub-api/blob/main/docs/architecture-doc.md)**

## Como Configurar e Executar 🏃‍♂️

### 1. Clone o Repositório

```bash
git clone https://github.com/RochaGabriell/fithub-api.git
```

### 2. Crie e Ative o Ambiente Virtual

#### Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows ou Mac:

Consulte a documentação da linguagem [Python](https://docs.python.org/pt-br/3/library/venv.html).

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DJANGO_SECRET_KEY='Sua SECRET_KEY'
```

### 5. Realize as Migrações

```bash
python manage.py migrate
```

### 6. Execute o Servidor

```bash
python manage.py runserver
```

A API estará disponível em [http://localhost:8000](http://localhost:8000).

### Documentação Interativa (Swagger)

Acesse [http://localhost:8000/swagger](http://localhost:8000/swagger) para explorar e testar a API usando a interface Swagger.

## Missão da FitHub API 🌐

A missão da FitHub API é alinhar-se aos princípios dos Objetivos de Desenvolvimento Sustentável (ODS), particularmente ao ODS 3, promovendo um estilo de vida saudável e sustentável. Acredito que a melhoria da saúde individual contribui para o fortalecimento das comunidades como um todo.

## Contribuição e Suporte 🤝

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas, sugerir melhorias ou enviar pull requests.

---

_Este projeto faz parte do meu trabalho integrador de faculdade, reforçando meu compromisso com a saúde e bem-estar, inspirado pelos Objetivos de Desenvolvimento Sustentável (ODS) da ONU._

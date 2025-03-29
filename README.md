# 🔐 Gerador de Senhas Seguras por Setor

Você agora é responsável por criar as senhas para os funcionários de uma empresa. Após ataques de força bruta, o time de segurança decidiu que era hora de agir: **precisamos de um algoritmo que crie senhas seguras e aleatórias para cada setor da empresa.**

---

## 🏢 Requisitos por Setor

Cada setor definiu um tamanho mínimo de senha para aumentar a segurança:

| Setor         | Tamanho da Senha |
|---------------|------------------|
| Administração | 20 caracteres    |
| TI            | 30 caracteres    |
| Produção      | 15 caracteres    |

---

## ✅ Regras de Geração

- O sistema deve receber **qual o setor** do funcionário.
- As senhas devem conter:
  - Letras **maiúsculas** e **minúsculas**
  - **Dígitos numéricos**
- As senhas devem ser **aleatórias**, **únicas** e **seguras**.

---

## 📌 Etapas do Projeto

### 1️⃣ Criando um Gerador de Senhas Seguras

O objetivo é gerar senhas aleatórias que sejam seguras e imprevisíveis.

---

## 🔍 Conceitos Importantes

### 1. O que faz uma senha ser segura?

Uma senha segura precisa ser:

- ✅ **Longa** (mínimo recomendado: 12 caracteres)
- ✅ **Complexa** (maiúsculas, minúsculas, números e símbolos)
- ✅ **Imprevisível** (sem padrões como `123456` ou `password`)
- ✅ **Única** (não usar senhas repetidas entre sistemas)

---

### 2. Aleatoriedade: `random` vs `secrets`

| Biblioteca | Segurança | Uso Recomendado |
|------------|-----------|-----------------|
| `random`   | ❌ Baixa  | Testes e simulações |
| `secrets`  | ✅ Alta   | Geração de senhas e tokens |

➡️ **Conclusão**: Usaremos a biblioteca `secrets` do Python, pois ela gera valores aleatórios adequados para segurança.

---

### 3. Entropia e Segurança

A **entropia** mede o nível de imprevisibilidade de uma senha.

**Fórmula:**
```plaintext
Entropia = log2(possibilidades ^ tamanho)
```

**Exemplos:**

- 8 letras minúsculas (26 opções):
  - `log2(26^8) ≈ 37.6 bits`
- 12 caracteres com 94 possibilidades (maiúsculas, minúsculas, números e símbolos):
  - `log2(94^12) ≈ 78.8 bits`

➡️ Quanto maior a entropia, **mais segura** a senha.

---

### 4. Tipos de Ataques Comuns

| Tipo de Ataque        | Descrição |
|------------------------|-----------|
| **Força Bruta**        | Testa todas as combinações possíveis |
| **Dicionário**         | Usa senhas comuns ou vazadas |
| **Engenharia Social**  | Usa informações pessoais previsíveis |

➡️ **Defesa:** Use senhas **longas**, **aleatórias** e **únicas** para se proteger.

---

## 💡 Conclusão

Criar senhas seguras exige:

- Geradores confiáveis como `secrets`
- Tamanhos apropriados por setor
- Complexidade e aleatoriedade
- Prevenção contra ataques comuns

Você pode agora implementar o sistema de geração de senhas com confiança e proteger sua empresa contra invasores!

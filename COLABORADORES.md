# Guia de Branches para Colaboradores

Este projeto utiliza um sistema de branches individual para cada colaborador, facilitando o trabalho em paralelo e a organização do código.

## 📋 Estrutura de Branches

- **`main`** - Branch principal (proteído)
- **`colaborador/<nome>`** - Branch individual para cada colaborador

## 👥 Colaboradores e seus branches

| Colaborador | Branch |
|---|---|
| Bigas282 | `colaborador/Bigas282` |
| LuisReis-Caixa | `colaborador/LuisReis-Caixa` |
| macmirian | `colaborador/macmirian` |
| Marcus Vinicius | `colaborador/Marcus-Vinicius` |
| PattyMayumi | `colaborador/PattyMayumi` |
| pedrohhecht-create | `colaborador/pedrohhecht-create` |
| Roselenesfm01 | `colaborador/Roselenesfm01` |
| Samoel Santos da Silva Galdino Mendes | `colaborador/Samoel-Santos-da-Silva-Galdino-Mendes` |
| saulosaopedro | `colaborador/saulosaopedro` |

## 🚀 Como usar seu branch

### 1. Clonar o repositório (primeira vez)
```bash
git clone https://github.com/flaviocrispin/tecnica_programacao.git
cd tecnica_programacao
```

### 2. Fazer checkout do seu branch
```bash
git checkout colaborador/<seu-nome>
```

### 3. Criar ou modificar arquivos
Adicione seus projetos e exercícios no seu branch:
```bash
# Exemplo: criar uma pasta com seu nome
mkdir seu-nome
# Adicionar seus arquivos
# Seus arquivos aqui
```

### 4. Fazer commit e push
```bash
# Ver mudanças
git status

# Adicionar arquivos
git add .

# Fazer commit
git commit -m "Descrição das suas mudanças"

# Fazer push para seu branch
git push origin colaborador/<seu-nome>
```

## 💡 Boas práticas

- ✅ Sempre trabalhe no seu branch individual
- ✅ Faça commits frequentes com mensagens descritivas
- ✅ Faça push regularmente para não perder seu trabalho
- ✅ Use mensagens de commit em português ou inglês
- ❌ Não fazer push diretamente para `main`

## 🔄 Se quiser mesclar seu trabalho para main

1. Abra uma Pull Request (PR) do seu branch para `main`
2. Aguarde revisão
3. Após aprovação, a PR será mesclada

## 📞 Dúvidas?

Para dúvidas sobre git ou o workflow, abra uma issue no repositório.

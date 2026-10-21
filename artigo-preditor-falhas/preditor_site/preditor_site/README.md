# NETSEC Research — Detecção de intrusões em redes

Site acadêmico estático para apresentar o artigo comparativo entre Decision Tree, Random Forest e XGBoost aplicado ao conjunto UNSW-NB15.

## Estrutura

- `index.html`: página principal.
- `assets/css/style.css`: identidade visual responsiva (tema escuro de cibersegurança).
- `assets/js/main.js`: menu móvel.
- `assets/img/`: gráficos do experimento.
- `docs/artigo.md`: documento Markdown usado como base.
- `comparacao_modelos.csv`: resultados numéricos do experimento.

## Visualizar localmente

1. Extraia o ZIP.
2. Abra a pasta no VS Code.
3. Use a extensão Live Server para abrir `index.html`, ou execute um servidor local na pasta do projeto:

```powershell
py -m http.server 8000
```

4. Acesse `http://localhost:8000` no navegador.

A página principal é HTML/CSS/JavaScript estático e não requer instalação de dependências Python.

## Publicar no GitHub Pages

1. Crie um repositório público no GitHub (por exemplo, `artigo-preditor-falhas`).
2. Envie o conteúdo desta pasta para a raiz do repositório, mantendo `index.html` na raiz.
3. No GitHub, abra **Settings → Pages**.
4. Em **Build and deployment**, selecione **Deploy from a branch**, escolha `main` e `/ (root)`, e salve.
5. Aguarde a publicação e teste a URL em um celular e em outro navegador.

## Dataset e reprodução

O conjunto UNSW-NB15 deve ser obtido a partir da página oficial da UNSW: https://research.unsw.edu.au/projects/unsw-nb15-dataset. Os arquivos do dataset não são incluídos neste pacote.

## Autoria e privacidade

Autores listados no artigo: Eduardo Quintino Filho, Felipe Veiga da Silva, Henrique de Aguiar Fernandes, Niccolas Lupetti dos Santos e Tharik Lima dos Santos. Adicione fotos, biografias e links profissionais somente após confirmar o conteúdo e obter o consentimento explícito de cada integrante.

## Observações antes da entrega

- Confira as figuras e legendas no navegador.
- Substitua/adicione os gráficos de matrizes de confusão originais se quiser exibi-los como figuras; nesta primeira versão os valores foram montados como matrizes HTML acessíveis.
- Preencha o endereço público do repositório após criá-lo.
- O site apresenta os resultados e limitações conhecidos; revise o artigo Markdown separadamente na etapa de revisão geral combinada.

# denise
Arquivos de configuração e informações para denise.matehackers.org

### Github

Renomeando o branch master para main (depois do primeiro commit)

```
git checkout -b main master     # crie e mude para o branch main
git push -u origin main         # envie o branch main para o repositório remoto
git branch -d master            # delete o repositório local master
```

Vá para a interface web. Configurações do repositório (repository settings), branches. Selecione "main" como o novo branch padrão (default).

```
git push --delete origin master   # delete branch master remoto
git remote prune origin           # delete o rastreamento desse branch
```

#!/bin/bash
## Download de todos vídeos do Matehackers espalhados por aí

## Menor tamanho possível (em espaço no disco)
QUALIDADE='worstvideo+worstaudio/worst'

## Lista de opções
OPCOES=(
"--format ${QUALIDADE}" \
"--batch-file ${LISTA_YTDL}" \
"--id" \
"--mark-watched" \
"--continue" \
"--yes-playlist" \
"--write-description" \
"--write-info-json" \
"--write-annotations" \
"--write-thumbnail" \
#"--write-all-thumbnails" \
"--all-subs" \
"--verbose" \
## Comentar as duas próximas opções pra efetivamente fazer o download dos vídeos/áudios
"--simulate" \
"--skip-download" \
)

###
### Não deveria ser necessário mudar nada daqui pra baixo
###

LISTA="matevideos.txt"
if  [ ! -f ${LISTA} ]
then
  echo "Que-de-lhe a lista de vídeos? Pede no https://t.me/matehackerspoa"
  exit
fi

## Organiza a ordem das URLs por razões de transtorno obsessivo compulsivo
LISTA_YTDL="matevideos.ytdl.txt"
sort ${LISTA} | uniq 1> ${LISTA_YTDL}

## Garante última versão da ferramenta auxiliar
python3 -m pip install --user --upgrade pip youtube-dl

## Presumindo Debian/Linux
${HOME}/.local/bin/youtube-dl ${OPCOES}


#!/bin/bash
## Download de todos vídeo do Matehackers

LISTA_NOVA="matevideos.txt"
LISTA="matevideos.ytdl.txt"

if  [ ! -f ${LISTA_NOVA} ]
then
  echo "Que-de-lhe a lista de vídeos? Pede no https://t.me/matehackerspoa"
  exit
fi

sort ${LISTA_NOVA} | uniq 1> ${LISTA}

## Menor tamanho possível
QUALIDADE='worstvideo+worstaudio/worst'
## Melhor qualidade possível
#QUALIDADE='bestvideo+bestaudio/best'

python3 -m pip install --user --upgrade youtube-dl

${HOME}/.local/bin/youtube-dl \
--format ${QUALIDADE} \
--batch-file ${LISTA} \
--ignore-errors \
--id \
--mark-watched \
--continue \
--yes-playlist \
--write-description \
--write-info-json \
--write-annotations \
--write-thumbnail \
--all-subs \
--verbose

## Usar estas opções para testar o script
#--simulate \
#--skip-download \


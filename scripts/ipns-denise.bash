#!/bin/bash
## Atualiza IPNS para denise.matehackers.org
## Atualmente ipns/denise.matehackers.org aponta para bafybeiduhsvjotywptuavwbbzwu27zhhc73girdmj5onwtlftvubh72ewy

## Diretório para arquivar
DIRETORIO="/var/www/denise"

ipfs name publish $(ipfs add --cid-version 1 -r -Q ${DIRETORIO})


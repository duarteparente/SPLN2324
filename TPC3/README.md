## TPC3

Gerador de templates de ficheiros de configuração para packages python

#### Estratégia adotada

São interpoladas as variáveis **author**, **email**, **project**, correspondentes às informações do autor e respetivo nome do package.

###### 1º Opção

Indicação do valor das variáveis configuráveis através de flags

- -n : Nome do Projeto
- -a : Nome do Autor
- -e : Email do Autor

###### 2º Opção

- Caso não sejam detetadas as flags relativas às informações do autor, será consultado um eventual ficheiro de metadados ```.metadata.json``` que terá de estar situado na root, e terá de conter as chaves **author** e **email**.

- Na eventualidade da falha na deteção do ficheio, a inferência do nome do autor será através do username do utilizador com sessão iniciada na linha de comandos, não sendo possível inferir o email do mesmo.

- Em relação ao nome do package, este será inferido na eventual deteção de 1 único ficheiro python na atual diretoria.
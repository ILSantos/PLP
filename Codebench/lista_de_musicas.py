#!/usr/bin/python3 

""" 
O Professor Leafar gosta de música e tem uma coleção de arquivos MP3. Ele quer montar uma playlists de músicas
para escutar quando sai para correr, mas como ele não é muito bom com programação, pediu sua ajuda. A músicas do
Prof. Leafar possuem as seguintes informações:
    Nome do artista
    Título da música
    Endereço do arquivo no disco
    Duração da música (em segundos)
Para gerar a lista, o professor lhe pediu para escrever um programa que lê a sua base de músicas e, depois, uma lista
de nomes de artistas e títulos de músicas que devem constar na playlist. Em seguida, para cada música que foi encontrada,
seu programa deve imprimir o número de músicas na lista, a duração da lista e, claro, os arquivos que o professor deverá
copiar para seu pen drive. A lista pode conter entradas repetidas. Mas a duração da lista tem um limite. Veja as restrições
ao final do enunciado.

Entrada
A entrada será uma sequência de números inteiros e strings. As strings serão combinações de quaisquer caracteres
imprimíveis (isto é, excluem-se apenas caracteres de controle), exceto brancos. O primeiro valor da entrada será
um inteiro N, indicando o número de músicas da base. A base terá no máximo 100 músicas. Em seguida, aparecem N registros.
Cada registro possui uma palavra que representa o nome do autor e uma palavra que representa o nome da
música, seguida de uma palavra que representa o endereço do arquivo da música no disco. Todas as palavras são strings
com no máximo 100 caracteres e não contêm espaços. Finalmente, o quarto valor é a duração da música em segundos (pelo
menos 1 e no máximo 5400 segundos). Cada parte da entrada aparece em uma única linha. Após a lista de músicas, haverá
um inteiro Q indicando o número de músicas que o professor deseja tentar adicionar à playlist. As 2×Q palavras seguintes
serão os nomes dos artistas e os títulos das suas respectivas músicas que o professor tentará incluir na playlist.

Saída
A saída deve conter várias linhas. Se a lista resultante contiver R músicas, então a primeira linha deve ter o texto
Lista gerada com R musicas e duração MM:SS Sendo que MM:SS deve representar a duração total da lista em minutos e
segundos. Note que a lista deve possuir no máximo 60 minutos (ver restrições a seguir). As R linhas seguintes devem
conter os nomes dos arquivos com as músicas.

Restrições
O Prof. Leafar é impaciente. Portanto a lista deve ter no máximo 60 minutos (3600 segundos). Não inclua nenhuma música
na playlist se ela fizer o tempo total ser maior que 60 minutos.

    Entrada:    8

                halc
                Earthbound-'The_Great_Blizzard_of_9X'
                ~/musicas/OCReMiX/blizzard.mp3
                204

                Navi
                PaRappa_The_Rapper-'Cooking_with_Fire'
                ~/musicas/OCReMiX/parappa.mp3
                230

                Detective_Tuesday_&_Melody
                Phoenix_Wright-'Spirit_of_Law'
                ~/musicas/OCReMiX/spirit.mp3
                266

                Tyler_Heath
                Chrono_Trigger-'Predetermination'
                ~/musicas/OCReMiX/predetermination.mp3
                420

                WillRock
                Sonic_the_Hedgehog-'Clockwork_Criminal'
                ~/musicas/OCReMiX/clockwork.mp3
                328

                Benjamin_Briggs
                Super_Mario-'Fleeting_Ecstasy'
                ~/musicas/OCReMiX/fleeting.mp3
                412

                OA
                Lufia2-'Last_Chance'
                ~/musicas/OCReMiX/last-chance.mp3
                456

                Disco_Dan
                Mega_Man_3-'Hot_Pursuit_in_the_Lost_City'
                ~/musicas/OCReMiX/hot.mp3
                706

                4

                halc
                Earthbound-'The_Great_Blizzard_of_9X'

                OA
                Lufia2-'Last_Chance'

                Benjamin_Briggs
                Never_Gonna_Give_You_Up

                Detective_Tuesday_&_Melody
    Saída:      Lista gerada com 3 musicas e duracao 15:26
                ~/musicas/OCReMiX/blizzard.mp3
                ~/musicas/OCReMiX/last-chance.mp3
                ~/musicas/OCReMiX/spirit.mp3
"""

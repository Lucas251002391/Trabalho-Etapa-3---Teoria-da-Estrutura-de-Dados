Sistema de Gestão Hospitalar

Disciplina: Teoria das Estruturas de Dados
Aluno: Lucas de Freitas Fonseca (RA 251-002391)
Tema sorteado: Tema 1 - Sistema de Gestão Hospitalar

Esse é o trabalho final da disciplina. É um sistema feito em Python, rodando pelo terminal, que usa as quatro estruturas que estudamos (Fila, Pilha, Lista e Árvore) para controlar a parte lógica de um hospital. Os dados podem ser salvos e carregados de um arquivo de texto, para não se perderem quando o programa fecha.


COMO EXECUTAR

1. Ter o Python 3 instalado no computador.
2. Baixar o arquivo main.py deste repositório.
3. Abrir o terminal na pasta onde está o main.py e digitar: python main.py
   (se não funcionar, digitar: python3 main.py)
4. Vai aparecer o menu principal. É só digitar o número da opção e apertar ENTER.

O sistema começa vazio. Para ter os dados de uma vez anterior é preciso usar a opção 6 (Carregar dados). Para guardar o que foi feito, usar a opção 5 (Salvar dados) ou responder S quando o programa pergunta na hora de sair. O arquivo dados_sistema.txt é criado sozinho na mesma pasta do main.py na primeira vez que salva.

Observação: não usar o caractere | quando for digitar os dados, pois ele é o separador usado no arquivo de texto.


JUSTIFICATIVA DAS ESTRUTURAS

Fila - Triagem de pacientes (deque)
Na triagem o paciente que chegou primeiro tem que ser atendido primeiro, ou seja, é o FIFO (primeiro a entrar, primeiro a sair). O paciente entra no fim com append() e sai do início com popleft(). Usei o deque e não a list normal, pois tirar o primeiro item de uma list faz o Python ter que puxar todos os outros uma posição para frente, e isso fica lento conforme a fila cresce. O deque foi feito para inserir e remover nas pontas de forma rápida. Não deixei remover paciente do meio da fila, pois isso quebraria o FIFO. No atualizar só muda a prioridade, mas o paciente continua na mesma posição.

Pilha - Histórico de prontuários acessados (deque)
O médico quase sempre quer revisar o último prontuário que abriu, então o mais recente tem que ficar mais à mão. Isso é o LIFO (último a entrar, primeiro a sair), igual uma pilha de papéis em cima da mesa. O prontuário entra no topo com append() e sai do topo com pop(). Para ver o topo uso pilha[-1] e para listar do topo até a base uso reversed(pilha). Atualizar e remover só funcionam no prontuário do topo, pois mexer no meio da pilha não faz sentido para essa estrutura.

Lista - Pacientes internados e leitos (list)
Os pacientes internados não seguem ordem de chegada nem de saída, um paciente pode ter alta a qualquer momento. Por isso precisava de uma estrutura que deixasse mexer em qualquer posição, e a list permite isso por índice ou buscando pelo dado (no meu caso pelo nome do paciente). Também uso a lista para verificar se um leito já está ocupado antes de cadastrar um novo paciente nele.

Árvore - Especialidades e diagnósticos (dicionários aninhados)
As especialidades são organizadas de forma hierárquica: uma área (Clínica Geral) tem várias especialidades (Cardiologia, Ortopedia) e cada especialidade tem vários diagnósticos (Arritmia, Fratura). Isso é uma árvore, igual as pastas de um computador. Como o Python não tem árvore pronta, fiz com dicionários dentro de dicionários. Cada chave é um nó e o valor dela é outro dicionário com os filhos. O diagnóstico é a folha, então recebe um dicionário vazio {}, pois não tem filhos.
Escolhi 3 níveis fixos (área > especialidade > diagnóstico), pois é o que o hospital precisa e assim consigo percorrer a árvore com 3 for, um para cada nível. Não usei árvore binária, pois uma especialidade pode ter mais de dois diagnósticos e a binária só deixa ter no máximo dois filhos.


PERSISTÊNCIA

Tudo é salvo em um único arquivo, o dados_sistema.txt. Cada linha começa com o nome da estrutura e depois vem os dados separados por |, por exemplo:

FILA|205|Roberto Alves|ALTA
PILHA|Carlos|Consulta cardiologia|40|12345678901
LISTA|Ana|Pneumonia|70|11122233344|Asma|10/11/2026|4
ARVORE|Clinica Geral|Cardiologia|Arritmia

Para salvar, percorro cada estrutura com for e escrevo uma linha para cada item. Para carregar, leio o arquivo linha por linha, separo com split('|') e olho a primeira parte para saber para qual estrutura vai. Os números (ID, idade e leito) voltam com int(), pois no arquivo tudo vira texto. Antes de carregar limpo as estruturas com clear() para não duplicar os dados. A ordem da fila e da pilha é mantida, pois salvo do primeiro ao último e carrego com append() na mesma ordem.


USO DE INTELIGÊNCIA ARTIFICIAL

Assim como fiz em alguns exercícios da lista de revisão, usei IA (Claude) de modo consultivo para entender como montar a árvore com dicionários aninhados e para revisar e corrigir erros do meu código. A estrutura dos menus e a validação das entradas com while, try/except e confirmação [S/N] são do jeito que aprendi no curso do Guanabara (Curso em Vídeo) e que já venho usando nos exercícios.
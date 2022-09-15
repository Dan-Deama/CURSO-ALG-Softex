Algoritmo "Vestibular"
//
// Autor(a)    : Danilo
// Data atual  : 27/07/2022
Var
   nome,turma, alunoa, alunob, alunoc, alunod, melhoraluno:caractere
   alunos,aprovados:inteiro
   nota,notaa,notab,notac,notad,maiornota:real
   aprova,aprovb,aprovc,aprovd: inteiro

Inicio
   escrevaL("-----Lista de Aprovados Vestibular-----")
   maiornota <-0
   aprovados<- 0
   para alunos <- 1 ate 100 faca
      escreval("Digite seu nome: ")
      leia(nome)
      escreval("Digite sua nota: ")
      leia(nota)
      Se nota >= 7 entao
         aprovados<- (aprovados+1)
      fimse
      Se (nota> maiornota) entao
         maiornota<- nota
         melhoraluno<- nome
      fimse
      escreva("Digite sua turma: [A][B][C][D] ")
      leia (turma)
      se (turma = "A") e (nota>= 7) entao
         aprova<- aprova + 1
         se (turma = "A") e (nota> notaa) entao
            alunoa<- (nome)
            notaa<- (nota)
         fimse
      fimse
      se (turma = "B") e (nota>= 7) entao
         aprovb<- (aprovb + 1)
      fimse
      se (turma = "B") e (nota> notab) entao
         alunob<- (nome)
         notab<- (nota)
      fimse
      se (turma = "C") e (nota>= 7) entao
         aprovc<- (aprovc + 1)
      fimse
      se (turma = "C") e (nota>notac) entao
         notac<- (nota)
         alunoc<- (nome)
      fimse
      se (turma = "D") e (nota>notad) e (nota>= 7) entao
         aprovd<- (aprovd + 1)
      fimse
      se (turma = "D") e (nota>notad) entao
         notad<- (nota)
         alunod<- (nome)
      fimse
   fimpara
   Escreval ("Quantidade de aprovados= ",aprovados,".")
   Escreval ("Quantidade de aprovados na turma A= ",aprova,".")
   Escreval("A maior nota turma A foi ", notaa,", do(a) aluno(a), ", alunoa,".")
   Escreval ("Quantidade de aprovados na turma B= ",aprovb,".")
   Escreval("A maior nota turma B foi ", notab,", do(a) aluno(a), ", alunob,".")
   Escreval ("Quantidade de aprovados na turma C= ",aprovc,".")
   Escreval("A maior nota turma C foi ", notac,", do(a) aluno(a), ", alunoc,".")
   Escreval ("Quantidade de aprovados na turma D= ",aprovd,".")
   Escreval("A maior nota turma D foi ", notad,", do(a) aluno(a), ", alunod,".")
Fimalgoritmo
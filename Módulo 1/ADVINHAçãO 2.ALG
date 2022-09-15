Algoritmo "Advinhação"
//Aluno: Danilo Augusto da SIlva Deama
//
Var
   resultado, input: caractere

Inicio
   //
   escreval("Escolha um dos veículos exibidos abaixo, e não diga para ninguém: ")
   escreval("Trator")
   escreval("Moto")
   escreval("Bicicleta")
   escreval("Trem")
   escreval("Carro")
   escreval("Caminhão")
   escreval("Ônibus")
   escreval("Paraquedas")
   escreval("Balão")
   escreval("Avisão")
   escreval("Helicóptero")
   escreval("Submarino")
   escreval("Barco")
   escreval("Navio")
   escreval("Lancha")
   escreval("Agora responda às seguintes perguntas com: S ou N, e eu vou adivinhar qual deles você escolheu: ")
   escreval("É terrestre? (s/n)")
   escreval("")
   leia(input)
   SE(input = "s") ENTAO
      escreval("Cabe apenas uma pessoa? (s/n)")
      leia(input)
      SE(input = "s") ENTAO
         escreval("É pesado?(s/n)")
         leia(input)
         SE(input = "s") ENTAO
            Resultado <- ("Trator")
         SENAO
            escreval("Tem pedal?(s/n)")
            leia(input)
            SE (input = "s") ENTAO
               Resultado <- ("Bicicleta")
            SENAO
               Resultado <- ("Moto")
            FIMSE
         FIMSE
      SENAO
         escreva("Anda sobre trilhos?(s/n)")
         leia(input)
         SE (input = "s") ENTAO
            Resultado <- ("Trem")
         SENAO
            escreval("É feito para transportar cargas?(s/n)")
            leia(input)
            SE (input = "s") ENTAO
               Resultado <- ("Caminhão")
            SENAO
               escreval("É um meio de transporte público?(s/n)")
               leia(input)
               SE (input = "s") ENTAO
                  Resultado <- ("Ônibus")
               SENAO
                  Resultado <- ("Carro")
               FIMSE
            FIMSE
         FIMSE
      FIMSE
   SENAO
      escreval("É aéreo?(s/n)")
      leia(input)
      SE (input = "s") ENTAO
         escreval("Tem motor?(s/n)")
         leia(input)
         SE (input = "s") ENTAO
         escreval("Tem asas fixas?(s/n)")
            leia(input)
            SE (input = "s") ENTAO
               Resultado <- ("Avião")
            SENAO
               Resultado <- ("Helicóptero")
            FIMSE
         SENAO
        escreval("Ele sobe?(s/n)")
            leia(input)
            SE (input = "s") ENTAO
               Resultado <- ("Balão")
            SENAO
               Resultado <- ("Paraquedas")
            FIMSE
         FIMSE
      SENAO
         escreval("Anda sobre a água?")
         leia(input)
         SE (input = "s") ENTAO
            escreval("Tem um volante ou um timão?(s/n)")
            leia(input)
            SE (input = "s") ENTAO
               escreval("É grande?")
               leia(input)
               SE (input = "s") ENTAO
                  Resultado <- ("Navio")
               SENAO
                  Resultado <- ("Lancha")
               FIMSE
            SENAO
               Resultado <- ("Barco")
            FIMSE
         SENAO
            Resultado <- ("Submarino")
         FIMSE
      FIMSE
   FIMSE
   escreval("Então, o transporte escolhido foi ", resultado)
   escreval("Acertei?")
   leia(input)
   SE (input = "s") ENTAO
      escreval("AHA! Eu te avisei!")
   SENAO
      escreval("Impossível!!! você deve ter mentido em alguma resposta…")
   FIMSE

Fimalgoritmo

INSTRUÇÕES DO PROJETO
Pesquise sobre padrões de projeto e escolha um para apresentar e descrever o seu funcionamento. Além disso, explique quais as vantagens e desvantagens comparados a outros e mostre suas referências.

Resolução:

Selecionei o Padrão Prototype, que consiste num padrão de projeto criacional que permite a criação de novos objetos a partir da clonagem de um modelo original,
que é o protótipo.
A estrutura desse padrão consiste em 3 elementos: 
1. o Prototype: uma classe que declara uma interface para objetos capazes de clonar a si mesmo;
2. prototype concreto — implementação de um prototype;
3. cliente — cria um novo objeto através de um prototype que é capaz de clonar a si mesmo.

Vantagem: Facilita a criação de objetos com as mesmas propriedades do protótipo, agilizando a programação e a criação dos novos objetos.
Em Javascript, onde quase tudo é um objeto, é possível estender e modificar métodos e propriedades de praticamente qualquer coisa com Prototype.

Desvantagem: Caso a aplicação necessite da criação de objetos complexos, com propriedades variadas, o uso do Prototype perde o sentido.

fontes: 

https://www.patterns.dev/posts/classic-design-patterns/#prototypepatternjavascript

https://pt.quora.com/O-que-%C3%A9-prototype-em-JavaScript

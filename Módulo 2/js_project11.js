const dog = {
    nome: 'Sakura',
    idade: 10,
    raca: 'viralata',
    comidas: ['carne', 'bifinho', 'ração úmida', 'lixo']
}
function checkStatus() {
    for(const status in dog) {
        console.log(`${status}: ${dog[status]}`)
    }
    console.log()
}

function Comidas() {
    console.log('Comida: ')
    for (const check of dog.comidas) {
        console.log(check)
    }
}

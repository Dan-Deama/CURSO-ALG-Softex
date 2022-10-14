(async () => {

    const database = require('./db');
    const Produto = require('./produto');
    await database.sync();

    const novoProduto = await Produto.create({
        nome: 'Feijão',
        preco: 5,
        descricao: 'Feijão Meu Biju 1 KG'
    })
    console.log(novoProduto);
})();
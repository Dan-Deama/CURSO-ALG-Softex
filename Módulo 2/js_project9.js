class  Banco {
    constructor(conta, saldo, tipo, agencia) {
        this.conta = conta;
        this.saldo = saldo;
        this.tipo = tipo;
        this.agencia = agencia;
    }

    agenciaeconta () {
        console.log(this.agencia)
        console.log(this.conta)
    }

    buscar_saldo () {
        console.log(this.saldo)
    }

    deposito(valor){
        const saldo = this.saldo + valor
        this.saldo = saldo
        console.log(saldo)

    }

    saque (valor) {
        const saque = this.saldo - valor
        this.saldo = saque
        console.log(saque)
    }
    tipo_conta(){
        console.log(this.tipo)
    }
}

cliente = new Banco(1515,1300,'Poupança', 0o001)
cliente.buscar_saldo()
cliente.deposito(200)
cliente.saque(500)
cliente.agenciaeconta()
cliente.tipo_conta()

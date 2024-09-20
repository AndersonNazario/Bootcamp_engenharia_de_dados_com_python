const valorSalario = parseFloat(gets());
const valorBeneficios = parseFloat(get());

const valorImposto = calcularImposto(valorSalario);

const saida = valorSalario - valorImposto + valorBeneficios;
print(saida.toFixed(2));

function calcularImposto(salario) {
    let alicota;
    if (salario >= 0 && salario <= 1100) {
        alicota = 0.05;
    } else if (salario >= 1100.01 && salario <= 2500.00) {
        //Atribui a licota de 5% mediante salario:
        alicota = 0.10;
    } else if (salario >= 2500.01){
        //Atribui a licota de 5% mediante salario:
        alicota = 0.15;
    }

    return alicota * salario;
}


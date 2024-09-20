import java.util.Scanner;

public class Desafio {
    public static void main(String[] args){
        //Lê os valores de entrada:
        scanner leitorDeEntradas = new Scanner(System.in);
        float valorSalario = leitorDeEntradas.nexxtFloat();
        float valorBeneficios = leitorDeEntradas.nexxtFloat();

        float valorImposto = 0;
        if (valorSalario >= 0 && valorSalario <= 1100) {
            //Atribui a licota de 5% mediante salario:
            valorImposto = 0.05F * valorSalario;
        }
       else if (valorSalario >= 1100.01 && valorSalario <= 2500.00) {
            //Atribui a licota de 5% mediante salario:
            valorImposto = 0.10F * valorSalario;
        } else (valorSalario >= 2500.01) {
            //Atribui a licota de 5% mediante salario:
            valorImposto = 0.15F * valorSalario;
        }

        //Calcular e imprimir saida (com 2 casas decimais):
        float saida = valorSalario - valorImposto + valorBeneficios;
        System.out.println(String.format("%.2F", saida));
    }
}
user System;
public class Desafio 
{
    public static void Main()
    {
        //Lê os valores de entrada:
        float valorSalario = float.Parse(Console.ReadLine());
        float valorBeneficios = float.Parse(Console.ReadLine());

        float valorImposto = 0;
        if (valorSalario >= 0 && valorSalario <= 1100) 
        {
            //Atribui a licota de 5% mediante salario:
            valorImposto = 0.05F * valorSalario;
        }
       else if (valorSalario >= 1100.01 && valorSalario <= 2500.00) 
       {
            //Atribui a licota de 5% mediante salario:
            valorImposto = 0.10F * valorSalario;
        } 
        else (valorSalario >= 2500.01) 
        {
            //Atribui a licota de 5% mediante salario:
            valorImposto = 0.15F * valorSalario;
        }

        //Calcular e imprimir saida (com 2 casas decimais):
        float saida = valorSalario - valorImposto + valorBeneficios;
        Console.WriteLine(saida.ToString("0.00"));
    }
}
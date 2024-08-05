
class ConvertToRoman():
    """
    Classe para converter números inteiros em numerais romanos.
    """

    def __init__(self, num, option):
        self.num = num
        self.option = option

    def romano_to_int(self) -> str:
        # Mapeamento de numerais romanos para inteiros
        romano_to_int_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        # Variáveis para armazenar o resultado e o valor do numeral romano anterior
        total = 0
        valor_anterior = 0

        # Iterar sobre cada caractere do numeral romano, da direita para a esquerda
        
        for char in reversed(self.num.upper()):
            value = romano_to_int_map[char]

            # Se o valor atual é menor que o valor anterior, subtrair do total
            if value < valor_anterior:
                total -= value
            else:
                total += value

            # Atualizar o valor anterior
            valor_anterior = value

        return total

    def int_to_romano(self):
        """
        Converte um número inteiro para um numeral romano.

        Returns:
            str: O numeral romano correspondente ao número inteiro.
        """
        # Mapeamento de inteiros para numerais romanos
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        simbolos = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        num = int(self.num)
        while num > 0:
            for k in range(num // val[i]):
                roman_num += simbolos[i]
                num -= val[i]
            i += 1
        return roman_num

    def handle(self):
        try:
            converter = ConvertToRoman(num=self.num, option=self.option)
            if self.option == "Arábicos - Romanos":
                return converter.int_to_romano()
            elif self.option == "Romanos - Arábicos":
                return converter.romano_to_int()
            else:
                return "Opcao Inválida"
        except Exception as e:
            return str(e)

    if __name__ == '__main__':
        ...

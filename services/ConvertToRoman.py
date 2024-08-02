
class ConvertToRoman():
    def __init__(self, num, option):
        self.num = num
        self.option = option
    
    def roman_to_int(num):
        # Mapeamento de numerais romanos para inteiros
        roman_to_int_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        # Variáveis para armazenar o resultado e o valor do numeral romano anterior
        total = 0
        prev_value = 0
        
        # Iterar sobre cada caractere do numeral romano, da direita para a esquerda
        for char in reversed(s):
            value = roman_to_int_map[char]
            
            # Se o valor atual é menor que o valor anterior, subtrair do total
            if value < prev_value:
                total -= value
            else:
                total += value
            
            # Atualizar o valor anterior
            prev_value = value
        
        return total    
    
    def int_to_roman(num):
        # Mapeamento de inteiros para numerais romanos
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
    
    def handle(num, option):
       try: 
            converter = ConvertToRoman(num, option)
            if option == '1':
                return converter.int_to_roman()
            elif option == '2':
                return converter.roman_to_int()
            else:
                return "Opcao Inválida"
       except Exception as e:
            return str(e)
    
    if __name__ == '__main__':
        ...
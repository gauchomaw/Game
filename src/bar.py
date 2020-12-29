
# Cria uma barra horizontal
class Bar():

    # actual = progressão atual
    # total = progressão máxima
    # len = tamanho da barra
    def __init__(self, actual, total, maxLen = 30):
        
        # total não pode ser zero (erro de divisão)
        if total <= 0:
            total = 1
        
        # Atual não pode ser maior que o total
        if actual > total:
            actual = total
        
        # a barra mínima terá 30 caracteres = ou -
        if maxLen < 30:
            maxLen = 30 

        self.actual = actual
        self.total = total
        self.maxLen = maxLen
    
    def show(self):    
        bar_len = self.maxLen
        filled_len = int(round(bar_len * self.actual / self.total))
        percents = int(round(self.total * self.actual / self.total, 1))
        bar = '=' * filled_len + '-' * (bar_len - filled_len)

        return('[%s] [%s/%s]' % (bar, percents, self.total))
        
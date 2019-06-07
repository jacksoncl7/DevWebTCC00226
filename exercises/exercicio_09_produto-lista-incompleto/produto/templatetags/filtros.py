from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

# Para usar esse filtro no template é preciso:
# 1. Acrescentar este tag no template: {% load filtros %}
# 2. E utilizar um pipe para aplicar o filtro: form.preco.value|separador_de_milhar
#                                              ou produto.preco|separador_de_milhar


@register.filter         # @register.filter(name='separador_de_milhar')
@stringfilter            # Se você está escrevendo um filtro que espera receber um string como primeiro argumento,
                         # você deveria utilizar o decorator stringfilter. Ele irá converter um objeto para um
                         # string antes de ser passado para a função.
def separador_de_milhar(valor, decimal_points=3, seperator=u'.'):
    valor = str(valor)
    valor = valor.replace('.', ',')
    pos_virgula = valor.find(',')
    if pos_virgula == -1:
        valor = valor + ',00'
    pos_virgula = valor.find(',')
    parte2 = valor[pos_virgula:]
    parte1 = valor[:pos_virgula]
    if len(parte1) <= decimal_points:
        return parte1 + parte2
    parts = []
    while parte1:
        parts.append(parte1[-decimal_points:])
        parte1 = parte1[:-decimal_points]
    # now we should have parts = ['345', '12']
    parts.reverse()
    # and the return value should be u'12.345'
    return seperator.join(parts) + parte2

# >>> x = "Hello World!"
# >>> x[2:]
# 'llo World!'
# >>> x[:2]
# 'He'

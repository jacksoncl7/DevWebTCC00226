from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from produto.forms import ProdutoForm, RemoveProdutoForm
from produto.models import Produto

def cadastra_produto(request):
    if request.POST:
        produto_id = request.POST.get('produto_id')
        if produto_id:
            produto = get_object_or_404(Produto, pk=produto_id)
            produto_form = ProdutoForm(request.POST, instance=produto)
        else:
            produto_form = ProdutoForm(request.POST)

        if produto_form.is_valid():
            produto = produto_form.save()
            if produto_id:
                messages.add_message(request, messages.INFO, 'Produto alterado com sucesso!')
            else:
                messages.add_message(request, messages.INFO, 'Produto cadastrado com sucesso!')
            return redirect('produto:exibe_produto', id=produto.id)
        else:
            messages.add_message(request, messages.ERROR, 'Corrija o(s) erro(s) abaixo.')
    else:
        produto_form = ProdutoForm()

    return render(request, 'produto/cadastra_produto.html', {'form': produto_form })


def exibe_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form_remove_produto = RemoveProdutoForm(initial={'produto_id': id})
    return render(request, 'produto/exibe_produto.html', {'produto': produto,
                                                          'form_remove_produto': form_remove_produto})


def edita_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    produto_form = ProdutoForm(instance=produto)
    produto_form.fields['produto_id'].initial = id
    return render(request, 'produto/cadastra_produto.html', {'form': produto_form })


def remove_produto(request):
    form_remove_produto = RemoveProdutoForm(request.POST)
    if form_remove_produto.is_valid():
        produto_id = form_remove_produto.cleaned_data['produto_id']
        produto = get_object_or_404(Produto, id=produto_id)
        produto.delete()
        messages.add_message(request, messages.INFO, 'Produto removido com sucesso.')
        return render(request, 'produto/exibe_produto.html', {'produto': produto})
    else:
        raise ValueError('Ocorreu um erro inesperado ao tentar remover um produto (produto_id não foi validado).')

















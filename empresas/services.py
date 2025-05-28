from django.core.exceptions import ObjectDoesNotExist
from .models import Empresa


def criar_empresa(nome, cnpj):
    empresa = Empresa.objects.create(nome=nome, cnpj=cnpj)
    return empresa


def listar_empresas():
    return Empresa.objects.all()


def buscar_empresa_por_id(empresa_id):
    try:
        return Empresa.objects.get(id=empresa_id)
    except Empresa.DoesNotExist:
        return None


def buscar_empresa_por_cnpj(cnpj):
    try:
        return Empresa.objects.get(cnpj=cnpj)
    except Empresa.DoesNotExist:
        return None


def atualizar_empresa(empresa_id, nome=None, cnpj=None):
    try:
        empresa = Empresa.objects.get(id=empresa_id)
        if nome:
            empresa.nome = nome
        if cnpj:
            empresa.cnpj = cnpj
        empresa.save()
        return empresa
    except Empresa.DoesNotExist:
        return None


def deletar_empresa(empresa_id):
    try:
        empresa = Empresa.objects.get(id=empresa_id)
        empresa.delete()
        return True
    except Empresa.DoesNotExist:
        return False

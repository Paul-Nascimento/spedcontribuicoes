from escrituracoes.models import (Registro0000, Registro0150, Registro0200,RegistroC100,RegistroC170,RegistroA100,RegistroA170,RegistroF100,
                                  RegistroF130,RegistroC500,RegistroC501,RegistroC505,RegistroD500,RegistroD501,RegistroD505,RegistroM100,
                                  RegistroM105,RegistroM200,RegistroM205,RegistroM210,RegistroM220,RegistroM225,RegistroM500,RegistroM505,
                                  RegistroM600,RegistroM605,RegistroM610,RegistroM620,RegistroM625,RegistroD100,RegistroD101,RegistroD105,
                                  ZFiscal,FBL3N)
from django.db import transaction
from datetime import datetime
import pandas as pd
from datetime import datetime
from .models import ZFiscal
from decimal import Decimal

def gerar_id_registro_0000(cnpj, competencia):
    return f"{cnpj}_{competencia}"

@transaction.atomic
def inserir_blocos_efd_contrib(data):
    cnpj = data['empresa_cnpj']
    competencia = data['competencia']
    registros_0000 = data.get('registros_0000', [])
    registros_0150 = data.get('registros_0150', [])
    registros_0200 = data.get('registros_0200', [])
    
    registros_a100 = data.get("registros_a100", [])
    registros_a170 = data.get('registros_a170', [])

    registros_c100 = data.get('registros_c100', [])
    registros_c170 = data.get('registros_c170', [])

    registros_c500 = data.get('registros_c500', [])
    registros_c501 = data.get('registros_c501', [])
    registros_c505 = data.get('registros_c505', [])
    

    registros_d100 = data.get('registros_d100', [])
    registros_d101 = data.get('registros_d101', [])
    registros_d105 = data.get('registros_d105', [])


    registros_d500 = data.get('registros_d500', [])
    registros_d501 = data.get('registros_d501', [])
    registros_d505 = data.get('registros_d505', [])

    registros_f100 = data.get('registros_f100', [])
    registros_f130 = data.get('registros_f130', [])

    registros_m100 = data.get('registros_m100', [])
    registros_m105 = data.get('registros_m105', [])
    registros_m500 = data.get('registros_m500', [])
    registros_m505 = data.get('registros_m505', [])

    registros_m200 = data.get('registros_m200', [])
    registros_m205 = data.get('registros_m205', [])
    registros_m210 = data.get('registros_m210', [])
    registros_m220 = data.get('registros_m220', [])
    registros_m225 = data.get('registros_m225', [])
    
    registros_m600 = data.get('registros_m600', [])
    registros_m605 = data.get('registros_m605', [])
    registros_m610 = data.get('registros_m610', [])
    registros_m620 = data.get('registros_m620', [])
    registros_m625 = data.get('registros_m625', [])


    # Criar ou obter o Registro0000
    #id_0000 = gerar_id_registro_0000(cnpj, competencia)
    

    print(registros_0000[0])
    registro_0000 = Registro0000.objects.create(
        **registros_0000[0]
    )

    # Inserir registros 0150
    for reg_0150 in registros_0150:
        Registro0150.objects.create(
            registro_0000=registro_0000,
            **reg_0150
        )
    # Inserir registros 0200
    for reg_0200 in registros_0200:
        
        # Criação do registro no banco
        Registro0200.objects.create(
            registro_0000=registro_0000,
            **reg_0200
        )
    
    for reg_a100 in registros_a100:
        # Criação do registro no banco
        print(reg_a100)
        RegistroA100.objects.create(
            registro_0000=registro_0000,
            **reg_a100
        )

    for reg_a170 in registros_a170:
        
        print(reg_a170)
        id_a100 = reg_a170.pop('id_a100')  
        print(id_a100)
        instancia_a100 = RegistroA100.objects.get(registro_0000=registro_0000,id_a100=id_a100)
        
        # Criação do registro no banco
        RegistroA170.objects.create(
            id_a100=instancia_a100,
            **reg_a170
        )

    for reg_c100 in registros_c100: 
        # Criação do registro no banco
        RegistroC100.objects.create(
            registro_0000=registro_0000,
            **reg_c100
        )

    for reg_c170 in registros_c170:
             
        id_c100 = reg_c170.pop('id_c100')  # ou 'registro_c100' dependendo do nome do campo
        instancia_c100 = RegistroC100.objects.get(registro_0000=registro_0000,id_c100=id_c100)
        
        # Criação do registro no banco
        RegistroC170.objects.create(
            id_c100=instancia_c100,
            **reg_c170
        )

    for reg_c500 in registros_c500:
         # Criação do registro no banco
        print(reg_c500)
        RegistroC500.objects.create(
            registro_0000=registro_0000,
            **reg_c500
        )

    for reg_c501 in registros_c501:
        print(reg_c501)
        id_c500 = reg_c501.pop('id_c500')  # Retira o ID usado para o relacionamento
        print(f'id_c500 (C501): {id_c500}')
        
        instancia_c500 = RegistroC500.objects.get(registro_0000=registro_0000,id_c500=id_c500)  # Busca a instância relacionada

        RegistroC501.objects.create(
            id_c500=instancia_c500,
            **reg_c501
        )

    for reg_c505 in registros_c505:
        print(reg_c505)
        id_c500 = reg_c505.pop('id_c500')  # Retira o ID usado para o relacionamento
        print(f'id_c500 (C505): {id_c500}')
        
        instancia_c500 = RegistroC500.objects.get(registro_0000=registro_0000,id_c500=id_c500)  # Busca a instância relacionada

        RegistroC505.objects.create(
            id_c500=instancia_c500,
            **reg_c505
        )
    
    for reg_d100 in registros_d100:
         # Criação do registro no banco
        print(reg_d100)
        RegistroD100.objects.create(
            registro_0000=registro_0000,
            **reg_d100
        )

    for reg_d101 in registros_d101:
        #print(reg_c501)
        id_d100 = reg_d101.pop('id_d100')  # Retira o ID usado para o relacionamento
        #print(f'id_c500 (C501): {id_c500}')
        
        instancia_d100 = RegistroD100.objects.get(registro_0000=registro_0000,id_d100=id_d100)  # Busca a instância relacionada
        
        RegistroD101.objects.create(
            registro_d100=instancia_d100,
            **reg_d101
        )

    for reg_d105 in registros_d105:
        #print(reg_d105)
        id_cd100 = reg_d105.pop('id_d100')  # Retira o ID usado para o relacionamento
        #print(f'id_c500 (C505): {id_c500}')
        
        instancia_d100 = RegistroD100.objects.get(registro_0000=registro_0000,id_d100=id_d100)  # Busca a instância relacionada

        RegistroD105.objects.create(
            registro_d100=instancia_d100,
            **reg_d105
        )
    
    for reg_d500 in registros_d500:
        print(reg_d500)
        RegistroD500.objects.create(
            registro_0000=registro_0000,
            **reg_d500
        )

    for reg_d501 in registros_d501:
        print(reg_d501)
        id_d500 = reg_d501.pop('id_d500')  # Retira o ID usado para o relacionamento
        print(f'id_d500 (D501): {id_d500}')
        
        instancia_d500 = RegistroD500.objects.get(registro_0000=registro_0000,id_d500=id_d500)  # Busca a instância relacionada

        RegistroD501.objects.create(
            id_d500=instancia_d500,
            **reg_d501
        )

    for reg_d505 in registros_d505:
        print(reg_d505)
        id_d500 = reg_d505.pop('id_d500')  # Retira o ID usado para o relacionamento
        print(f'id_d500 (D505): {id_d500}')
        
        instancia_d500 = RegistroD500.objects.get(registro_0000=registro_0000,id_d500=id_d500)  # Busca a instância relacionada

        RegistroD505.objects.create(
            id_d500=instancia_d500,
            **reg_d505
        )

    for reg_f100 in registros_f100:
        
         # Criação do registro no banco
        RegistroF100.objects.create(
            registro_0000=registro_0000,
            **reg_f100
        )

    for reg_f130 in registros_f130:
        
         # Criação do registro no banco
        RegistroF130.objects.create(
            registro_0000=registro_0000,
            **reg_f130
        )

    for reg_m100 in registros_m100:
        
        print(reg_m100)
        RegistroM100.objects.create(
            registro_0000=registro_0000,
            **reg_m100
        )

    for reg_m105 in registros_m105:
        print(reg_m105)
        RegistroM105.objects.create(
            registro_0000=registro_0000,
            **reg_m105
        )

    for reg_m200 in registros_m200:
        
        RegistroM200.objects.create(
            registro_0000=registro_0000,
            **reg_m200
        )

    for reg_m205 in registros_m205:
        print(reg_m205)
        RegistroM205.objects.create(
            registro_0000=registro_0000,
            **reg_m205
        )

    for reg_m210 in registros_m210:
        RegistroM210.objects.create(
            registro_0000=registro_0000,
            **reg_m210
        )

    for reg_m220 in registros_m220:
        RegistroM220.objects.create(
            registro_0000=registro_0000,
            **reg_m220
        )

    for reg_m225 in registros_m225:
        print(reg_m225)
        RegistroM225.objects.create(
            registro_0000=registro_0000,
            **reg_m225
        )

    for reg_m500 in registros_m500:
        RegistroM500.objects.create(
            registro_0000=registro_0000,
            **reg_m500
        )

    for reg_m505 in registros_m505:
        RegistroM505.objects.create(
            registro_0000=registro_0000,
            **reg_m505
        )

    for reg_m600 in registros_m600:
        RegistroM600.objects.create(
            registro_0000=registro_0000,
            **reg_m600
        )

    for reg_m605 in registros_m605:
        RegistroM605.objects.create(
            registro_0000=registro_0000,
            **reg_m605
        )

    for reg_m610 in registros_m610:
        RegistroM610.objects.create(
            registro_0000=registro_0000,
            **reg_m610
        )

    for reg_m620 in registros_m620:
        RegistroM620.objects.create(
            registro_0000=registro_0000,
            **reg_m620
        )

    for reg_m625 in registros_m625:
        print(reg_m625)
        RegistroM625.objects.create(
            registro_0000=registro_0000,
            **reg_m625
        )

    return registro_0000

def converter_data(valor):
    try:
        if pd.isna(valor) or str(valor).strip() == "":
            return None
        data = pd.to_datetime(valor, dayfirst=True, errors='coerce')
        if pd.isna(data):
            return None
        return data.date()
    except:
        return None

def truncar(valor, limite):
    if valor is None:
        return ""
    return str(valor)[:limite]

def converter_decimal(valor):
    try:
        return Decimal(str(valor).replace(",", "."))
    except:
        return None

def converter_int(valor):
    try:
        return int(valor)
    except:
        return None

def converter_bool(valor):
    return str(valor).strip().lower() in ["sim", "s", "true", "1"]


def inserir_fbl3n(dados):
    return FBL3N.objects.create(**dados)

def importar_planilha_zfiscal(caminho_arquivo):
    df = pd.read_excel(caminho_arquivo, dtype=str)  # Usa dtype=str para evitar erros de tipo
    df.fillna("", inplace=True)  # Preenche valores NaN com string vazia

    registros = []
    for _, row in df.iterrows():

        print(row)
        registro = ZFiscal(
            numero_doc_faturamento=truncar(row.get("Nº doc.faturamento", ""), 50),
            documento_compras=truncar(row.get("Documento de compras", ""), 50),
            numero_documento=row.get("Nº documento", ""),
            categoria_nf=row.get("Ctg.nota fiscal", ""),
            tipo_documento=row.get("Tipo de documento", ""),
            direcao_movimento=row.get("Dir.movim.mercads.", ""),
            data_documento=converter_data(row.get("Data documento", "")),
            data_lancamento=converter_data(row.get("Data de lançamento", "")),
            modelo_nf=truncar(row.get("Modelo nota fiscal", ""), 10),
            serie=row.get("Séries", ""),
            numero_nf=row.get("Nº nota fiscal", ""),
            nf_eletronica=row.get("Nº da nota fiscal eletrônica", ""),
            local_negocios=row.get("Local de negócios", ""),
            estornado=converter_bool(row.get("Estornado", "")),
            data_estorno=converter_data(row.get("Data de estorno", "")),
            status_documento=row.get("Status do documento", ""),
            id_parceiro=row.get("ID parceiro", ""),
            nome_parceiro=row.get("Nome 1", ""),
            regiao=row.get("Região", ""),
            cgc=truncar(row.get("Code CGC", ""), 14),
            cpf=truncar(row.get("NºCPF", ""),14),
            id_fiscal_regional=row.get("NºID fiscal regional", ""),
            moeda=row.get("Moeda do documento", ""),
            numero_item=converter_int(row.get("Nº item do documento", "")),
            material=row.get("Material", ""),
            grupo_mercadorias=row.get("Grupo de mercadorias", ""),
            descricao_material=row.get("Texto breve de material", ""),
            cfop=row.get("CFOP", ""),
            origem_material=row.get("Origem de material", ""),
            sit_tributaria_icms=row.get("Sit.tributária ICMS", ""),
            quantidade=converter_decimal(row.get("Quantidade", "")),
            unidade_medida=row.get("Unidade de medida", ""),
            centro=row.get("Centro", ""),
            codigo_imposto=row.get("Código de imposto", ""),
            lei_cofins=row.get("Lei COFINS", ""),
            lei_pis=row.get("Lei tributária PIS", ""),
            tipo_imposto=row.get("Tipo de imposto", ""),
            montante_basico=converter_decimal(row.get("Montante básico", "")),
            valor_fiscal=converter_decimal(row.get("Valor fiscal", "")),
            montante_base_excluido=converter_decimal(row.get("Mont.base excluído", "")),
            outro_montante_basico=converter_decimal(row.get("Outro mont.básico", "")),
            empresa=row.get("Empresa", ""),
            exercicio=row.get("Exercício", ""),
            codigo_transacao=row.get("Código de transação", ""),
            usuario=row.get("Nome do usuário", ""),
            referencia=row.get("Referência", ""),
            contrato_basico=row.get("Contrato básico", ""),
            centro_custo=row.get("Centro custo", ""),
            imobilizado=row.get("Imobilizado", ""),
            sub_numero=row.get("Subnº", ""),
            ordem=row.get("Ordem", ""),
            pep_elemento=row.get("Elemento PEP", ""),
            diagrama_rede=row.get("Diagrama de rede", ""),
            operacao_rede=row.get("Operacao diagrama de rede", ""),
            ficha_orcamentaria=row.get("Ficha orçamentária", ""),
            conta_razao=row.get("Conta do Razão", ""),
            tipo_doc_compras=row.get("Tp.doc.compras", ""),
            texto_parte1=row.get("Texto-parte1", ""),
            texto_parte2=row.get("Texto-parte2", ""),
            texto_parte3=row.get("Texto-parte3", ""),
            texto_parte4=row.get("Texto-parte4", "")
        )
        #registros.append(registro)
        registro.save()
    
    #ZFiscal.objects.bulk_create(registros)
    return f"{len(registros)} registros inseridos com sucesso."

def importar_planilha_fbl3n(caminho_arquivo):
    df = pd.read_excel(caminho_arquivo, dtype=str)
    df.fillna("", inplace=True)

    registros = []
    for _, row in df.iterrows():
        registro = FBL3N(
            atribuicao=truncar(row.get("Atribuição", ""), 50),
            empresa=truncar(row.get("Empresa", ""), 10),
            conta_razao=truncar(row.get("Conta do Razão", ""), 50),
            numero_documento=truncar(row.get("Nº documento", ""), 50),
            divisao=truncar(row.get("Divisão", ""), 10),
            tipo_documento=truncar(row.get("Tipo de documento", ""), 50),
            referencia=truncar(row.get("Referência", ""), 50),
            data_lancamento=converter_data(row.get("Data de lançamento", "")),
            data_documento=converter_data(row.get("Data do documento", "")),
            chave_lancamento=truncar(row.get("Chave de lançamento", ""), 50),
            montante_moeda_interna=converter_decimal(row.get("Montante em moeda interna", "")),
            moeda_interna=truncar(row.get("Moeda interna", ""), 10),
            doc_compensacao=truncar(row.get("Doc.compensação", ""), 50),
            texto=truncar(row.get("Texto", ""), 255),
            centro_custo=truncar(row.get("Centro custo", ""), 50),
            nome_usuario=truncar(row.get("Nome do usuário", ""), 50),
            elemento_pep=truncar(row.get("Elemento PEP", ""), 50),
            periodo_contabil=truncar(row.get("Período contábil", ""), 10),
            pedido=truncar(row.get("Pedido", ""), 50),
            contrato=truncar(row.get("Contrato", ""), 50)
        )
        registros.append(registro)

    FBL3N.objects.bulk_create(registros)
    return f"{len(registros)} registros FBL3N inseridos com sucesso."
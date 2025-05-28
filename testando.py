"""
identificação do arquivo
"""
from pathlib import Path
from datetime import datetime
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

codigos_iva = {
    'C0' : 'Não',
    'C1' : 'Não',
    'C2' : 'Não',
    'C3' : 'Não',
    'C4' : 'Não',
    'C5' : 'Não',
    'C7' : 'Não',
    'D0' : 'Sim',
    'D1' : 'Sim',
    'D2' : 'Sim',
    'D3' : 'Sim',
    'D4' : 'Sim',
    'D5' : 'Sim',
    'D6' : 'Sim',
    'D7' : 'Sim',
    'S1' : 'Não',
    'S2' : 'Não',
    'S3' : 'Não',
    'S4' : 'Não',
    'S5' : 'Não',
    'S6' : 'Não',
    'S7' : 'Não',
    'S8' : 'Não',
    'S9' : 'Não',
    'SA' : 'Não',
    'SB' : 'Não',
    'SC' : 'Sim',
    'SF' : 'Sim',
    'SG' : 'Sim',
    'SH' : 'Sim',
    'SJ' : 'Sim',
    'SK' : 'Sim',
    'SL' : 'Sim',
    'SM' : 'Sim',
    'SN' : 'Sim',
    'SO' : 'Sim',
    'SP' : 'Sim',
    'SQ' : 'Não',
    'SR' : 'Não',
    'SS' : 'Não',
    'ST' : 'Não',
    'SU' : 'Não',
    'SV' : 'Não',
    'U1' : 'Não',
    'U2' : 'Não',
    'U3' : 'Não',
    'U4' : 'Sim',
    'U5' : 'Sim',
    'W0' : 'Sim',
    'W1' : 'Não',
    'W2' : 'Sim',
    'W3' : 'Não',
    'W4' : 'Não',
    'W5' : 'Sim',
    'W6' : 'Sim',
    'W7' : 'Não',
    'W8' : 'Sim',
    'W9' : 'Não',
    'WA' : 'Sim',
    'WB' : 'Não',
    'WC' : 'Sim',
    'WD' : 'Não',
    'WE' : 'Não',
    'WF' : 'Sim',
    'WG' : 'Sim',
    'WH' : 'Não',
    'WI' : 'Não',
    'WJ' : 'Sim',
    'WK' : 'Não',
    'WL' : 'Não',
    'WM' : 'Sim',
    'WN' : 'Sim',
    'ZZ' : 'Sim'
}

desc_ind_oper = {
    '0': 'Entrada',
    '1': 'Saída'
}

desc_ind_emit = {
    '0': 'Emissão própria',
    '1': 'Terceiros'
}

desc_ind_pgto = {
    '0': 'À vista',
    '1': 'A prazo',
    '2': 'Outros'
}

desc_ind_orig_cred = {
    '0': 'Operações próprias',
    '1': 'Evento de incorporação, cisão ou fusão'
}

desc_ind_frt = {
    '0': 'Frete por conta do remetente (CIF)',
    '1': 'Frete por conta do destinatário (FOB)',
    '2': 'Frete por conta de terceiros',
    '3': 'Transporte próprio por conta do remetente',
    '4': 'Transporte próprio por conta do destinatário',
    '9': 'Sem ocorrência de transporte'
}

desc_cod_mod = {
    '1': "Nota Fiscal",
    "1B": "Nota Fiscal Avulsa",
    '4': "Nota Fiscal de Produtor",
    '6': "Nota Fiscal/Conta de Energia Elétrica",
    '7': "Nota Fiscal de Serviço de Transporte",
    '8': "Conhecimento de Transporte Rodoviário de Cargas",
    '9': "Conhecimento de Transporte Aquaviário de Cargas",
    '10': "Conhecimento Aéreo de Cargas",
    '11': "Conhecimento de Transporte Ferroviário de Cargas",
    '13': "Bilhete de Passagem Rodoviário",
    '14': "Bilhete de Passagem Aquaviário",
    '15': "Bilhete de Passagem e Nota de Bagagem",
    '21': "Nota Fiscal de Serviço de Comunicação",
    '22': "Nota Fiscal de Serviço de Telecomunicações",
    '23': "GNRE",
    '25': "Manifesto de Carga",
    '26': "Conhecimento de Transporte Multimodal de Cargas",
    '27': "Nota Fiscal de Transporte Ferroviário de Carga",
    '28': "Nota Fiscal/Conta de Fornecimento de Gás Canalizado",
    '29': "Nota Fiscal/Conta de Fornecimento de Água Canalizada",
    '55': "Nota Fiscal Eletrônica (NF-e)",
    '57': "Conhecimento de Transporte Eletrônico (CT-e)",
    '65': "Nota Fiscal de Consumidor Eletrônica (NFC-e)",
    '66': "Cupom Fiscal Eletrônico",
    '67': 'Conhecimento Eletrônico modelo 67'
    }

desc_cod_0200 = {
    
        '0': "Mercadoria para Revenda",
        '1': "Matéria-Prima",
        '2': "Embalagem",
        '3': "Produto em Processo",
        '4': "Produto Acabado",
        '5': "Subproduto",
        '6': "Produto Intermediário",
        '7': "Material de Uso e Consumo",
        '8': "Ativo Imobilizado",
        '9': "Serviços",
        '10': "Outros insumos",
        '99': "Outras"
}

desc_cod_sit = {
        '00': 'Documento regular',
        '01': 'Documento regular extemporâneo',
        '02': 'Documento cancelado',
        '03': 'Documento cancelado extemporâneo',
        '04': 'NF-e, CT-e ou NFC-e denegada',
        '05': 'NF-e, CT-e ou NFC-e – Numeração inutilizada',
        '06': 'Documento fiscal complementar',
        '07': 'Documento fiscal complementar extemporâneo',
        '08': 'Documento fiscal emitido com base em Regime Especial ou Norma específica'
    }

desc_cst_pis = {
        '1': 'Operação tributável – base de cálculo = valor da operação alíquota normal cumulativo/não cumulativo',
        '2': 'Operação tributável – base de cálculo = valor da operação (alíquota diferenciada)',
        '3': 'Operação tributável – base de cálculo = quantidade vendida × alíquota por unidade de produto',
        '4': 'Operação tributável – monofásica – revenda a alíquota zero',
        '5': 'Operação tributável – substituição tributária',
        '6': 'Operação tributável – alíquota zero',
        '7': 'Operação isenta da contribuição',
        '8': 'Operação sem incidência da contribuição',
        '9': 'Operação com suspensão da contribuição',
        '49': 'Outras operações de saída',
        '50': 'Operação com direito a crédito – vinculada exclusivamente a receita tributada no mercado interno',
        '51': 'Operação com direito a crédito – vinculada exclusivamente a receita não tributada no mercado interno',
        '52': 'Operação com direito a crédito – vinculada exclusivamente a receita de exportação',
        '53': 'Operação com direito a crédito – vinculada a receitas tributadas e não tributadas no mercado interno',
        '54': 'Operação com direito a crédito – vinculada a receitas tributadas no mercado interno e de exportação',
        '55': 'Operação com direito a crédito – vinculada a receitas não tributadas no mercado interno e de exportação',
        '56': 'Operação com direito a crédito – vinculada a receitas tributadas e não tributadas no mercado interno e de exportação',
        '60': 'Crédito presumido – operação de aquisição vinculada exclusivamente a receita tributada no mercado interno',
        '61': 'Crédito presumido – operação de aquisição vinculada exclusivamente a receita não tributada no mercado interno',
        '62': 'Crédito presumido – operação de aquisição vinculada exclusivamente a receita de exportação',
        '63': 'Crédito presumido – operação de aquisição vinculada a receitas tributadas e não tributadas no mercado interno',
        '64': 'Crédito presumido – operação de aquisição vinculada a receitas tributadas no mercado interno e de exportação',
        '65': 'Crédito presumido – operação de aquisição vinculada a receitas não tributadas no mercado interno e de exportação',
        '66': 'Crédito presumido – operação de aquisição vinculada a receitas tributadas e não tributadas no mercado interno e de exportação',
        '67': 'Crédito presumido – outras operações',
        '70': 'Operação de aquisição sem direito a crédito',
        '71': 'Operação de aquisição com isenção',
        '72': 'Operação de aquisição com suspensão',
        '73': 'Operação de aquisição a alíquota zero',
        '74': 'Operação de aquisição sem incidência da contribuição',
        '75': 'Operação de aquisição por substituição tributária',
        '98': 'Outras operações de entrada',
        '99': 'Outras operações'
    }

desc_cst_icms = {
    '000': "Sem substituição tributária",
    '001': "Com substituição tributária",
    '002': "Com substituição tributária - ICMS retido anteriormente por ST",
    '003': "ICMS ST devido anteriormente por substituição tributária",
    '009': "Outros"
    }

desc_cst_ipi = {
        '0': "Entrada com recuperação de crédito",
        '1': "Entrada tributada com alíquota zero",
        '2': "Entrada isenta",
        '3': "Entrada não-tributada",
        '4': "Entrada imune",
        '5': "Entrada com suspensão",
        '49': "Outras entradas",
        '50': "Saída tributada",
        '51': "Saída tributada com alíquota zero",
        '52': "Saída isenta",
        '53': "Saída não-tributada",
        '54': "Saída imune",
        '55': "Saída com suspensão",
        '99': "Outras saídas"
    }

desc_cst_pis = {
    # Regime Não Cumulativo
    '1': "Operação tributável com alíquota básica",
    '2': "Operação tributável com alíquota diferenciada",
    '3': "Operação tributável com alíquota por unidade de medida",
    '4': "Operação tributável monofásica – alíquota zero",
    '5': "Operação tributável por substituição tributária",
    '6': "Operação tributável a alíquota zero",
    '7': "Operação isenta da contribuição",
    '8': "Operação sem incidência da contribuição",
    '9': "Operação com suspensão da contribuição",

    # Regime Cumulativo ou substitutivo
    '49': "Outras operações de saída",

    # Entradas com direito a crédito
    '50': "Entrada com crédito vinculado exclusivamente a receita tributada no mercado interno",
    '51': "Entrada com crédito vinculado exclusivamente a receita não tributada no mercado interno",
    '52': "Entrada com crédito vinculado exclusivamente a receita de exportação",
    '53': "Entrada com crédito vinculado a mais de uma das receitas anteriores",
    '54': "Entrada sem direito a crédito",
    '55': "Entrada com crédito presumido",
    '56': "Entrada com crédito vinculado a receita tributada e não tributada no mercado interno",
    '57': "Entrada com crédito vinculado a receita tributada no mercado interno e de exportação",
    '58': "Entrada com crédito vinculado a receita não tributada no mercado interno e de exportação",
    '59': "Entrada com crédito vinculado a receita tributada, não tributada no mercado interno e de exportação",

    # Outras
    '98': "Outras operações de entrada",
    '99': "Outras operações"
}

desc_cod_gen = {
    "00": "Serviço",
    "01": "Animais vivos",
    "02": "Carnes e miudezas, comestíveis",
    "03": "Peixes e crustáceos, moluscos e os outros invertebrados aquáticos",
    "04": "Leite e laticínios; ovos de aves; mel natural; produtos comestíveis de origem animal, não especificados nem compreendidos em outros Capítulos da TIPI",
    "05": "Outros produtos de origem animal, não especificados nem compreendidos em outros Capítulos da TIPI",
    "06": "Plantas vivas e produtos de floricultura",
    "07": "Produtos hortícolas, plantas, raízes e tubérculos, comestíveis",
    "08": "Frutas; cascas de cítricos e de melões",
    "09": "Café, chá, mate e especiarias",
    "10": "Cereais",
    "11": "Produtos da indústria de moagem; malte; amidos e féculas; inulina; glúten de trigo",
    "12": "Sementes e frutos oleaginosos; grãos, sementes e frutos diversos; plantas industriais ou medicinais; palha e forragem",
    "13": "Gomas, resinas e outros sucos e extratos vegetais",
    "14": "Matérias para entrançar e outros produtos de origem vegetal, não especificadas nem compreendidas em outros Capítulos da NCM",
    "15": "Gorduras e óleos animais ou vegetais; produtos da sua dissociação; gorduras alimentares elaboradas; ceras de origem animal ou vegetal",
    "16": "Preparações de carne, de peixes ou de crustáceos, de moluscos ou de outros invertebrados aquáticos",
    "17": "Açúcares e produtos de confeitaria",
    "18": "Cacau e suas preparações",
    "19": "Preparações à base de cereais, farinhas, amidos, féculas ou de leite; produtos de pastelaria",
    "20": "Preparações de produtos hortícolas, de frutas ou de outras partes de plantas",
    "21": "Preparações alimentícias diversas",
    "22": "Bebidas, líquidos alcoólicos e vinagres",
    "23": "Resíduos e desperdícios das indústrias alimentares; alimentos preparados para animais",
    "24": "Fumo (tabaco) e seus sucedâneos, manufaturados",
    "25": "Sal; enxofre; terras e pedras; gesso, cal e cimento",
    "26": "Minérios, escórias e cinzas",
    "27": "Combustíveis minerais, óleos minerais e produtos de sua destilação; matérias betuminosas; ceras minerais",
    "28": "Produtos químicos inorgânicos; compostos inorgânicos ou orgânicos de metais preciosos, de elementos radioativos, de metais das terras raras ou de isótopos",
    "29": "Produtos químicos orgânicos",
    "30": "Produtos farmacêuticos",
    "31": "Adubos ou fertilizantes",
    "32": "Extratos tanantes e tintoriais; taninos e seus derivados; pigmentos e outras matérias corantes, tintas e vernizes, mástiques; tintas de escrever",
    "33": "Óleos essenciais e resinóides; produtos de perfumaria ou de toucador preparados e preparações cosméticas",
    "34": "Sabões, agentes orgânicos de superfície, preparações para lavagem, preparações lubrificantes, ceras artificiais, ceras preparadas, produtos de conservação e limpeza, velas e artigos semelhantes, massas ou pastas para modelar, \"ceras para dentistas\" e composições para dentistas à base de gesso",
    "35": "Matérias albuminóides; produtos à base de amidos ou de féculas modificados; colas; enzimas",
    "36": "Pólvoras e explosivos; artigos de pirotecnia; fósforos; ligas pirofóricas; matérias inflamáveis",
    "37": "Produtos para fotografia e cinematografia",
    "38": "Produtos diversos das indústrias químicas",
    "39": "Plásticos e suas obras",
    "40": "Borracha e suas obras",
    "41": "Peles, exceto a peleteria (peles com pêlo*), e couros",
    "42": "Obras de couro; artigos de correeiro ou de seleiro; artigos de viagem, bolsas e artefatos semelhantes; obras de tripa",
    "43": "Peleteria (peles com pêlo*) e suas obras; peleteria (peles com pêlo*) artificial",
    "44": "Madeira, carvão vegetal e obras de madeira",
    "45": "Cortiça e suas obras",
    "46": "Obras de espartaria ou de cestaria",
    "47": "Pastas de madeira ou de outras matérias fibrosas celulósicas; papel ou cartão de reciclar (desperdícios e aparas)",
    "48": "Papel e cartão; obras de pasta de celulose, de papel ou de cartão",
    "49": "Livros, jornais, gravuras e outros produtos das indústrias gráficas; textos manuscritos ou datilografados, planos e plantas",
    "50": "Seda",
    "51": "Lã e pêlos finos ou grosseiros; fios e tecidos de crina",
    "52": "Algodão",
    "53": "Outras fibras têxteis vegetais; fios de papel e tecido de fios de papel",
    "54": "Filamentos sintéticos ou artificiais",
    "55": "Fibras sintéticas ou artificiais, descontínuas",
    "56": "Pastas (\"ouates\"), feltros e falsos tecidos; fios especiais; cordéis, cordas e cabos; artigos de cordoaria",
    "57": "Tapetes e outros revestimentos para pavimentos, de matérias têxteis",
    "58": "Tecidos especiais; tecidos tufados; rendas; tapeçarias; passamanarias; bordados",
    "59": "Tecidos impregnados, revestidos, recobertos ou estratificados; artigos para usos técnicos de matérias têxteis",
    "60": "Tecidos de malha",
    "61": "Vestuário e seus acessórios, de malha",
    "62": "Vestuário e seus acessórios, exceto de malha",
    "63": "Outros artefatos têxteis confeccionados; sortidos; artefatos de matérias têxteis, calçados, chapéus e artefatos de uso semelhante, usados; trapos",
    "64": "Calçados, polainas e artefatos semelhantes, e suas partes",
    "65": "Chapéus e artefatos de uso semelhante, e suas partes",
    "66": "Guarda-chuvas, sombrinhas, guarda-sóis, bengalas, bengalas-assentos, chicotes, e suas partes",
    "67": "Penas e penugem preparadas, e suas obras; flores artificiais; obras de cabelo",
    "68": "Obras de pedra, gesso, cimento, amianto, mica ou de matérias semelhantes",
    "69": "Produtos cerâmicos",
    "70": "Vidro e suas obras",
    "71": "Pérolas naturais ou cultivadas, pedras preciosas ou semipreciosas e semelhantes, metais preciosos, metais folheados ou chapeados de metais preciosos, e suas obras; bijuterias; moedas",
    "72": "Ferro fundido, ferro e aço",
    "73": "Obras de ferro fundido, ferro ou aço",
    "74": "Cobre e suas obras",
    "75": "Níquel e suas obras",
    "76": "Alumínio e suas obras",
    "77": "(Reservado para uma eventual utilização futura no SH)",
    "78": "Chumbo e suas obras",
    "79": "Zinco e suas obras",
    "80": "Estanho e suas obras",
    "81": "Outros metais comuns; ceramais (\"cermets\"); obras dessas matérias",
    "82": "Ferramentas, artefatos de cutelaria e talheres, e suas partes, de metais comuns",
    "83": "Obras diversas de metais comuns",
    "84": "Reatores nucleares, caldeiras, máquinas, aparelhos e instrumentos mecânicos, e suas partes",
    "85": "Máquinas, aparelhos e materiais elétricos, e suas partes; aparelhos de gravação ou de reprodução de som, aparelhos de gravação ou de reprodução de imagens e de som em televisão, e suas partes e acessórios",
    "86": "Veículos e material para vias férreas ou semelhantes, e suas partes; aparelhos mecânicos (incluídos os eletromecânicos) de sinalização para vias de comunicação",
    "87": "Veículos automóveis, tratores, ciclos e outros veículos terrestres, suas partes e acessórios",
    "88": "Aeronaves e aparelhos espaciais, e suas partes",
    "89": "Embarcações e estruturas flutuantes",
    "90": "Instrumentos e aparelhos de óptica, fotografia ou cinematografia, medida, controle ou de precisão; instrumentos e aparelhos médico-cirúrgicos; suas partes e acessórios",
    "91": "Aparelhos de relojoaria e suas partes",
    "92": "Instrumentos musicais, suas partes e acessórios",
    "93": "Armas e munições; suas partes e acessórios",
    "94": "Móveis, mobiliário médico-cirúrgico; colchões; iluminação e construção pré-fabricadas",
    "95": "Brinquedos, jogos, artigos para divertimento ou para esporte; suas partes e acessórios",
    "96": "Obras diversas",
    "97": "Objetos de arte, de coleção e antiguidades",
    "98": "(Reservado para usos especiais pelas Partes Contratantes)",
    "99": "Operações especiais (utilizado exclusivamente pelo Brasil para classificar operações especiais na exportação)"
}

desc_tipo_item = {
    "00": "Mercadoria para Revenda",
    "01": "Matéria-Prima",
    "02": "Embalagem",
    "03": "Produto em Processo",
    "04": "Produto Acabado",
    "05": "Subproduto",
    "06": "Produto Intermediário",
    "07": "Material de Uso e Consumo",
    "08": "Ativo Imobilizado",
    "09": "Serviços",
    "10": "Outros insumos",
    "99": "Outras"
}


def preencher_pa(row):
        # Extraíndo mês e ano das datas relevantes para uso posterior
        mes_ano_data_doc = row['DATA_DOC'].strftime('%m/%Y')
        mes_ano_data_lcto = row['DATA_LCTO'].strftime('%m/%Y')

        # Regra para 'PV'
        if row['TIPO_DOC'] == 'PV':
            return "PV " + mes_ano_data_doc

        # Regras para 'RE', 'AP', 'RV' e 'ZA'
        if row['TIPO_DOC'] in ['RE', 'AP', 'RV'] and row['CONTA_RAZAO'] == 1105104001:
            return "PIS-" + mes_ano_data_lcto
        if row['TIPO_DOC'] in ['RE', 'AP', 'RV'] and row['CONTA_RAZAO'] == 1105105001:
            return "COFINS-" + mes_ano_data_lcto

        if row['TIPO_DOC'] == 'ZA' and row['CONTA_RAZAO'] == 1105104001:
            return "PIS-" + mes_ano_data_doc
        if row['TIPO_DOC'] == 'ZA' and row['CONTA_RAZAO'] == 1105105001:
            return "COFINS-" + mes_ano_data_doc

        # Caso não se enquadre em nenhuma regra, pode definir um valor padrão ou deixar como None
        return None

def datetime_to_excel_date(date_val):
        # Verifica se date_val é uma string
        if isinstance(date_val, str):
            # Convertendo a string para um objeto datetime
            date_obj = datetime.strptime(date_val, '%d/%m/%Y')
            # Definindo a data de início do Excel como 1 de janeiro de 1900
            start_date = datetime(1900, 1, 1)
            # Calculando a diferença de dias
            delta = date_obj - start_date
            # Retornando a diferença em dias (Excel adiciona +2 devido à questão do ano bissexto)
            return delta.days + 2
        else:
            # Retornar None ou algum outro valor padrão para valores não-string
            return None

def tratar_numero_item(num):
    num_str = str(num)
    if num_str.endswith('0'):
        if len(num_str) == 3 or len(num_str) == 4:
            return int(num_str[:-1])
        else:
            return int(num_str.rstrip('0'))
    return int(num_str)

def date_to_int(given_date):
    if isinstance(given_date, str):
        given_date = datetime.strptime(given_date, '%d/%m/%Y')
    base_date = datetime(1900, 1, 1) - timedelta(days=2)  # Excel date offset
    return (given_date - base_date).days

def identificar_arquivo(arquivo):
    #Verificar extensão
    file = Path(arquivo)
    if file.is_file():
        if file.suffix == '.txt':
            #É TXT
            text_content = file.read_text()

            if '|A100|' in text_content:
                return {
                        "file":'efdcontribuicoes'
                    }
            
def processar_efd_contribuicoes(file):
    #Recebe um arquivo e converte em um dicionario estruturado
    efd_file = Path(file)
    
    bloco_0150 = []
    bloco_0200 = []
    bloco_0000 = []
    bloco_c100 = []
    bloco_c170 = []
    bloco_a100 = []
    bloco_a170 = []
    bloco_f100 = []
    bloco_f130 = []
    bloco_c500 = []
    bloco_c501 = []
    bloco_c505 = []
    bloco_d500 = []
    bloco_d501 = []
    bloco_d505 = []
    bloco_d100 = []
    bloco_d101 = []
    bloco_d105 = []
    bloco_m100 = []
    bloco_m105 = []
    bloco_m500 = []
    bloco_m505 = []
    bloco_m200 = []
    bloco_m205 = []
    bloco_m210 = []
    bloco_m220 = []
    bloco_m225 = []
    bloco_m600 = []
    bloco_m605 = []
    bloco_m610 = []
    bloco_m620 = []
    bloco_m625 = []



    CAMPOS_0000 = [
        'id',                 # Texto fixo "0000"
        'cod_ver',             # Código da versão do leiaute
        'tipo_escrit',         # Tipo de escrituração
        'ind_sit_esp',         # Indicador de situação especial
        'num_rec_anterior',    # Número do recibo anterior (se retificadora)
        'dt_ini',              # Data inicial das informações
        'dt_fin',              # Data final das informações
        'nome',                # Nome empresarial
        'cnpj',                # CNPJ da matriz
        'uf',                  # UF
        'cod_mun',             # Código do município (IBGE)
        'suframa',             # Inscrição SUFRAMA
        'ind_nat_pj',          # Indicador da natureza da pessoa jurídica
        'ind_ativ'             # Indicador de tipo de atividade preponderante
    ]
    
    CAMPOS_0150 = [
    'cod_part', 'nome', 'cod_pais', 'cnpj', 'cpf', 'ie', 'cod_mun',
    'suframa', 'end', 'num', 'compl', 'bairro'
            ]

    CAMPOS_0200 = [
    'cod_item', 'descr_item', 'cod_barra', 'cod_ant_item', 'unid_inv',
    'tipo_item', 'cod_ncm', 'ex_ipi', 'cod_gen', 'cod_lst', 'aliq_icms'
    ]    
    
    CAMPOS_A100 = [
        'ind_oper',         # Indicador do tipo de operação
        'ind_emit',         # Indicador do emitente do documento fiscal
        'cod_part',         # Código do participante (emitente ou adquirente)
        'cod_sit',          # Código da situação do documento fiscal
        'ser',              # Série do documento fiscal
        'sub',              # Subsérie do documento fiscal
        'num_doc',          # Número do documento fiscal
        'chv_nfse',         # Chave da NFSe
        'dt_doc',           # Data da emissão do documento fiscal
        'dt_exe_serv',      # Data de execução/conclusão do serviço
        'vl_doc',           # Valor total do documento
        'ind_pgto',         # Indicador do tipo de pagamento
        'vl_desc',          # Valor total do desconto
        'vl_bc_pis',        # Base de cálculo do PIS
        'vl_pis',           # Valor do PIS
        'vl_bc_cofins',     # Base de cálculo da COFINS
        'vl_cofins',        # Valor da COFINS
        'vl_pis_ret',       # Valor do PIS retido
        'vl_cofins_ret',    # Valor da COFINS retido
        'vl_iss',           # Valor do ISS
        'id_a100',
        'CNPJ_ESTAB'
                              # ID do registro A100
    ]

    CAMPOS_A170 = [
        'num_item',         # Número sequencial do item no documento
        'cod_item',         # Código do item (registro 0200)
        'descr_compl',      # Descrição complementar do item
        'vl_item',          # Valor total do item
        'vl_desc',          # Valor do desconto comercial
        'nat_bc_cred',      # Código da base de cálculo do crédito
        'ind_orig_cred',    # Indicador da origem do crédito
        'cst_pis',          # Código da situação tributária do PIS
        'vl_bc_pis',        # Base de cálculo do PIS
        'aliq_pis',         # Alíquota do PIS
        'vl_pis',           # Valor do PIS
        'cst_cofins',       # Código da situação tributária da COFINS
        'vl_bc_cofins',     # Base de cálculo da COFINS
        'aliq_cofins',      # Alíquota da COFINS
        'vl_cofins',        # Valor da COFINS
        'cod_cta',          # Código da conta contábil
        'cod_ccus',          # Código do centro de custos
        'id_a100'
    ]

    CAMPOS_C100 = [
                  # Texto fixo "C100"
        
         
        'ind_oper',        # Indicador do tipo de operação
        'ind_emit',        # Indicador do emitente
        'cod_part',        # Código do participante (registro 0150)
        'cod_mod',         # Modelo do documento fiscal
        'cod_sit',         # Situação do documento
        'ser',             # Série do documento
        'num_doc',         # Número do documento
        'chv_nfe',         # Chave da NF-e (PK)
        'dt_doc',          # Data de emissão
        'dt_e_s',          # Data da entrada/saída
        'vl_doc',          # Valor total do documento
        'ind_pgto',        # Indicador de tipo de pagamento
        'vl_desc',         # Valor do desconto
        'vl_abat_nt',      # Valor do abatimento não tributado
        'vl_merc',         # Valor total das mercadorias/serviços
        'ind_frt',         # Indicador de tipo de frete
        'vl_frt',          # Valor do frete
        'vl_seg',          # Valor do seguro
        'vl_out_da',       # Outras despesas acessórias
        'vl_bc_icms',      # Base de cálculo do ICMS
        'vl_icms',         # Valor do ICMS
        'vl_bc_icms_st',   # Base de cálculo do ICMS ST
        'vl_icms_st',      # Valor do ICMS ST
        'vl_ipi',          # Valor do IPI
        'vl_pis',          # Valor do PIS
        'vl_cofins',       # Valor da COFINS
        'vl_pis_st',       # Valor do PIS ST
        'vl_cofins_st',     # Valor da COFINS ST
        'id_c100',
        'CNPJ_ESTAB'
        ]   
    
    CAMPOS_C170 = [
    
    'num_item',
    'cod_item',
    'descr_compl',
    'qtd',
    'unid',
    'vl_item',
    'vl_desc',
    'ind_mov',
    'cst_icms',
    'cfop',
    'cod_nat',
    'vl_bc_icms',
    'aliq_icms',
    'vl_icms',
    'vl_bc_icms_st',
    'aliq_st',
    'vl_icms_st',
    'ind_apur',
    'cst_ipi',
    'cod_enq',
    'vl_bc_ipi',
    'aliq_ipi',
    'vl_ipi',
    'cst_pis',
    'vl_bc_pis',
    'aliq_pis',
    'quant_bc_pis',
    'aliq_pis_quant',
    'vl_pis',
    'cst_cofins',
    'vl_bc_cofins',
    'aliq_cofins',
    'quant_bc_cofins',
    'aliq_cofins_quant',
    'vl_cofins',
    'cod_cta',
    'id_c100'
    ]

    CAMPOS_C500 = [
        'cod_part',       # Código do participante (fornecedor)
        'cod_mod',        # Código do modelo do documento fiscal
        'cod_sit',        # Código da situação do documento fiscal
        'ser',            # Série do documento fiscal
        'sub',            # Subsérie do documento fiscal
        'num_doc',        # Número do documento fiscal
        'dt_doc',         # Data da emissão
        'dt_ent',         # Data da entrada
        'vl_doc',         # Valor total do documento fiscal
        'vl_icms',        # Valor do ICMS
        'cod_inf',        # Código da informação complementar
        'vl_pis',         # Valor do PIS/PASEP
        'vl_cofins',      # Valor da COFINS
        'chv_doce',       # Chave do Documento Fiscal Eletrônico
        'id_c500'         # Identificador para uso com blocos C501 e C505
    ]

    CAMPOS_C501 = [
        'cst_pis',       # Código da Situação Tributária do PIS
        'vl_item',       # Valor total dos itens
        'nat_bc_cred',   # Código da base de cálculo do crédito
        'vl_bc_pis',     # Valor da base de cálculo do PIS
        'aliq_pis',      # Alíquota do PIS
        'vl_pis',        # Valor do PIS
        'cod_cta',       # Conta contábil
        'id_c500'        # Identificador para relacionamento com C500
    ]

    CAMPOS_C505 = [
        'cst_cofins',     # Código da Situação Tributária da COFINS
        'vl_item',        # Valor total dos itens
        'nat_bc_cred',    # Código da base de cálculo do crédito
        'vl_bc_cofins',   # Base de cálculo da COFINS
        'aliq_pis',       # Alíquota da COFINS (nome técnico do layout)
        'vl_pis',         # Valor da COFINS (nome técnico do layout)
        'cod_cta',        # Conta contábil
        'id_c500'         # Identificador para relacionamento com C500
    ]

    CAMPOS_D500 = [
        'ind_oper',       # Indicador do tipo de operação
        'ind_emit',       # Indicador do emitente
        'cod_part',       # Código do participante (registro 0150)
        'cod_mod',        # Código do modelo do documento fiscal
        'cod_sit',        # Situação do documento fiscal
        'ser',            # Série do documento
        'sub',            # Subsérie do documento
        'num_doc',        # Número do documento fiscal
        'dt_doc',         # Data da emissão
        'dt_a_p',         # Data da entrada ou aquisição
        'vl_doc',         # Valor total do documento fiscal
        'vl_desc',        # Valor do desconto
        'vl_serv',        # Valor da prestação de serviços
        'vl_serv_nt',     # Valor de serviços não tributados
        'vl_terc',        # Valores cobrados em nome de terceiros
        'vl_da',          # Outras despesas
        'vl_bc_icms',     # Base de cálculo do ICMS
        'vl_icms',        # Valor do ICMS
        'cod_inf',        # Código da informação complementar
        'vl_pis',         # Valor do PIS
        'vl_cofins',      # Valor da COFINS
        'id_d500'         # Identificador auxiliar para blocos filhos (D501, D505)
    ]

    CAMPOS_D501 = [
        'cst_pis',        # Código da Situação Tributária do PIS
        'vl_item',        # Valor total dos itens (serviços)
        'nat_bc_cred',    # Código da base de cálculo do crédito
        'vl_bc_pis',      # Base de cálculo do PIS
        'aliq_pis',       # Alíquota do PIS
        'vl_pis',         # Valor do PIS
        'cod_cta',        # Conta contábil
        'id_d500'         # Identificador para relacionamento com D500
    ]

    CAMPOS_D505 = [
        'cst_cofins',     # Código da Situação Tributária da COFINS
        'vl_item',        # Valor total dos itens (serviços)
        'nat_bc_cred',    # Código da base de cálculo do crédito
        'vl_bc_cofins',   # Valor da base de cálculo da COFINS
        'aliq_cofins',    # Alíquota da COFINS
        'vl_cofins',      # Valor da COFINS
        'cod_cta',        # Conta contábil
        'id_d500'         # Identificador para relacionamento com D500
    ]

    CAMPOS_D100 = [
        'ind_oper', 'ind_emit', 'cod_part', 'cod_mod', 'cod_sit', 'ser', 'sub',
        'num_doc', 'chv_cte', 'dt_doc', 'dt_a_p', 'tp_cte', 'chv_cte_ref',
        'vl_doc', 'vl_desc', 'ind_frt', 'vl_serv', 'vl_bc_icms', 'vl_icms', 'vl_nt',
        'cod_inf', 'cod_cta', 'id_d100'
    ]

    CAMPOS_D101 = [
    'ind_nat_frt', 'vl_item', 'cst_pis', 'nat_bc_cred', 'vl_bc_pis',
    'aliq_pis', 'vl_pis', 'cod_cta', 'id_d100'
    ]

    CAMPOS_D105 = [
        'ind_nat_frt', 'vl_item', 'cst_cofins', 'nat_bc_cred', 'vl_bc_cofins',
        'aliq_cofins', 'vl_cofins', 'cod_cta', 'id_d100'
    ]
    
    CAMPOS_F100 = [
    'ind_oper',         # Indicador do tipo da operação
    'cod_part',         # Código do participante (registro 0150)
    'cod_item',         # Código do item (registro 0200)
    'dt_oper',          # Data da operação
    'vl_oper',          # Valor da operação/item
    'cst_pis',          # Código da situação tributária do PIS
    'vl_bc_pis',        # Base de cálculo do PIS
    'aliq_pis',         # Alíquota do PIS
    'vl_pis',           # Valor do PIS
    'cst_cofins',       # Código da situação tributária da COFINS
    'vl_bc_cofins',     # Base de cálculo da COFINS
    'aliq_cofins',      # Alíquota da COFINS
    'vl_cofins',        # Valor da COFINS
    'nat_bc_cred',      # Código da base de cálculo dos créditos
    'ind_orig_cred',    # Indicador da origem do crédito
    'cod_cta',          # Código da conta contábil
    'cod_ccus',         # Código do centro de custos
    'desc_doc_oper'     # Descrição do documento/operação
]
    
    CAMPOS_F130 = [
        'nat_bc_cred',         # Código da base de cálculo do crédito
        'ident_bem_imob',      # Identificação do bem ou grupo de bens
        'ind_orig_cred',       # Origem do bem incorporado ao ativo
        'ind_util_bem_imob',   # Indicador de utilização dos bens
        'mes_oper_aquis',      # Mês/ano de aquisição
        'vl_oper_aquis',       # Valor da aquisição
        'parc_oper_nao_bc_cred',  # Parcela a excluir da base de cálculo
        'vl_bc_cred',          # Base de cálculo do crédito
        'ind_nr_parc',         # Indicador do número de parcelas
        'cst_pis',             # CST do PIS
        'vl_bc_pis',           # Base de cálculo mensal do PIS
        'aliq_pis',            # Alíquota do PIS
        'vl_pis',              # Valor do crédito de PIS
        'cst_cofins',          # CST da COFINS
        'vl_bc_cofins',        # Base de cálculo mensal da COFINS
        'aliq_cofins',         # Alíquota da COFINS
        'vl_cofins',           # Valor do crédito de COFINS
        'cod_cta',             # Conta contábil
        'cod_ccus',            # Centro de custos
        'desc_bem_imob'        # Descrição do bem
    ]

    CAMPOS_M100 = [
    'cod_cred', 'ind_cred_ori', 'vl_bc_pis', 'aliq_pis', 'quant_bc_pis',
    'aliq_pis_quant', 'vl_cred', 'vl_ajus_acres', 'vl_ajus_reduc', 'vl_cred_dif',
    'vl_cred_disp', 'ind_desc_cred', 'vl_cred_desc', 'sld_cred'
    ]

    CAMPOS_M105 = [
        'nat_bc_cred', 'cst_pis', 'vl_bc_pis_tot', 'vl_bc_pis_cum',
        'vl_bc_pis_nc', 'vl_bc_pis', 'quant_bc_pis_tot', 'quant_bc_pis', 'desc_cred'
    ]

    CAMPOS_M500 = [
        'cod_cred', 'ind_cred_ori', 'vl_bc_cofins', 'aliq_cofins', 'quant_bc_cofins',
        'aliq_cofins_quant', 'vl_cred', 'vl_ajus_acres', 'vl_ajus_reduc',
        'vl_cred_difer', 'vl_cred_disp', 'ind_desc_cred', 'vl_cred_desc', 'sld_cred'
    ]

    CAMPOS_M505 = [
    'nat_bc_cred', 'cst_cofins', 'vl_bc_cofins_tot', 'vl_bc_cofins_cum',
    'vl_bc_cofins_nc', 'vl_bc_cofins', 'quant_bc_cofins_tot', 'quant_bc_cofins',
    'desc_cred'
    ]

    CAMPOS_M200 = [
        'vl_tot_cont_nc_per', 'vl_tot_cred_desc', 'vl_tot_cred_desc_ant', 'vl_tot_cont_nc_dev',
        'vl_ret_nc', 'vl_out_ded_nc', 'vl_cont_nc_rec', 'vl_tot_cont_cum_per', 'vl_ret_cum',
        'vl_out_ded_cum', 'vl_cont_cum_rec', 'vl_tot_cont_rec'
    ]

    CAMPOS_M205 = [
        'num_campo', 'cod_rec', 'vl_debito', 'id_m200'
    ]

    CAMPOS_M210 = [
        'cod_cont', 'vl_rec_brt', 'vl_bc_cont', 'aliq_pis', 'quant_bc_pis', 'aliq_pis_quant',
        'vl_cont_apur', 'vl_ajus_acres', 'vl_ajus_reduc', 'vl_cont_difer', 'vl_cont_difer_ant', 'vl_cont_per'
    ]

    CAMPOS_M220 = [
        'ind_aj', 'vl_aj', 'cod_aj', 'num_doc', 'descr_aj', 'dt_ref', 'id_m210'
    ]

    CAMPOS_M225 = [
        'det_valor_aj', 'cst_pis', 'det_bc_cred', 'det_aliq', 'dt_oper_aj',
        'desc_aj', 'cod_cta', 'info_compl', 'id_m220'
    ]

    CAMPOS_M600 = [
        'vl_tot_cont_nc_per', 'vl_tot_cred_desc', 'vl_tot_cred_desc_ant', 'vl_tot_cont_nc_dev',
        'vl_ret_nc', 'vl_out_ded_nc', 'vl_cont_nc_rec', 'vl_tot_cont_cum_per',
        'vl_ret_cum', 'vl_out_ded_cum', 'vl_cont_cum_rec', 'vl_tot_cont_rec'
    ]

    CAMPOS_M605 = [
        'num_campo', 'cod_rec', 'vl_debito', 'id_m600'
    ]

    CAMPOS_M610 = [
        'cod_cont', 'vl_rec_brt', 'vl_bc_cont', 'aliq_cofins', 'quant_bc_cofins', 'aliq_cofins_quant',
        'vl_cont_apur', 'vl_ajus_acres', 'vl_ajus_reduc', 'vl_cont_difer', 'vl_cont_difer_ant', 'vl_cont_per'
    ]

    CAMPOS_M620 = [
        'ind_aj', 'vl_aj', 'cod_aj', 'num_doc', 'descr_aj', 'dt_ref', 'id_m610'
    ]

    CAMPOS_M625 = [
        'det_valor_aj', 'cst_cofins', 'det_bc_cred', 'det_aliq', 'dt_oper_aj',
        'desc_aj', 'cod_cta', 'info_compl', 'id_m620'
    ]


    cnpj = None
    competencia = None
    index_c100 = 0
    index_a100 = 0
    index_c500 = 0
    index_d500 = 0
    index_d100 = 0
    index_m600 = 0
    index_m610 = 0
    index_m620 = 0


    with efd_file.open('r', encoding='utf-8', errors='ignore') as sped:
        for line in sped:

            if line.startswith("|0000|"):
                splited_0000 = line.strip().split("|")[2:]
                
                splited_0000[4] = datetime.strptime(splited_0000[4], "%d%m%Y")
                splited_0000[5] = datetime.strptime(splited_0000[5], "%d%m%Y")
                competencia = splited_0000[4]
                cnpj = splited_0000[7]

                splited_0000.insert(0,f'{cnpj}_{competencia}')
                reg_dict = dict(zip(CAMPOS_0000, splited_0000))
                bloco_0000 = [reg_dict]

            if line.startswith('|0150|'):
                splited_0150 = line.strip().split("|")[2:]
                reg_dict = dict(zip(CAMPOS_0150, splited_0150))


                bloco_0150.append(reg_dict)

            elif line.startswith('|0200|'):
                splited_0200 = line.strip().split("|")[2:]
                splited_0200[10] = splited_0200[10].replace(",",".") 

                if splited_0200[10] in ['None',None,'']:
                    splited_0200[10] = '0.0'

                reg_dict = dict(zip(CAMPOS_0200, splited_0200))
                bloco_0200.append(reg_dict)
            
            elif line.startswith("|C010|"):
                splited_c010 = line.split("|")
                cnpj_estab_c = splited_c010[2]

                print(f'O CNPJ É {cnpj_estab_c}')
                
            elif line.startswith('|C100|'):
                splited_c100 = line.split("|")
                index_c100 += 1
                #id_c100 = splited_c100[9]
            
                try:
                    splited_c100[10] = datetime.strptime(splited_c100[10], "%d%m%Y")
                    splited_c100[11] = datetime.strptime(splited_c100[11], "%d%m%Y")
                except:
                    splited_c100[10] = None
                    splited_c100[11] = None
                
                splited_c100[12] = splited_c100[12].replace(",",".")    if splited_c100[12] != '' else 0
                splited_c100[14] = splited_c100[14].replace(",",".")    if splited_c100[14] != '' else 0
                splited_c100[15] = splited_c100[15].replace(",",".")    if splited_c100[15] != '' else 0
                splited_c100[16] = splited_c100[16].replace(",",".")    if splited_c100[16] != '' else 0
                splited_c100[18] = splited_c100[18].replace(",",".")    if splited_c100[18] != '' else 0
                splited_c100[19] = splited_c100[19].replace(",",".")    if splited_c100[19] != '' else 0
                splited_c100[20] = splited_c100[20].replace(",",".")    if splited_c100[20] != '' else 0
                splited_c100[21] = splited_c100[21].replace(",",".")    if splited_c100[21] != '' else 0
                splited_c100[22] = splited_c100[22].replace(",",".")    if splited_c100[22] != '' else 0
                splited_c100[23] = splited_c100[23].replace(",",".")    if splited_c100[23] != '' else 0
                splited_c100[24] = splited_c100[24].replace(",",".")    if splited_c100[24] != '' else 0
                splited_c100[25] = splited_c100[25].replace(",",".")    if splited_c100[25] != '' else 0
                splited_c100[26] = splited_c100[26].replace(",",".")    if splited_c100[26] != '' else 0
                splited_c100[27] = splited_c100[27].replace(",",".")    if splited_c100[27] != '' else 0
                splited_c100[28] = splited_c100[28].replace(",",".")    if splited_c100[28] != '' else 0
                splited_c100[29] = splited_c100[29].replace(",",".")    if splited_c100[29] != '' else 0

                splited_c100[-1] = index_c100
                splited_c100.append(cnpj_estab_c)

                
                splited_c100 = splited_c100[2:]
                
                reg_dict = dict(zip(CAMPOS_C100, splited_c100))
                
                bloco_c100.append(reg_dict)

            elif line.startswith('|C170|'):
                splited_c170 = line.split("|")

                splited_c170[5] = splited_c170[5].replace(",",".")      if splited_c170[5] != '' else 0
                splited_c170[7] = splited_c170[7].replace(",",".")      if splited_c170[7] != '' else 0
                splited_c170[8] = splited_c170[8].replace(",",".")      if splited_c170[8] != '' else 0
                splited_c170[13] = splited_c170[13].replace(",",".")    if splited_c170[13] != '' else 0
                splited_c170[14] = splited_c170[14].replace(",",".")    if splited_c170[14] != '' else 0
                splited_c170[15] = splited_c170[15].replace(",",".")    if splited_c170[15] != '' else 0
                splited_c170[16] = splited_c170[16].replace(",",".")    if splited_c170[16] != '' else 0
                splited_c170[17] = splited_c170[17].replace(",",".")    if splited_c170[17] != '' else 0
                splited_c170[18] = splited_c170[18].replace(",",".")    if splited_c170[18] != '' else 0
                splited_c170[22] = splited_c170[22].replace(",",".")    if splited_c170[22] != '' else 0
                splited_c170[23] = splited_c170[23].replace(",",".")    if splited_c170[23] != '' else 0
                splited_c170[24] = splited_c170[24].replace(",",".")    if splited_c170[24] != '' else 0
                splited_c170[26] = splited_c170[26].replace(",",".")    if splited_c170[26] != '' else 0
                splited_c170[27] = splited_c170[27].replace(",",".")    if splited_c170[27] != '' else 0
                splited_c170[28] = splited_c170[28].replace(",",".")    if splited_c170[28] != '' else 0
                splited_c170[29] = splited_c170[29].replace(",",".")    if splited_c170[29] != '' else 0
                splited_c170[30] = splited_c170[30].replace(",",".")    if splited_c170[30] != '' else 0
                splited_c170[31] = splited_c170[31].replace(",",".")    if splited_c170[31] != '' else 0
                splited_c170[32] = splited_c170[32].replace(",",".")    if splited_c170[32] != '' else 0
                splited_c170[33] = splited_c170[33].replace(",",".")    if splited_c170[33] != '' else 0
                splited_c170[34] = splited_c170[34].replace(",",".")    if splited_c170[34] != '' else 0
                splited_c170[35] = splited_c170[35].replace(",",".")    if splited_c170[35] != '' else 0
                splited_c170[36] = splited_c170[36].replace(",",".")    if splited_c170[36] != '' else 0

                splited_c170[-1] = index_c100


                #print(splited_c170)
                splited_c170= splited_c170[2:]
                
                reg_dict = dict(zip(CAMPOS_C170, splited_c170))

                bloco_c170.append(reg_dict)

            elif line.startswith("|A010|"):
                splited_a010 = line.split("|")
                cnpj_estab_a = splited_a010[2]
                print(f'O cnpj É {cnpj_estab_a}')
                

            elif line.startswith("|A100|"):
                splited_a100 = line.split("|")
                index_a100 += 1
                #id_c100 = splited_c100[9]
            
                try:
                    splited_a100[10] = datetime.strptime(splited_a100[10], "%d%m%Y")
                    splited_a100[11] = datetime.strptime(splited_a100[11], "%d%m%Y")
                except:
                    splited_a100[10] = None
                    splited_a100[11] = None
                
                splited_a100[12] = splited_a100[12].replace(",",".")    if splited_a100[12] != '' else 0
                splited_a100[14] = splited_a100[14].replace(",",".")    if splited_a100[14] != '' else 0
                splited_a100[15] = splited_a100[15].replace(",",".")    if splited_a100[15] != '' else 0
                splited_a100[16] = splited_a100[16].replace(",",".")    if splited_a100[16] != '' else 0
                splited_a100[17] = splited_a100[17].replace(",",".")    if splited_a100[17] != '' else 0
                splited_a100[18] = splited_a100[18].replace(",",".")    if splited_a100[18] != '' else 0
                splited_a100[19] = splited_a100[19].replace(",",".")    if splited_a100[19] != '' else 0
                splited_a100[20] = splited_a100[20].replace(",",".")    if splited_a100[20] != '' else 0
                splited_a100[21] = splited_a100[21].replace(",",".")    if splited_a100[21] != '' else 0
                

                splited_a100[-1] = index_a100
                splited_a100.append(cnpj_estab_a)
              
                
                splited_a100 = splited_a100[2:]
                

                #print('BLOCO 100')
                #print(splited_a100)
                reg_dict = dict(zip(CAMPOS_A100, splited_a100))
                #print(reg_dict)
                bloco_a100.append(reg_dict)

            elif line.startswith("|A170|"):
                splited_a170 = line.split("|")

                splited_a170[5] = splited_a170[5].replace(",",".")      if splited_a170[5] != '' else 0
                splited_a170[6] = splited_a170[6].replace(",",".")      if splited_a170[6] != '' else 0
                
                splited_a170[10] = splited_a170[10].replace(",",".")      if splited_a170[10] != '' else 0
                splited_a170[11] = splited_a170[11].replace(",",".")      if splited_a170[11] != '' else 0
                splited_a170[12] = splited_a170[12].replace(",",".")      if splited_a170[12] != '' else 0

                splited_a170[14] = splited_a170[14].replace(",",".")      if splited_a170[14] != '' else 0
                splited_a170[15] = splited_a170[15].replace(",",".")      if splited_a170[15] != '' else 0
                splited_a170[16] = splited_a170[16].replace(",",".")      if splited_a170[16] != '' else 0
                

                splited_a170[-1] = index_a100


                #print(splited_c170)
                splited_a170= splited_a170[2:]
                
                reg_dict = dict(zip(CAMPOS_A170, splited_a170))

                print('BLOCO 170')
                print(reg_dict)
                bloco_a170.append(reg_dict)

            elif line.startswith("|F100|"):

                splited_f100 = line.split("|")

                splited_f100[6] = splited_f100[6].replace(",",".")      if splited_f100[6] != '' else 0
                splited_f100[8] = splited_f100[8].replace(",",".")      if splited_f100[8] != '' else 0
                splited_f100[9] = splited_f100[9].replace(",",".")      if splited_f100[9] != '' else 0
                splited_f100[10] = splited_f100[10].replace(",",".")      if splited_f100[10] != '' else 0
                splited_f100[12] = splited_f100[12].replace(",",".")      if splited_f100[12] != '' else 0
                splited_f100[13] = splited_f100[13].replace(",",".")      if splited_f100[13] != '' else 0
                splited_f100[14] = splited_f100[14].replace(",",".")      if splited_f100[14] != '' else 0

                try:
                    splited_f100[5] = datetime.strptime(splited_f100[5], "%d%m%Y")
                except:
                    splited_f100[5] = None


                splited_f100= splited_f100[2:]
                
                reg_dict = dict(zip(CAMPOS_F100, splited_f100))

                print('BLOCO 170')
                print(reg_dict)
                bloco_f100.append(reg_dict)

            elif line.startswith("|F130|"):

                splited_f130 = line.split("|")

                splited_f130[7] = splited_f130[7].replace(",",".")      if splited_f130[7] != '' else 0
                splited_f130[8] = splited_f130[8].replace(",",".")      if splited_f130[8] != '' else 0
                splited_f130[9] = splited_f130[9].replace(",",".")      if splited_f130[9] != '' else 0
                splited_f130[12] = splited_f130[12].replace(",",".")      if splited_f130[12] != '' else 0
                splited_f130[13] = splited_f130[13].replace(",",".")      if splited_f130[13] != '' else 0
                splited_f130[14] = splited_f130[14].replace(",",".")      if splited_f130[14] != '' else 0
                splited_f130[16] = splited_f130[16].replace(",",".")      if splited_f130[16] != '' else 0
                splited_f130[17] = splited_f130[17].replace(",",".")      if splited_f130[17] != '' else 0
                splited_f130[18] = splited_f130[18].replace(",",".")      if splited_f130[18] != '' else 0


                splited_f130= splited_f130[2:]
                
                reg_dict = dict(zip(CAMPOS_F130, splited_f130))

                print('BLOCO 170')
                print(reg_dict)
                bloco_f130.append(reg_dict)
            
            elif line.startswith("|C500|"):
                
                splited_c500 = line.split("|")
                index_c500 += 1
                #id_c100 = splited_c100[9]
            
                try:
                    splited_c500[8] = datetime.strptime(splited_c500[8], "%d%m%Y")
                    splited_c500[9] = datetime.strptime(splited_c500[9], "%d%m%Y")
                except:
                    splited_c500[8] = None
                    splited_c500[9] = None
                

                splited_c500[10] = splited_c500[10].replace(",",".")    if splited_c500[10] != '' else 0
                splited_c500[11] = splited_c500[11].replace(",",".")    if splited_c500[11] != '' else 0
                splited_c500[13] = splited_c500[13].replace(",",".")    if splited_c500[13] != '' else 0
                splited_c500[14] = splited_c500[14].replace(",",".")    if splited_c500[14] != '' else 0
                
                splited_c500[-1] = index_c500

                splited_c500 = splited_c500[2:]
                

                #print('BLOCO 100')
                #print(splited_c500)
                reg_dict = dict(zip(CAMPOS_C500, splited_c500))
                #print(reg_dict)
                bloco_c500.append(reg_dict)

            elif line.startswith("|C501|"):
                splited_c501 = line.split("|")

                splited_c501[3] = splited_c501[3].replace(",",".")      if splited_c501[3] != '' else 0
                splited_c501[5] = splited_c501[5].replace(",",".")      if splited_c501[5] != '' else 0
                splited_c501[6] = splited_c501[6].replace(",",".")      if splited_c501[6] != '' else 0
                splited_c501[7] = splited_c501[7].replace(",",".")      if splited_c501[7] != '' else 0
               
                splited_c501[-1] = index_c500

                splited_c501= splited_c501[2:]
                
                reg_dict = dict(zip(CAMPOS_C501, splited_c501))

                print('BLOCO 170')
                print(reg_dict)
                bloco_c501.append(reg_dict)

            elif line.startswith("|C505|"):
                splited_c505 = line.split("|")

                splited_c505[3] = splited_c505[3].replace(",",".")      if splited_c505[3] != '' else 0
                splited_c505[5] = splited_c505[5].replace(",",".")      if splited_c505[5] != '' else 0
                splited_c505[6] = splited_c505[6].replace(",",".")      if splited_c505[6] != '' else 0
                splited_c505[7] = splited_c505[7].replace(",",".")      if splited_c505[7] != '' else 0
               
                splited_c505[-1] = index_c500

                splited_c505= splited_c505[2:]
                
                reg_dict = dict(zip(CAMPOS_C505, splited_c505))

                print('BLOCO 170')
                print(reg_dict)
                bloco_c505.append(reg_dict)
            
            elif line.startswith("|D500|"):
                splited_d500 = line.split("|")
                index_d500 += 1

                try:
                    splited_d500[10] = datetime.strptime(splited_d500[10], "%d%m%Y")  # DT_DOC
                    splited_d500[11] = datetime.strptime(splited_d500[11], "%d%m%Y")  # DT_A_P
                except:
                    splited_d500[10] = None
                    splited_d500[11] = None

                # Conversão de valores decimais
                for i in [12, 13, 14, 15, 16, 17, 18, 19, 21, 22]:
                    splited_d500[i] = splited_d500[i].replace(",", ".") if splited_d500[i] != '' else 0

                splited_d500[-1] = index_d500  # id_d500
                splited_d500 = splited_d500[2:]  # Remove REG e deixa só os dados úteis

                reg_dict = dict(zip(CAMPOS_D500, splited_d500))
                bloco_d500.append(reg_dict)

            elif line.startswith("|D501|"):
                splited_d501 = line.split("|")

                # Conversão de valores decimais
                splited_d501[3] = splited_d501[3].replace(",", ".") if splited_d501[3] != '' else 0  # nat_bc_cred
                splited_d501[5] = splited_d501[5].replace(",", ".") if splited_d501[5] != '' else 0  # vl_bc_pis
                splited_d501[6] = splited_d501[6].replace(",", ".") if splited_d501[6] != '' else 0  # aliq_pis
                splited_d501[7] = splited_d501[7].replace(",", ".") if splited_d501[7] != '' else 0  # vl_pis

                splited_d501[-1] = index_d500  # Relacionamento com D500
                splited_d501 = splited_d501[2:]  # Remove REG e CODIGO fixo

                reg_dict = dict(zip(CAMPOS_D501, splited_d501))

                print('BLOCO D501')
                print(reg_dict)
                bloco_d501.append(reg_dict)

            elif line.startswith("|D505|"):
                splited_d505 = line.split("|")

                # Conversão de valores decimais
                splited_d505[3] = splited_d505[3].replace(",", ".") if splited_d505[3] != '' else 0  # nat_bc_cred
                splited_d505[5] = splited_d505[5].replace(",", ".") if splited_d505[5] != '' else 0  # vl_bc_cofins
                splited_d505[6] = splited_d505[6].replace(",", ".") if splited_d505[6] != '' else 0  # aliq_cofins
                splited_d505[7] = splited_d505[7].replace(",", ".") if splited_d505[7] != '' else 0  # vl_cofins

                splited_d505[-1] = index_d500  # Relacionamento com D500
                splited_d505 = splited_d505[2:]  # Remove REG e posiciona campos úteis

                reg_dict = dict(zip(CAMPOS_D505, splited_d505))

                print('BLOCO D505')
                print(reg_dict)
                bloco_d505.append(reg_dict)

            elif line.startswith("|D100|"):
                index_d100 += 1
                splited_d100 = line.strip().split("|")
                splited_d100[12] = datetime.strptime(splited_d100[12], "%d%m%Y") if splited_d100[12] else None
                splited_d100[11] = datetime.strptime(splited_d100[11], "%d%m%Y") if splited_d100[11] else None
                for i in [15, 16, 18, 19, 20, 21]:
                    splited_d100[i] = splited_d100[i].replace(",", ".") if splited_d100[i] else 0
                splited_d100[-1] = index_d100

                splited_d100 = splited_d100[2:]
                reg_dict = dict(zip(CAMPOS_D100, splited_d100))
                bloco_d100.append(reg_dict)

            # --- ELIF para |D101| ---
            elif line.startswith("|D101|"):
                parts = line.strip().split("|")[2:]
                for i in [2, 4, 5, 6]:
                    parts[i] = parts[i].replace(",", ".") if parts[i] else 0
                parts[-1] = index_d100
                reg_dict = dict(zip(CAMPOS_D101, parts))
                bloco_d101.append(reg_dict)

            # --- ELIF para |D105| ---
            elif line.startswith("|D105|"):
                parts = line.strip().split("|")[2:]
                for i in [2, 4, 5, 6]:
                    parts[i] = parts[i].replace(",", ".") if parts[i] else 0
                parts[-1] = index_d100
                reg_dict = dict(zip(CAMPOS_D105, parts))
                bloco_d105.append(reg_dict)

            # --- ELIF para |M100| ---
            elif line.startswith("|M100|"):
                parts = line.strip().split("|")[2:]
                for i in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14]:
                    parts[i] = parts[i].replace(",", ".") if parts[i] else 0
                reg_dict = dict(zip(CAMPOS_M100, parts))
                bloco_m100.append(reg_dict)

            # --- ELIF para |M105| ---
            elif line.startswith("|M105|"):
                parts = line.strip().split("|")[2:]
                for i in [3, 4, 5, 6, 7, 8]:
                    parts[i] = parts[i].replace(",", ".") if parts[i] else 0
                reg_dict = dict(zip(CAMPOS_M105, parts))
                bloco_m105.append(reg_dict)

            # --- ELIF para |M500| ---
            elif line.startswith("|M500|"):
                parts = line.strip().split("|")[2:]
                for i in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14]:
                    parts[i] = parts[i].replace(",", ".") if parts[i] else 0
                reg_dict = dict(zip(CAMPOS_M500, parts))
                bloco_m500.append(reg_dict)

            # --- ELIF para |M505| ---
            elif line.startswith("|M505|"):
                parts = line.strip().split("|")[2:]
                for i in [3, 4, 5, 6, 7, 8]:
                    parts[i] = parts[i].replace(",", ".") if parts[i] else 0
                reg_dict = dict(zip(CAMPOS_M505, parts))
                bloco_m505.append(reg_dict)
    
            elif line.startswith("|M200|"):
                parts = line.strip().split("|")[2:]
                parts = [p.replace(",", ".") if i > 0 else p for i, p in enumerate(parts)]
                reg_dict = dict(zip(CAMPOS_M200, parts))
                bloco_m200.append(reg_dict)
                index_m200 = len(bloco_m200)

            elif line.startswith("|M205|"):
                parts = line.strip().split("|")[2:]
                parts[2] = parts[2].replace(",", ".") if parts[2] else 0
                parts.append(index_m200)
                reg_dict = dict(zip(CAMPOS_M205, parts))
                bloco_m205.append(reg_dict)

            elif line.startswith("|M210|"):
                parts = line.strip().split("|")[2:]
                for i in range(len(parts)):
                    if i >= 1:  # pular REG
                        parts[i] = parts[i].replace(",", ".") if parts[i] else 0
                reg_dict = dict(zip(CAMPOS_M210, parts))
                bloco_m210.append(reg_dict)
                index_m210 = len(bloco_m210)

            elif line.startswith("|M220|"):
                parts = line.strip().split("|")[2:]
                if parts[5]:  # DT_REF
                    try:
                        parts[5] = datetime.strptime(parts[5], "%d%m%Y")
                    except:
                        parts[5] = None
                parts.append(index_m210)
                reg_dict = dict(zip(CAMPOS_M220, parts))
                bloco_m220.append(reg_dict)

            elif line.startswith("|M225|"):
                parts = line.strip().split("|")[2:]
                for i in [0, 2, 3, 4]:
                    parts[i] = parts[i].replace(",", ".") if parts[i] else 0
                if parts[5]:
                    try:
                        parts[5] = datetime.strptime(parts[5], "%d%m%Y")
                    except:
                        parts[5] = None
                parts.append(len(bloco_m220))
                reg_dict = dict(zip(CAMPOS_M225, parts))
                bloco_m225.append(reg_dict)

            elif line.startswith("|M600|"):
                parts = line.strip().split("|")[2:]
                parts = [p.replace(",", ".") if i > 0 else p for i, p in enumerate(parts)]
                reg_dict = dict(zip(CAMPOS_M600, parts))
                bloco_m600.append(reg_dict)
                index_m600 = len(bloco_m600)

            elif line.startswith("|M605|"):
                parts = line.strip().split("|")[2:]
                parts[2] = parts[2].replace(",", ".") if parts[2] else 0
                parts.append(index_m600)
                reg_dict = dict(zip(CAMPOS_M605, parts))
                bloco_m605.append(reg_dict)

            elif line.startswith("|M610|"):
                parts = line.strip().split("|")[2:]
                for i in range(len(parts)):
                    if i >= 1:
                        parts[i] = parts[i].replace(",", ".") if parts[i] else 0
                reg_dict = dict(zip(CAMPOS_M610, parts))
                bloco_m610.append(reg_dict)
                index_m610 = len(bloco_m610)

            elif line.startswith("|M620|"):
                parts = line.strip().split("|")[2:]
                parts[5] = datetime.strptime(parts[5], "%d%m%Y") if parts[5] else None
                parts.append(index_m610)
                reg_dict = dict(zip(CAMPOS_M620, parts))
                bloco_m620.append(reg_dict)
                index_m620 = len(bloco_m620)

            elif line.startswith("|M625|"):
                parts = line.strip().split("|")[2:]
                print(parts)
                for i in [0, 2, 3]:
                    parts[i] = parts[i].replace(",", ".") if parts[i] else 0
                parts[4] = datetime.strptime(parts[4], "%d%m%Y") if parts[4] else None
                parts.append(index_m620)
                reg_dict = dict(zip(CAMPOS_M625, parts))
                bloco_m625.append(reg_dict)

    return {

        'empresa_cnpj':cnpj,
        'competencia':competencia,

        'registros_0000':bloco_0000,
        'registros_0150':bloco_0150,
        'registros_0200':bloco_0200,

        'registros_a100':bloco_a100,
        'registros_a170':bloco_a170,

        'registros_c100':bloco_c100,
        'registros_c170':bloco_c170,

        'registros_c500':bloco_c500,
        'registros_c501':bloco_c501,
        'registros_c505':bloco_c505,

        'registros_d100':bloco_d100,
        'registros_d101':bloco_d101,
        'registros_d105':bloco_d105,

        'registros_d500':bloco_d500,
        'registros_d501':bloco_d501,
        'registros_d505':bloco_d505,

        'registros_f100':bloco_f100,
        'registros_f130':bloco_f130,
        
        'registros_m100':bloco_m100,
        'registros_m105':bloco_m105,

        
        'registros_m200':bloco_m200,
        'registros_m205':bloco_m205,
        'registros_m210':bloco_m210,
        'registros_m220':bloco_m220,
        'registros_m225':bloco_m225,

        'registros_m500':bloco_m500,
        'registros_m505':bloco_m505,
        
        'registros_m600': bloco_m600,
        'registros_m605': bloco_m605,
        'registros_m610': bloco_m610,
        'registros_m620': bloco_m620,
        'registros_m625': bloco_m625,

        }

def gerar_a100_x_a170(dados_dict):
    df_a100 = pd.DataFrame(dados_dict['registros_a100'])
    
    df_a170 = pd.DataFrame(dados_dict['registros_a170'])

    df_final = df_a170.merge(
        df_a100,
        how='left',
        left_on='id_a100',   # PK2 na A170
        right_on='id_a100',    # PK na A100
        suffixes=('', '.1')
    )

    #Junto COD PART NUM DOC e o DATA INDEX
    
    df_final['cod_item'] = df_final['cod_item'].astype(str).str.lstrip('0')
    df_final['cod_part'] = df_final['cod_part'].astype(str).str.lstrip('V').str.lstrip('0')
    df_final['num_doc'] = df_final['num_doc'].astype(str).str.lstrip('0')
    df_final['num_item'] = df_final['num_item'].astype(str).str.lstrip('0')
    df_final['DATA_INDEX'] = df_final['dt_doc'].apply(date_to_int)
    df_final['DATA_INDEX'] = df_final['DATA_INDEX'].astype(str)
    df_final['DATA_INDEX'] = df_final['DATA_INDEX'].str.replace('.0', '')
    df_final['cod_part'] = df_final['cod_part'].astype(str)
    df_final['num_doc'] = df_final['num_doc'].astype(str)
    df_final['DATA_INDEX'] = df_final['DATA_INDEX'].astype(str)

    df_final['INDEX'] = df_final['cod_part'] + df_final['num_doc'] + df_final['DATA_INDEX']
    df_final['INDEX_ITEM'] = df_final['INDEX'] + df_final['num_item'].astype(str)
    
    df_final['DESC_IND_OPER'] = df_final['ind_oper'].astype(str).map(desc_ind_oper)
    df_final['DESC_IND_EMIT'] = df_final['ind_emit'].astype(str).map(desc_ind_emit)
    df_final['DESC_IND_PGTO'] = df_final['ind_pgto'].astype(str).map(desc_ind_pgto)
    df_final['DESC_COD_SIT'] = df_final['cod_sit'].astype(str).map(desc_cod_sit)
    df_final['DESC_IND_ORIG_CRED'] = df_final['ind_orig_cred'].astype(str).map(desc_ind_orig_cred)


    colunas_reorganizadas = [
        # Cabeçalho
        'INDEX', 'INDEX_ITEM', 'id_a100','CNPJ_ESTAB' ,'DATA_INDEX',  # INDEX/INDEX_ITEM substituem os controles internos
        'ind_oper', 'DESC_IND_OPER', 'ind_emit', 'DESC_IND_EMIT',
        'cod_part', 'cod_sit', 'ser', 'sub', 'num_doc', 'chv_nfse',
        'dt_doc', 'dt_exe_serv', 'vl_doc', 'ind_pgto', 'DESC_IND_PGTO','DESC_COD_SIT', 'vl_desc',
        'vl_bc_pis', 'vl_pis', 'vl_bc_cofins', 'vl_cofins',
        'vl_pis_ret', 'vl_cofins_ret', 'vl_iss',

        # Itens da nota
        'num_item', 'cod_item', 'descr_compl', 'vl_item', 'vl_desc.1',
        'nat_bc_cred', 'ind_orig_cred', 'DESC_IND_ORIG_CRED',
        'cst_pis', 'vl_bc_pis.1', 'aliq_pis', 'vl_pis.1',
        'cst_cofins', 'vl_bc_cofins.1', 'aliq_cofins', 'vl_cofins.1',
        'cod_cta', 'cod_ccus'
    ]

    df_final = df_final[colunas_reorganizadas]

    """
    df_final = df_final.merge(
        df_a100,
        how='left',
        left_on='id_a100',   # PK2 na A170
        right_on='id_a100'    # PK na A100
    )
    """



    return df_final

def gerar_c100_x_c170(dados_dict):

    # DataFrames
    df_c100 = pd.DataFrame(dados_dict['registros_c100'])

    print(df_c100)
    print(df_c100.columns)
    
    df_c170 = pd.DataFrame(dados_dict['registros_c170'])

    # Merge base
    df_final = df_c170.merge(
        df_c100,
        how='left',
        left_on='id_c100',
        right_on='id_c100',
        suffixes=('', '.1')
    )

    # Criar INDEX e INDEX_ITEM
    
    df_final['cod_item'] = df_final['cod_item'].astype(str).str.lstrip('0')
    df_final['cod_part'] = df_final['cod_part'].astype(str).str.lstrip('V')
    df_final['cod_part'] = df_final['cod_part'].astype(str).str.lstrip('0')
    df_final['num_item'] = df_final['num_item'].astype(str).str.lstrip('C')
    df_final['num_item'] = df_final['num_item'].astype(str).str.lstrip('B')
    df_final['num_item'] = df_final['num_item'].astype(str).str.lstrip('0')
    

    
    df_final['num_doc'] = df_final['num_doc'].astype(str).str.lstrip('0')
    
    df_final['num_doc'] = df_final['num_doc'].astype(str).str.lstrip('0')
    df_final['DATA_INDEX'] = df_final['dt_doc'].apply(date_to_int).astype(str).str.replace('.0', '')
    df_final['cod_part'] = df_final['cod_part'].astype(str)
    df_final['num_doc'] = df_final['num_doc'].astype(str)

    df_final['INDEX'] = df_final['cod_part'] + df_final['num_doc'] + df_final['DATA_INDEX']
    df_final['INDEX_ITEM'] = df_final['INDEX'] + df_final['num_item'].astype(str)
    

    # Mapear descrições de campos IND_
    df_final['DESC_IND_OPER'] = df_final['ind_oper'].astype(str).map(desc_ind_oper)
    df_final['DESC_IND_EMIT'] = df_final['ind_emit'].astype(str).map(desc_ind_emit)
    df_final['DESC_IND_FRT'] = df_final['ind_frt'].astype(str).map(desc_ind_frt)

    df_final['DESC_COD_SIT'] = df_final['cod_sit'].astype(str).map(desc_cod_sit)

    # Reorganizar colunas conforme especificado
    colunas = [
        "INDEX", "INDEX_ITEM", "num_doc_contab", "data", "cnpj", "reg", "cnpj_estab", "id_c100", "ind_oper",
        "DESC_IND_OPER", "ind_emit", "DESC_IND_EMIT", "cod_part", "cnpj_part", "ie_part", "cpf_part",
        "nome_part", "pais_part", "uf_part", "municipio_part", "cod_mod", "desc_cod_mod", "cod_sit",
        "desc_cod_sit", "ser", "num_doc", "chv_nfe", "dt_doc", "dt_e_s", "vl_doc", "ind_pgto",
        "vl_desc", "vl_abat_nt", "vl_merc", "ind_frt", "DESC_IND_FRT", "vl_frt", "vl_seg", "vl_out_da",
        "vl_bc_icms", "vl_icms", "vl_bc_icms_st", "vl_icms_st", "vl_ipi", "vl_pis", "vl_cofins",
        "vl_pis_st", "vl_cofins_st", "reg_1", "pk_1", "num_item", "cod_item", "descr_compl",
        "descr_item_0200", "desc_tipo_item_0200", "cod_ncm_0200", "desc_cod_gen_0200", "qtd", "unid",
        "vl_item", "vl_desc_1", "ind_mov", "cst_icms", "desc_st_icms", "cfop", "desc_cfop", "cod_nat",
        "vl_bc_icms_1", "aliq_icms", "vl_icms_1", "vl_bc_icms_st_1", "aliq_st", "vl_icms_st_1",
        "ind_apur", "cst_ipi", "desc_cst_ipi", "cod_enq", "vl_bc_ipi", "aliq_ipi", "vl_ipi_1",
        "cst_pis", "desc_cst_pis", "vl_bc_pis", "aliq_pis", "quant_bc_pis", "aliq_pis_quant",
        "vl_pis_1", "cst_cofins", "vl_bc_cofins", "aliq_cofins", "quant_bc_cofins",
        "aliq_cofins_quant", "vl_cofins_1", "cod_cta", "DATA_INDEX", "data_doc_aux_c",
        "num_item_doc", "index_item", "pedido", "classif_contab", "op_diagrama", "pis", "cofins",
        "teste_vl_item", "ficha_orcamentaria", "item", "conta", "texto", "iva_credito", "tipo_doc_compras",
        "contrato", "Crédito?", "Natureza"
    ]

    # Ajustar para colunas presentes no DataFrame
    #colunas_existentes = [col for col in colunas if col in df_final.columns]
    #df_final = df_final[colunas_existentes]
    print(df_final.columns)
    print(df_final)

    return df_final

def cruzar_blocos_com_dados_dos_participantes(dados_dict):
    bloco_a100_x_a170 = gerar_a100_x_a170(dados_dict)
    bloco_c100_x_c170 = gerar_c100_x_c170(dados_dict)
    
    bloco_participantes = leitor_paises_e_municipios(dados_dict,tabela_paises='paises.txt',tabela_municipios='municipios.txt')
    print(bloco_participantes)


    
    bloco_participantes['cod_part'] = bloco_participantes['cod_part'].astype(str).str.lstrip('V').str.lstrip('0')

    df_a100_final = bloco_a100_x_a170.merge(
        bloco_participantes,
        how='left',
        left_on='cod_part',
        right_on='cod_part'
    )

   

    df_c100_final = bloco_c100_x_c170.merge(
        bloco_participantes,
        how='left',
        left_on='cod_part',
        right_on='cod_part'
    )


   

    print(bloco_c100_x_c170[['vl_merc']])
   
    return df_a100_final,df_c100_final

def cruzar_blocos_com_dados_dos_materiais(dados_dict):
    bloco_a100_x_a170,bloco_c100_x_c170 = cruzar_blocos_com_dados_dos_participantes(dados_dict)
 
    bloco_materiais = pd.DataFrame(dados_dict['registros_0200'])

    print(bloco_materiais)
    bloco_materiais['cod_item'] = bloco_materiais['cod_item'].astype(str).str.lstrip('0')

    df_a100_final = bloco_a100_x_a170.merge(
        bloco_materiais[['cod_item','descr_item','tipo_item','cod_lst']], #'cod_gen'
        how='left',
        left_on='cod_item',
        right_on='cod_item'
    )

    df_c100_final = bloco_c100_x_c170.merge(
        bloco_materiais[['cod_item','descr_item','tipo_item','cod_lst','cod_gen','cod_ncm']],
        how='left',
        left_on='cod_item',
        right_on='cod_item'
    )
     

    return df_a100_final,df_c100_final

def leitor_paises_e_municipios(dados_dict,tabela_paises,tabela_municipios):

    bloco_0150 = dados_dict['registros_0150']
    bloco_paises = []
    bloco_municipios = []
    bloco_paises_columns = [
            
            "cod_pais",
            "PAIS",
            "DATA",
            "",
            
        ]
        
    
    bloco_municipios_columns = [
        
        "cod_mun",
        "MUN",
        "DATA",
        ""
    ]


    with open(tabela_paises,'r+',encoding='utf-8') as paises:
        for line in paises.readlines():
            splited_paises = line.split("|")
            bloco_paises.append(splited_paises)
            print(splited_paises)

    with open(tabela_municipios,'r+',encoding='utf-8') as municipios:
        for line in municipios.readlines():
            splited_municipios = line.split("|")
            bloco_municipios.append(splited_municipios)

            print(splited_municipios)


    df_participantes = pd.DataFrame(bloco_0150)
    df_municipios = pd.DataFrame(bloco_municipios,columns=bloco_municipios_columns)

    df_paises = pd.DataFrame(bloco_paises,columns=bloco_paises_columns)

    print(df_paises.columns)
    print(df_participantes.columns)

    print(df_paises['cod_pais'])
    print(df_participantes[['cod_pais','nome']])


    del df_paises['DATA']
    del df_paises['']

    del df_municipios['DATA']
    del df_municipios['']

    df_participantes['cod_pais'] = df_participantes['cod_pais'].astype(str).str.lstrip('0')
    df_paises['cod_pais'] = df_paises['cod_pais'].astype(str).str.lstrip('0')

    df_participantes_com_paises = df_participantes.merge(df_paises,on='cod_pais',how='left')

   
    
   
    df_participantes_com_paises_e_municipios = df_participantes_com_paises.merge(df_municipios,on='cod_mun',how='left')
    #df_c500 = pd.DataFrame(c500)
    #df_participantes = df_participantes.drop('SUFRAMA',axis=1)
    del df_participantes_com_paises_e_municipios['suframa']
    del df_participantes_com_paises_e_municipios['end']
    del df_participantes_com_paises_e_municipios['num']
    del df_participantes_com_paises_e_municipios['compl']
    del df_participantes_com_paises_e_municipios['bairro']
    #del df_participantes_com_paises_e_municipios['reg']

    df_participantes_com_paises_e_municipios['ie_part'] = df_participantes_com_paises_e_municipios['ie']
    del df_participantes_com_paises_e_municipios['ie']
    #del df_participantes_com_paises_e_municipios['cpf']

    del df_participantes_com_paises_e_municipios['cod_pais']
    #del df_participantes_com_paises_e_municipios['']

    del df_participantes_com_paises_e_municipios['cod_mun']

    

    return df_participantes_com_paises_e_municipios

def processar_zfiscal(zfiscal,planilha_creditos=r'W:\04 - Diretoria Financeira\contabilidade\GESTÃO TRIBUTÁRIA\IV. PLANEJAMENTO TRIBUTARIO\PIS COFINS\Análise de créditos\Estudo Créditos (03.23-04.24).xlsb'):

    df_zfiscal = pd.read_excel(zfiscal)

    ## Tratamento de colunas para index ##

    df_zfiscal['Nº da nota fiscal eletrônica'] = df_zfiscal['Nº da nota fiscal eletrônica'].astype(str)
    df_zfiscal['Nº nota fiscal'] = df_zfiscal['Nº nota fiscal'].astype(str)

    df_zfiscal['Nº da nota fiscal eletrônica'] = df_zfiscal['Nº da nota fiscal eletrônica'].str.replace('.0', '')

    #### TRANSFORMANDO A DATA EM NUM EXCEL PARA O INDEX ####
    # Formatando a coluna 'Data documento' para o formato desejado 'dd/mm/yyyy'
    df_zfiscal['Data documento'] = df_zfiscal['Data documento'].dt.strftime('%d/%m/%Y')
    df_zfiscal['Data documento'] = df_zfiscal['Data documento'].astype(str)

    df_zfiscal['DATA_DOC_AUX'] = df_zfiscal['Data documento'].apply(datetime_to_excel_date)

    df_zfiscal['DATA_DOC_AUX'] = df_zfiscal['DATA_DOC_AUX'].astype(str)
    df_zfiscal['DATA_DOC_AUX'] = df_zfiscal['DATA_DOC_AUX'].str.replace('.0', '')

    ## Criando Index concatenado da ZFISCAL ##

    ## INDEX ZFISCAL ##

    # Transformando todas as colunas em STR para fazer o tratamento
    df_zfiscal['ID parceiro'] = df_zfiscal['ID parceiro'].astype(str)
    df_zfiscal['Nº da nota fiscal eletrônica'] = df_zfiscal['Nº da nota fiscal eletrônica'].astype(str)
    df_zfiscal['Nº nota fiscal'] = df_zfiscal['Nº nota fiscal'].astype(str)
    #df_zfiscal['DATA_DOC_AUX'] = pd.to_datetime(df_zfiscal['DATA_DOC_AUX']).dt.strftime('%Y%m%d')  # Convertendo para string e removendo os '-'

    # Aplicando a lógica condicional para criar a nova coluna 'INDEX'
    df_zfiscal['INDEX'] = df_zfiscal.apply(lambda x: x['ID parceiro'] + (x['Nº da nota fiscal eletrônica'] if x['Nº da nota fiscal eletrônica'] != 'nan' else x['Nº nota fiscal']) + x['DATA_DOC_AUX'], axis=1)

    ## Criando o novo Index_item da ZFISCAL ##

    # Aplica a função na coluna 'Nº item do documento' para remover os (zeros finais)
    df_zfiscal['Nº item do documento'] = df_zfiscal['Nº item do documento'].apply(tratar_numero_item)
    df_zfiscal['NUM_ITEM_DOC'] = df_zfiscal['Nº item do documento'].astype(str)
    df_zfiscal['NUM_ITEM_DOC'] = df_zfiscal['NUM_ITEM_DOC'].astype(str)

    # Criando a coluna 'INDEX_ITEM'
    df_zfiscal['INDEX_ITEM'] = df_zfiscal.apply(lambda x: x['ID parceiro'] + (x['Nº da nota fiscal eletrônica'] if x['Nº da nota fiscal eletrônica'] != 'nan' else x['Nº nota fiscal']) + x['DATA_DOC_AUX'] + x['NUM_ITEM_DOC'], axis=1)
    df_zfiscal['Nº doc.faturamento'] = df_zfiscal['Nº doc.faturamento'].astype(str)


    df_zfiscal['DATA_INDEX'] = df_zfiscal['Data documento'].apply(date_to_int).astype(str)
    df_zfiscal['NUM_ITEM_DOC'] = df_zfiscal['Nº item do documento'].apply(tratar_numero_item).astype(str).str.replace('.0', '')
    df_zfiscal['NUM_DOC'] = df_zfiscal['Nº da nota fiscal eletrônica'].combine_first(df_zfiscal['Nº nota fiscal']).astype(str).str.replace('.0', '') #Retirar zeros
    df_zfiscal['ID parceiro'] = df_zfiscal['ID parceiro'].astype(str)
    df_zfiscal['CLASSIFICACAO_CONTABIL'] = df_zfiscal[
        ['Elemento PEP', 'Diagrama de rede', 'Centro custo', 'Imobilizado']
    ].bfill(axis=1).iloc[:, 0]


    

    df_zfiscal['Texto'] = (
        df_zfiscal['Texto-parte1'].astype(str)
        + df_zfiscal['Texto-parte2'].astype(str)
        + df_zfiscal['Texto-parte3'].astype(str)
        + df_zfiscal['Texto-parte4'].astype(str)
        )

    
    

    df_zfiscal = df_zfiscal[['INDEX_ITEM','CLASSIFICACAO_CONTABIL','ID parceiro','Nome 1','Ficha orçamentária',
                             'Conta do Razão','Texto','Item do documento','Nº doc.faturamento',
                             'Documento de compras','Tp.doc.compras','Operacao diagrama de rede',
                             'Contrato básico','Código de imposto','NUM_ITEM_DOC']]
    
    #Vincular com créditos
    df_contratos=pd.read_excel(planilha_creditos)

    df_bloco_com_creditos = df_zfiscal.merge(
                df_contratos[['Contratos','Crédito?', 'Natureza']],
                how='left',
                left_on='Contrato básico',
                right_on='Contratos'
            )

    return df_bloco_com_creditos   

def cruzar_zfiscal_com_blocos(dados_dict,path_zfiscal):
    bloco_a100,bloco_c100 = cruzar_blocos_com_dados_dos_materiais(dados_dict=dados_dict)
    bloco_zfiscal = processar_zfiscal(path_zfiscal)


    
    df_a100_final = bloco_a100.merge(
        bloco_zfiscal,
        how='left',
        on='INDEX_ITEM'
    )

    df_c100_final = bloco_c100.merge(
        bloco_zfiscal,
        how='left',
        on='INDEX_ITEM'
    )

    df_c100_final = df_c100_final.drop_duplicates() 
    #df_a100_final.to_excel('a100.xlsx')
    #df_c100_final.to_excel('c100.xlsx')
    #bloco_zfiscal.to_excel('zfiscal_e.xlsx')


    return df_a100_final,df_c100_final,bloco_zfiscal

def gerar_colunas_adicionais(dados_dict,path_zfiscal):
    
    df_bloco_a,df_bloco_c,bloco_zfiscal = cruzar_zfiscal_com_blocos(dados_dict,path_zfiscal=path_zfiscal) 

            
    fator_pis = 1.65 / 100
    fator_cofins = 7.6 / 100

    #Bloco A

    df_bloco_a['vl_bc_pis'] = df_bloco_a['vl_bc_pis'].astype(float)
    df_bloco_a['vl_bc_cofins'] = df_bloco_a['vl_bc_cofins'].astype(float)
    df_bloco_a['vl_doc'] = df_bloco_a['vl_doc'].astype(float)
    df_bloco_a['vl_item'] = df_bloco_a['vl_item'].astype(float)

    df_bloco_a['PIS'] = df_bloco_a['vl_bc_pis'] * fator_pis
    df_bloco_a['COFINS'] = df_bloco_a['vl_bc_cofins'] * fator_cofins
    soma_vl_item = df_bloco_a.groupby('INDEX')['vl_item'].transform('sum')
    
    print(df_bloco_a['vl_doc'])
    print(type(df_bloco_a['vl_doc']))
    print(soma_vl_item)
    df_bloco_a['TESTE_VL_ITEM'] = df_bloco_a['vl_doc'] - soma_vl_item
    
    df_bloco_a['IVA_CREDITO']=df_bloco_a['Código de imposto'].map(codigos_iva)

    #Bloco C
    """"""
    df_bloco_c['vl_bc_pis'] = df_bloco_c['vl_bc_pis'].astype(float)
    df_bloco_c['vl_bc_cofins'] = df_bloco_c['vl_bc_cofins'].astype(float)
    df_bloco_c['vl_doc'] = df_bloco_c['vl_doc'].astype(float)
    df_bloco_c['vl_item'] = df_bloco_c['vl_item'].astype(float)
    
    df_bloco_c['PIS'] = df_bloco_c['vl_bc_pis'] * fator_pis
    df_bloco_c['COFINS'] = df_bloco_c['vl_bc_cofins'] * fator_cofins
    soma_vl_item = df_bloco_c.groupby('INDEX')['vl_item'].transform('sum')
    
    df_bloco_c['TESTE_VL_ITEM'] = df_bloco_c['vl_doc'] - soma_vl_item
    df_bloco_c['IVA_CREDITO']=df_bloco_c['Código de imposto'].map(codigos_iva)

    
   
   
    mapeamento_a100 = {
        'NOME': 'NOME_PART',
        'cnpj': 'CNPJ_PART',
        'CPF': 'CPF_PART',
        'PAIS': 'PAIS_PART',
        'MUN': 'MUNICIPIO',
        'ie_part': 'IE',
        'CLASSIFICACAO_CONTABIL': 'CLASSIF_CONTAB',
        'Ficha orçamentária': 'FICHA_ORCAMENTARIA',
        'Conta do Razão': 'CONTA',
        'Item do documento': 'ITEM',
        'Documento de compras': 'PEDIDO',
        'Operacao diagrama de rede': 'OP_DIAGRAMA',
        'dt_doc':'DATA_DOC',
        'dt_exe_serv':'DATA_EXE_SERV',
        'id_a100':'PK.1',
        'Nº doc.faturamento':'NUM_DOC_CONTAB'

    }

    mapeamento_c100 = {
        'NOME': 'NOME_PART',
        'cnpj': 'CNPJ_PART',
        'cpf': 'CPF_PART',
        'PAIS_PART': 'PAIS',
        'MUNICIPIO': 'MUNICIPIO_PART',
        'ie': 'IE_PART',
        'uf':'UF_PART',
        'CLASSIFICACAO_CONTABIL': 'CLASSIF_CONTAB',
        'Ficha orçamentária': 'FICHA_ORCAMENTARIA',
        'Conta do Razão': 'CONTA',
        'Item do documento': 'ITEM',
        'Documento de compras': 'PEDIDO',
        'Operacao diagrama de rede': 'OP_DIAGRAMA',
        'dt_doc':'DATA_DOC',
        'dt_exe_serv':'DATA_E_S',
        'id_c100':'PK.1',
        'Nº doc.faturamento':'NUM_DOC_CONTAB'

    }
    

    print(dados_dict['registros_0000'][0]['dt_ini'])
    
    
    
    df_bloco_a['DATA'] = dados_dict['registros_0000'][0]['dt_ini']
    
    #df_bloco_a['CNPJ_ESTAB'] = None
    
    df_bloco_a['REG.1'] = None
    df_bloco_a['UF'] = None
    #df_bloco_a['DESC_COD_SIT'] = None
    df_bloco_a['REG'] = None
    df_bloco_a['PK']=None

    
    df_bloco_c['DATA'] = dados_dict['registros_0000'][0]['dt_ini']
    
    #df_bloco_c['CNPJ_ESTAB'] = None
    
    df_bloco_c['REG.1'] = None
    df_bloco_c['UF'] = None
    #df_bloco_c['DESC_COD_SIT'] = None
    df_bloco_c['REG'] = None
    df_bloco_c['PK']=None

    df_bloco_a['DESC_TIPO_ITEM'] = df_bloco_a['tipo_item'].map(desc_tipo_item)

    df_bloco_c['DESC_ST_ICMS'] = df_bloco_c['cst_icms'].map(desc_cst_icms)
    df_bloco_c['DESC_COD_MOD'] = df_bloco_c['cod_mod'].map(desc_cod_mod)
    df_bloco_c['DESC_COD_GEN_0200'] = df_bloco_c['cod_gen'].map(desc_cod_gen)
    df_bloco_c['DESC_TIPO_ITEM_0200'] = df_bloco_c['tipo_item'].map(desc_tipo_item) #NÃO É COD_ITEM, VERIIFCAR QUAL

    #df_bloco_c['DESC_CFOP'] = ''
    #df_bloco_c['DATA_INDEX'] = df_bloco_a['cfop']
    tabela_cfop = pd.read_excel('TABELA_CFOP.xlsx')
    tabela_cfop['CFOP'] = tabela_cfop['CFOP'].astype(str).str.replace('.0', '')
    tabela_cfop_dict = tabela_cfop.set_index('CFOP')['Descricao'].to_dict()

    print(tabela_cfop)

    df_bloco_c['DESC_CST_IPI'] = df_bloco_c['cst_ipi'].map(desc_cst_ipi)
    df_bloco_c['DESC_CFOP'] = df_bloco_c['cfop'].map(tabela_cfop_dict)

    df_bloco_a = df_bloco_a.rename(columns=mapeamento_a100)
    df_bloco_c = df_bloco_c.rename(columns=mapeamento_c100)

    df_bloco_a['cnpj'] = dados_dict['registros_0000'][0]['cnpj']
    df_bloco_a['REG'] = 'A100'
    df_bloco_a['REG.1'] = 'A170'
    df_bloco_c['cnpj'] = dados_dict['registros_0000'][0]['cnpj']




    df_bloco_c['REG'] = 'C100'
    df_bloco_c['REG.1'] = 'C170'
    df_bloco_c['DATA_DOC_AUX_C'] = df_bloco_c['DATA']
    #Reposicionar colunas   


    colunas_a = [
    'INDEX', 'INDEX_ITEM', 'NUM_DOC_CONTAB', 'DATA', 'cnpj', 'REG.1', 'PK.1', 'CNPJ_ESTAB',
    'ind_oper', 'DESC_IND_OPER', 'ind_emit', 'DESC_IND_EMIT', 'cod_part','nome', 'CNPJ_PART',
    'IE', 'cpf', 'PAIS_PART', 'UF', 'MUNICIPIO', 'cod_sit', 'DESC_COD_SIT', 'ser', 'sub',
    'num_doc', 'DATA_DOC', 'DATA_EXE_SERV', 'chv_nfse', 'vl_doc', 'ind_pgto', 'vl_desc.1', #'DESC_IND_PGTO',
    'vl_bc_pis.1', 'vl_pis.1', 'vl_bc_cofins.1', 'vl_cofins.1', 'vl_pis_ret', 'vl_cofins_ret',
    'vl_iss', 'REG', 'PK', 'num_item', 'cod_item', 'descr_item', 'descr_compl','tipo_item','DESC_TIPO_ITEM', #'cod_gen',
    'cod_lst', 'vl_item', 'vl_desc', 'nat_bc_cred', 'ind_orig_cred', 'cst_pis', 'DESC_COD_SIT', #'DESC_IND_ORIG_CRED',
    'vl_bc_pis', 'aliq_pis', 'vl_pis', 'cst_cofins', 'vl_bc_cofins', 'aliq_cofins', 'vl_cofins',
    'cod_cta', 'cod_ccus', 'DATA_INDEX',  'NUM_ITEM_DOC', 'INDEX_ITEM', 'PEDIDO',
    'CLASSIF_CONTAB', 'OP_DIAGRAMA', 'PIS', 'COFINS', 'TESTE_VL_ITEM', 'FICHA_ORCAMENTARIA',
    'ITEM', 'CONTA', 'Texto', 'IVA_CREDITO', 
    'Tp.doc.compras', 'Contrato básico', 'Código de imposto', 'Contratos', 'Crédito?',
    'Natureza'

       
        ]
    
    print(df_bloco_a.columns)
    df_bloco_a = df_bloco_a[colunas_a]

    df_bloco_a['PK'] = df_bloco_a['PK.1']
    colunas_c = [
    'INDEX', 'INDEX_ITEM', 'NUM_DOC_CONTAB', 'DATA', 'cnpj', 'REG', 'CNPJ_ESTAB', 'PK',
    'ind_oper', 'DESC_IND_OPER', 'ind_emit', 'DESC_IND_EMIT', 'cod_part', 'CNPJ_PART',
    'ie_part', 'CPF_PART', 'nome', 'PAIS','UF', 'MUN', 'cod_mod', 'DESC_COD_MOD',
    'cod_sit', 'DESC_COD_SIT','ser', 'num_doc', 'chv_nfe', 'DATA_DOC', 'dt_e_s', 'vl_doc', 
    'ind_pgto', 'vl_desc',
    'vl_abat_nt', 'vl_merc', 'ind_frt', 'DESC_IND_FRT', 'vl_frt', 'vl_seg', 'vl_out_da',
    'vl_bc_icms', 'vl_icms', 'vl_bc_icms_st', 'vl_icms_st', 'vl_ipi', 'vl_pis', 'vl_cofins',
    'vl_pis_st', 'vl_cofins_st', 'REG.1', 'PK.1', 'num_item', 'cod_item', 'descr_compl',
    'descr_item','tipo_item',  'DESC_TIPO_ITEM_0200', 'cod_ncm', 'DESC_COD_GEN_0200', 'qtd', 'unid', #FALTA NCM
    'vl_item', 'vl_desc.1', 'ind_mov', 'cst_icms', 'DESC_ST_ICMS', 'cfop', 'DESC_CFOP',
    'cod_nat', 'vl_bc_icms.1', 'aliq_icms', 'vl_icms.1', 'vl_bc_icms_st.1', 'aliq_st',
    'vl_icms_st.1', 'ind_apur', 'cst_ipi', 'DESC_CST_IPI', 'cod_enq', 'vl_bc_ipi', 'aliq_ipi',
    'vl_ipi.1', 'cst_pis', 'DESC_CST_IPI', 'vl_bc_pis', 'aliq_pis', 'quant_bc_pis',
    'aliq_pis_quant', 'vl_pis.1', 'cst_cofins', 'vl_bc_cofins', 'aliq_cofins',
    'quant_bc_cofins', 'aliq_cofins_quant', 'vl_cofins.1', 'cod_cta', 'DATA_INDEX','DATA_DOC_AUX_C',
    'NUM_ITEM_DOC', 'INDEX_ITEM', 'PEDIDO', 'CLASSIF_CONTAB', 'OP_DIAGRAMA', 'PIS', 'COFINS',
    'TESTE_VL_ITEM', 'FICHA_ORCAMENTARIA', 'ITEM', 'CONTA', 'Texto', 'IVA_CREDITO',
    'cod_lst', 'cod_gen','Tp.doc.compras', 'Contrato básico', 'Código de imposto', 'Contratos',
    'Crédito?', 'Natureza', 

    # 🟨 Campos de c_1 que não estão em c_2:
    
]

    df_bloco_c = df_bloco_c[colunas_c]

    
    df_bloco_c['PK'] = df_bloco_c['PK.1']

    bloco_zfiscal.to_excel('example.xlsx')
    return df_bloco_a,df_bloco_c,bloco_zfiscal

def gera_indice_fbl3n(dados_dict,path_zfiscal,fbl3n_file):
    #Gera dict do a100
    #Gera dict do c100
    #Gera dict do zfiscal
    bloco_a,bloco_c,bloco_zfiscal=gerar_colunas_adicionais(dados_dict=dados_dict,path_zfiscal=path_zfiscal)

    df_zfiscal_cru = pd.read_excel(path_zfiscal)
    df_razao = pd.read_excel(fbl3n_file)
    df_razao['CONTA'] = None
    df_razao['REGISTRO_SPED'] = None
    print(df_razao.columns)
    df_razao = df_razao.rename(columns={
        'Nº documento' : 'NUM_DOC_CONTAB',
        'Conta do Razão' : 'CONTA_RAZAO',
        'Montante em moeda interna' : 'MONTANTE',
        'Data do documento' : 'DATA_DOC',
        'Data de lançamento' : 'DATA_LCTO',
        'Tipo de documento' : 'TIPO_DOC'
    })

    print(bloco_a.columns)
    print(bloco_c.columns)
    previa_dict = bloco_a.set_index('NUM_DOC_CONTAB')['cod_part'].to_dict()
    previa_c_dict = bloco_c.set_index('NUM_DOC_CONTAB')['cod_part'].to_dict()
    
    #zfiscal_dict = df_zfiscal_aux.set_index('Nº doc.faturamento.1')['ID parceiro'].to_dict()
    zfiscal_dict = bloco_zfiscal.set_index('Nº doc.faturamento')['ID parceiro'].to_dict()

    # Itere por cada linha do df_razao para atualizar 'CONTA' e 'REGISTRO_SPED'
    for idx, row in df_razao.iterrows():
        num_doc = row['NUM_DOC_CONTAB']
        
        # Verifique em df_previa
        if num_doc in previa_dict:
            df_razao.at[idx, 'CONTA'] = previa_dict[num_doc]
            df_razao.at[idx, 'REGISTRO_SPED'] = 'A100'
            continue  # Pula para a próxima iteração
        
        # Verifique em df_previa_c
        if num_doc in previa_c_dict:
            df_razao.at[idx, 'CONTA'] = previa_c_dict[num_doc]
            df_razao.at[idx, 'REGISTRO_SPED'] = 'C100'
            continue  # Pula para a próxima iteração
        
        # Verifique em df_zfiscal
        if num_doc in zfiscal_dict:
            df_razao.at[idx, 'CONTA'] = zfiscal_dict[num_doc]
            df_razao.at[idx, 'REGISTRO_SPED'] = 'ZFISCAL'


    ### ['FORNECEDOR'] ###
    # Inicialize a coluna 'FORNECEDOR' no df_razao
    df_razao['FORNECEDOR'] = None

    # Converta as colunas relevantes dos dataframes de referência para dicionários para acesso rápido
    previa_fornecedor_dict = bloco_a.set_index('NUM_DOC_CONTAB')['nome'].to_dict()
    previa_c_fornecedor_dict = bloco_c.set_index('NUM_DOC_CONTAB')['nome'].to_dict()
    #zfiscal_fornecedor_dict = df_zfiscal_aux.set_index('Nº doc.faturamento.1')['Nome 1'].to_dict()
    zfiscal_fornecedor_dict = bloco_zfiscal.set_index('Nº doc.faturamento')['Nome 1'].to_dict()

    # Itere por cada linha do df_razao para atualizar 'FORNECEDOR'
    for idx, row in df_razao.iterrows():
        num_doc = row['NUM_DOC_CONTAB']
        
        # Verifique em df_previa
        if num_doc in previa_fornecedor_dict:
            df_razao.at[idx, 'FORNECEDOR'] = previa_fornecedor_dict[num_doc]
            continue  # Pula para a próxima iteração
        
        # Verifique em df_previa_c
        if num_doc in previa_c_fornecedor_dict:
            df_razao.at[idx, 'FORNECEDOR'] = previa_c_fornecedor_dict[num_doc]
            continue  # Pula para a próxima iteração
        
        # Verifique em df_zfiscal
        if num_doc in zfiscal_fornecedor_dict:
            df_razao.at[idx, 'FORNECEDOR'] = zfiscal_fornecedor_dict[num_doc]

    
    df_razao['NAT_BC'] = None

    ### ['BC PIS/COFINS'] ###

    # Calculando 'BC PIS/COFINS' com base nas condições fornecidas
    df_razao['BC PIS/COFINS'] = np.where(
        df_razao['CONTA_RAZAO'] == 1105104001,  # Se a condição para '1105104001' for verdadeira
        df_razao['MONTANTE'] / 0.0165,            # Calcule usando esta fórmula
        np.where(
            df_razao['CONTA_RAZAO'] == 1105105001,  # Se a condição para '1105105001' for verdadeira
            df_razao['MONTANTE'] / 0.076,             # Calcule usando esta fórmula
            0  # Caso contrário (você pode definir um valor padrão ou deixar como está se não houver outro caso)
        )
    )

    ### ['Referencia2'] ###
    df_razao['Referencia2'] = df_razao['Referência'].str.split('-').str[0]

    ### ['DATA_DOC'] ###

    # Formatando a coluna 'Data documento' para o formato desejado 'dd/mm/yyyy'
    df_razao['DATA_DOC'] = df_razao['DATA_DOC'].dt.strftime('%d/%m/%Y')
    df_razao['DATA_DOC'] = df_razao['DATA_DOC'].astype(str)

    df_razao['DATA_DOC_AUX'] = df_razao['DATA_DOC'].apply(datetime_to_excel_date)


    ### ['INDEX'] RAZÃO ###

    ## Concatenando para criar o INDEX do Razão ##
    df_razao['INDEX'] = df_razao.apply(lambda x: str(x['CONTA']) + str(x['Referencia2']) + str(x['DATA_DOC_AUX']), axis=1)

    ### ['PA'] PERIODO APURACAO ###
    #Validando se 'DATA_DOC' e 'DATA_LCTO' estão no formato correto (datetime64)
    df_razao['DATA_DOC'] = pd.to_datetime(df_razao['DATA_DOC'], format='%d/%m/%Y')
    df_razao['DATA_LCTO'] = pd.to_datetime(df_razao['DATA_LCTO'], format='%d/%m/%Y')

    #Aplicando a função com o método apply para criar a coluna 'PA'
    print(df_razao.columns)
    df_razao['PA'] = df_razao.apply(preencher_pa, axis=1)


    ### Mudando a posição da coluna ['Referência'] ###
    # Obtém uma lista de todas as colunas
    colunas_razao = list(df_razao.columns)
    # Encontra o índice da coluna 'Referência'
    indice_referencia = colunas_razao.index('Referência')

    # Remove 'Referencia2' de sua posição atual e a insere após 'Referência'
    if 'Referencia2' in colunas_razao:
        colunas_razao.remove('Referencia2')
        colunas_razao.insert(indice_referencia + 1, 'Referencia2')

    # Reordena o DataFrame de acordo com a nova ordem de colunas_razao
    df_razao = df_razao[colunas_razao]

    ### Mudando Posição das colunas do Razão ###
    colunas_razao = ['INDEX', 'PA'] + [col for col in df_razao.columns if col not in ['INDEX', 'PA']]
    df_razao = df_razao[colunas_razao]

    bloco_zfiscal.to_excel('zfiscaloficiall.xlsx')
    bloco_a['NUM_DOC_CONTAB'] = bloco_a['NUM_DOC_CONTAB'].str.replace('.0', '')
    bloco_c['NUM_DOC_CONTAB'] = bloco_c['NUM_DOC_CONTAB'].str.replace('.0', '')
    
    return bloco_a,bloco_c,df_zfiscal_cru, df_razao

def gerar_excel(dados_dict, zfiscal_file, fbl3n_file, caminho_arquivo='saida_efd.xlsx'):

    bloco_a,bloco_c,bloco_zfiscal,bloco_fbl3n=gera_indice_fbl3n(dados_dict=dados_dict,path_zfiscal=zfiscal_file,fbl3n_file=fbl3n_file)

    

    bloco_a = bloco_a.drop_duplicates(subset='INDEX_ITEM',keep='first')
    with pd.ExcelWriter(caminho_arquivo, engine='xlsxwriter') as writer:

        bloco_a.to_excel(writer,sheet_name='A100 x A170',index=False)
        bloco_c.to_excel(writer,sheet_name='C100 x C170',index=False)
        bloco_zfiscal.to_excel(writer,sheet_name='ZFISCAL',index=False)
        bloco_fbl3n.to_excel(writer,sheet_name='FBL3N',index=False)

        for chave, registros in dados_dict.items():
            if isinstance(registros, list) and registros and isinstance(registros[0], dict):
                df = pd.DataFrame(registros)
                df.to_excel(writer, sheet_name=chave[:31], index=False)  # Limita a 31 caracteres para o nome da aba
            elif isinstance(registros, (str, int, float)):
                df = pd.DataFrame([{chave: registros}])
                df.to_excel(writer, sheet_name=chave[:31], index=False)

    print(f"Arquivo Excel gerado em: {caminho_arquivo}")

path_fbl3n =r'C:\Users\paulo.nascimento\Downloads\Nova pasta (19)\BASE_FBL3N 2.XLSX'
path_zfiscal = r'C:\Users\paulo.nascimento\Downloads\Nova pasta (19)\BASE_ZFISCAL 2 (1).XLSX'
data = processar_efd_contribuicoes(r'C:\Users\paulo.nascimento\Downloads\Nova pasta (19)\SPED_05.2025 1.txt')

print(data['registros_c170'])

#df = pd.DataFrame(data['registros_c170'])
#df.to_excel('sped.xlsx')
gerar_excel(data,zfiscal_file=path_zfiscal,fbl3n_file=path_fbl3n)
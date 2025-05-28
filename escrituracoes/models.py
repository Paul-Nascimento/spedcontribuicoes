from django.db import models

class Registro0000(models.Model):
    id = models.CharField(primary_key=True, max_length=32)  # Ex: CNPJ_COMPETENCIA

    cod_ver = models.CharField(max_length=3)  # Código da versão do leiaute
    tipo_escrit = models.CharField(max_length=1)  # 0 - Original, 1 - Retificadora
    ind_sit_esp = models.CharField(max_length=1, null=True, blank=True)  # Situação especial (0-4)
    num_rec_anterior = models.CharField(max_length=41, null=True, blank=True)  # Recibo da escrituração anterior

    dt_ini = models.DateField()  # Data inicial das informações
    dt_fin = models.DateField()  # Data final das informações
    nome = models.CharField(max_length=100)  # Nome empresarial
    cnpj = models.CharField(max_length=14)  # CNPJ da matriz
    uf = models.CharField(max_length=2)  # Unidade da Federação
    cod_mun = models.CharField(max_length=7)  # Código do município (IBGE)
    suframa = models.CharField(max_length=9, null=True, blank=True)  # Inscrição na SUFRAMA

    ind_nat_pj = models.CharField(max_length=2, null=True, blank=True)  # Natureza jurídica
    ind_ativ = models.CharField(max_length=1)  # Tipo de atividade preponderante
    

    class Meta:
        db_table = 'registro_0000'
        verbose_name = 'Abertura do Arquivo (0000)'
        verbose_name_plural = 'Aberturas do Arquivo (0000)'

    def __str__(self):
        return f'{self.id} - {self.nome}'

class Registro0200(models.Model):
    registro_0000 = models.ForeignKey(Registro0000, on_delete=models.CASCADE, related_name='registros_0200')

    cod_item = models.CharField(max_length=60)
    descr_item = models.TextField()
    cod_barra = models.CharField(max_length=80, null=True, blank=True)
    cod_ant_item = models.CharField(max_length=60, null=True, blank=True)
    unid_inv = models.CharField(max_length=6, null=True, blank=True)
    tipo_item = models.CharField(max_length=2)
    cod_ncm = models.CharField(max_length=8, null=True, blank=True)
    ex_ipi = models.CharField(max_length=3, null=True, blank=True)
    cod_gen = models.CharField(max_length=2, null=True, blank=True)
    cod_lst = models.CharField(max_length=5, null=True, blank=True)
    aliq_icms = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'registro_0200'
        verbose_name = 'Item de Estoque (0200)'
        verbose_name_plural = 'Itens de Estoque (0200)'

    def __str__(self):
        return f'{self.cod_item} - {self.descr_item}'
    
class Registro0150(models.Model):
    registro_0000 = models.ForeignKey(Registro0000, on_delete=models.CASCADE, related_name='registros_0150')
    
    cod_part = models.CharField(max_length=60)
    nome = models.CharField(max_length=100)
    cod_pais = models.CharField(max_length=5)
    cnpj = models.CharField(max_length=14, null=True, blank=True)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    ie = models.CharField(max_length=14, null=True, blank=True)
    cod_mun = models.CharField(max_length=7, null=True, blank=True)
    suframa = models.CharField(max_length=9, null=True, blank=True)
    end = models.CharField(max_length=60, null=True, blank=True)
    num = models.CharField(max_length=20, null=True, blank=True)
    compl = models.CharField(max_length=60, null=True, blank=True)
    bairro = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        db_table = 'registro_0150'
        verbose_name = 'Participante (0150)'
        verbose_name_plural = 'Participantes (0150)'

    def __str__(self):
        return f'{self.cod_part} - {self.nome}'

class RegistroA100(models.Model):

    registro_0000 = models.ForeignKey(
        Registro0000,
        on_delete=models.CASCADE,
        related_name='registros_a100'
    )

    ind_oper = models.CharField(max_length=1)  # 0: Serviço Contratado, 1: Prestado
    ind_emit = models.CharField(max_length=1)  # 0: Própria, 1: Terceiros
    cod_part = models.CharField(max_length=60)
    cod_sit = models.CharField(max_length=2)
    ser = models.CharField(max_length=20, null=True, blank=True)
    sub = models.CharField(max_length=20, null=True, blank=True)
    num_doc = models.CharField(max_length=60)
    chv_nfse = models.CharField(max_length=60, null=True, blank=True)
    dt_doc = models.DateField(null=True,blank=True)
    dt_exe_serv = models.DateField(null=True, blank=True)
    vl_doc = models.DecimalField(max_digits=15, decimal_places=2)
    ind_pgto = models.CharField(max_length=1)
    vl_desc = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_bc_pis = models.DecimalField(max_digits=15, decimal_places=2)
    vl_pis = models.DecimalField(max_digits=15, decimal_places=2)
    vl_bc_cofins = models.DecimalField(max_digits=15, decimal_places=2)
    vl_cofins = models.DecimalField(max_digits=15, decimal_places=2)
    vl_pis_ret = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_cofins_ret = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_iss = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    

    id_a100 = models.IntegerField()  # Campo adicional ao final
    cnpj_estab = models.CharField(max_length=14,default=None)

    class Meta:
        db_table = 'registro_a100'
        verbose_name = 'Documento Fiscal de Serviço (A100)'
        verbose_name_plural = 'Documentos Fiscais de Serviço (A100)'

    def __str__(self):
        return f'A100 - Doc {self.num_doc} ({self.dt_doc})'

class RegistroA170(models.Model):
    id_a100 = models.ForeignKey(
        RegistroA100,
        on_delete=models.CASCADE,
        related_name='registros_a170',
        db_column='id_a100'
    )


    num_item = models.IntegerField()
    cod_item = models.CharField(max_length=60)
    descr_compl = models.TextField(null=True, blank=True)
    vl_item = models.DecimalField(max_digits=15, decimal_places=2)
    vl_desc = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    nat_bc_cred = models.CharField(max_length=2, null=True, blank=True)
    ind_orig_cred = models.CharField(max_length=1, null=True, blank=True)
    cst_pis = models.CharField(max_length=2)
    vl_bc_pis = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    aliq_pis = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    vl_pis = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    cst_cofins = models.CharField(max_length=2)
    vl_bc_cofins = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    aliq_cofins = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    vl_cofins = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    cod_cta = models.CharField(max_length=255, null=True, blank=True)
    cod_ccus = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'registro_a170'
        verbose_name = 'Item do Documento Fiscal de Serviço (A170)'
        verbose_name_plural = 'Itens dos Documentos Fiscais de Serviço (A170)'

    def __str__(self):
        return f'A170 - Item {self.num_item} do A100 {self.id_a100_id}'

class RegistroC100(models.Model):
    

    registro_0000 = models.ForeignKey(
        Registro0000,
        on_delete=models.CASCADE,
        related_name='registros_c100'
    )

    ind_oper = models.CharField(max_length=1)  # 0: Entrada, 1: Saída
    ind_emit = models.CharField(max_length=1)  # 0: Própria, 1: Terceiros
    cod_part = models.CharField(max_length=60)
    cod_mod = models.CharField(max_length=2)
    cod_sit = models.CharField(max_length=2)
    ser = models.CharField(max_length=3, null=True, blank=True)
    num_doc = models.CharField(max_length=9)
    chv_nfe = models.CharField(max_length=44)  # Chave da NF-e como PK
    dt_doc = models.DateField(null=True,blank=True)
    dt_e_s = models.DateField(null=True, blank=True)
    vl_doc = models.DecimalField(max_digits=15, decimal_places=2)
    ind_pgto = models.CharField(max_length=1)
    vl_desc = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_abat_nt = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_merc = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    ind_frt = models.CharField(max_length=1)
    vl_frt = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_seg = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_out_da = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_bc_icms = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_icms = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_bc_icms_st = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_icms_st = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_ipi = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_pis = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_cofins = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_pis_st = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_cofins_st = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    id_c100 = models.IntegerField(default=0)
    cnpj_estab = models.CharField(max_length=14,default=None,null=True)

    class Meta:
        db_table = 'registro_c100'
        verbose_name = 'Documento Fiscal (C100)'
        verbose_name_plural = 'Documentos Fiscais (C100)'

    def __str__(self):
        return f'{self.cod_mod} {self.num_doc} - {self.dt_doc}'

class RegistroC170(models.Model):

    id_c100 = models.ForeignKey(
        RegistroC100,
        on_delete=models.CASCADE,
        related_name='registros_c170',
        db_column='id_c100'
    )

    num_item = models.IntegerField()
    cod_item = models.CharField(max_length=60)
    descr_compl = models.TextField(null=True, blank=True)
    qtd = models.DecimalField(max_digits=15, decimal_places=5, null=True, blank=True)
    unid = models.CharField(max_length=6, null=True, blank=True)
    vl_item = models.DecimalField(max_digits=15, decimal_places=2)
    vl_desc = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    ind_mov = models.CharField(max_length=1, null=True, blank=True)
    cst_icms = models.CharField(max_length=3, null=True, blank=True)
    cfop = models.CharField(max_length=4)
    cod_nat = models.CharField(max_length=10, null=True, blank=True)
    vl_bc_icms = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    aliq_icms = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    vl_icms = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_bc_icms_st = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    aliq_st = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    vl_icms_st = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    ind_apur = models.CharField(max_length=1, null=True, blank=True)
    cst_ipi = models.CharField(max_length=2, null=True, blank=True)
    cod_enq = models.CharField(max_length=3, null=True, blank=True)
    vl_bc_ipi = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    aliq_ipi = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    vl_ipi = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    cst_pis = models.CharField(max_length=2)
    vl_bc_pis = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    aliq_pis = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)
    quant_bc_pis = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)
    aliq_pis_quant = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True)
    vl_pis = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    cst_cofins = models.CharField(max_length=2)
    vl_bc_cofins = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    aliq_cofins = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)
    quant_bc_cofins = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)
    aliq_cofins_quant = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True)
    vl_cofins = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    cod_cta = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'registro_c170'
        verbose_name = 'Item do Documento Fiscal (C170)'
        verbose_name_plural = 'Itens dos Documentos Fiscais (C170)'

    def __str__(self):
        return f'{self.chv_nfe_id} - Item {self.num_item}'

class RegistroF100(models.Model):
    registro_0000 = models.ForeignKey(
        Registro0000,
        on_delete=models.CASCADE,
        related_name='registros_f100'
    )

    ind_oper = models.CharField(max_length=1)  # Indicador do tipo da operação
    cod_part = models.CharField(max_length=60, null=True, blank=True)  # Código do participante (0150)
    cod_item = models.CharField(max_length=60, null=True, blank=True)  # Código do item (0200)
    dt_oper = models.DateField(null=True,blank=True)  # Data da operação
    vl_oper = models.DecimalField(max_digits=15, decimal_places=2)  # Valor da operação
    cst_pis = models.CharField(max_length=2)  # CST do PIS
    vl_bc_pis = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True)  # BC do PIS
    aliq_pis = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)  # Alíquota do PIS
    vl_pis = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # Valor do PIS
    cst_cofins = models.CharField(max_length=2)  # CST da COFINS
    vl_bc_cofins = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True)  # BC da COFINS
    aliq_cofins = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)  # Alíquota da COFINS
    vl_cofins = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # Valor da COFINS
    nat_bc_cred = models.CharField(max_length=2, null=True, blank=True)  # Código da base de cálculo do crédito
    ind_orig_cred = models.CharField(max_length=1, null=True, blank=True)  # Origem do crédito
    cod_cta = models.CharField(max_length=255, null=True, blank=True)  # Conta contábil
    cod_ccus = models.CharField(max_length=255, null=True, blank=True)  # Centro de custos
    desc_doc_oper = models.TextField(null=True, blank=True)  # Descrição do documento/operação

    class Meta:
        db_table = 'registro_f100'
        verbose_name = 'Operação F100'
        verbose_name_plural = 'Operações F100'

    def __str__(self):
        return f'F100 - {self.dt_oper} / {self.vl_oper}'

class RegistroF130(models.Model):
    registro_0000 = models.ForeignKey(
        'Registro0000',
        on_delete=models.CASCADE,
        related_name='registros_f130'
    )

    nat_bc_cred = models.CharField(max_length=2)  # Código da base de cálculo do crédito
    ident_bem_imob = models.CharField(max_length=2)  # Identificação do bem incorporado ao ativo imobilizado
    ind_orig_cred = models.CharField(max_length=1, null=True, blank=True)  # Origem do bem (interna/externa)
    ind_util_bem_imob = models.CharField(max_length=1)  # Utilização dos bens
    mes_oper_aquis = models.CharField(max_length=6, null=True, blank=True)  # Mês/ano da aquisição
    vl_oper_aquis = models.DecimalField(max_digits=15, decimal_places=2)  # Valor de aquisição
    parc_oper_nao_bc_cred = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # Parcela excluída da base
    vl_bc_cred = models.DecimalField(max_digits=15, decimal_places=2)  # Base de cálculo do crédito
    ind_nr_parc = models.CharField(max_length=1)  # Indicador de número de parcelas
    cst_pis = models.CharField(max_length=2)  # CST PIS
    vl_bc_pis = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # Base mensal PIS
    aliq_pis = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)  # Alíquota PIS
    vl_pis = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # Valor PIS
    cst_cofins = models.CharField(max_length=2)  # CST COFINS
    vl_bc_cofins = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # Base mensal COFINS
    aliq_cofins = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)  # Alíquota COFINS
    vl_cofins = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # Valor COFINS
    cod_cta = models.CharField(max_length=255, null=True, blank=True)  # Conta contábil
    cod_ccus = models.CharField(max_length=255, null=True, blank=True)  # Centro de custos
    desc_bem_imob = models.TextField(null=True, blank=True)  # Descrição complementar do bem

    class Meta:
        db_table = 'registro_f130'
        verbose_name = 'Crédito Ativo Imobilizado (F130)'
        verbose_name_plural = 'Créditos Ativo Imobilizado (F130)'

    def __str__(self):
        return f'F130 - Bem {self.ident_bem_imob} - {self.vl_oper_aquis}'

class RegistroC500(models.Model):
    registro_0000 = models.ForeignKey(
        'Registro0000',
        on_delete=models.CASCADE,
        related_name='registros_c500'
    )

    cod_part = models.CharField(max_length=60)  # Código do participante (fornecedor)
    cod_mod = models.CharField(max_length=2)  # Modelo do documento fiscal
    cod_sit = models.CharField(max_length=2)  # Situação do documento
    ser = models.CharField(max_length=4, null=True, blank=True)  # Série
    sub = models.CharField(max_length=3, null=True, blank=True)  # Subsérie
    num_doc = models.CharField(max_length=9)  # Número do documento
    dt_doc = models.DateField()  # Data da emissão
    dt_ent = models.DateField(null=True, blank=True)  # Data da entrada
    vl_doc = models.DecimalField(max_digits=15, decimal_places=2)  # Valor total do documento
    vl_icms = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # Valor do ICMS
    cod_inf = models.CharField(max_length=6, null=True, blank=True)  # Código da informação complementar
    vl_pis = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # Valor do PIS
    vl_cofins = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # Valor da COFINS
    chv_doce = models.CharField(max_length=44, null=True, blank=True)  # Chave do documento eletrônico

    id_c500 = models.IntegerField(default=0)  # Identificador numérico para relacionamentos (ex: C501, C505)

    class Meta:
        db_table = 'registro_c500'
        verbose_name = 'Documento Fiscal (C500)'
        verbose_name_plural = 'Documentos Fiscais (C500)'

    def __str__(self):
        return f'C500 - {self.cod_mod} {self.num_doc}'

class RegistroC501(models.Model):
    id_c500 = models.ForeignKey(
        'RegistroC500',
        on_delete=models.CASCADE,
        related_name='registros_c501',
        db_column='id_c500'
    )

    cst_pis = models.CharField(max_length=2)  # Código da Situação Tributária referente ao PIS/PASEP
    vl_item = models.DecimalField(max_digits=15, decimal_places=2)  # Valor total dos itens
    nat_bc_cred = models.CharField(max_length=2, null=True, blank=True)  # Código da base de cálculo do crédito
    vl_bc_pis = models.DecimalField(max_digits=15, decimal_places=2)  # Valor da base de cálculo do PIS/PASEP
    aliq_pis = models.DecimalField(max_digits=8, decimal_places=4)  # Alíquota do PIS/PASEP
    vl_pis = models.DecimalField(max_digits=15, decimal_places=2)  # Valor do PIS/PASEP
    cod_cta = models.CharField(max_length=255, null=True, blank=True)  # Conta contábil

    class Meta:
        db_table = 'registro_c501'
        verbose_name = 'Detalhamento do Documento (C501)'
        verbose_name_plural = 'Detalhamentos do Documento (C501)'

    def __str__(self):
        return f'C501 - Item {self.vl_item} | PIS {self.vl_pis}'

class RegistroC505(models.Model):
    id_c500 = models.ForeignKey(
        'RegistroC500',
        on_delete=models.CASCADE,
        related_name='registros_c505',
        db_column='id_c500'
    )

    cst_cofins = models.CharField(max_length=2)  # Código da Situação Tributária referente à COFINS
    vl_item = models.DecimalField(max_digits=15, decimal_places=2)  # Valor total dos itens
    nat_bc_cred = models.CharField(max_length=2, null=True, blank=True)  # Código da base de cálculo do crédito
    vl_bc_cofins = models.DecimalField(max_digits=15, decimal_places=2)  # Base de cálculo da COFINS
    aliq_pis = models.DecimalField(max_digits=8, decimal_places=4)  # Alíquota da COFINS (nome mantido do layout)
    vl_pis = models.DecimalField(max_digits=15, decimal_places=2)  # Valor da COFINS (nome mantido do layout)
    cod_cta = models.CharField(max_length=255, null=True, blank=True)  # Conta contábil

    class Meta:
        db_table = 'registro_c505'
        verbose_name = 'Detalhamento COFINS (C505)'
        verbose_name_plural = 'Detalhamentos COFINS (C505)'

    def __str__(self):
        return f'C505 - Item {self.vl_item} | COFINS {self.vl_pis}'

class RegistroD500(models.Model):
    registro_0000 = models.ForeignKey(
        'Registro0000',
        on_delete=models.CASCADE,
        related_name='registros_d500'
    )

    ind_oper = models.CharField(max_length=1)  # Indicador do tipo de operação: 0 - aquisição
    ind_emit = models.CharField(max_length=1)  # Indicador do emitente do documento: 0 - própria, 1 - terceiros
    cod_part = models.CharField(max_length=60)  # Código do participante (0150)
    cod_mod = models.CharField(max_length=2)  # Código do modelo do documento fiscal
    cod_sit = models.CharField(max_length=2)  # Situação do documento fiscal
    ser = models.CharField(max_length=4, null=True, blank=True)  # Série
    sub = models.CharField(max_length=3, null=True, blank=True)  # Subsérie
    num_doc = models.CharField(max_length=9)  # Número do documento fiscal
    dt_doc = models.DateField()  # Data da emissão
    dt_a_p = models.DateField()  # Data da entrada/aquisição
    vl_doc = models.DecimalField(max_digits=15, decimal_places=2)  # Valor total do documento
    vl_desc = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # Valor do desconto
    vl_serv = models.DecimalField(max_digits=15, decimal_places=2)  # Valor da prestação de serviços
    vl_serv_nt = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # Serviços não tributados
    vl_terc = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # Valores cobrados em nome de terceiros
    vl_da = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # Outras despesas
    vl_bc_icms = models.DecimalField(max_digits=15, decimal_places=2)  # Base de cálculo do ICMS
    vl_icms = models.DecimalField(max_digits=15, decimal_places=2)  # Valor do ICMS
    cod_inf = models.CharField(max_length=6, null=True, blank=True)  # Código da informação complementar
    vl_pis = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # Valor do PIS
    vl_cofins = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # Valor da COFINS

    id_d500 = models.IntegerField(default=0)  # Campo auxiliar para relacionamentos com D501/D505

    class Meta:
        db_table = 'registro_d500'
        verbose_name = 'Documento Fiscal de Serviço (D500)'
        verbose_name_plural = 'Documentos Fiscais de Serviço (D500)'

    def __str__(self):
        return f'D500 - {self.cod_mod} {self.num_doc}'

class RegistroD501(models.Model):
    id_d500 = models.ForeignKey(
        'RegistroD500',
        on_delete=models.CASCADE,
        related_name='registros_d501',
        db_column='id_d500'
    )

    cst_pis = models.CharField(max_length=2)  # Código da Situação Tributária do PIS
    vl_item = models.DecimalField(max_digits=15, decimal_places=2)  # Valor total dos itens (serviços)
    nat_bc_cred = models.CharField(max_length=2, null=True, blank=True)  # Código da base de cálculo do crédito
    vl_bc_pis = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # Base de cálculo do PIS
    aliq_pis = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)  # Alíquota do PIS
    vl_pis = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # Valor do PIS
    cod_cta = models.CharField(max_length=255, null=True, blank=True)  # Conta contábil

    class Meta:
        db_table = 'registro_d501'
        verbose_name = 'Detalhamento do Serviço - PIS (D501)'
        verbose_name_plural = 'Detalhamentos do Serviço - PIS (D501)'

    def __str__(self):
        return f'D501 - Item {self.vl_item} | PIS {self.vl_pis}'

class RegistroD505(models.Model):
    id_d500 = models.ForeignKey(
        'RegistroD500',
        on_delete=models.CASCADE,
        related_name='registros_d505',
        db_column='id_d500'
    )

    cst_cofins = models.CharField(max_length=2)  # Código da Situação Tributária da COFINS
    vl_item = models.DecimalField(max_digits=15, decimal_places=2)  # Valor total dos itens (serviços)
    nat_bc_cred = models.CharField(max_length=2, null=True, blank=True)  # Código da base de cálculo do crédito
    vl_bc_cofins = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # Base de cálculo COFINS
    aliq_cofins = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)  # Alíquota COFINS
    vl_cofins = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # Valor COFINS
    cod_cta = models.CharField(max_length=255, null=True, blank=True)  # Conta contábil

    class Meta:
        db_table = 'registro_d505'
        verbose_name = 'Detalhamento do Serviço - COFINS (D505)'
        verbose_name_plural = 'Detalhamentos do Serviço - COFINS (D505)'

    def __str__(self):
        return f'D505 - Item {self.vl_item} | COFINS {self.vl_cofins}'

class RegistroD100(models.Model):

    registro_0000 = models.ForeignKey('Registro0000', on_delete=models.CASCADE, related_name='registros_d100')

    ind_oper = models.CharField(max_length=1)
    ind_emit = models.CharField(max_length=1)
    cod_part = models.CharField(max_length=60)
    cod_mod = models.CharField(max_length=2)
    cod_sit = models.CharField(max_length=2)
    ser = models.CharField(max_length=4, null=True, blank=True)
    sub = models.CharField(max_length=3, null=True, blank=True)
    num_doc = models.CharField(max_length=9)
    chv_cte = models.CharField(max_length=44, null=True, blank=True)
    dt_doc = models.DateField()
    dt_a_p = models.DateField(null=True, blank=True)
    tp_cte = models.CharField(max_length=1, null=True, blank=True)
    chv_cte_ref = models.CharField(max_length=44, null=True, blank=True)
    vl_doc = models.DecimalField(max_digits=15, decimal_places=2)
    vl_desc = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    ind_frt = models.CharField(max_length=1)
    vl_serv = models.DecimalField(max_digits=15, decimal_places=2)
    vl_bc_icms = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_icms = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_nt = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    cod_inf = models.CharField(max_length=6, null=True, blank=True)
    cod_cta = models.CharField(max_length=255, null=True, blank=True)

    id_d100 = models.IntegerField(default=0)  # Campo auxiliar para relacionamentos com D501/D505

    class Meta:
        db_table = 'registro_d100'
        verbose_name = 'Conhecimento de Transporte (D100)'
        verbose_name_plural = 'Conhecimentos de Transporte (D100)'

class RegistroD101(models.Model):
    registro_d100 = models.ForeignKey('RegistroD100', on_delete=models.CASCADE, related_name='registros_d101')

    ind_nat_frt = models.CharField(max_length=1)
    vl_item = models.DecimalField(max_digits=15, decimal_places=2)
    cst_pis = models.CharField(max_length=2)
    nat_bc_cred = models.CharField(max_length=2, null=True, blank=True)
    vl_bc_pis = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    aliq_pis = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)
    vl_pis = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    cod_cta = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'registro_d101'
        verbose_name = 'Detalhamento do Frete - PIS (D101)'
        verbose_name_plural = 'Detalhamentos do Frete - PIS (D101)'

class RegistroD105(models.Model):
    registro_d100 = models.ForeignKey('RegistroD100', on_delete=models.CASCADE, related_name='registros_d105')

    ind_nat_frt = models.CharField(max_length=1)
    vl_item = models.DecimalField(max_digits=15, decimal_places=2)
    cst_cofins = models.CharField(max_length=2)
    nat_bc_cred = models.CharField(max_length=2, null=True, blank=True)
    vl_bc_cofins = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    aliq_cofins = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)
    vl_cofins = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    cod_cta = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'registro_d105'
        verbose_name = 'Detalhamento do Frete - COFINS (D105)'
        verbose_name_plural = 'Detalhamentos do Frete - COFINS (D105)'

class RegistroM100(models.Model):
    registro_0000 = models.ForeignKey('Registro0000', on_delete=models.CASCADE, related_name='registros_m100')

    cod_cred = models.CharField(max_length=3)
    ind_cred_ori = models.CharField(max_length=1)
    vl_bc_pis = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    aliq_pis = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)
    quant_bc_pis = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)
    aliq_pis_quant = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True)
    vl_cred = models.DecimalField(max_digits=15, decimal_places=2)
    vl_ajus_acres = models.DecimalField(max_digits=15, decimal_places=2)
    vl_ajus_reduc = models.DecimalField(max_digits=15, decimal_places=2)
    vl_cred_dif = models.DecimalField(max_digits=15, decimal_places=2)
    vl_cred_disp = models.DecimalField(max_digits=15, decimal_places=2)
    ind_desc_cred = models.CharField(max_length=1)
    vl_cred_desc = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    sld_cred = models.DecimalField(max_digits=15, decimal_places=2)
    

    class Meta:
        db_table = 'registro_m100'
        verbose_name = 'Crédito Apurado PIS (M100)'
        verbose_name_plural = 'Créditos Apurados PIS (M100)'

class RegistroM105(models.Model):
    registro_0000 = models.ForeignKey('Registro0000', on_delete=models.CASCADE, related_name='registros_m105')

    nat_bc_cred = models.CharField(max_length=2)
    cst_pis = models.CharField(max_length=2)
    vl_bc_pis_tot = models.DecimalField(max_digits=15, decimal_places=2)
    vl_bc_pis_cum = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_bc_pis_nc = models.DecimalField(max_digits=15, decimal_places=2)
    vl_bc_pis = models.DecimalField(max_digits=15, decimal_places=2)
    quant_bc_pis_tot = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)
    quant_bc_pis = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)
    desc_cred = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'registro_m105'
        verbose_name = 'Detalhamento Crédito PIS (M105)'
        verbose_name_plural = 'Detalhamentos Crédito PIS (M105)'

class RegistroM500(models.Model):
    registro_0000 = models.ForeignKey('Registro0000', on_delete=models.CASCADE, related_name='registros_m500')

    cod_cred = models.CharField(max_length=3)
    ind_cred_ori = models.CharField(max_length=1)
    vl_bc_cofins = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    aliq_cofins = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)
    quant_bc_cofins = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)
    aliq_cofins_quant = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True)
    vl_cred = models.DecimalField(max_digits=15, decimal_places=2)
    vl_ajus_acres = models.DecimalField(max_digits=15, decimal_places=2)
    vl_ajus_reduc = models.DecimalField(max_digits=15, decimal_places=2)
    vl_cred_difer = models.DecimalField(max_digits=15, decimal_places=2)
    vl_cred_disp = models.DecimalField(max_digits=15, decimal_places=2)
    ind_desc_cred = models.CharField(max_length=1)
    vl_cred_desc = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    sld_cred = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        db_table = 'registro_m500'
        verbose_name = 'Crédito Apurado COFINS (M500)'
        verbose_name_plural = 'Créditos Apurados COFINS (M500)'

class RegistroM505(models.Model):
    
    registro_0000 = models.ForeignKey('Registro0000', on_delete=models.CASCADE, related_name='registros_m505')

    nat_bc_cred = models.CharField(max_length=2)
    cst_cofins = models.CharField(max_length=2)
    vl_bc_cofins_tot = models.DecimalField(max_digits=15, decimal_places=2)
    vl_bc_cofins_cum = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_bc_cofins_nc = models.DecimalField(max_digits=15, decimal_places=2)
    vl_bc_cofins = models.DecimalField(max_digits=15, decimal_places=2)
    quant_bc_cofins_tot = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)
    quant_bc_cofins = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)
    desc_cred = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'registro_m505'
        verbose_name = 'Detalhamento Crédito COFINS (M505)'
        verbose_name_plural = 'Detalhamentos Crédito COFINS (M505)'

class RegistroM200(models.Model):
    registro_0000 = models.ForeignKey('Registro0000', on_delete=models.CASCADE, related_name='registros_m200')

    vl_tot_cont_nc_per = models.DecimalField(max_digits=15, decimal_places=2)
    vl_tot_cred_desc = models.DecimalField(max_digits=15, decimal_places=2)
    vl_tot_cred_desc_ant = models.DecimalField(max_digits=15, decimal_places=2)
    vl_tot_cont_nc_dev = models.DecimalField(max_digits=15, decimal_places=2)
    vl_ret_nc = models.DecimalField(max_digits=15, decimal_places=2)
    vl_out_ded_nc = models.DecimalField(max_digits=15, decimal_places=2)
    vl_cont_nc_rec = models.DecimalField(max_digits=15, decimal_places=2)
    vl_tot_cont_cum_per = models.DecimalField(max_digits=15, decimal_places=2)
    vl_ret_cum = models.DecimalField(max_digits=15, decimal_places=2)
    vl_out_ded_cum = models.DecimalField(max_digits=15, decimal_places=2)
    vl_cont_cum_rec = models.DecimalField(max_digits=15, decimal_places=2)
    vl_tot_cont_rec = models.DecimalField(max_digits=15, decimal_places=2)

class RegistroM205(models.Model):
    registro_0000 = models.ForeignKey('Registro0000', on_delete=models.CASCADE, related_name='registros_m205')

    num_campo = models.CharField(max_length=2)
    cod_rec = models.CharField(max_length=6)
    vl_debito = models.DecimalField(max_digits=15, decimal_places=2)

class RegistroM210(models.Model):
    registro_0000 = models.ForeignKey('Registro0000', on_delete=models.CASCADE, related_name='registros_m210')

    cod_cont = models.CharField(max_length=2)
    vl_rec_brt = models.DecimalField(max_digits=15, decimal_places=2)
    vl_bc_cont = models.DecimalField(max_digits=15, decimal_places=2)
    aliq_pis = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)
    quant_bc_pis = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)
    aliq_pis_quant = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True)
    vl_cont_apur = models.DecimalField(max_digits=15, decimal_places=2)
    vl_ajus_acres = models.DecimalField(max_digits=15, decimal_places=2)
    vl_ajus_reduc = models.DecimalField(max_digits=15, decimal_places=2)
    vl_cont_difer = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_cont_difer_ant = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_cont_per = models.DecimalField(max_digits=15, decimal_places=2)

class RegistroM220(models.Model):
    registro_0000 = models.ForeignKey('Registro0000', on_delete=models.CASCADE, related_name='registros_m220')

    ind_aj = models.CharField(max_length=1)
    vl_aj = models.DecimalField(max_digits=15, decimal_places=2)
    cod_aj = models.CharField(max_length=2)
    num_doc = models.CharField(max_length=100, null=True, blank=True)
    descr_aj = models.TextField(null=True, blank=True)
    dt_ref = models.DateField(null=True, blank=True)

class RegistroM225(models.Model):
    registro_0000 = models.ForeignKey('Registro0000', on_delete=models.CASCADE, related_name='registros_m225')

    det_valor_aj = models.DecimalField(max_digits=15, decimal_places=2)
    cst_pis = models.CharField(max_length=2, null=True, blank=True)
    det_bc_cred = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)
    det_aliq = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)
    dt_oper_aj = models.DateField()
    desc_aj = models.TextField(null=True, blank=True)
    cod_cta = models.CharField(max_length=255, null=True, blank=True)
    info_compl = models.TextField(null=True, blank=True)

class RegistroM600(models.Model):
    registro_0000 = models.ForeignKey('Registro0000', on_delete=models.CASCADE, related_name='registros_m600')

    vl_tot_cont_nc_per = models.DecimalField(max_digits=15, decimal_places=2)
    vl_tot_cred_desc = models.DecimalField(max_digits=15, decimal_places=2)
    vl_tot_cred_desc_ant = models.DecimalField(max_digits=15, decimal_places=2)
    vl_tot_cont_nc_dev = models.DecimalField(max_digits=15, decimal_places=2)
    vl_ret_nc = models.DecimalField(max_digits=15, decimal_places=2)
    vl_out_ded_nc = models.DecimalField(max_digits=15, decimal_places=2)
    vl_cont_nc_rec = models.DecimalField(max_digits=15, decimal_places=2)
    vl_tot_cont_cum_per = models.DecimalField(max_digits=15, decimal_places=2)
    vl_ret_cum = models.DecimalField(max_digits=15, decimal_places=2)
    vl_out_ded_cum = models.DecimalField(max_digits=15, decimal_places=2)
    vl_cont_cum_rec = models.DecimalField(max_digits=15, decimal_places=2)
    vl_tot_cont_rec = models.DecimalField(max_digits=15, decimal_places=2)

class RegistroM605(models.Model):
    registro_0000 = models.ForeignKey('Registro0000', on_delete=models.CASCADE, related_name='registros_m605')

    num_campo = models.CharField(max_length=2)
    cod_rec = models.CharField(max_length=6)
    vl_debito = models.DecimalField(max_digits=15, decimal_places=2)

class RegistroM610(models.Model):
    registro_0000 = models.ForeignKey('Registro0000', on_delete=models.CASCADE, related_name='registros_m610')

    cod_cont = models.CharField(max_length=2)
    vl_rec_brt = models.DecimalField(max_digits=15, decimal_places=2)
    vl_bc_cont = models.DecimalField(max_digits=15, decimal_places=2)
    aliq_cofins = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)
    quant_bc_cofins = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)
    aliq_cofins_quant = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True)
    vl_cont_apur = models.DecimalField(max_digits=15, decimal_places=2)
    vl_ajus_acres = models.DecimalField(max_digits=15, decimal_places=2)
    vl_ajus_reduc = models.DecimalField(max_digits=15, decimal_places=2)
    vl_cont_difer = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_cont_difer_ant = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vl_cont_per = models.DecimalField(max_digits=15, decimal_places=2)

class RegistroM620(models.Model):
    registro_0000 = models.ForeignKey('Registro0000', on_delete=models.CASCADE, related_name='registros_m620')

    ind_aj = models.CharField(max_length=1)
    vl_aj = models.DecimalField(max_digits=15, decimal_places=2)
    cod_aj = models.CharField(max_length=2)
    num_doc = models.CharField(max_length=100, null=True, blank=True)
    descr_aj = models.TextField(null=True, blank=True)
    dt_ref = models.DateField(null=True, blank=True)

class RegistroM625(models.Model):
    registro_0000 = models.ForeignKey('Registro0000', on_delete=models.CASCADE, related_name='registros_m625')

    det_valor_aj = models.DecimalField(max_digits=15, decimal_places=2)
    cst_cofins = models.CharField(max_length=2, null=True, blank=True)
    det_bc_cred = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)
    det_aliq = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)
    dt_oper_aj = models.DateField()
    desc_aj = models.TextField(null=True, blank=True)
    cod_cta = models.CharField(max_length=255, null=True, blank=True)
    info_compl = models.TextField(null=True, blank=True)

class ZFiscal(models.Model):
    numero_doc_faturamento = models.CharField(max_length=50, null=True, blank=True)
    documento_compras = models.CharField(max_length=50, null=True, blank=True)
    numero_documento = models.CharField(max_length=50, null=True, blank=True)
    categoria_nf = models.CharField(max_length=50, null=True, blank=True)
    tipo_documento = models.CharField(max_length=50, null=True, blank=True)
    direcao_movimento = models.CharField(max_length=50, null=True, blank=True)
    data_documento = models.DateField(null=True, blank=True)
    data_lancamento = models.DateField(null=True, blank=True)
    modelo_nf = models.CharField(max_length=10, null=True, blank=True)
    serie = models.CharField(max_length=10, null=True, blank=True)
    numero_nf = models.CharField(max_length=50, null=True, blank=True)
    nf_eletronica = models.CharField(max_length=50, null=True, blank=True)
    local_negocios = models.CharField(max_length=100, null=True, blank=True)
    estornado = models.BooleanField(default=False)
    data_estorno = models.DateField(null=True, blank=True)
    status_documento = models.CharField(max_length=50, null=True, blank=True)

    # Parceiro
    id_parceiro = models.CharField(max_length=50, null=True, blank=True)
    nome_parceiro = models.CharField(max_length=255, null=True, blank=True)
    regiao = models.CharField(max_length=50, null=True, blank=True)
    cgc = models.CharField(max_length=200, null=True, blank=True)
    cpf = models.CharField(max_length=20, null=True, blank=True)
    id_fiscal_regional = models.CharField(max_length=50, null=True, blank=True)

    # Itens
    moeda = models.CharField(max_length=10, null=True, blank=True)
    numero_item = models.IntegerField(null=True, blank=True)
    material = models.CharField(max_length=50, null=True, blank=True)
    grupo_mercadorias = models.CharField(max_length=50, null=True, blank=True)
    descricao_material = models.TextField(null=True, blank=True)
    cfop = models.CharField(max_length=10, null=True, blank=True)
    origem_material = models.CharField(max_length=10, null=True, blank=True)
    sit_tributaria_icms = models.CharField(max_length=10, null=True, blank=True)
    quantidade = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)
    unidade_medida = models.CharField(max_length=10, null=True, blank=True)

    # Impostos
    centro = models.CharField(max_length=20, null=True, blank=True)
    codigo_imposto = models.CharField(max_length=20, null=True, blank=True)
    lei_cofins = models.CharField(max_length=50, null=True, blank=True)
    lei_pis = models.CharField(max_length=50, null=True, blank=True)
    tipo_imposto = models.CharField(max_length=20, null=True, blank=True)
    montante_basico = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    valor_fiscal = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    montante_base_excluido = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    outro_montante_basico = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    # Informações complementares
    empresa = models.CharField(max_length=10, null=True, blank=True)
    exercicio = models.CharField(max_length=10, null=True, blank=True)
    codigo_transacao = models.CharField(max_length=50, null=True, blank=True)
    usuario = models.CharField(max_length=50, null=True, blank=True)
    referencia = models.CharField(max_length=50, null=True, blank=True)
    contrato_basico = models.CharField(max_length=50, null=True, blank=True)
    centro_custo = models.CharField(max_length=50, null=True, blank=True)
    imobilizado = models.CharField(max_length=50, null=True, blank=True)
    sub_numero = models.CharField(max_length=50, null=True, blank=True)
    ordem = models.CharField(max_length=50, null=True, blank=True)
    pep_elemento = models.CharField(max_length=50, null=True, blank=True)
    diagrama_rede = models.CharField(max_length=50, null=True, blank=True)
    operacao_rede = models.CharField(max_length=50, null=True, blank=True)
    ficha_orcamentaria = models.CharField(max_length=50, null=True, blank=True)
    conta_razao = models.CharField(max_length=50, null=True, blank=True)
    tipo_doc_compras = models.CharField(max_length=50, null=True, blank=True)

    # Textos descritivos
    texto_parte1 = models.TextField(null=True, blank=True)
    texto_parte2 = models.TextField(null=True, blank=True)
    texto_parte3 = models.TextField(null=True, blank=True)
    texto_parte4 = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'zfiscal'

class FBL3N(models.Model):
    atribuicao = models.CharField(max_length=50, null=True, blank=True)
    empresa = models.CharField(max_length=10, null=True, blank=True)
    conta_razao = models.CharField(max_length=50, null=True, blank=True)
    numero_documento = models.CharField(max_length=50, null=True, blank=True)
    divisao = models.CharField(max_length=10, null=True, blank=True)
    tipo_documento = models.CharField(max_length=50, null=True, blank=True)
    referencia = models.CharField(max_length=50, null=True, blank=True)
    data_lancamento = models.DateField(null=True, blank=True)
    data_documento = models.DateField(null=True, blank=True)
    chave_lancamento = models.CharField(max_length=50, null=True, blank=True)
    montante_moeda_interna = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    moeda_interna = models.CharField(max_length=10, null=True, blank=True)
    doc_compensacao = models.CharField(max_length=50, null=True, blank=True)
    texto = models.TextField(null=True, blank=True)
    centro_custo = models.CharField(max_length=50, null=True, blank=True)
    nome_usuario = models.CharField(max_length=50, null=True, blank=True)
    elemento_pep = models.CharField(max_length=50, null=True, blank=True)
    periodo_contabil = models.CharField(max_length=10, null=True, blank=True)
    pedido = models.CharField(max_length=50, null=True, blank=True)
    contrato = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = "fbl3n"

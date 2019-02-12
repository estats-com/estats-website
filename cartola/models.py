from django.db import models
from django.conf import settings
import os
import datetime
from operator import itemgetter

def get_defaultPic():
    return os.path.join(settings.BASE_DIR, '/media/logoEstats.png')

class Jogador(models.Model):

    POSICOES = (
    (1,'GOL'),
    (2,'LAT'),
    (3,'ZAG'),
    (4,'MEI'),
    (5,'ATA'),
    (6,'TEC')
    )

    id = models.IntegerField(primary_key = True)
    nome = models.CharField(max_length = 50)
    posicao = models.IntegerField(choices = POSICOES)
    foto = models.ImageField(default = get_defaultPic(), upload_to = os.path.join(settings.BASE_DIR, '/media/jogadores/'))

    class Meta:
        ordering = ['nome', 'posicao', 'id']
        verbose_name = 'jogador'
        verbose_name_plural = 'jogadores'

    def __str__(self):
        return "%s (%s)"%(self.nome, self.get_posicao_display())

    def get_absolute_url(self):
        return "/jog%s/"%self.id

    def get_clubeByData(self, dia):
        if not isinstance(dia, datetime.date):
            raise ValueError(u'Valor deve ser do tipo datetime.date')
        return da.contrato_set.get(data_fim__gt = dia)

class Estadio(models.Model):
    ESTADOS = (('RS', 'Rio Grande do Sul'),
               ('PR', 'Paraná'),
               ('SC', 'Santa Catarina'),
               ('SP', 'São Paulo'),
               ('RJ', 'Rio de Janeiro'),
               ('MG', 'Minas Gerais'),
               ('ES', 'Espírito Santo'),
               ('MS', 'Mato Grosso do Sul'),
               ('MT', 'Mato Grosso'),
               ('GO', 'Goiás'),
               ('TO', 'Tocantins'),
               ('RO', 'Rondônia'),
               ('AC', 'Acre'),
               ('AM', 'Amazonas'),
               ('RR', 'Roraima'),
               ('AM', 'Amapá'),
               ('PA', 'Pará'),
               ('MA', 'Maranhão'),
               ('PI', 'Piauí'),
               ('CE', 'Ceará'),
               ('RN', 'Rio Grande do Norte'),
               ('PB', 'Paraiba'),
               ('PE', 'Pernambuco'),
               ('AL', 'Alagoas'),
               ('SE', 'Sergipe'),
               ('BA', 'Bahia'),
              )
    ESTADOS = sorted(list(ESTADOS), key = itemgetter(1))
    nome = models.CharField(max_length = 50)
    longitude = models.FloatField(blank = True, null= True)
    latitude = models.FloatField(blank = True, null = True)
    cidade = models.CharField(max_length = 50, blank = True)
    uf = models.CharField(max_length = 2, blank = True, choices = ESTADOS)

    def __str__(self):
        return "{} ({})".format(self.nome, self.uf)

class Clube(models.Model):
    id = models.IntegerField(primary_key = True)
    nome = models.CharField(max_length = 30)
    nomeCBF = models.CharField(max_length = 30, blank = True)
    nomeELO = models.CharField(max_length = 30, blank = True)
    plantel = models.ManyToManyField(Jogador, through = "Contrato")
    estadio = models.ForeignKey(Estadio, blank = True, null = True, related_name = 'clubes', on_delete = models.CASCADE)
    escudoP = models.ImageField(default = get_defaultPic(), upload_to = os.path.join(settings.BASE_DIR, 'media/clubes/P/'))
    escudoM = models.ImageField(default = get_defaultPic(), upload_to = os.path.join(settings.BASE_DIR, 'media/clubes/M/'))
    escudoG = models.ImageField(default = get_defaultPic(), upload_to = os.path.join(settings.BASE_DIR, 'media/clubes/G/'))

    class Meta:
        ordering = ['nome','id']

    def __str__(self):
        return "%s"%(self.nome)

    def get_absolute_url(self):
        return "/clube%s/"%self.id

class Contrato(models.Model):
    jogador = models.ForeignKey(Jogador, on_delete = models.CASCADE)
    clube = models.ForeignKey(Clube, on_delete = models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField(default = datetime.datetime(9999,12,31))

    def em_vigor(self):
        return self.data_fim > datetime.datetime.now().date()


class Partida(models.Model):
    ano = models.IntegerField()
    rodada = models.IntegerField()
    mandante = models.ForeignKey(Clube, related_name = 'mandante', on_delete = models.CASCADE)
    visitante = models.ForeignKey(Clube, related_name = 'visitante', on_delete = models.CASCADE)
    gol_mandante = models.IntegerField(blank = True, null = True)
    gol_visitante = models.IntegerField(blank = True, null = True)
    resultado = models.CharField(max_length = 1, blank = True)
    data = models.DateTimeField()
    validaCartola = models.BooleanField()
    estadio = models.ForeignKey(Estadio, related_name = 'partidas', on_delete = models.CASCADE)

    def save(self, *args, **kwds):
        if self.gol_mandante and self.gol_visitante:
            if self.gol_mandante > self.gol_visitante:
                self.resultado = 'M'
            elif self.gol_mandante < self.gol_visitante:
                self.resultado = 'V'
            else:
                self.resultado = 'E'
        super(Partida, self).save(*args, **kwds)

    def __str__(self):
        return "{} - {}/{} {} {} x {} {}".format(self.id,
                                                 self.ano,
                                                 self.rodada,
                                                 self.mandante,
                                                 self.gol_mandante,
                                                 self.gol_visitante,
                                                 self.visitante)


class Scouts(models.Model):
    STATUS = ((1,'NA'),
              (2,'Dúvida'),
              (3,'Suspenso'),
              (4,'NA'),
              (5,'Lesionado'),
              (6,'Sem informação'),
              (7,'Provável'),
    )
    jogador = models.ForeignKey(Jogador, related_name = 'scouts', on_delete=models.CASCADE)
    partida = models.ForeignKey(Partida, related_name ='scouts', on_delete=models.CASCADE)
    para = models.CharField(max_length = 10, default = 'mandante')
    #getClubeByData -> usar classe Membership para buscar qual clube na data da partida estava o jogador
    #local - MAN ou VIS dependendo da partida e qual clue membership na data
    preco = models.FloatField()
    variacao = models.FloatField()
    pontos = models.FloatField()
    status = models.IntegerField(default = 6, choices = STATUS)
    rb = models.IntegerField(default = 0)
    fc = models.IntegerField(default = 0)
    fs = models.IntegerField(default = 0)
    gc = models.IntegerField(default = 0)
    ca = models.IntegerField(default = 0)
    cv = models.IntegerField(default = 0)
    sg = models.IntegerField(default = 0)
    dd = models.IntegerField(default = 0)
    dp = models.IntegerField(default = 0)
    gs = models.IntegerField(default = 0)
    pe = models.IntegerField(default = 0)
    a = models.IntegerField(default = 0)
    g = models.IntegerField(default = 0)
    i = models.IntegerField(default = 0)
    pp = models.IntegerField(default = 0)
    ft = models.IntegerField(default = 0)
    fd = models.IntegerField(default = 0)
    ff = models.IntegerField(default = 0)

    def save(self, *args, **kwds):
        clu = self.jogador.get_clubeByData(self.partida.data)
        if clu == self.partida.mandante:
            self.para = 'mandante'
        else:
            self.para = 'visitante'
        super(Scouts, self).save(*args, **kwds)

    def __str__(self):
        return "%s %s/%s"%(self.jogador.nome, self.partida.ano, self.partida.rodada)

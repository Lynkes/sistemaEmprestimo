from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from utils.gerador_hash import gerar_hash
    
class Emprestimo(models.Model): 
    locador = models.ForeignKey('usuario.Usuario', verbose_name= 'Locador', on_delete=models.PROTECT)
    objeto = models.ManyToManyField('objeto.Objeto', verbose_name= 'Objeto(s) emprestado(s)')
    dataEmprestimo = models.DateTimeField(_('Data do empréstimo '), max_length=10, help_text='Use dd/mm/aaaa')
    devolvido = models.BooleanField(_('Já foi devolvido? '), default='Não')

    slug = models.SlugField('Hash',max_length= 200, null=True, blank=True)
    
    objects = models.Manager()
    
    class Meta:
        ordering            =   ['locador']
        verbose_name        =   ('emprestimo')
        verbose_name_plural =   ('emprestimos')
        unique_together     =   [['locador','dataEmprestimo']]

    def __str__(self):
        return "Objeto: %s. Pessoa: %s." % (self.objeto, self.locador)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_hash()
        super(Emprestimo, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('emprestimo_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('emprestimo_delete', args=[str(self.id)]) 
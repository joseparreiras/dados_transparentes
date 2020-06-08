# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest


class BaixarCasosSpider(scrapy.Spider):
    name = 'baixar_casos'
    allowed_domains = ['dadostransparentes.com.br']
    start_urls = ['http://www.dadostransparentes.com.br/graficos_regiao/painel.php']

    def parse(self, response):
        uf_list = ['11','12','13','14','15','16','17','21','22','23','24','25','26','27','28','29',
        '31','32','33','35','41','42','43','50','51','52','53']
        for uf in uf_list:
            yield FormRequest('http://www.dadostransparentes.com.br/graficos_regiao/painel.php',
                  formdata={'uf_origem':uf},
                  callback=self.parse_uf)

    def parse_uf(self, response):
        regioes = response.xpath("//iframe/@src").extract()
        url_regioes = ['http://www.dadostransparentes.com.br/graficos_regiao/'+x for x in regioes]
        for url in url_regioes:
            yield scrapy.Request(url = url, callback = self.parse_regiao)

    def parse_regiao(self, response):
        script = response.xpath("//script").extract()[-1]
        name = script.split('text:')[-1].split('"')[1]
        data = script.split('data')[1].split('[')[1].split(']')[0].replace(' ','').split(',')
        time = script.split('categories')[1].split('[')[1].split(']')[0].replace('\r','').replace('\n','').replace(' ','').replace("'",'').split(',')
        dic = {"Nome":name,
                "Data": time,
                "Casos": data}    
        yield dic

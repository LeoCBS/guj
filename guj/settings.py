# -*- coding: utf-8 -*-

# Scrapy settings for guj project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'guj'

SPIDER_MODULES = ['guj.spiders']
NEWSPIDER_MODULE = 'guj.spiders'
#nao sobre carregar o site
DOWNLOAD_DELAY = 5
# evitar looping de recursividade
REDIRECT_MAX_TIMES = 5
#para evitar acesso remoto
TELNETCONSOLE_ENABLED = False

ITEM_PIPELINES = {
    'guj.pipelines.GujPipeline': 300,
    'guj.pipelines.JsonWithEncodingPipeline': 800
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'guj (+http://www.yourdomain.com)'

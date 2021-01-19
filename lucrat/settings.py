BOT_NAME = 'lucrat'
LOG_LEVEL = 'WARNING'
SPIDER_MODULES = ['lucrat.spiders']
NEWSPIDER_MODULE = 'lucrat.spiders'
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
    'lucrat.pipelines.DatabasePipeline': 300,
}
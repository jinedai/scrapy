BOT_NAME = 'Logo'

SPIDER_MODULES = ['Logo.spiders']
NEWSPIDER_MODULE = 'Logo.spiders'

ITEM_PIPELINES={
    # 'sucai.pipelines.SucaiPipeline':1
    'Logo.pipelines.JsonWithEncodingPipeline':2,
    'Logo.pipelines.DownloadImagesPipeline':1
}
IMAGES_STORE='F:\Logo\picture'

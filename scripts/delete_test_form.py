def run():
    from api.models import Item, NumericItem, TextItem, DataFormTemplate
    
    models = [Item, NumericItem, TextItem, DataFormTemplate]
    
    for model in models:
        model.objects.all().delete()
    
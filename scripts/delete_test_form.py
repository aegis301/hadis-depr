def run():
    from api.models import Item, NumericItem, TextItem, DataForm
    
    models = [Item, NumericItem, TextItem, DataForm]
    
    for model in models:
        model.objects.all().delete()
    
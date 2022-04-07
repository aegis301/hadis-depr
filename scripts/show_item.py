def run():
    from api.models import Item, NumericItem, TextItem, DataForm
    
    items = Item.objects.all().select_subclasses()
    for item in items:
        print(item.description)
        print(item.value)
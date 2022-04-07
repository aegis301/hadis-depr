def run():
    from api.models import Item, NumericItem, TextItem, DataForm
    
    f1 = DataForm(title="Test", description="This is a test form")
    
    i1 = NumericItem(name="TestNum", description="Test Num Item", type=Item.NUMERIC, value=0.5)
    
    i2 = TextItem(name="TestText", description="Test Num Item", type=Item.TEXT, value="Hello World")
    
    f1.save()
    
    i1.save()
    
    i2.save()
    
    f1.items.add(i1)
    f1.items.add(i2)
    
    print(f"Current forms: {DataForm.objects.all().title}")
    # print(f"Current forms: {Item.objects.all().name}")
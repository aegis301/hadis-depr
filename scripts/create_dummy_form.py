from turtle import numinput, title
from dataforms.models import Item, NumericItem, TextItem, BooleanItem, DataFormTemplate
from django.contrib.auth.models import User

def create_echo(user):
    echo = DataFormTemplate(
        title="Echocardiography", 
        description="Standard form for results of echocardiography in our outpatients clinic.",
        created_by= user
        )
    visual_sys_func = TextItem(
        name = "Visual Systolic Function",
        description = "Visual assesment of systolic function of the left ventricular"
    )
    lv_func = NumericItem(
        name = "LV Function",
        description = "LV Function in percent ejection fraction"
    )
    aortic_stenosis = BooleanItem(
        name = "Aortic Stenosis",
        description = "Is aortic stenosis apparent?"
    )
    
    echo.save()
    visual_sys_func.save()
    lv_func.save()
    aortic_stenosis.save()
    
    echo.items.add(visual_sys_func)
    echo.items.add(lv_func)
    echo.items.add(aortic_stenosis)
    
def create_lab(user):
    lab = DataFormTemplate(
        title="Lab Results", 
        description="Lab results from standard laboratory tests.",
        created_by= user
        )
    hb = NumericItem(
        name = "Hb",
        description = "Hemoglobin value"
    )
    lac = NumericItem(
        name = "Lactate",
        description = "Lactate value"
    )
    bili = NumericItem(
        name = "Bilirubin",
        description = "Bilirubin value"
        
    )
    
    lab.save()
    hb.save()
    lac.save()
    bili.save()
    
    lab.items.add(hb)
    lab.items.add(lac)
    lab.items.add(bili)
    
def create_geri(user):
    geri = DataFormTemplate(
        title="Geriatric Scoring", 
        description="Our standard geriatric scoring system for patients > 75 years of age.",
        created_by= user
        )
    bath = BooleanItem(
        name = "Bathin",
        description = "Does need help bathing"
    )
    feed = BooleanItem(
        name = "Feeding",
        description = "Does need help feeding"
    )
    dress = NumericItem(
        name = "Dressing",
        description = "Does need help dressing"
        
    )
    
    geri.save()
    bath.save()
    feed.save()
    dress.save()
    
    geri.items.add(bath)
    geri.items.add(feed)
    geri.items.add(dress)
    
def run():
    user = User.objects.first()
    print(type(user))

    create_echo(user)
    create_lab(user)
    create_geri(user)
    

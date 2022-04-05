from turtle import numinput, title
from api.models import Item, NumericItem, TextItem, BooleanItem, DataForm

def create_echo():
    echo = DataForm(
        title="Echocardiography", 
        description="Standard form for results of echocardiography in our outpatients clinic."
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
    
def create_lab():
    lab = DataForm(
        title="Lab Results", 
        description="Lab results from standard laboratory tests."
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
    
def create_geri():
    geri = DataForm(
        title="Geriatric Scoring", 
        description="Our standard geriatric scoring system for patients > 75 years of age."
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
    create_echo()
    create_lab()
    create_geri()
    

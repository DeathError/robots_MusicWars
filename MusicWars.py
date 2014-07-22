#Начальныый этап
def else_none_boi():  #если кончились бои то можем пока прокачать 
    Region(13,223,109,320).click("ZIIH.png")
    sleep(0.23)
    Region(173,253,774,554).click("VL.png")
    if Region(173,253,774,554).exists("3a6par1Q1.png"):
         Region(173,253,774,554).click("3a6par1Q1.png")
         sleep(10)
         Region(173,253,774,554).click("13aKa33Tb1.png")
         sleep(1)
         close_monah()
    else:
        if Region(213,656,359,76).exists("MonaxMonmcq.png"):
            close_monah()
        else:
         Region(173,253,774,554).click("13aKa33Tb1.png")
         sleep(1)
         close_monah()

def close_monah():
     Region(13,222,106,392).click("1404565025484.png")
     sleep(0.23)
     Region(173,253,774,554).click("QBLBnp0Ma01y.png")
     sleep(0.23)
     Region(173,253,774,554).click("fx01.png")
     open_atomka()     

def open_atomka():
    if Region(177,301,766,494).exists("Baxpumnannaa.png"):
        Region(177,301,766,494).click("Hanan.png")
        sleep(0.5)
        open_atomka_vidor()
    else:
        open_atomka_vidor()
        
def open_atomka_vidor():        
    if Region(177,249,764,393).exists(Pattern("HanacrnZE.png").targetOffset(-17,3)):
        if Region(219,324,480,208).exists("1404567418743.png"):
            Region(219,324,480,208).hover("1404567418743.png")
            sleep(0.10)
            open_boi_load()
        else:    
            Region(173,253,774,554).click(Pattern("HanacrnZE.png").targetOffset(-17,3))
            sleep(30)
            if Region(240,250,652,320).exists("QBuxcn.png"):
                sleep(0)
                Region(240,250,652,320).click("QBuxcn.png")
            else:
                click(Location(555,484))
                if Region(237,253,652,311).exists("1404559699899.png"):
                     Region(237,253,652,311).click("1404559699899.png")
                     sleep(0.10)
                     Region(240,250,652,320).click("QBuxcn.png")
                     sleep(10)
                     open_boi_load()
                else:
                    sleep(30)
                    Region(240,250,652,320).click("QBuxcn.png")                    
    else:
        open_boi_load()
    
def close_boi(): #закрываем окно после боя
    if Region(240,250,652,320).exists("QBuxcn.png"):
        Region(240,250,652,320).click("QBuxcn.png")
        new_okno_boi()
    else:
        click(Location(555,484))
        Region(237,253,652,311).click("1404559699899.png")
        if Region(183,266,767,547).exists("Floanpanrmen.png"):
            Region(183,266,767,547).click("1404562484299.png")
            Region(240,250,652,320).click("QBuxcn.png")
            new_okno_boi()
        else:
            sleep(0)
            Region(183,266,767,547).click("QBuxcn.png")
            sleep(10)
            new_okno_boi() #после закрытия подготовливаем к новым боям   

def new_okno_boi(): #всё что нужно для нового боя
     Region(411,279,155,100).click("1404557642674.png")
     if Region(177,306,378,486).exists("BUKBAJI.png"):
          Region(195,412,201,102).click("BUKBAJI.png")
          sleep(0.10)
          Region(736,627,220,179).hover("1404582245445.png")
          sleep(2)
          Region(192,316,740,474).click(Pattern("1404559393979.png").targetOffset(-55,20))
          if Region(181,253,142,41).exists("BVITBA.png"):
              left_open_doi()
          else:
              sleep(0.10)
              Region(192,316,740,474).click(Pattern("1404559393979.png").targetOffset(-55,20))
              Region(175,306,770,489).click("1404547957758.png")
              left_open_doi()
     else:
         if Region(216,326,149,128).exists("DBOPbI.png"):
             Region(188,310,190,151).click("DBOPbI-1.png")
             Region(736,627,220,179).hover("1404582245445.png")
             sleep(2)
             Region(192,316,740,474).click(Pattern("1404559393979.png").targetOffset(-55,20))
             if Region(181,253,142,41).exists("BVITBA.png"):
                 left_open_doi()
             else:
                 sleep(0.10)
                 Region(192,316,740,474).click(Pattern("1404559393979.png").targetOffset(-55,20))
                 Region(175,306,770,489).click("1404547957758.png")
                 left_open_doi()
         else:
             if Region(376,313,125,121).exists("KOCTEFI.png"):
                 Region(373,313,127,108).click("KOCTEFI-1.png")
                 Region(736,627,220,179).hover("1404582245445.png")
                 sleep(2)
                 Region(192,316,740,474).click(Pattern("1404559393979.png").targetOffset(-55,20))
                 if Region(181,253,142,41).exists("BVITBA.png"):
                     left_open_doi()
                 else:
                     sleep(0.10)
                     Region(192,316,740,474).click(Pattern("1404559393979.png").targetOffset(-55,20))
                     Region(175,306,770,489).click("1404547957758.png")
                     left_open_doi()
             
#Начинаем поиск противника

def left_open_doi(): #смотрим слева
    region_left = Region(561,414,386,387)
    if region_left.exists("aIE.png"): #если уровень меньше
        if region_left.exists("HAI1ACIh2g.png"):
            region_left.hover("Cmna.png")
            if region_left.exists("1404561848539.png"):
                right_open_boi()
            else:
                region_left.click("HAI1ACIh2g.png")
                if Region(177,250,779,551).exists("1404562400404.png"):
                    Region(177,250,779,551).click("1404562484299.png")
                    sleep(0.23)
                    new_okno_boi()
                else:
                    if Region(161,175,795,633).exists("Heqocrarouuo.png"):
                        Region(161,175,795,633).click("1404562484299.png")
                        else_none_boi()
                    else:
                        if Region(163,171,797,636).exists("HEAOCTBTOHH0.png"):
                            sleep(100)
                            new_okno_boi()
                        else:
                            sleep(30)
                            close_boi()
        else:
           right_open_boi()
    else:
        right_open_boi()

def right_open_boi():
    region_right = Region(175,418,388,381)
    if region_right.exists("aIE-1.png"):
        if region_right.exists("HAI1ACIh2g.png"):
            region_right.hover("Cmna.png")
            if Region(447,499,96,22).exists("1404561848539.png"):
                new_okno_boi()
            else:
                region_right.click("HAI1ACIh2g.png")
                if Region(177,250,779,551).exists("1404562400404.png"):
                    Region(177,250,779,551).click("1404562484299.png")
                    sleep(0.23)
                    new_okno_boi()
                else:
                    if Region(161,175,795,633).exists("Heqocrarouuo.png"):
                        Region(161,175,795,633).click("1404562484299.png")
                        else_none_boi()
                    else:
                        if Region(163,171,797,636).exists("HEAOCTBTOHH0.png"):
                            sleep(100)
                            new_okno_boi()
                        else:
                            sleep(30)
                            close_boi()
        else:
            new_okno_boi()
    else:
        new_okno_boi()
      
def open_boi_load():
    if Region(14,193,165,114).exists("1404566085321.png"):
        Region(14,193,165,114).click("YZ.png")
        sleep(0.23)
        Region(167,179,782,389).click("1404566159549.png")
        Region(10,209,124,652).click("IUHTlf.png")
        Region(736,627,220,179).hover("1404582245445.png")
        sleep(1)
        Region(192,316,740,474).click(Pattern("1404559393979.png").targetOffset(-55,20))
        if Region(181,253,142,41).exists("BVITBA.png"):
             left_open_doi()
        else:
            sleep(0)
            Region(175,306,770,489).click("1404547957758.png")
            sleep(1)
            left_open_doi()
    else:
         Region(22,221,100,248).click("IUHTlf.png")
         sleep(1)
         Region(736,627,220,179).hover("1404582245445.png")
         sleep(1)
         Region(192,316,740,474).click(Pattern("1404559393979.png").targetOffset(-55,20))
         if Region(181,253,142,41).exists("BVITBA.png"):
             left_open_doi()
         else:
             sleep(0)
             Region(175,306,770,489).click("1404547957758.png")
             sleep(0.10)
             left_open_doi()

def start():
    if Region(89,168,879,706).exists(Pattern("1404545006957.png").similar(0.90),10):
        Region(89,168,879,706).click("1404545006957.png")   # Закрыть окно
        if  Region(89,168,879,706).exists(Pattern("1404545006957.png").similar(0.90),10):
            f1 = find("1404544876487.png")
            click(Location(882,301)) #Закрыть окно
            if Region(89,168,879,706).exists("EMEAHEBHbleI.png"):
                click(Location(561,631))
                open_boi_load()
            else:
                open_boi_load()
        else:
            if  Region(89,168,879,706).exists("EMEAHEBHbleI.png"):
                click(Location(561,631))
                open_boi_load()
            else:
                open_boi_load()
    else:
        if  Region(89,168,879,706).exists(Pattern("1404545006957.png").similar(0.90),10):
            f1 = find("1404544876487.png")
            click(Location(882,301)) #Закрыть окно
            if Region(89,168,879,706).exists("EMEAHEBHbleI.png"):
                click(Location(561,631))
                open_boi_load()
            else:
                open_boi_load()
        else:
            if  Region(89,168,879,706).exists("EMEAHEBHbleI.png"):
                click(Location(561,631))
                open_boi_load()
            else:
                open_boi_load()
        
start()

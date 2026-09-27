import pygame
import sys
import os
pygame.init()

info = pygame.display.Info()
WIDTH,HEIGHT = info.current_w,info.current_h
MENU_WIDTH,MENU_HEI = 500,700
class Utility:
    def __init__(self) -> None:
        self.ColorRect_Size = 18
        self.ColorGrid = int(UTILWID/13)

        self.Color_Asset = {(1,1):[(51,0,0)],
                            (1,2):[(51,25,0)],
                            (1,3):[(51,51,0)],
                            (1,4):[(25,51,0)],
                            (1,5):[(0,51,0)],
                            (1,6):[(0,51,25)],
                            (1,7):[(0,51,51)],
                            (1,8):[(0,25,51)],
                            (1,9):[(0,0,51)],
                            (1,10):[(25,0,51)],
                            (1,11):[(51,0,51)],
                            (1,12):[(51,0,25)],
                            (1,13):[(0,0,0)],

                            (2,1):[(102,0,0)],
                            (2,2):[(102,51,0)],
                            (2,3):[(102,102,0)],
                            (2,4):[(51,102,0)],
                            (2,5):[(0,102,0)],
                            (2,6):[(0,102,51)],
                            (2,7):[(0,102,102)],
                            (2,8):[(0,51,102)],
                            (2,9):[(0,0,102)],
                            (2,10):[(51,0,102)],
                            (2,11):[(102,0,102)],
                            (2,12):[(102,0,51)],
                            (2,13):[(32,32,32)],
                            
                            (3,1):[(153,0,0)],
                            (3,2):[(153,76,0)],
                            (3,3):[(153,153,0)],
                            (3,4):[(76,153,0)],
                            (3,5):[(0,153,0)],
                            (3,6):[(0,153,76)],
                            (3,7):[(0,153,153)],
                            (3,8):[(0,76,153)],
                            (3,9):[(0,0,153)],
                            (3,10):[(76,0,153)],
                            (3,11):[(153,0,153)],
                            (3,12):[(153,0,76)],
                            (3,13):[(64,64,64)],
                            
                            (4,1):[(204,0,0)],
                            (4,2):[(204,102,0)],
                            (4,3):[(204,204,0)],
                            (4,4):[(102,204,0)],
                            (4,5):[(0,204,0)],
                            (4,6):[(0,204,102)],
                            (4,7):[(0,204,204)],
                            (4,8):[(0,102,204)],
                            (4,9):[(0,0,204)],
                            (4,10):[(102,0,204)],
                            (4,11):[(204,0,204)],
                            (4,12):[(204,0,102)],
                            (4,13):[(96,96,96)],
                            
                            (5,1):[(255,0,0)],
                            (5,2):[(255,128,0)],
                            (5,3):[(255,255,0)],
                            (5,4):[(128,255,0)],
                            (5,5):[(0,255,0)],
                            (5,6):[(0,255,128)],
                            (5,7):[(0,255,255)],
                            (5,8):[(0,128,255)],
                            (5,9):[(0,0,255)],
                            (5,10):[(127,0,255)],
                            (5,11):[(255,0,255)],
                            (5,12):[(255,0,127)],
                            (5,13):[(128,128,128)],
                            
                            (6,1):[(255,51,51)],
                            (6,2):[(255,153,51)],
                            (6,3):[(255,255,51)],
                            (6,4):[(153,255,51)],
                            (6,5):[(51,255,51)],
                            (6,6):[(51,255,153)],
                            (6,7):[(51,255,255)],
                            (6,8):[(51,153,255)],
                            (6,9):[(51,51,255)],
                            (6,10):[(153,51,255)],
                            (6,11):[(255,51,255)],
                            (6,12):[(255,51,153)],
                            (6,13):[(160,160,160)],
                            
                            (7,1):[(255,102,102)],
                            (7,2):[(255,178,102)],
                            (7,3):[(255,255,102)],
                            (7,4):[(178,255,102)],
                            (7,5):[(102,255,102)],
                            (7,6):[(102,255,178)],
                            (7,7):[(102,255,255)],
                            (7,8):[(102,178,255)],
                            (7,9):[(102,102,255)],
                            (7,10):[(178,102,255)],
                            (7,11):[(255,102,255)],
                            (7,12):[(255,102,178)],
                            (7,13):[(192,192,192)],
                            
                            (8,1):[(255,153,153)],
                            (8,2):[(255,204,153)],
                            (8,3):[(255,255,153)],
                            (8,4):[(204,255,153)],
                            (8,5):[(153,255,153)],
                            (8,6):[(153,255,204)],
                            (8,7):[(153,255,255)],
                            (8,8):[(153,204,255)],
                            (8,9):[(153,153,255)],
                            (8,10):[(204,153,255)],
                            (8,11):[(255,153,255)],
                            (8,12):[(255,153,204)],
                            (8,13):[(224,224,224)],

                            (9,1):[(255,204,204)],
                            (9,2):[(255,229,204)],
                            (9,3):[(255,255,204)],
                            (9,4):[(229,255,204)],
                            (9,5):[(204,255,204)],
                            (9,6):[(204,255,229)],
                            (9,7):[(204,255,255)],
                            (9,8):[(204,229,255)],
                            (9,9):[(204,204,255)],
                            (9,10):[(229,204,255)],
                            (9,11):[(255,204,255)],
                            (9,12):[(255,204,229)],
                            (9,13):[(255,255,255)],
                            }
        for i,obj in enumerate(self.Color_Asset):
            self.Color_Asset[obj].append(pygame.Rect(obj[1]*20,obj[0]*20,self.ColorRect_Size,self.ColorRect_Size))
        self.Pen_Asset = {'pen':[pygame.transform.scale(pygame.image.load("Asset/pen_01.png"),(50,50)),
                                 pygame.Rect(60,400,60,60)],
                          'eraser':[pygame.transform.scale(pygame.image.load("Asset/eraser.png"),(50,50)),
                                    pygame.Rect(180,400,60,60)]}
        
        self.Grid_y = int((900 - 180)/50)
        self.Grid_x = int(320/50)
        self.Grid_size = 50

        self.BrushAsset = {1:[2],2:[4],3:[6],4:[8],5:[10]}
        self.BrushUsingColor = (153,255,153)
        self.Active_Color = (153,255,153)
        for i,br in enumerate(self.BrushAsset):
            self.BrushAsset[br].append(pygame.Rect(self.Grid_size*br - 12,self.Grid_size+180,30,30))
            self.BrushAsset[br].append((255,255,255))
        self.BrushAsset[3][2] = self.BrushUsingColor

        self.ZoomAsset = {'in':[pygame.transform.scale(pygame.image.load('Asset/zoomin_50.png'),(50,50)),
                                pygame.Rect(60,300,60,60)],
                          'out':[pygame.transform.scale(pygame.image.load('Asset/zoomout_50.png'),(50,50)),
                                 pygame.Rect(180,300,60,60)]}
        self.PixelFont = pygame.font.Font('Asset/PixelFont.ttf',20)
        Text_Color = (255,255,255)
        Text_Color_Tile = (153,0,17)
        self.Command_Asset = {'clear':[self.PixelFont.render('CLEAR',True,Text_Color)],
                              'save':[self.PixelFont.render('SAVE',True,Text_Color)],
                              'tileproject':[self.PixelFont.render('TILE-PROJECT',True,Text_Color)],
                              'newproject':[self.PixelFont.render('NEW-PROJECT',True,Text_Color)],
                              }#text surface, rect
        self.Command_Asset_Tile = {'clear':[self.PixelFont.render('CLEAR',True,Text_Color_Tile)],
                              'save':[self.PixelFont.render('SAVE',True,Text_Color_Tile)],
                              'drawproject':[self.PixelFont.render('DRAW-PROJECT',True,Text_Color_Tile)],
                              'newproject':[self.PixelFont.render('NEW-PROJECT',True,Text_Color_Tile)],
                              }#text surface, rect
        self.comwid = 180
        self.comhei = 50
        for i,entity in enumerate(self.Command_Asset):
            self.Command_Asset[entity].append(pygame.Rect(self.Get_Mid(self.comwid,320),500+(60*i),self.comwid,self.comhei))
        for i,entity in enumerate(self.Command_Asset_Tile):
            self.Command_Asset_Tile[entity].append(pygame.Rect(self.Get_Mid(self.comwid,320),500+(60*i),self.comwid,self.comhei))
    def update(self):
        for i,color in enumerate(util.Color_Asset):
            pygame.draw.rect(draw.Utility_Surface,self.Color_Asset[color][0],self.Color_Asset[color][1])
        for i,brush in enumerate(self.BrushAsset):
            pygame.draw.circle(draw.Utility_Surface,(255,255,255),self.BrushAsset[brush][1].center,self.BrushAsset[brush][0])
            pygame.draw.rect(draw.Utility_Surface,self.BrushAsset[brush][2],self.BrushAsset[brush][1],1)
        for i,zoom in enumerate(self.ZoomAsset):
            draw.Utility_Surface.blit(self.ZoomAsset[zoom][0],(self.ZoomAsset[zoom][1].x+5,self.ZoomAsset[zoom][1].y+5))
        for i,com in enumerate(self.Command_Asset):
            x = self.Get_Mid(self.Command_Asset[com][0].get_width(),self.comwid)+(self.Command_Asset[com][1].x)
            y = self.Get_Mid(self.Command_Asset[com][0].get_height(),self.comhei)+(self.Command_Asset[com][1].y)
            draw.Utility_Surface.blit(self.Command_Asset[com][0],(x,y))
        draw.Utility_Surface.blit(self.Pen_Asset['pen'][0],(util.Pen_Asset['pen'][1].x+5,util.Pen_Asset['pen'][1].y+5))
        draw.Utility_Surface.blit(self.Pen_Asset['eraser'][0],(util.Pen_Asset['eraser'][1].x+5,util.Pen_Asset['eraser'][1].y+5))
    def TileUpdate(self):
        for i,color in enumerate(util.Color_Asset):
            pygame.draw.rect(tile.Utility_Surface,self.Color_Asset[color][0],self.Color_Asset[color][1])
        for i,com in enumerate(self.Command_Asset_Tile):
            x = self.Get_Mid(self.Command_Asset_Tile[com][0].get_width(),self.comwid)+(self.Command_Asset_Tile[com][1].x)
            y = self.Get_Mid(self.Command_Asset_Tile[com][0].get_height(),self.comhei)+(self.Command_Asset_Tile[com][1].y)
            tile.Utility_Surface.blit(self.Command_Asset_Tile[com][0],(x,y))
        tile.Utility_Surface.blit(self.Pen_Asset['pen'][0],(util.Pen_Asset['pen'][1].x+5,util.Pen_Asset['pen'][1].y+5))
        tile.Utility_Surface.blit(self.Pen_Asset['eraser'][0],(util.Pen_Asset['eraser'][1].x+5,util.Pen_Asset['eraser'][1].y+5))
    def Get_Mid(self,size,scr_size):
        return (scr_size/2) - (size/2)
class Menu:

    def __init__(self) -> None:
        Get_Size_Text = 'Enter Width/Height'
        font = pygame.font.Font("Asset/Font2.ttf",38)
        self.SizeText_Surface = font.render(Get_Size_Text,True,(153,204,255))
        self.InputBox_Wid = pygame.Rect((MENU_WIDTH-200)/2,225,200,50)
        self.InputBox_Hei = pygame.Rect((MENU_WIDTH-200)/2,325,200,50)
        self.SizeText_Surface_x,self.SizeText_Surface_y = util.Get_Mid(self.SizeText_Surface.get_width(),MENU_WIDTH),util.Get_Mid(self.SizeText_Surface.get_height(),MENU_HEI)-250
        self.Typing_Width = False
        self.Typing_Hei = False
     
        self.UI_Wid = ''
        self.UI_Hei = ''
        
        self.UI_Font = pygame.font.Font("Asset/Font2.ttf",20)
        self.Hei_Active_Color = (255,255,255)
        self.Wid_Active_Color = (255,255,255)

        self.EnterRect = pygame.Rect((MENU_WIDTH-130)/2,425,130,50)
        self.EnterText_Surface = pygame.font.Font("Asset/Font2.ttf",20).render("Enter",True,(0,0,0))

        self.Error_Surface_1 = pygame.font.Font("Asset/Font2.ttf",10).render("Max Width  1120",True,(255,102,102))
        self.Error_Surface_2 = pygame.font.Font("Asset/Font2.ttf",10).render("Max Height  900",True,(255,102,102))
        
        self.Menu_Button_Asset = {'draw':["DRAW"],'tile':['TILE']}
        for i,menu in enumerate(self.Menu_Button_Asset):
            font_size = 20
            Menu_Font = pygame.font.Font("Asset/PixelFont.ttf",font_size)
            Menu_Text = self.Menu_Button_Asset[menu][0]
            Menu_Color = (155,204,17)
            self.But_Wid,self.But_Hei = 130,50
            But_x = (MENU_WIDTH - self.But_Wid)/2
            But_y = 155
            print(i)
            self.Menu_Button_Asset[menu].append(Menu_Font.render(Menu_Text,True,Menu_Color))
            self.Menu_Button_Asset[menu].append(pygame.Rect(But_x,But_y,self.But_Wid,self.But_Hei))

    def main(self):
        Display.fill((70,70,72))
        Display.blit(self.SizeText_Surface,(self.SizeText_Surface_x,self.SizeText_Surface_y))

        pygame.draw.rect(Display,(255,255,255),self.Menu_Button_Asset['tile'][2],1)
        x = self.Menu_Button_Asset['tile'][2].x + ((self.But_Wid - self.Menu_Button_Asset['tile'][1].get_width())/2)
        y = self.Menu_Button_Asset['tile'][2].y + ((self.But_Hei - self.Menu_Button_Asset['tile'][1].get_height())/2)
        Display.blit(self.Menu_Button_Asset['tile'][1],(x,y))

        Display.blit(self.Error_Surface_1,(util.Get_Mid(self.Error_Surface_1.get_width(),MENU_WIDTH),585))
        Display.blit(self.Error_Surface_2,(util.Get_Mid(self.Error_Surface_2.get_width(),MENU_WIDTH),610))
        
        pygame.draw.rect(Display,self.Wid_Active_Color,self.InputBox_Wid,2)
        pygame.draw.rect(Display,self.Hei_Active_Color,self.InputBox_Hei,2)

        pygame.draw.rect(Display,(102,255,102),self.EnterRect)
        Display.blit(self.EnterText_Surface,(self.EnterRect.x+30,self.EnterRect.y+10))

        Wid_Sur = self.UI_Font.render(self.UI_Wid,True,(255,153,204))
        Hei_Sur = self.UI_Font.render(self.UI_Hei,True,(153,204,255))
        
        Wid_x,Wid_y = util.Get_Mid(Wid_Sur.get_width(),200),util.Get_Mid(Wid_Sur.get_height(),50)
        Hei_x,Hei_y = util.Get_Mid(Hei_Sur.get_width(),200),util.Get_Mid(Hei_Sur.get_height(),50)
        Display.blit(Wid_Sur,(Wid_x+self.InputBox_Wid.x,Wid_y+self.InputBox_Wid.y))
        Display.blit(Hei_Sur,(Hei_x+self.InputBox_Hei.x,Hei_y+self.InputBox_Hei.y))

        self.Start_Draw = False

        #UI input 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.InputBox_Wid.collidepoint(event.pos):
                    self.Typing_Width = True
                    self.Wid_Active_Color = (25,150,25)
                else:
                    self.Typing_Width = False
                    self.Wid_Active_Color = (255,255,255)

                if self.InputBox_Hei.collidepoint(event.pos):
                    self.Typing_Hei = True
                    self.Hei_Active_Color = (25,150,25)
                else:
                    self.Typing_Hei = False
                    self.Hei_Active_Color = (255,255,255)
                if self.EnterRect.collidepoint(event.pos):
                    self.Start_Draw = True

                if self.Menu_Button_Asset['tile'][2].collidepoint(event.pos):
                    global StateFlag,InstanceFlag,TiledFlag
                    StateFlag = 3
                    InstanceFlag = 0
                    TiledFlag = True

            if self.Typing_Width:
                if event.type == pygame.KEYDOWN:
                    try:
                        if event.key == pygame.K_BACKSPACE:
                            self.UI_Wid = self.UI_Wid[:-1]
                        elif event.key == pygame.K_RETURN:
                            self.Typing_Width = False
                            self.Typing_Hei = True
                            self.Wid_Active_Color = (255,255,255)
                            self.Hei_Active_Color = (25,150,25)
                        else:
                            if len(self.UI_Wid) < 4:
                                input = int(event.unicode)
                                self.UI_Wid += str(input)
                    except:
                        pass
            if self.Typing_Hei:
                if event.type == pygame.KEYDOWN:
                    try:
                        if event.key == pygame.K_BACKSPACE:
                            self.UI_Hei = self.UI_Hei[:-1]
                        elif event.key == pygame.K_RETURN:
                            self.Start_Draw = True
                        else:
                            if len(self.UI_Hei) < 3:
                                input = int(event.unicode)
                                self.UI_Hei += str(input)
                    except:
                        pass

        if self.Start_Draw:
            self.Draw_Check()
    def Draw_Check(self):
        global StateFlag,DRAWSURWID,DRAWSURHEI,InstanceFlag
        try:
            Hei = int(self.UI_Hei)
            Wid = int(self.UI_Wid)
            if Hei > 900 or Wid > 1120:
                self.Start_Draw = False
            else:
                self.UI_Wid = ''
                self.UI_Hei = ''
                self.Typing_Width = False
                self.Typing_Hei = False
                self.Wid_Active_Color = (255,255,255)
                self.Hei_Active_Color = (255,255,255)
                StateFlag = 2
                InstanceFlag = 0
                DRAWSURWID,DRAWSURHEI = Wid,Hei
        except:
            self.Start_Draw = False
    def TiledInitiasion(self):
        Get_Size_Text = 'Pixels in X,Y Direction'
        font = pygame.font.Font("Asset/Font2.ttf",38)
        self.SizeText_Surface = font.render(Get_Size_Text,True,(153, 0, 17))
        self.InputBox_Wid = pygame.Rect((MENU_WIDTH-200)/2,225,200,50)
        self.InputBox_Hei = pygame.Rect((MENU_WIDTH-200)/2,325,200,50)
        self.SizeText_Surface_x,self.SizeText_Surface_y = util.Get_Mid(self.SizeText_Surface.get_width(),MENU_WIDTH),util.Get_Mid(self.SizeText_Surface.get_height(),MENU_HEI)-250
        self.Typing_Width = False
        self.Typing_Hei = False
     
        self.UI_Wid = ''
        self.UI_Hei = ''
        
        self.UI_Font = pygame.font.Font("Asset/Font2.ttf",20)
        self.Wid_Active_Color = (153, 0, 17)
        self.Hei_Active_Color = (153, 0, 17)

        self.EnterRect = pygame.Rect((MENU_WIDTH-130)/2,425,130,50)
        self.EnterText_Surface = pygame.font.Font("Asset/Font2.ttf",20).render("Enter",True,(252, 246, 245))

        self.Error_Surface_1 = pygame.font.Font("Asset/Font2.ttf",12).render("Max   X   Pixels <- ",True,(153, 0, 17))
        self.Error_Surface_2 = pygame.font.Font("Asset/Font2.ttf",12).render("Max   Y   Pixels <- ",True,(153, 0, 17))
        
    def TiledMenu(self):
        Display.fill((252, 246, 245))
        Display.blit(self.SizeText_Surface,(self.SizeText_Surface_x,self.SizeText_Surface_y))

        Display.blit(self.Error_Surface_1,(util.Get_Mid(self.Error_Surface_1.get_width(),MENU_WIDTH),585))
        Display.blit(self.Error_Surface_2,(util.Get_Mid(self.Error_Surface_2.get_width(),MENU_WIDTH),610))
        
        pygame.draw.rect(Display,(153,0,17),self.Menu_Button_Asset['draw'][2],1)
        x = self.Menu_Button_Asset['draw'][2].x + ((self.But_Wid - self.Menu_Button_Asset['draw'][1].get_width())/2)
        y = self.Menu_Button_Asset['draw'][2].y + ((self.But_Hei - self.Menu_Button_Asset['draw'][1].get_height())/2)
        Display.blit(self.Menu_Button_Asset['draw'][1],(x,y))

        pygame.draw.rect(Display,self.Wid_Active_Color,self.InputBox_Wid,2)
        pygame.draw.rect(Display,self.Hei_Active_Color,self.InputBox_Hei,2)

        pygame.draw.rect(Display,(153, 0, 17),self.EnterRect)
        Display.blit(self.EnterText_Surface,(self.EnterRect.x+30,self.EnterRect.y+10))

        Wid_Sur = self.UI_Font.render(self.UI_Wid,True,(153, 0, 17))
        Hei_Sur = self.UI_Font.render(self.UI_Hei,True,(153, 0, 17))
        
        Wid_x,Wid_y = util.Get_Mid(Wid_Sur.get_width(),200),util.Get_Mid(Wid_Sur.get_height(),50)
        Hei_x,Hei_y = util.Get_Mid(Hei_Sur.get_width(),200),util.Get_Mid(Hei_Sur.get_height(),50)
        Display.blit(Wid_Sur,(Wid_x+self.InputBox_Wid.x,Wid_y+self.InputBox_Wid.y))
        Display.blit(Hei_Sur,(Hei_x+self.InputBox_Hei.x,Hei_y+self.InputBox_Hei.y))

        self.Start_TiledProject = False

        #UI input 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.InputBox_Wid.collidepoint(event.pos):
                    self.Typing_Width = True
                    self.Wid_Active_Color = (25,150,25)
                else:
                    self.Typing_Width = False
                    self.Wid_Active_Color = (153, 0, 17)

                if self.InputBox_Hei.collidepoint(event.pos):
                    self.Typing_Hei = True
                    self.Hei_Active_Color = (25,150,25)
                else:
                    self.Typing_Hei = False
                    self.Hei_Active_Color = (153, 0, 17)
                if self.EnterRect.collidepoint(event.pos):
                    self.Start_TiledProject = True
                if self.Menu_Button_Asset['draw'][2].collidepoint(event.pos):
                    global StateFlag,InstanceFlag,TiledFlag
                    StateFlag = 1
                    InstanceFlag = 0
                    TiledFlag = True


            if self.Typing_Width:
                if event.type == pygame.KEYDOWN:
                    try:
                        if event.key == pygame.K_BACKSPACE:
                            self.UI_Wid = self.UI_Wid[:-1]
                        elif event.key == pygame.K_RETURN:
                            self.Typing_Width = False
                            self.Typing_Hei = True
                            self.Wid_Active_Color = (153, 0, 17)
                            self.Hei_Active_Color = (25,150,25)
                        else:
                            if len(self.UI_Wid) < 4:
                                input = int(event.unicode)
                                self.UI_Wid += str(input)
                    except:
                        pass
            if self.Typing_Hei:
                if event.type == pygame.KEYDOWN:
                    try:
                        if event.key == pygame.K_BACKSPACE:
                            self.UI_Hei = self.UI_Hei[:-1]
                        elif event.key == pygame.K_RETURN:
                            self.Start_TiledProject = True
                        else:
                            if len(self.UI_Hei) < 3:
                                input = int(event.unicode)
                                self.UI_Hei += str(input)
                    except:
                        pass

        if self.Start_TiledProject:
            self.Tile_Check()
    def Tile_Check(self):
        global StateFlag,TILEWID,TILEHEI,InstanceFlag
        try:
            Hei = int(self.UI_Hei)
            Wid = int(self.UI_Wid)
            if Hei > 1000 or Wid > 1000:
                self.Start_TiledProject = False
            else:
                self.UI_Wid = ''
                self.UI_Hei = ''
                self.Typing_Width = False
                self.Typing_Hei = False
                self.Wid_Active_Color = (153, 0, 17)
                self.Hei_Active_Color = (153, 0, 17)
                StateFlag = 4
                InstanceFlag = 0
                TILEWID,TILEHEI = Wid,Hei

        except:
            self.Start_TiledProject = False
class Draw:
    
    def __init__(self):
        self.MaxDrawWid,self.MaxDrawHei = 1120,900
        self.Utility_Surface = pygame.Surface((UTILWID,UTILHEI))
        self.Drawing_Surface = pygame.Surface((DRAWSURWID,DRAWSURHEI))
        
        self.Drawing_Surface.fill((255,255,255,0))
        
        self.Draw_Color = (0,0,0)

        self.LastPos = None
        self.CurrentPos = None
        #Utility Setup
        self.Utility_Surface.fill((100,100,100))
        self.BrushSize = 6
        self.Paint_Mode = 1 #1 for draw #2 for erase
        self.PenDown = False

        self.UserInput_Asset = {'input':'','rect':pygame.Rect(util.Get_Mid(util.comwid,320),500+(60*4),util.comwid,util.comhei),'color':(255,255,255)}
        self.DefaultIndex = 0
    def FloodFill(self,x,y,target,fill):
        Queue = [(x,y)]
        while Queue:
            x,y = Queue.pop()
            if 0<x<self.Drawing_Surface.get_width() and 0<y<self.Drawing_Surface.get_height():
                if self.Drawing_Surface.get_at((x,y)) == target:
                    self.Drawing_Surface.set_at((x,y),fill)
                    if x+1 < self.Drawing_Surface.get_width():
                        Queue.append((x+1,y))
                    if x-1 > 0:
                        Queue.append((x-1,y))
                    if y+1 < self.Drawing_Surface.get_height():
                        Queue.append((x,y+1))
                    if y-1 > 0:
                        Queue.append((x,y-1))


    def main(self):
        Display.fill((60,60,60))
        self.DS_x,self.DS_y = (self.MaxDrawWid - self.Drawing_Surface.get_width())/2 , (HEIGHT - self.Drawing_Surface.get_height()) /2
        Display.blit(self.Drawing_Surface,(self.DS_x,self.DS_y))
        Display.blit(self.Utility_Surface,(1120,0))

        pygame.draw.rect(self.Utility_Surface,self.UserInput_Asset['color'],self.UserInput_Asset['rect'],1)
        Input_Surface = util.PixelFont.render(self.UserInput_Asset['input'],True,(0,0,0))
        x = self.UserInput_Asset['rect'].x + util.Get_Mid(Input_Surface.get_width(),util.comwid)
        y = self.UserInput_Asset['rect'].y + util.Get_Mid(Input_Surface.get_height(),util.comhei)
        Display.blit(Input_Surface,(x+1120,y))

        if self.PenDown:
            if self.Paint_Mode == 1:
                self.CurrentPos = pygame.mouse.get_pos()
                pygame.draw.line(self.Drawing_Surface,self.Draw_Color,(self.CurrentPos[0]-self.DS_x,self.CurrentPos[1]-self.DS_y),(self.LastPos[0]-self.DS_x,self.LastPos[1]-self.DS_y),self.BrushSize)
                self.LastPos = self.CurrentPos
            elif self.Paint_Mode == 2:
                self.CurrentPos = pygame.mouse.get_pos()
                pygame.draw.line(self.Drawing_Surface,(255,255,255,0),(self.CurrentPos[0]-self.DS_x,self.CurrentPos[1]-self.DS_y),(self.LastPos[0]-self.DS_x,self.LastPos[1]-self.DS_y),self.BrushSize)
                self.LastPos = self.CurrentPos
    def Clear(self):
        self.Drawing_Surface.fill((255,255,255,0))
    def SaveImage(self):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

        if self.UserInput_Asset['input'] == '':
            filename = 'NewImage'+str(self.DefaultIndex)+'.png'
            self.DefaultIndex +=1
        else:
            filename = self.UserInput_Asset['input'] + '.png'

        self.UserInput_Asset['input'] = ''
        filename = os.path.join(desktop_path, filename)
        pygame.image.save(self.Drawing_Surface,filename)
        self.Clear()
    def NewProject(self):
        global StateFlag,InstanceFlag,Display
        StateFlag = 1
        InstanceFlag = 0
        Display = pygame.display.set_mode((MENU_WIDTH,MENU_HEI))
    def TiledProject(self):
        global StateFlag,InstanceFlag,Display,TiledFlag
        StateFlag = 3
        InstanceFlag = 0
        TiledFlag = True
        Display = pygame.display.set_mode((MENU_WIDTH,MENU_HEI))

class TiledProject:
    def __init__(self) -> None:
        self.TileSize = min(1120/TILEWID,900/TILEHEI)

        self.TileSurface = pygame.Surface((self.TileSize*TILEWID,self.TileSize*TILEHEI))
        self.TileSurface.fill((255,255,255,0))
        self.Utility_Surface = pygame.Surface((UTILWID,UTILHEI))
        self.Paint_Mode = 1 #write, erase
        self.Tile_Color = (0,0,0)
        self.TS_x,self.TS_y = (1120 - self.TileSurface.get_width())/2 , (HEIGHT - self.TileSurface.get_height()) /2
        self.WHITE = (252, 246, 245)
        self.RED = (153,0,17)
        self.Utility_Surface.fill(self.WHITE)
        self.FileIndex = 0
        self.UserInput_Asset = {'input':'','rect':pygame.Rect(util.Get_Mid(util.comwid,320),500+(60*4),util.comwid,util.comhei),'color':(153,0,17)}
        self.Draw_Grid()
    def Color_Tile(self,x,y,target,fill):
        Queue = [(x,y)]
        while Queue:
            x,y = Queue.pop()
            if 0 < x < self.TileSurface.get_width() and 0 < y < self.TileSurface.get_height():
                if self.TileSurface.get_at((x,y)) == target:
                    self.TileSurface.set_at((x,y),fill)
                    if x+1 < self.TileSurface.get_width():
                        Queue.append((x+1,y))
                    if x-1 > 0:
                        Queue.append((x-1,y))
                    if y+1 < self.TileSurface.get_height():
                        Queue.append((x,y+1))
                    if y-1 > 0:
                        Queue.append((x,y-1))

    def main(self):
        Display.fill((255,204,204))
        Display.blit(self.TileSurface,(self.TS_x,self.TS_y))
        Display.blit(self.Utility_Surface,(1120,0))
        
        pygame.draw.rect(self.Utility_Surface,self.UserInput_Asset['color'],self.UserInput_Asset['rect'],1)
        Input_Surface = util.PixelFont.render(self.UserInput_Asset['input'],True,(0,0,0))
        x = self.UserInput_Asset['rect'].x + util.Get_Mid(Input_Surface.get_width(),util.comwid)
        y = self.UserInput_Asset['rect'].y + util.Get_Mid(Input_Surface.get_height(),util.comhei)
        Display.blit(Input_Surface,(x+1120,y))

    def Draw_Grid(self):
        color = (1,1,1,0)
        for i in range(TILEWID+1):
            for j in range(TILEHEI+1):
                pygame.draw.line(self.TileSurface,color,(self.TileSize*i,0),(self.TileSize*i,self.TileSize*TILEHEI))
                pygame.draw.line(self.TileSurface,color,(0,self.TileSize*j),(self.TileSize*TILEWID,self.TileSize*j))

    def NewProject(self):
        global StateFlag,InstanceFlag,Display
        StateFlag = 3
        InstanceFlag = 0
        Display = pygame.display.set_mode((MENU_WIDTH,MENU_HEI))

    def DrawProject(self):
        global StateFlag,InstanceFlag,Display
        StateFlag = 1
        InstanceFlag = 0
        Display = pygame.display.set_mode((MENU_WIDTH,MENU_HEI))

    def Clear(self):
        self.TileSurface.fill((255,255,255,0))
        self.Draw_Grid()

    def Save(self):
        desktop_path = os.path.join(os.path.expanduser('~'),"Desktop")

        if self.UserInput_Asset['input'] != '':
            file = self.UserInput_Asset['input']+'.png'
        else:
            file = 'NewImage'+str(self.FileIndex)+'.png'
        file = os.path.join(desktop_path,file)
        pygame.image.save(self.TileSurface,file)
        self.Clear()
        self.UserInput_Asset['input'] = ''

#CONSTANT
DRAWSURWID,DRAWSURHEI = None,None
UTILWID,UTILHEI = 320,900
clock = pygame.time.Clock()
Display = pygame.display.set_mode(((MENU_WIDTH,MENU_HEI)))
pygame.display.set_caption("Drawing Application")
Avatar = pygame.image.load('Paintings/Yoofie.png')
pygame.display.set_icon(Avatar)
util = Utility()
menu = Menu()

TILEHEI,TILEWID = None,None
TiledFlag = False
StateFlag = 1 #1 for main menu 2 for drawing 3 for tiled menu 4 for tiled project
Tile = False
InstanceFlag = 0

while True:
    if  StateFlag == 1:
        if InstanceFlag == 0:
            menu = Menu()
            InstanceFlag = 1
        menu.main()
    elif StateFlag == 2:
        if InstanceFlag == 0:
            draw = Draw()
            Display = pygame.display.set_mode((WIDTH-10,HEIGHT-10),pygame.RESIZABLE)
            Typing_Active = False
            InstanceFlag+=1
        draw.main()
        util.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    if draw.DS_x < event.pos[0] < draw.DS_x + draw.Drawing_Surface.get_width() and draw.DS_y < event.pos[1] < draw.DS_y +draw.Drawing_Surface.get_height():
                        target = draw.Drawing_Surface.get_at((event.pos[0] - int(draw.DS_x), event.pos[1] - int(draw.DS_y)))
                        x = pygame.mouse.get_pos()[0] - int(draw.DS_x)
                        y = pygame.mouse.get_pos()[1] - int(draw.DS_y)
                        draw.FloodFill(x,y,target,draw.Draw_Color)

                if event.button == 1:

                    draw.UserInput_Asset['color'] = (255,255,255)
                    if event.pos[0]>1120:
                        Typing_Active = False
                        if event.pos[1]<220:
                            pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['save'][1],1)
                            pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['newproject'][1],1)
                            pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['clear'][1],1)
                            pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['tileproject'][1],1)
                            pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.ZoomAsset['out'][1],1)
                            pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.ZoomAsset['in'][1],1)
                            for i,obj in enumerate(util.Color_Asset):
                                if util.Color_Asset[obj][1].collidepoint((event.pos[0]-1120,event.pos[1])):
                                    draw.Draw_Color = util.Color_Asset[obj][0]
                        elif event.pos[1]<280:
                            pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['save'][1],1)
                            pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['newproject'][1],1)
                            pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['clear'][1],1)
                            pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['tileproject'][1],1)
                            pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.ZoomAsset['out'][1],1)
                            pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.ZoomAsset['in'][1],1)
                            for i, brush in enumerate(util.BrushAsset):
                                if util.BrushAsset[brush][1].collidepoint((event.pos[0]-1120,event.pos[1])):
                                    draw.BrushSize = util.BrushAsset[brush][0]
                                    for j,color in enumerate(util.BrushAsset):
                                        if util.BrushAsset[color][2] == (util.Active_Color):
                                            util.BrushAsset[color][2] = (255,255,255)
                                            util.BrushAsset[brush][2] = util.Active_Color
                        elif event.pos[1]<380:
                            pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['save'][1],1)
                            pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['newproject'][1],1)
                            pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['clear'][1],1)
                            pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['tileproject'][1],1)

                            for i, zoom in enumerate(util.ZoomAsset):
                                if util.ZoomAsset[zoom][1].collidepoint((event.pos[0]-1120,event.pos[1])):
                                    if zoom == 'in':
                                        pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.ZoomAsset['out'][1],1)
                                        pygame.draw.rect(draw.Utility_Surface,util.Active_Color,util.ZoomAsset[zoom][1],1)
                                        if draw.Drawing_Surface.get_width()*1.1 <=1120 and draw.Drawing_Surface.get_height()*1.1<=900:
                                            draw.Drawing_Surface = pygame.transform.scale(draw.Drawing_Surface,(draw.Drawing_Surface.get_width()*1.1,draw.Drawing_Surface.get_height()*1.1))
                                    else:
                                        pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.ZoomAsset['in'][1],1)
                                        pygame.draw.rect(draw.Utility_Surface,util.Active_Color,util.ZoomAsset[zoom][1],1)
                                        if draw.Drawing_Surface.get_width()*0.9 >=10 and draw.Drawing_Surface.get_height()*0.9>10:
                                            draw.Drawing_Surface = pygame.transform.scale(draw.Drawing_Surface,(draw.Drawing_Surface.get_width()*0.9,draw.Drawing_Surface.get_height()*0.9))
                        elif event.pos[1]<480:
                            pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['save'][1],1)
                            pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['newproject'][1],1)
                            pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['clear'][1],1)
                            pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['tileproject'][1],1)
                            pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.ZoomAsset['out'][1],1)
                            pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.ZoomAsset['in'][1],1)
                            for i,pen in enumerate(util.Pen_Asset):
                                if util.Pen_Asset[pen][1].collidepoint((event.pos[0]-1120,event.pos[1])):
                                    if pen == 'pen':
                                        draw.Paint_Mode = 1
                                        pygame.draw.rect(draw.Utility_Surface,util.Active_Color,util.Pen_Asset['pen'][1],1)
                                        pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Pen_Asset['eraser'][1],1)
                                    else:
                                        draw.Paint_Mode = 2
                                        pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Pen_Asset['pen'][1],1)
                                        pygame.draw.rect(draw.Utility_Surface,util.Active_Color,util.Pen_Asset['eraser'][1],1)
                        elif event.pos[1]<735:
                            for i,com in enumerate(util.Command_Asset):
                                if util.Command_Asset[com][1].collidepoint((event.pos[0]-1120),event.pos[1]):
                                    if com == 'clear':
                                        draw.Clear()
                                        pygame.draw.rect(draw.Utility_Surface,(255,255,255),util.Command_Asset[com][1],1)
                                        pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['save'][1],1)
                                        pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['newproject'][1],1)
                                        pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['tileproject'][1],1)
                                    elif com == 'save':
                                        draw.SaveImage()
                                        pygame.draw.rect(draw.Utility_Surface,(255,255,255),util.Command_Asset[com][1],1)
                                        pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['newproject'][1],1)
                                        pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['tileproject'][1],1)
                                        pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['clear'][1],1)
                                    elif com == 'newproject':
                                        draw.NewProject()
                                        pygame.draw.rect(draw.Utility_Surface,(255,255,255),util.Command_Asset[com][1],1)
                                        pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['save'][1],1)
                                        pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['tileproject'][1],1)
                                        pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['clear'][1],1)
                                    elif com == 'tileproject':
                                        draw.TiledProject()
                                        pygame.draw.rect(draw.Utility_Surface,(255,255,255),util.Command_Asset[com][1],1)
                                        pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['save'][1],1)
                                        pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['newproject'][1],1)
                                        pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.Command_Asset['clear'][1],1)
                            pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.ZoomAsset['out'][1],1)
                            pygame.draw.rect(draw.Utility_Surface,(100,100,100),util.ZoomAsset['in'][1],1)
                        else:
                            if draw.UserInput_Asset['rect'].collidepoint(event.pos[0]-1120,event.pos[1]):
                                Typing_Active = True
                    else:
                        draw.PenDown = True
                        draw.LastPos = pygame.mouse.get_pos()
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    draw.PenDown = False
            if event.type == pygame.KEYDOWN:
                if Typing_Active:
                    if event.key == pygame.K_RETURN:
                        Typing_Active = False
                    elif event.key == pygame.K_BACKSPACE:
                        draw.UserInput_Asset['input'] = draw.UserInput_Asset['input'][:-1]
                    else:
                        draw.UserInput_Asset['input'] += event.unicode
        if Typing_Active:
            draw.UserInput_Asset['color'] = util.Active_Color
    elif StateFlag == 3:
        if InstanceFlag == 0:
            menu.TiledInitiasion()
            InstanceFlag+=1
            Display = pygame.display.set_mode(((MENU_WIDTH,MENU_HEI)))
        menu.TiledMenu()
    elif StateFlag == 4:
        if InstanceFlag == 0:
            Temp = (0,0,0)
            tile = TiledProject()
            InstanceFlag+=1
            Typing_Active = False
            Display = pygame.display.set_mode((WIDTH-10,HEIGHT-10),pygame.RESIZABLE)
        util.TileUpdate()
        tile.main()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    tile.UserInput_Asset['color'] = (153,0,17)
                    if event.pos[0]>1120:
                        Typing_Active = False
                        if event.pos[1]<220:
                            pygame.draw.rect(tile.Utility_Surface,(153,0,17),util.Command_Asset_Tile['save'][1],1)
                            pygame.draw.rect(tile.Utility_Surface,(153,0,17),util.Command_Asset_Tile['newproject'][1],1)
                            pygame.draw.rect(tile.Utility_Surface,(153,0,17),util.Command_Asset_Tile['clear'][1],1)
                            pygame.draw.rect(tile.Utility_Surface,(153,0,17),util.Command_Asset_Tile['drawproject'][1],1)

                            for i,obj in enumerate(util.Color_Asset):
                                if util.Color_Asset[obj][1].collidepoint((event.pos[0]-1120,event.pos[1])):
                                    tile.Tile_Color = util.Color_Asset[obj][0]

                        elif event.pos[1]<480:
                            pygame.draw.rect(tile.Utility_Surface,(153,0,17),util.Command_Asset_Tile['save'][1],1)
                            pygame.draw.rect(tile.Utility_Surface,(153,0,17),util.Command_Asset_Tile['newproject'][1],1)
                            pygame.draw.rect(tile.Utility_Surface,(153,0,17),util.Command_Asset_Tile['clear'][1],1)
                            pygame.draw.rect(tile.Utility_Surface,(153,0,17),util.Command_Asset_Tile['drawproject'][1],1)

                            for i,pen in enumerate(util.Pen_Asset):
                                if util.Pen_Asset[pen][1].collidepoint((event.pos[0]-1120,event.pos[1])):
                                    if pen == 'pen':
                                        tile.Paint_Mode = 1
                                        pygame.draw.rect(tile.Utility_Surface,util.Active_Color,util.Pen_Asset['pen'][1],1)
                                        pygame.draw.rect(tile.Utility_Surface,(153,0,17),util.Pen_Asset['eraser'][1],1)
                                        tile.Tile_Color = Temp
                                    else:
                                        Temp = tile.Tile_Color
                                        tile.Tile_Color = (255,255,255,0)
                                        tile.Paint_Mode = 2
                                        pygame.draw.rect(tile.Utility_Surface,(153,0,17),util.Pen_Asset['pen'][1],1)
                                        pygame.draw.rect(tile.Utility_Surface,util.Active_Color,util.Pen_Asset['eraser'][1],1)
                        elif event.pos[1]<735:
                            for i,com in enumerate(util.Command_Asset_Tile):
                                if util.Command_Asset_Tile[com][1].collidepoint((event.pos[0]-1120),event.pos[1]):
                                    if com == 'clear':
                                        tile.Clear()
                                        pygame.draw.rect(tile.Utility_Surface,(255,204,204),util.Command_Asset_Tile[com][1],1)
                                        pygame.draw.rect(tile.Utility_Surface,(153,0,17),util.Command_Asset_Tile['save'][1],1)
                                        pygame.draw.rect(tile.Utility_Surface,(153,0,17),util.Command_Asset_Tile['newproject'][1],1)
                                        pygame.draw.rect(tile.Utility_Surface,(153,0,17),util.Command_Asset_Tile['drawproject'][1],1)
                                    elif com == 'save':
                                        tile.Save()
                                        pygame.draw.rect(tile.Utility_Surface,(255,204,204),util.Command_Asset_Tile[com][1],1)
                                        pygame.draw.rect(tile.Utility_Surface,(153,0,17),util.Command_Asset_Tile['newproject'][1],1)
                                        pygame.draw.rect(tile.Utility_Surface,(153,0,17),util.Command_Asset_Tile['drawproject'][1],1)
                                        pygame.draw.rect(tile.Utility_Surface,(153,0,17),util.Command_Asset_Tile['clear'][1],1)
                                    elif com == 'newproject':
                                        tile.NewProject()
                                        pygame.draw.rect(tile.Utility_Surface,(255,204,204),util.Command_Asset_Tile[com][1],1)
                                        pygame.draw.rect(tile.Utility_Surface,(153,0,17),util.Command_Asset_Tile['save'][1],1)
                                        pygame.draw.rect(tile.Utility_Surface,(153,0,17),util.Command_Asset_Tile['drawproject'][1],1)
                                        pygame.draw.rect(tile.Utility_Surface,(153,0,17),util.Command_Asset_Tile['clear'][1],1)
                                    elif com == 'drawproject':
                                        tile.DrawProject()
                                        pygame.draw.rect(tile.Utility_Surface,(255,204,204),util.Command_Asset_Tile[com][1],1)
                                        pygame.draw.rect(tile.Utility_Surface,(153,0,17),util.Command_Asset_Tile['save'][1],1)
                                        pygame.draw.rect(tile.Utility_Surface,(153,0,17),util.Command_Asset_Tile['newproject'][1],1)
                                        pygame.draw.rect(tile.Utility_Surface,(153,0,17),util.Command_Asset_Tile['clear'][1],1)
                        else:
                            if tile.UserInput_Asset['rect'].collidepoint(event.pos[0]-1120,event.pos[1]):
                                Typing_Active = True
                    elif event.pos[0] <1120:
                        Tile = True
                        
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button==1 and event.pos[0] <1120:
                    Tile = False
            if event.type == pygame.KEYDOWN:
                if Typing_Active:
                    if event.key == pygame.K_RETURN:
                        Typing_Active = False
                    elif event.key == pygame.K_BACKSPACE:
                        tile.UserInput_Asset['input'] = tile.UserInput_Asset['input'][:-1]
                    else:
                        tile.UserInput_Asset['input'] += event.unicode
        if Typing_Active:
            tile.UserInput_Asset['color'] = util.Active_Color
        if Tile:
            x = event.pos[0] - int(tile.TS_x)
            y = event.pos[1] - int(tile.TS_y)
            if (x > 0 and x < tile.TileSurface.get_width()) and y>0 and y<tile.TileSurface.get_height():
                target = tile.TileSurface.get_at((x,y))
                if tile.TileSurface.get_at((x,y)) != (1,1,1,0) and target != tile.Tile_Color:
                    tile.Color_Tile(x,y,target,tile.Tile_Color)

    pygame.display.update()
    clock.tick(60)
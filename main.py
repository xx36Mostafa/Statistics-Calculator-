from kivy.lang import Builder
from kivymd.app import MDApp
from statistics import *

KV = '''
MDScreen:

    MDCard:
        orientation: "vertical"
        padding: 0, 0, 0 , "36dp"
        size_hint: .8, .8
        pos_hint: {"center_x": .5, "center_y": .5}
        elevation: 4
        shadow_radius: 6
        shadow_offset: 0, 2

        Widget:
            size_hint_y:None
            height:10

        MDLabel:
            text: "Calculators - Statistics "
            halign: "center"
            valign: "center"
            bold: True
            font_style: "H5"
        Widget:
            size_hint_y:None
            height:10
        MDTextField:
            id:dataset
            mode:"rectangle"
            fond_size:"20"
            hint_text: "Enter Data Set"
            helper_text: "example 1,2,3,4,4,5 dont forget comma"
            helper_text_mode: "on_focus"
            icon_right_color: app.theme_cls.primary_color
            pos_hint:{'center_x': 0.5, 'center_y': 0.6}
            size_hint_x:None
            width:350

        Widget:
            size_hint_y:None
            height:60
        MDCard:
            orientation: "horizontal"
            padding: 0, 0, 0 , "36dp"
            size_hint: 0.5, 1
            pos_hint: {"center_x": .5, "center_y": .8}

            MDRaisedButton:
                text: "Clear"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.328,'center_y': 0.01}
                size_hint_x:0.2
                on_release: app.clear()

            Widget:
                size_hint_y:None
                height:10    
            MDRaisedButton:
                text: "Calc"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.676,'center_y': 0.01}
                size_hint_x:0.2
                on_release: app.data(dataset.text)




        MDLabel:
            id:themain
            text: "Mean : "
            halign: "center"
            valign: "center"
            bold: True
            font_style: "H5"
        Widget:
            size_hint_y:None
            height:5
        MDLabel:
            id:themode
            text: "Mode : "
            halign: "center"
            valign: "center"
            bold: True
            font_style: "H5"
        Widget:
            size_hint_y:None
            height:5
        MDLabel:
            id:themedian
            text: "Median : "
            halign: "center"
            valign: "center"
            bold: True
            font_style: "H5"
        Widget:
            size_hint_y:None
            height:5
        MDLabel:
            id :IQR
            text: "IQR : "
            halign: "center"
            valign: "center"
            bold: True
            font_style: "H5"
        Widget:
            size_hint_y:None
            height:5
        MDLabel:
            id: QT
            text: "Quantiless : "
            halign: "center"
            valign: "center"
            bold: True
            font_style: "H5"
        Widget:
            size_hint_y:None
            height:5
        MDLabel:
            id: thevariance
            text: "Variance : "
            halign: "center"
            valign: "center"
            bold: True
            font_style: "H5"
        Widget:
            size_hint_y:None
            height:5
        MDLabel:
            id:stdevnn
            text: "Standerd Dev : "
            halign: "center"
            valign: "center"
            bold: True
            font_style: "H5"
        Widget:
            size_hint_y:None
            height:5
        MDLabel:
            id:distribution
            text: "Distribution : "
            halign: "center"
            valign: "center"
            bold: True
            font_style: "H5"
        Widget:
            size_hint_y:None
            height:5
        MDLabel:
            id:distribution_data
            text: "Distribution Data : "
            halign: "center"
            valign: "center"
            bold: True
            font_style: "H5"
        Widget:
            size_hint_y:None
            height:5
        MDLabel:
            id:cofficient
            text: "Cofficient Variation : "
            halign: "center"
            valign: "center"
            bold: True
            font_style: "H5"
        Widget:
            size_hint_y:None
            height:10
        MDRaisedButton:
            text: "Change theme"
            on_release: app.switch_theme_style()
            pos_hint: {"center_x": .5}
'''


class statistics(MDApp):
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        
        return Builder.load_string(KV)


    def data(self,gg):
        full_list = [int(x.strip()) for x in gg.split(',')]
        stdevn = stdev(full_list)
        meann = mean(full_list)
        modee = multimode(full_list)
        modde = mode(full_list)
        mediann = median(full_list)
        varincee = variance(full_list)
        quantiless = quantiles(full_list)

        #### mode #####
        first_mode = str(modee).replace('[','')
        final_mode = first_mode.replace(']','')
        ############
        q1 = float(quantiless[0])
        q2 = str(quantiless[1])
        q3 = float(quantiless[2])
        IQR2 = q3-q1
        s = str(quantiless).replace(']','')
        m=s.replace('[','')
        ###################
        if len(modee) == 1:
            mode_new=str(modee[0])
            new_distribution = 'uniModal'
        elif len(modee) == 2:

            mode_new3=str(modee[0])
            mode_new2=str(modee[1])
            mode_new=mode_new3+mode_new2
            new_distribution = 'biModal'
        elif len(modee) == 3:

            mode_new3=str(modee[0])
            mode_new2=str(modee[1])
            mode_new4=str(modee[2])
            mode_new=mode_new3+mode_new2+mode_new4
            new_distribution = 'triModal'
        elif len(modee) >= 4:
            mode_new3=str(modee[0])
            mode_new2=str(modee[1])
            mode_new4=str(modee[2])
            mode_new5=str(modee[3])
            mode_new=mode_new3+mode_new2+mode_new4+mode_new5
            new_distribution = 'multiModal'
        ######################    
        def distribution_data(meann,modde,mediann):
                dd = str(modde).replace('[','')
                mm = dd.replace(']','')
                meannn = float(meann)
                if len(modde) == 1:
                    mode_new=int(modde[0])
                elif len(modde) == 2:
                    mode_new3=int(modde[0])
                    mode_new2=int(modde[1])
                elif len(modde) == 3:
                    mode_new3=int(modde[0])
                    mode_new2=int(modde[1])
                    mode_new4=int(modde[2])

                elif len(modde) <= 4:

                    mode_new3=int(modde[0])
                    mode_new2=int(modde[1])
                    mode_new4=int(modde[2])
                    mode_new5=int(modde[3])
                    
                #final_mode = float(mm)
                print(meannn)
                print(modde[0])
                print(modde)
                if meannn == float(mediann):
                    return 'Symmetric'

                elif len(modde) == 1:
                    if meannn == float(modde[0]):
                        return 'Symmetric'

                    if float(meannn)>float(mediann):
                        return 'Positively Skewed'

                    elif float(meannn)<float(mediann):
                        return 'Negatively Skewed'
                
                elif float(meannn)>float(mediann):
                    return 'Positively Skewed'

                elif float(meannn)<float(mediann):
                    return 'Negatively Skewed'

        data = distribution_data(meann,modee,mediann)
        mn = str(meann)
        final_mean = mn[0:6]
        self.root.ids.themain.text = 'Mean : '+final_mean
        self.root.ids.themode.text = 'Mode : '+str(final_mode)
        self.root.ids.themedian.text = 'Median : '+str(float(mediann))
        self.root.ids.IQR.text = 'IQR : '+str(IQR2)
        self.root.ids.QT.text = 'Quantiless : '+str(m)
        var = str(varincee)
        final_varincee=var[0:5]
        self.root.ids.thevariance.text = 'Variance : '+final_varincee
        stt = str(float(stdevn))
        Standerd = stt[0:5]
        self.root.ids.stdevnn.text = 'Standerd Dev : '+Standerd
        self.root.ids.distribution.text = 'Distribution : '+new_distribution
        self.root.ids.distribution_data.text = 'Distribution Data : '+data
        final_coff = str(str(float(float(stdevn)/meann*100))+'%')
        Variation=final_coff[0:5]
        self.root.ids.cofficient.text = 'Cofficient Variation : '+Variation+'%'
        



    def clear(self):
        self.root.ids.dataset.text = ''
        self.root.ids.themain.text = 'Mean : '
        self.root.ids.themode.text = 'Mode : '
        self.root.ids.themedian.text = 'Median : '
        self.root.ids.IQR.text = 'IQR : '
        self.root.ids.QT.text = 'Quantiless : '
        self.root.ids.thevariance.text = 'Variance : '
        self.root.ids.stdevnn.text = 'Standerd Dev : '
        self.root.ids.distribution.text = 'Distribution : '
        self.root.ids.distribution_data.text = 'Distribution Data : '
        self.root.ids.cofficient.text = 'Cofficient Variation : '

    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            "Red" if self.theme_cls.primary_palette == "Purple" else "Purple"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )


statistics().run()
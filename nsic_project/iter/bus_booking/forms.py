from django import forms
from bus_booking.models  import passenger
from django.forms.models import modelformset_factory

class passenger_details(forms.Form):
    gender_choice = (
            ('Male','Male'),
            ('Female', 'Female'),
            ('others', 'others'),

                                )
    age_choice= (
                ('1','1'),
                ('2', '2'),
                ('3', '3'),
                ('4','4'),
                ('5', '5'),
                ('6', '6'),
                ('7','7'),
                ('8', '8'),
                ('9', '9'),
                ('10', '10'),
                ('11','11'),
                ('12', '12'),
                ('13', '13'),
                ('14','14'),
                ('15', '15'),
                ('16', '16'),
                ('17','17'),
                ('18', '18'),
                ('19', '19'),
                ('20', '20'),
                ('21','21'),
                ('22', '22'),
                ('23', '23'),
                ('24','24'),
                ('25', '25'),
                ('26', '26'),
                ('27','27'),
                ('28', '28'),
                ('29', '29'),
                ('30', '30'),
                ('31','31'),
                ('32', '32'),
                ('33', '33'),
                ('34','34'),
                ('35', '35'),
                ('36', '36'),
                ('37','37'),
                ('38', '38'),
                ('39', '39'),
                ('40', '40'),
                ('41','41'),
                ('42', '42'),
                ('43', '43'),
                ('44','44'),
                ('45', '45'),
                ('46', '46'),
                ('47','47'),
                ('48', '48'),
                ('49', '49'),
                ('50', '50'),
                ('51','51'),
                ('52', '52'),
                ('53', '53'),
                ('54','54'),
                ('55', '55'),
                ('56', '56'),
                ('57','57'),
                ('58', '58'),
                ('59', '59'),
                ('60', '60'),
                ('61','61'),
                ('62', '62'),
                ('63', '63'),
                ('64','64'),
                ('65', '65'),
                ('66', '66'),
                ('67','67'),
                ('68', '68'),
                ('69', '69'),
                ('70', '70'),
                ('71','71'),
                ('72', '72'),
                ('73', '73'),
                ('74','74'),
                ('75', '75'),
                ('76', '76'),
                ('77','77'),
                ('78', '78'),
                ('79', '79'),
                ('80', '80'),
                ('81','81'),
                ('82', '82'),
                ('83', '83'),
                ('84','84'),
                ('85', '85'),
                ('86', '86'),
                ('87','87'),
                ('88', '88'),
                ('89', '89'),
                ('90', '90'),
                ('91','91'),
                ('92', '92'),
                ('93', '93'),
                ('94','94'),
                ('95', '95'),
                ('96', '96'),
                ('97','97'),
                ('98', '98'),
                ('99', '99'),
                ('100', '100'),


                                    )

    name=forms.CharField(min_length=1,max_length=100,label='',required=True,widget=forms.TextInput())
    age=forms.ChoiceField(choices = age_choice, initial='',label='', widget=forms.Select(), required=True)
    gender=forms.ChoiceField(choices = gender_choice, initial='',label='', widget=forms.Select(attrs={
    'class':"selection-2"
    }
    ), required=True)


    class Meta:
        model = passenger
        fields = ['name','age','gender']

class contactform(forms.Form):
    phone_number = forms.CharField(min_length=10, max_length=10, required=True, widget=forms.TextInput())
    email=forms.EmailField()
    class Meta:
        fields = ['phone_number','email']


class bus_search(forms.Form):
    start_city=forms.CharField(min_length=1,max_length=100,required=True,widget=forms.TextInput(),label='')
    destination_city=forms.CharField(min_length=1,max_length=100,required=True,widget=forms.TextInput(),label="")
    start_date=forms.DateField(input_formats=['%Y-%m-%d'])


    class Meta:
        fields = ['start_city','destination_city','start_date']

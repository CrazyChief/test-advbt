from django import forms
from django.forms import ModelForm, RadioSelect, TypedChoiceField
from django.utils.translation import ugettext_lazy as _
from .models import Order

Alabama = 'AL'
Alaska = 'AK'
Arizona = 'AZ'
Arkansas = 'AR'
California = 'CA'
Colorado = 'CO'
Connecticut = 'CT'
Delaware = 'DE'
District_of_Columbia = 'DC'
Florida = 'FL'
Georgia = 'GA'
Hawaii = 'HI'
Idaho = 'ID'
Illinois = 'IL'
Indiana = 'IN'
Iowa = 'IA'
Kansas = 'KS'
Kentucky = 'KY'
Louisiana = 'LA'
Maine = 'ME'
Maryland = 'MD'
Massachusetts = 'MA'
Michigan = 'MI'
Minnesota = 'MN'
Mississippi = 'MS'
Missouri = 'MO'
Montana = 'MT'
Nebraska = 'NE'
Nevada = 'NV'
New_Hampshire = 'NH'
New_Jersey = 'NJ'
New_Mexico = 'NM'
New_York = 'NY'
North_Carolina = 'NC'
North_Dakota = 'ND'
Ohio = 'OH'
Oklahoma = 'OK'
Oregon = 'OR'
Pennsylvania = 'PA'
Rhode_Island = 'RI'
South_Carolina = 'SC'
South_Dakota = 'SD'
Tennessee = 'TN'
Texas = 'TX'
Utah = 'UT'
Vermont = 'VT'
Virginia = 'VA'
Washington = 'WA'
West_Virginia = 'WV'
Wisconsin = 'WI'
Wyoming = 'WY'

STATE_CHOICES = (
    (Alabama, 'AL'),
    (Alaska, 'AK'),
    (Arizona, 'AZ'),
    (Arkansas, 'AR'),
    (California, 'CA'),
    (Colorado, 'CO'),
    (Connecticut, 'CT'),
    (Delaware, 'DE'),
    (District_of_Columbia, 'DC'),
    (Florida, 'FL'),
    (Georgia, 'GA'),
    (Hawaii, 'HI'),
    (Idaho, 'ID'),
    (Illinois, 'IL'),
    (Indiana, 'IN'),
    (Iowa, 'IA'),
    (Kansas, 'KS'),
    (Kentucky, 'KY'),
    (Louisiana, 'LA'),
    (Maine, 'ME'),
    (Maryland, 'MD'),
    (Massachusetts, 'MA'),
    (Michigan, 'MI'),
    (Minnesota, 'MN'),
    (Mississippi, 'MS'),
    (Missouri, 'MO'),
    (Montana, 'MT'),
    (Nebraska, 'NE'),
    (Nevada, 'NV'),
    (New_Hampshire, 'NH'),
    (New_Jersey, 'NJ'),
    (New_Mexico, 'NM'),
    (New_York, 'NY'),
    (North_Carolina, 'NC'),
    (North_Dakota, 'ND'),
    (Ohio, 'OH'),
    (Oklahoma, 'OK'),
    (Oregon, 'OR'),
    (Pennsylvania, 'PA'),
    (Rhode_Island, 'RI'),
    (South_Carolina, 'SC'),
    (South_Dakota, 'SD'),
    (Tennessee, 'TN'),
    (Texas, 'TX'),
    (Utah, 'UT'),
    (Vermont, 'VT'),
    (Virginia, 'VA'),
    (Washington, 'WA'),
    (West_Virginia, 'WV'),
    (Wisconsin, 'WI'),
    (Wyoming, 'WY'),
)


class OrderCreateForm(ModelForm):
    shipping_state = TypedChoiceField(choices=STATE_CHOICES)

    class Meta:
        model = Order
        fields = [
            'shipping_first_name',
            'shipping_last_name',
            'shipping_type',
            'shipping_country',
            'shipping_state',
            'shipping_postcode',
            'shipping_city',
            'shipping_to_home',
            'shipping_street',
            'shipping_home',
            'shipping_phone',
            'shipping_email',
            'pay_type',
        ]
        labels = {
            'shipping_first_name': _('Name'),
            'shipping_last_name': _('Surname'),
            'shipping_type': _('Delivery'),
            'shipping_city': _('City'),
            'shipping_country': _('Country'),
            'shipping_state': _('State'),
            'shipping_postcode': _('Post code'),
            'shipping_to_home': _('Home delivery'),
            'shipping_street': _('Street'),
            'shipping_home': _('Home number, flat number'),
            'shipping_phone': _('Phone'),
            'shipping_email': _('Email'),
            'pay_type': _('How do you plan to pay?'),
        }
        error_messages = {
            'shipping_first_name': {
                'max_length': _("This name is too long. Max number of letters is 100")
            },
            'shipping_last_name': {
                'max_length': _("This surname is too long. Max number of letters is 100")
            }
        }
        widgets = {
            # 'shipping_state': TypedChoiceField(choices=STATE_CHOICES),
            'shipping_type': RadioSelect,
            'pay_type': RadioSelect,
        }

    # class Media:
    #     js = ('checkout.js',)












from django import forms
from django.core.validators import *
from django.core.exceptions import ValidationError
from django.core import validators
from django.forms import widgets
from django.utils.translation import ugettext as _
from django.core.validators import RegexValidator


class IntegerFieldForm(forms.Form):
    integerField = forms.IntegerField(required=True,)
    # integerField = forms.IntegerField(max_value=None)
    # integerField = forms.IntegerField(min_value=None)
    # integerField = forms.IntegerField(required=False, empty_value='empty_value')
    # integerField = forms.IntegerField(required=True)
    # integerField = forms.IntegerField(label=None)
    # integerField = forms.IntegerField(initial=None)
    # integerField = forms.IntegerField(help_text='')
    # integerField = forms.IntegerField(error_messages=None)
    # integerField = forms.IntegerField(show_hidden_initial=False)
    # integerField = forms.IntegerField(localize=False)
    # integerField = forms.IntegerField(disabled=False)
    # integerField = forms.IntegerField(label_suffix=None)
    # integerField = forms.IntegerField(hidden_widget=None)
    # integerField = forms.IntegerField(default_validators=None)
    # integerField = forms.IntegerField(default_error_messages=None)
    # integerField = forms.IntegerField(re_decimal=None)
    # integerField = forms.IntegerField(widget=None)
    # integerField = forms.IntegerField(validators=())












# def check_size(value):
#   if len(value) < 5:
#     raise forms.ValidationError("Minimum 5 characters required")

# class CharFieldFieldForm(forms.Form):
    # charFieldXXXXXXXXXX = forms.CharField()
    # charField = forms.CharField(max_length=5)
    # charField = forms.CharField(min_length=6)
    # charField = forms.CharField(strip=True)
    # charField = forms.CharField(required=False, empty_value='empty_value')
    # charField = forms.CharField(required=True)
    # charField = forms.CharField(initial='INITIAL')#(initial={'name':'DELL'})#(initial={'Male'})
    # charField = forms.CharField(label='label')
    # charField = forms.CharField(help_text='help_text')
    # charField = forms.CharField(show_hidden_initial=True)
    # charField = forms.CharField(disabled=True)
    # charField = forms.CharField(localize=True)
    # charField = forms.CharField(label_suffix=' + label_suffix')
    # charField = forms.CharField(required=True, error_messages={'required': "Please Enter your Name"})
    # charField = forms.CharField(validators=[MaxLengthValidator(5, message='Max Val is 5')])#MinLengthValidator

    # charField = forms.CharField(validators=[check_size])
    '''charField = forms.CharField()
    def clean_charField(self): #def clean(self):

        # data from the form is fetched using super function
        super(CharFieldFieldForm, self).clean()

        # extract the username and text field from the data
        CF = self.cleaned_data.get('charField')

        # conditions to be met for the username length
        if len(CF) < 3:
            self._errors['charField'] = self.error_class([
                'Minimum 5 characters required'])
        if len(CF) > 5:
            self._errors['charField'] = self.error_class([
                'It Should not contain more than 10 characters'])

        # return any errors if found
        return self.cleaned_data'''

    # charField = forms.CharField(widget=forms.Textarea)#Textarea#TextInput#HiddenInput
#---------------------------------------------------------------------------------
    # CheckboxInput = forms.BooleanField()
    # CheckboxInput = forms.BooleanField(required=True)
    # CheckboxInput = forms.BooleanField(initial={'name':'DELL'})#(initial={'name':'DELL'})#(initial={'Male'})
    # CheckboxInput = forms.BooleanField(label='label')
    # CheckboxInput = forms.BooleanField(help_text='help_text')
    # CheckboxInput = forms.BooleanField(required=False,error_messages={'required': 'Please enter your name'})
    # CheckboxInput = forms.BooleanField(show_hidden_initial=True)
    # CheckboxInput = forms.BooleanField(disabled=True)
    # CheckboxInput = forms.BooleanField(localize=True)
    # CheckboxInput = forms.BooleanField(validators=[validate_slug])
    # CheckboxInput = forms.BooleanField(label_suffix=' + label_suffix')
    # CheckboxInput = forms.BooleanField(widget=forms.CheckboxInput) #TextInput#HiddenInput
    #
    #--------------------------------------------------------------------------------
    # external = forms.BooleanField(label=_('External link'), required=False)
    # is_superuser = forms.BooleanField(label=_("Administrator"), required=False,
    #     help_text=_('Administrators have full access to manage any object or setting.'))
    #--------------------------------------------------------------------------------
    # required -- Boolean that specifies whether the field is required. (True / False)
    #             True by default.
    # initial -- A value to use in this Field's initial display. This value
    #            is *not* used as a fallback if data isn't given.
    # label -- A verbose name for this field, for use in displaying this
    #          field in a form. By default, Django will use a "pretty"
    #          version of the form field name, if the Field is part of a
    #          Form.
    # help_text -- An optional string to use as "help text" for this Field.
    # error_messages -- An optional dictionary to override the default
    #                   messages that the field will raise.
    # show_hidden_initial -- Boolean that specifies if it is needed to render a
    #                        hidden widget with initial value after widget.
    # disabled -- Boolean that specifies whether the field is disabled, that
    #             is its widget is shown in the form but not editable.
    # localize -- Boolean that specifies if the field should be localized.
    # validators -- List of additional validators to use
    # label_suffix -- Suffix to be added to the label. Overrides
    #                 form's label_suffix.
    # widget -- A Widget class, or instance of a Widget class, that should
    #           be used for this Field when displaying it. Each Field has a
    #           default Widget that it'll use if you don't specify this. In
    #           most cases, the default widget is TextInput.
    #           ----------------List of all Widgets ---------------------------------
                # forms.Media
                # forms.MediaDefiningClass
                # forms.Widget
                # forms.TextInput
                # forms.NumberInput
                # forms.EmailInput
                # forms.URLInput
                # forms.PasswordInput
                # forms.HiddenInput
                # forms.MultipleHiddenInput
                # forms.FileInput
                # forms.ClearableFileInput
                # forms.Textarea
                # forms.DateInput
                # forms.DateTimeInput
                # forms.TimeInput
                # forms.CheckboxInput
                # forms.Select
                # forms.NullBooleanSelect
                # forms.SelectMultiple
                # forms.RadioSelect
                # forms.CheckboxSelectMultiple
                # forms.MultiWidget
                # forms.SplitDateTimeWidget
                # forms.SplitHiddenDateTimeWidget
                # forms.SelectDateWidget




























































    # class MyModelForm(forms.ModelForm):
    #     boolfield = forms.TypedChoiceField(
    #         coerce=lambda x: x == 'True',
    #         choices=((False, 'False'), (True, 'True')),
    #         widget=forms.RadioSelect
    #     )
        #
        # class Meta:
        #     model = MyModel





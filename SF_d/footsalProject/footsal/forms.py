#from attr import fields
from django import forms
from django.core.mail import EmailMessage
from .models import PhotoPost,PhotoOnlyPost


#Formはフォームのスーパークラスでこれを継承すればFromの機能が使用可能になり、独自の処理も可能になる。
class ContactForm(forms.Form):
    #データ型によって下記のようにフィールドを定義する。詳細はP264
    name=forms.CharField(label='お名前')
    email=forms.EmailField(label='メールアドレス')
    title=forms.CharField(label='件名')
    message=forms.CharField(label='メッセージ',widget=forms.Textarea)

    #下記関数でメッセージフォームのひな形でそれぞれがレンダリングで表される。
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['name'].widget.attrs['placeholder']='お名前を入力してください'
        self.fields['name'].widget.attrs['class']='form-control'

        self.fields['email'].widget.attrs['placeholder']='メールアドレスを入力してください'
        self.fields['email'].widget.attrs['class']='form-control'

        self.fields['title'].widget.attrs['placeholder']='タイトルを入力してください'
        self.fields['title'].widget.attrs['class']='form-control'

        self.fields['message'].widget.attrs['placeholder']='メッセージを入力してください'
        self.fields['message'].widget.attrs['class']='form-control'

    #下記関数でメール送信処理を行う。
    def send_email(self):
        name=self.cleaned_data['name']
        email=self.cleaned_data['email']
        title=self.cleaned_data['title']
        message=self.cleaned_data['message']
        subject = 'お問い合わせ:{}'.format(title)
        message='＜送信者名＞\n{0}\n＜メールアドレス＞\n{1}\n ＜タイトル＞\n{2}\n ＜メッセージ＞\n{3}\n'.format(name,email,title,message)
        from_email='chaco7chaco@gmail.com' #送信元メールアドレス
        to_list=['chaco7chaco@gmail.com']  #送信先メールアドレス
        message=EmailMessage(subject=subject,
                            body=message,
                            from_email=from_email,
                            to=to_list,
                            )
        message.send()

class TopicForm(forms.ModelForm):

    class Meta:
        model   = PhotoPost
        fields  = ["title","category"]
#上記のfieldsに全てのカラムを設定する場合は'__all__'とする。

class TopicImageForm(forms.ModelForm):
    image1 =forms.ImageField(label="galaryの画像",
                    widget=forms.ClearableFileInput(attrs={'multiple':True}))
    class Meta:
        model   = PhotoOnlyPost
        fields  = ["p_id","image1"]
        
        #60,61行目でfileのinput時にmultipleが有効になる。
        
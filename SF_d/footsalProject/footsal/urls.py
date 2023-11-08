from django.urls import path
from . import views


app_name = 'footsal'

urlpatterns = [
    path('',views.IndexView.as_view(),name = 'index'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('schedule/',views.ScheduleView.as_view(),name='schedule'),
    path('postAll/',views.PostAllView.as_view(),name='postAll'),
    path('uploadPhoto/',views.UploadView.as_view(),name='uploadPhoto'),
    path('photoGallery',views.GalleryView.as_view(),name='photoGallery'),

    path('ichikawa/',views.IchiView.as_view(),name='ichi'),
    path('funabashi/',views.FunaView.as_view(),name='funa'),
    path('konodai/',views.KonoView.as_view(),name='kono'),
    path('tobu/',views.TobuView.as_view(),name='tobu'),
    path('kashiwa/',views.KashiView.as_view(),name='kashiwa'),
    path('school/',views.SchoolView.as_view(),name='school'),
    path('legend/',views.LegendView.as_view(),name='legend'),

    path('detail/page_<int:pk>/',views.DetailPageView.as_view(),name='detail'),
    path('detail_photo/page_<int:pk>/',views.DetailPhotoView.as_view(),name='detail_photo')
]
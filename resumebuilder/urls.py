from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.basepage,name='base'),
    path('home/',views.homepage,name='home'),
    path('addclient/',views.AddClient.as_view(),name='addclient'),
    path('addeducation/',views.addeducation,name='addeducation'),
    path('<int:pk>',views.CandidateView.as_view(),name='candidate'),
    path('',views.loginpage,name='login'),
    path('signup/',views.signpage,name='signup'),
    path('logout/',views.logoutpage,name='logout'),
    path('delete/<int:id>/',views.delete_data,name='deletedata'),
    path('edit/<int:id>/',views.edit_data,name='editdata'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

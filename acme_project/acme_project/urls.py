# Импортируем настройки проекта.
from django.conf import settings
# Добавьте новые строчки с импортами классов.
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
# Импортируем функцию, позволяющую серверу разработки отдавать файлы.
from django.conf.urls.static import static
from django.contrib import admin
# К импортам из django.urls добавьте импорт функции reverse_lazy
from django.urls import include, path, reverse_lazy

handler404 = 'core.views.page_not_found' 

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    # Подключаем urls.py приложения для работы с пользователями.
    path('auth/', include('django.contrib.auth.urls')),
    path('birthday/', include('birthday.urls')),
    # В конце добавляем к списку вызов функции static.
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#path(
  #      'auth/registration/', 
  #      CreateView.as_view(
  #          template_name='registration/registration_form.html',
  #          form_class=UserCreationForm,
 #           success_url=reverse_lazy('pages:homepage'),
 #       ),
#       name='registration',
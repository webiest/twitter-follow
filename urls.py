# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from ragendja.urlsauto import urlpatterns
from ragendja.auth.urls import urlpatterns as auth_patterns
from myapp.forms import UserRegistrationForm


handler500 = 'ragendja.views.server_error'

urlpatterns = auth_patterns + patterns('',
	(r'^$', 'views.disp'),
) + urlpatterns

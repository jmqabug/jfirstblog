from django.conf.orls import url

from views.import template views

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^', include(blog.urls)),
	]
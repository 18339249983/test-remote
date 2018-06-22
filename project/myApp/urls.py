from django.conf.urls import url
from myApp import views
urlpatterns = [
    url(r'^$', views.myweb),
    url(r'^home/$', views.home),
    url(r'^market/(\w+)/(\w+)/(\w+)/$', views.market),
    url(r'^cart/$', views.cart),

    url(r'^mine/$', views.mine),
    # 登陆界面
    url(r'^login/$', views.login),
    url(r'^quit/$', views.quit),
    url(r'^addAddress/$', views.addAddress),
    url(r'^showAddress/$', views.showAddress),
    url(r'detail/(\w+)/$', views.detail),
    #     修改购物车  增加减少
    url(r'^changecart/(\w+)/$', views.changecart),
    # 修改购物车 是否选中
    url(r'^changecart2/$', views.changecart2),
    url(r'^qOrder/$', views.qOrder),
    url(r'^map/$', views.map),
    url(r'search/$', views.search),

]
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view),

    path('products/', views.product_list),
    path('add-to-cart/', views.add_to_cart),
    path('remove-from-cart/<int:pid>/', views.remove_from_cart),
    path('cart/', views.view_cart),
    path('checkout/', views.checkout),
    path('orders/', views.order_history),
]

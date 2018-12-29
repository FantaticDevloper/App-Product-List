from django.conf.urls import url
from allauth.account import views as allauthviews

from .views import (
    add_to_cart,
    delete_from_cart,
    order_details,
    checkout,
    update_transaction_records,
    success,
    process_payment
)

app_name = 'shopping_cart'

urlpatterns = [
    url(r'^add-to-cart/(?P<item_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),
    url(r'^order-summary/$', order_details, name="order_summary"),
    url(r'^success/$', success, name='purchase_success'),
    url(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
    url(r'^checkout/$', checkout, name='checkout'),
    url(r'^payment/(?P<order_id>[-\w]+)/$', process_payment, name="process_payment"),
    url(r'^update-transaction/(?P<token>[-\w]+)/$', update_transaction_records,
        name='update_records'),
    url(r'/logout', allauthviews.logout, name="logout"),
]
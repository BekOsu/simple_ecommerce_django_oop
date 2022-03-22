import json
from cart.models import Cart

def get_logged_user_cart(request):
    if request.user.is_authenticated:
         user = request.user
         cart,_ = Cart.objects.get_or_create(id=user.id)
         return cart
     
     
def get_cart_from_session(request):
    if request.user.is_authenticated:
         cart_items = json.loads(request.session['cart_items'])
         cart = get_logged_user_cart(request)
         return (cart.get_cart_products_info(cart_items))


def store_cart_to_session(request, cart_items= None):
    if request.user.is_authenticated:
         if cart_items is None : 
             cart_items = get_logged_user_cart(request)
    
         request.session['cart_items'] = json.dumps(cart_items)
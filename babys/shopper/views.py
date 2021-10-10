from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .form import LoginForm
from .models import CartInfos, OrderInfos
from commodity.models import CommodityInfos

# Create your views here.

# def loginView(request):
#     title = '用户登录'
#     classContent = 'logins'
#     if request.method == 'POST':
#         infos = LoginForm(data=request.POST)
#         # 验证表单字段的数据是否正确
#         if infos.is_valid():
#             data = infos.cleaned_data
#             # 获取请求参数 username 和 password
#             username = data['username']
#             password = data['password']
#
#             # 查询 username 的数据是否存在内置模型 User
#             if User.objects.filter(username=username):
#                 # 验证账号密码与模型 User 的账号密码是否一致
#                 user = authenticate(username=username, password=password)
#                 # 通过验证则使用内置函数 login 执行用户登录
#                 # 登录成功后跳转到个人中心页
#                 if user:
#                     login(request, user)
#                     return redirect(reverse('shopper:shopper'))
#
#             # username 的数据不存在内置模型 User
#             else:
#                 # 执行用户注册
#                 state = '注册成功'
#                 d = dict(username=username, password=password, is_staff=1, is_active=1)
#                 user = User.objects.create_user(**d)
#                 user.save()
#
#         else:
#             # 获取错误信息，并以 JSON 格式输出
#             error_msg = infos.errors.as_json()
#             print(error_msg)
#
#     # 处理 HTTP 的 GET 的请求
#     else:
#         infos = LoginForm()
#     return render(request, 'login.html', locals())

def loginView(request):
    title = '用户登录'
    classContent = 'logins'
    if request.method == 'POST':
        infos = LoginForm(data=request.POST)
        if infos.is_valid():
            data = infos.cleaned_data
            username = data['username']
            password = data['password']
            if User.objects.filter(username=username):
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    return redirect(reverse('shopper:shopper'))
            else:
                state = '注册成功'
                d = dict(username=username, password=password, is_staff=1, is_active=1)
                user = User.objects.create_user(**d)
                user.save()
        else:
            # 获取错误信息，并以JSON格式输出
            error_msg = infos.errors.as_json()
            print(error_msg)
    else:
        infos = LoginForm()
    return render(request, 'login.html', locals())


@login_required(login_url='/shopper/login.html')
def shopperView(request):
    title = '个人中心'
    classContent = 'informations'
    p = request.GET.get('p', 1)
    # 处理已支付的订单
    t = request.GET.get('t', '')  # 代表用户购买商品的支付时间
    payTime = request.session.get('payTime', '')
    if t and payTime and t == payTime:
        payInfo = request.session.get('payInfo', '')
        OrderInfos.objects.create(**payInfo)
        del request.session['payTime']
        del request.session['payInfo']
    # 根据当前用户查询用户订单信息
    orderInfos = OrderInfos.objects.filter(user_id=request.user.id).order_by('-created')
    # 分页功能
    paginator = Paginator(orderInfos, 7)  # 每页设置7条订单信息
    try:
        pages = paginator.page(p)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    return render(request, 'shopper.html', locals())


def logoutView(request):
    # 使用内置函数logout退出用户登录状态
    logout(request)
    # 网页自动跳转到首页
    return redirect(reverse('index:index'))


@login_required(login_url='/shopper/login.html')
def shopcartView(request):
    title = '我的购物车'
    classContent = 'shopcarts'

    # 获取请求参数
    id = request.GET.get('id', '')
    quantity = request.GET.get('quantity', 1)
    userID = request.user.id

    # 存在请求参数id，则对模型 CartInfos 新增数据
    if id:
        CartInfos.objects.update_or_create(commodityInfos_id=id, user_id=userID, quantity=quantity)
        return redirect('shopper:shopcart')

    # 查询当前用户的购物车信息
    getUserId = CartInfos.objects.filter(user_id=userID)

    # 从当前用户的购物车信息获取商品id和购买属性
    commodityDcit = {x.commodityInfos_id: x.quantity for x in getUserId}

    # 从商品 id 获取商品详细信息
    commodityInfos = CommodityInfos.objects.filter(id__in=commodityDcit.keys())
    return render(request, 'shopcart.html', locals())


def deleteAPI(request):
    result = {'state': 'success'}
    userId = request.GET.get('userId', '')
    commodityId = request.GET.get('commodityId', '')
    if userId:
        CartInfos.objects.filter(user_id=userId).delete()
    elif commodityId:
        CartInfos.objects.filter(commodityInfos_id=commodityId).delete()
    else:
        result = {'state': 'fail'}

    return JsonResponse(result)

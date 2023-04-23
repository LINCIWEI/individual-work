from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        # 处理登录表单的提交
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 验证表单数据
            user = form.get_user()
            login(request, user)
            messages.success(request, '登录成功')
            return redirect('index')  # 重定向到 index 页面
        else:
            # 登录失败
            messages.error(request, '登录失败，请检查用户名和密码')
    else:
        # 渲染登录页面
        form = AuthenticationForm(request)
    return render(request, 'accounts/login.html', {'form': form})

# 用户注销
def logout_view(request):
    return LogoutView.as_view(template_name='logged_out.html')(request)

# 用户注册

def register_view(request):
    if request.method == 'POST':
        # 检查请求方法是否为 POST

        form = UserCreationForm(request.POST)
        # 根据 UserCreationForm 创建表单实例，并传入 POST 数据

        if form.is_valid():
            # 检查表单数据是否有效
            user = form.save()
            # 保存用户信息

            # 注册成功后可以执行其他操作，例如自动登录等

            return redirect('index')
            # 返回注册成功后的页面，这里假设 home 是一个 URL 名称
    else:
        form = UserCreationForm()
        # 若请求方法不是 POST，则创建一个空的 UserCreationForm 实例

    return render(request, 'accounts/register.html', {'form': form})
    # 渲染注册页面并传递表单实例给模板
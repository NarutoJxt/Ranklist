from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, FormView,ListView

from Rank.forms import RankInsertionForm
from Rank.models import User


class RankCreateView(FormView):
    template_name = "port1.html"
    form_class = RankInsertionForm
    def get_queryset(self):
        users = User.objects.all()
        return users
    def get_query_set_order_by_score(self):
        users = self.get_queryset()
        users = users.order_by("-score")
        return users
    def get_queryset_order_by_client(self):
        users = self.get_queryset()
        users = users.order_by("client")
        return users
    def get_context_data(self, **kwargs):
        context = super(RankCreateView,self).get_context_data(**kwargs)
        context["users"] = self.get_query_set_order_by_score()
        context["users_options"] =self.get_queryset_order_by_client()
        return context
    def form_invalid(self, form):
        return self.render_to_response(
            {
                "form":form,
                "users": self.get_query_set_order_by_score()
            }
        )
    def form_valid(self, form):
        if form.cleaned_data["score"] > 10000000:
            return self.render_to_response(
                {
                    "form":form,
                    "error_message":"你输入得分数超过范",
                    "users": self.get_query_set_order_by_score()

                }
            )
        else:
            client = form.cleaned_data["client"]
            score = form.cleaned_data["score"]
            flag = 0
            try:
                user = User.objects.get(client=client)
            except Exception as e:
                if score < 0 or score > 10000000:
                    error_message = "您输入的数字超过范围"
                    flag = 1
                else:
                    user = form.save()
                    user.save()
            else:
                if score < 0 or score > 10000000:
                    error_message = "您输入的数字超过范围"
                    flag = 1
                else:
                    user.score = score
                    user.save()
            finally:
                if flag == 0:
                    url = reverse(
                    "Rank:set_score"
                    )
                    return HttpResponseRedirect(url)
                else:
                    return self.render_to_response({
                        "form":form,
                        "error_message":error_message,
                        "users":self.get_query_set_order_by_score(),
                        "users_options":self.get_queryset_order_by_client()
                    })
class RankListView(ListView):
    model = User
    template_name = "port2.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RankListView,self).get_context_data(**kwargs)
        user_list = self.get_queryset()
        user_list = user_list.order_by("-score")
        users_options = user_list.order_by("client")
        start_num = self.request.GET.get("start_num")
        end_num = self.request.GET.get("end_num")
        client = int(self.request.GET.get("client"))
        lenghth = len(user_list)
        error_message = ""
        if not start_num.isdigit() or not end_num.isdigit():
            error_message = "请输入合法得字符"
            context["users"] = user_list
            context["start"] = 1
        else:
            start_num = int(start_num)
            end_num = int(end_num)
            user = User.objects.get(client=client)
            if 0 <= start_num <= end_num <=lenghth:
                users = user_list[start_num:end_num]
                user = User.objects.get(client=client)
                context["self"] = user
                context["users"] = users
                context["start"] = start_num
                context["seq"] = list(user_list).index(user)+1
            else:
                error_message = "请输入(1-" + str(lenghth) + "合法字符"
                context["error_message"] = error_message
        context["users_options"] = users_options
        context["error_message"] = error_message
        context["user_count"] = lenghth
        return context

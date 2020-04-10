from django.urls import path

from Rank.views import RankCreateView, RankListView

app_name = "Rank"
urlpatterns = [
    path("",RankCreateView.as_view(),name="set_score"),
    path("rankList/",RankListView.as_view(),name="get_rank")
]
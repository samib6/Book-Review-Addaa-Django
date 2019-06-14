from django.urls import path
from .views import ReviewCreate,ReviewDetail,ReviewList,ReviewDelete
urlpatterns = [
    path(r'',ReviewCreate.as_view(),name='create'),
    path('Reviews/',ReviewList.as_view(),name='bookreview_list'),
    path('BookReview/<int:pk>',ReviewDetail.as_view(),name='review_detail'),
    path('BookReview/delete/<int:pk>',ReviewDelete.as_view(),name='review_delete')
    #path('BookReviewList/',Reviewlist.as_view(),name='BookReviewList'),
]

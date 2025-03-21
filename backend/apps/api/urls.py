
from django.urls import path
from .views import (
    PublicationList, 
    DataTypesList,
    DataCategoriesList,
    FileUploadView,
    LoginView,
    SignupView, 
    LogoutView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
    UserProfileView,
    SearchView,
    DownloadView,
    VoltammetryDataView,
    RecentDatasetsView,
    CSRFTokenView
)

urlpatterns = [
    path('publications/', PublicationList.as_view(), name='publication-list'),
    path('data-types/', DataTypesList.as_view(), name='data-types-list'),
    path('data-categories/', DataCategoriesList.as_view(), name='data-categories-list'),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    
    # Authentication endpoints
    path('auth/csrf/', CSRFTokenView.as_view(), name='csrf-token'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/signup/', SignupView.as_view(), name='signup'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    path('auth/password-reset/confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('auth/profile/', UserProfileView.as_view(), name='user-profile'),
    
    # Search endpoint
    path('search/', SearchView.as_view(), name='search'),
    
    # Download endpoint
    path('download/', DownloadView.as_view(), name='download'),
    
    # Voltammetry endpoints
    path('voltammetry/', VoltammetryDataView.as_view(), name='voltammetry-list'),
    path('voltammetry/<str:experiment_id>/', VoltammetryDataView.as_view(), name='voltammetry-detail'),
    
    # Recent datasets endpoint
    path('recent-datasets/', RecentDatasetsView.as_view(), name='recent-datasets'),
]

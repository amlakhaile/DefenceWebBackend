from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from colleges import views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('collages',views.Collageviewset)
router.register('university',views.Universityviewset)
router.register('News',views.Newsviewset)
router.register('Events',views.Eventsviewset)
Collagerouter = routers.NestedSimpleRouter(router, 'collages', lookup='collage')
Collagerouter.register('partner', views.PartnerViewset, basename='collage-partner')

Collagerouter.register('department', views.DepartmentViewset, basename='collage-department')
Collagerouter.register('facilities', views.FacilitiesViewset, basename='collage-facilities')
Collagerouter.register('office', views.OfficeViewset, basename='collage-office')
Officerouter=routers.NestedSimpleRouter(Collagerouter,'office',lookup='office')

Officerouter.register('staffmember', views.StaffmemberViewset, basename='office-staffmember')


Collagerouter.register('gallery', views.GalleryViewset, basename='collage-gallery')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(Collagerouter.urls)),
    path('',include(Officerouter.urls))
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

import xadmin
from xadmin import views


class GlobalSetting(object):
    # 设置base_site.html的Title
    site_title = '零娱网'
    # 设置base_site.html的Footer
    site_footer = '零娱网'


xadmin.site.register(views.CommAdminView, GlobalSetting)

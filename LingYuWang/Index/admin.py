import xadmin
from xadmin import views


class GlobalSetting(object):
    # 设置base_site.html的Title
    site_title = '零娱网'
    # 设置base_site.html的Footer
    site_footer = '零娱网'
    # 开启分组折叠


class BaseSetting:
    enable_themes = True  # 开启主题功能
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)

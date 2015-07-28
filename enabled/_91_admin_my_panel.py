# The name of the panel to be added to HORIZON_CONFIG. Required.
PANEL = 'my_panel'

# The name of the dashboard the PANEL associated with. Required.
PANEL_DASHBOARD = 'admin'

# The name of the panel group the PANEL is associated with.
PANEL_GROUP = 'my_panel_group'

# Python panel class of the PANEL to be added.
ADD_PANEL = 'my_panel.panel.MyPanel'

ADD_INSTALLED_APPS = ['my_panel']

ADD_ANGULAR_MODULES = ['hz.dashboard.admin.my-panel']

ADD_JS_FILES = [
  'dashboard/admin/my-panel/my-panel.js',
]

ADD_SCSS_FILES = [
  'dashboard/admin/my-panel/my-panel.scss'
]